#!/usr/bin/env python3
"""
Simple demo script to test FinScraper functionality
"""

import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

def main():
    print("=== FinScraper Demo ===\n")
    
    try:
        # Test basic import
        from finscraper import FinancialDataScraper
        print("✓ Successfully imported FinancialDataScraper")
        
        # Test compatibility
        from finscraper.utils.compatibility import get_available_features
        features = get_available_features()
        print("✓ Available features:")
        for feature, available in features.items():
            status = "✓" if available else "✗"
            print(f"  {status} {feature.replace('_', ' ').title()}")
        
        # Create scraper instance
        print("\n✓ Creating scraper instance...")
        scraper = FinancialDataScraper()
        
        # Add a test ticker
        print("✓ Adding test ticker (AAPL)...")
        result = scraper.add_ticker("AAPL")
        if result:
            print("  - Successfully added AAPL")
        else:
            print("  - AAPL already exists")
        
        # Get data
        print("✓ Retrieving data...")
        data_list = scraper.get_all_data()
        if data_list:
            for data in data_list:
                print(f"  - {data.ticker}: {data.company_name} - ${data.price} (P/E: {data.pe_ratio})")
        else:
            print("  - No data available")
        
        # Export test
        print("✓ Testing export...")
        try:
            json_file = scraper.export_data("json")
            print(f"  - JSON export: {json_file}")
            csv_file = scraper.export_data("csv") 
            print(f"  - CSV export: {csv_file}")
        except Exception as e:
            print(f"  - Export error: {e}")
        
        # Statistics
        print("✓ Getting statistics...")
        stats = scraper.get_stats()
        print(f"  - Total tickers: {stats['total_tickers']}")
        print(f"  - Data sources: {stats['source_count']}")
        
        print("\n=== Demo completed successfully! ===")
        
    except Exception as e:
        print(f"✗ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main() 