#!/usr/bin/env python3
"""
Basic tests for FinScraper functionality
"""

import sys
import os
import unittest
import tempfile
import shutil

# Add the src directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from finscraper import FinancialDataScraper, FinancialData
from finscraper.utils.compatibility import get_available_features


class TestFinScraper(unittest.TestCase):
    """Basic tests for FinScraper functionality"""
    
    def setUp(self):
        """Set up test environment"""
        # Create a temporary directory for test storage
        self.test_dir = tempfile.mkdtemp()
        self.test_storage_file = os.path.join(self.test_dir, "test_financial_data.json")
        self.scraper = FinancialDataScraper(storage_file=self.test_storage_file)
    
    def tearDown(self):
        """Clean up test environment"""
        # Remove temporary directory
        shutil.rmtree(self.test_dir, ignore_errors=True)
    
    def test_scraper_initialization(self):
        """Test scraper initialization"""
        self.assertIsNotNone(self.scraper)
        self.assertEqual(len(self.scraper.get_ticker_list()), 0)
    
    def test_ticker_validation(self):
        """Test ticker validation"""
        self.assertTrue(self.scraper.validate_ticker("AAPL"))
        self.assertTrue(self.scraper.validate_ticker("GOOGL"))
        self.assertFalse(self.scraper.validate_ticker(""))
        self.assertFalse(self.scraper.validate_ticker("INVALID123456789"))
        self.assertFalse(self.scraper.validate_ticker("BAD-TICKER"))
    
    def test_add_ticker(self):
        """Test adding tickers"""
        # Add a valid ticker (will use mock data as fallback)
        result = self.scraper.add_ticker("AAPL")
        self.assertTrue(result)
        self.assertEqual(len(self.scraper.get_ticker_list()), 1)
        self.assertIn("AAPL", self.scraper.get_ticker_list())
        
        # Try to add the same ticker again
        result = self.scraper.add_ticker("AAPL")
        self.assertFalse(result)
        self.assertEqual(len(self.scraper.get_ticker_list()), 1)
    
    def test_remove_ticker(self):
        """Test removing tickers"""
        # Add a ticker first
        self.scraper.add_ticker("AAPL")
        self.assertEqual(len(self.scraper.get_ticker_list()), 1)
        
        # Remove the ticker
        self.scraper.remove_ticker("AAPL")
        self.assertEqual(len(self.scraper.get_ticker_list()), 0)
    
    def test_get_data(self):
        """Test getting data"""
        # Add a ticker
        self.scraper.add_ticker("AAPL")
        
        # Get all data
        data_list = self.scraper.get_all_data()
        self.assertEqual(len(data_list), 1)
        self.assertIsInstance(data_list[0], FinancialData)
        self.assertEqual(data_list[0].ticker, "AAPL")
        
        # Get specific ticker data
        aapl_data = self.scraper.get_ticker_data("AAPL")
        self.assertIsNotNone(aapl_data)
        self.assertEqual(aapl_data.ticker, "AAPL")
    
    def test_clear_all(self):
        """Test clearing all data"""
        # Add multiple tickers
        self.scraper.add_ticker("AAPL")
        self.scraper.add_ticker("GOOGL")
        self.assertEqual(len(self.scraper.get_ticker_list()), 2)
        
        # Clear all
        self.scraper.clear_all()
        self.assertEqual(len(self.scraper.get_ticker_list()), 0)
    
    def test_export_data(self):
        """Test data export"""
        # Add a ticker
        self.scraper.add_ticker("AAPL")
        
        # Test JSON export
        json_file = self.scraper.export_data("json")
        self.assertTrue(os.path.exists(json_file))
        
        # Test CSV export
        csv_file = self.scraper.export_data("csv")
        self.assertTrue(os.path.exists(csv_file))
        
        # Clean up export files
        try:
            os.remove(json_file)
            os.remove(csv_file)
        except:
            pass
    
    def test_stats(self):
        """Test statistics"""
        stats = self.scraper.get_stats()
        self.assertIn('total_tickers', stats)
        self.assertIn('cached_tickers', stats)
        self.assertIn('data_sources', stats)
        self.assertIn('source_count', stats)
    
    def test_financial_data(self):
        """Test FinancialData class"""
        data = FinancialData(ticker="TEST", company_name="Test Company", price="100.00")
        
        # Test validation
        self.assertTrue(data.is_valid())
        
        # Test dict conversion
        data_dict = data.to_dict()
        self.assertIsInstance(data_dict, dict)
        self.assertEqual(data_dict['ticker'], "TEST")
        
        # Test from_dict
        new_data = FinancialData.from_dict(data_dict)
        self.assertEqual(new_data.ticker, "TEST")
        self.assertEqual(new_data.company_name, "Test Company")
    
    def test_available_features(self):
        """Test feature availability check"""
        features = get_available_features()
        self.assertIsInstance(features, dict)
        self.assertIn('json_export', features)
        self.assertIn('csv_export', features)
        self.assertTrue(features['json_export'])
        self.assertTrue(features['csv_export'])


if __name__ == '__main__':
    print("Running FinScraper tests...")
    unittest.main(verbosity=2) 