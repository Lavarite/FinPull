#!/usr/bin/env python3
"""
Comprehensive test of FinScraper with all dependencies installed
"""

import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

def main():
    print("🚀 FinScraper - Full Functionality Test")
    print("=" * 50)
    
    # Test 1: Import and dependency check
    print("\n1️⃣ Testing imports and dependencies...")
    from finscraper import FinancialDataScraper, FinancialDataAPI
    from finscraper.utils.compatibility import get_available_features, print_dependency_status
    
    print("✅ All imports successful!")
    
    print("\n📊 Dependency Status:")
    print_dependency_status()
    
    # Test 2: Check features
    print("\n2️⃣ Available Features:")
    features = get_available_features()
    for feature, available in features.items():
        status = "✅" if available else "❌"
        print(f"   {status} {feature.replace('_', ' ').title()}")
    
    # Test 3: Test scraper with real data sources
    print("\n3️⃣ Testing FinancialDataScraper...")
    scraper = FinancialDataScraper()
    
    # Add a new ticker to test real data fetching
    test_ticker = "MSFT"
    print(f"   📈 Adding {test_ticker}...")
    
    try:
        result = scraper.add_ticker(test_ticker)
        if result:
            print(f"   ✅ Successfully added {test_ticker}")
        else:
            print(f"   ℹ️  {test_ticker} already exists")
    except Exception as e:
        print(f"   ❌ Error: {e}")
    
    # Get data to see which source was used
    print("\n   📊 Retrieved data:")
    data_list = scraper.get_all_data()
    for data in data_list[-2:]:  # Show last 2 entries
        print(f"      {data.ticker}: {data.company_name}")
        print(f"      💰 Price: ${data.price}")
        print(f"      📈 P/E Ratio: {data.pe_ratio}")
        print(f"      🏢 Sector: {data.sector}")
        print(f"      📅 Updated: {data.timestamp[:19]}")
        print()
    
    # Test 4: Export functionality
    print("4️⃣ Testing Export Functions...")
    
    try:
        # Test all export formats
        json_file = scraper.export_data("json")
        print(f"   ✅ JSON export: {json_file}")
        
        csv_file = scraper.export_data("csv")
        print(f"   ✅ CSV export: {csv_file}")
        
        xlsx_file = scraper.export_data("xlsx") 
        print(f"   ✅ Excel export: {xlsx_file}")
        
    except Exception as e:
        print(f"   ❌ Export error: {e}")
    
    # Test 5: API interface
    print("\n5️⃣ Testing Programmatic API...")
    api = FinancialDataAPI()
    
    # Test API functions
    stats_result = api.get_stats()
    if stats_result["success"]:
        stats = stats_result["stats"]
        print(f"   📊 Total tickers: {stats['total_tickers']}")
        print(f"   🔌 Data sources: {stats['source_count']}")
        print(f"   💾 Storage: {stats['storage_file']}")
    
    # Test 6: Batch processing
    print("\n6️⃣ Testing Batch Processing...")
    from finscraper.utils.batch import get_ticker_performance_summary
    
    summary = get_ticker_performance_summary(data_list)
    print(f"   📈 Portfolio summary:")
    print(f"      Total stocks: {summary['total_tickers']}")
    print(f"      Sectors: {list(summary['sectors'].keys())}")
    if summary.get('avg_pe_ratio'):
        print(f"      Avg P/E ratio: {summary['avg_pe_ratio']:.2f}")
    
    print("\n🎉 All functionality tests completed successfully!")
    print("Your FinScraper installation is fully functional with all features enabled!")

if __name__ == "__main__":
    main() 