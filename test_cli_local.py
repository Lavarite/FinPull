#!/usr/bin/env python3
"""
Test the CLI interface locally before publishing to PyPI
"""

import subprocess
import sys
import os

def run_command(cmd):
    """Run a command and show the output"""
    print(f"\n🔍 Running: {cmd}")
    print("-" * 50)
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, cwd=os.getcwd())
        if result.stdout:
            print(result.stdout)
        if result.stderr:
            print("STDERR:", result.stderr)
        return result.returncode == 0
    except Exception as e:
        print(f"Error: {e}")
        return False

def main():
    print("🧪 Testing FinScraper CLI Locally")
    print("=" * 60)
    
    # Install in development mode
    print("\n📦 Installing package in development mode...")
    if not run_command("pip install -e ."):
        print("❌ Failed to install package")
        return False
    
    # Test basic commands
    tests = [
        ("finscraper --help", "Help command"),
        ("finscraper add AAPL", "Add ticker"),
        ("finscraper list", "List tickers"),
        ("finscraper show AAPL", "Show detailed view"),
        ("finscraper show --summary", "Show summary"),
        ("finscraper stats", "Show statistics"),
        ("finscraper export --format json", "Export to JSON"),
    ]
    
    print("\n🧪 Running CLI Tests:")
    success_count = 0
    
    for cmd, description in tests:
        print(f"\n📋 Test: {description}")
        if run_command(cmd):
            print("✅ PASSED")
            success_count += 1
        else:
            print("❌ FAILED")
    
    print(f"\n🎯 Test Results: {success_count}/{len(tests)} passed")
    
    if success_count == len(tests):
        print("🎉 All tests passed! Ready for PyPI publishing.")
    else:
        print("⚠️  Some tests failed. Fix issues before publishing.")
    
    print("\n📖 Available Commands After Publishing:")
    print("  finscraper add AAPL              # Add Apple stock")
    print("  finscraper show AAPL             # Show detailed table")
    print("  finscraper show --summary        # Show summary table")
    print("  finscraper export --format xlsx  # Export to Excel")
    print("  finscraper refresh               # Refresh all data")
    print("  finscraper --interactive         # Interactive mode")
    print("  finscraper --gui                 # GUI mode")

if __name__ == "__main__":
    main() 