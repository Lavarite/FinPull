#!/usr/bin/env python3
"""
Batch processing example for FinScraper
"""

import sys
import os

# Add the src directory to the path to import finscraper
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from finscraper.utils.batch import batch_fetch_tickers, get_ticker_performance_summary
from finscraper.utils.compatibility import get_available_features

def main():
    print("=== FinScraper Batch Processing Example ===\n")
    
    # Check available features
    features = get_available_features()
    print("Available features:")
    for feature, available in features.items():
        status = "✓" if available else "✗"
        print(f"  {status} {feature.replace('_', ' ').title()}")
    print()
    
    # Define list of tickers to process
    tech_stocks = ["AAPL", "GOOGL", "MSFT", "AMZN", "META", "NVDA", "TSLA"]
    financial_stocks = ["JPM", "BAC", "WFC", "C", "GS"]
    
    print("=== Processing Tech Stocks ===")
    tech_data = batch_fetch_tickers(tech_stocks)
    
    if tech_data:
        print(f"Successfully fetched {len(tech_data)}/{len(tech_stocks)} tech stocks:")
        for data in tech_data:
            print(f"  {data.ticker}: {data.company_name} - ${data.price}")
        
        # Get performance summary
        tech_summary = get_ticker_performance_summary(tech_data)
        print(f"\nTech stocks summary:")
        print(f"  Average P/E: {tech_summary.get('avg_pe_ratio', 'N/A')}")
        print(f"  Average Price: ${tech_summary.get('avg_price', 'N/A')}")
        print(f"  Sectors: {list(tech_summary.get('sectors', {}).keys())}")
    
    print("\n=== Processing Financial Stocks ===")
    financial_data = batch_fetch_tickers(financial_stocks)
    
    if financial_data:
        print(f"Successfully fetched {len(financial_data)}/{len(financial_stocks)} financial stocks:")
        for data in financial_data:
            print(f"  {data.ticker}: {data.company_name} - ${data.price}")
        
        # Get performance summary
        financial_summary = get_ticker_performance_summary(financial_data)
        print(f"\nFinancial stocks summary:")
        print(f"  Average P/E: {financial_summary.get('avg_pe_ratio', 'N/A')}")
        print(f"  Average Price: ${financial_summary.get('avg_price', 'N/A')}")
        print(f"  Sectors: {list(financial_summary.get('sectors', {}).keys())}")
    
    # Combined analysis
    all_data = tech_data + financial_data
    if all_data:
        print(f"\n=== Combined Analysis ({len(all_data)} stocks) ===")
        combined_summary = get_ticker_performance_summary(all_data)
        
        print(f"Overall statistics:")
        print(f"  Total tickers: {combined_summary['total_tickers']}")
        print(f"  Average P/E: {combined_summary.get('avg_pe_ratio', 'N/A')}")
        print(f"  Average Price: ${combined_summary.get('avg_price', 'N/A')}")
        
        if 'pe_range' in combined_summary and combined_summary['pe_range']:
            pe_min, pe_max = combined_summary['pe_range']
            print(f"  P/E Range: {pe_min:.1f} - {pe_max:.1f}")
        
        if 'price_range' in combined_summary and combined_summary['price_range']:
            price_min, price_max = combined_summary['price_range']
            print(f"  Price Range: ${price_min:.2f} - ${price_max:.2f}")
        
        print(f"  Sector distribution:")
        for sector, count in combined_summary.get('sectors', {}).items():
            print(f"    {sector}: {count}")

if __name__ == "__main__":
    main() 