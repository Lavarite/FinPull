#!/usr/bin/env python3
"""
Script to help publish FinScraper to PyPI
"""

import subprocess
import sys
import os

def run_command(cmd, show_output=True):
    """Run a command and return success status"""
    if show_output:
        print(f"🔍 Running: {cmd}")
    try:
        result = subprocess.run(cmd, shell=True, check=True, capture_output=not show_output, text=True)
        if not show_output and result.stdout:
            print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Command failed: {e}")
        if not show_output and e.stderr:
            print(f"Error: {e.stderr}")
        return False

def check_requirements():
    """Check if required tools are installed"""
    print("🔍 Checking requirements...")
    
    required_packages = ['build', 'twine']
    missing = []
    
    for package in required_packages:
        try:
            __import__(package)
            print(f"✅ {package} is installed")
        except ImportError:
            missing.append(package)
            print(f"❌ {package} is missing")
    
    if missing:
        print(f"\n📦 Installing missing packages: {', '.join(missing)}")
        cmd = f"pip install {' '.join(missing)}"
        return run_command(cmd)
    
    return True

def build_package():
    """Build the package"""
    print("\n🏗️  Building package...")
    
    # Clean previous builds
    if os.path.exists('dist'):
        print("🧹 Cleaning previous builds...")
        run_command("rm -rf dist build *.egg-info", show_output=False)
    
    # Build package
    return run_command("python -m build")

def upload_to_pypi(test=True):
    """Upload package to PyPI"""
    repo = "testpypi" if test else "pypi"
    repo_url = "https://test.pypi.org/legacy/" if test else "https://upload.pypi.org/legacy/"
    
    print(f"\n📤 Uploading to {'Test ' if test else ''}PyPI...")
    
    cmd = f"python -m twine upload --repository-url {repo_url} dist/*"
    return run_command(cmd)

def main():
    print("🚀 FinScraper PyPI Publishing Tool")
    print("=" * 60)
    
    # Check if setup.py exists
    if not os.path.exists('setup.py'):
        print("❌ setup.py not found. Make sure you're in the project root.")
        return False
    
    print("⚠️  Before publishing, make sure you've updated:")
    print("   1. setup.py: author, author_email, url")
    print("   2. Package name (currently 'finscraper-pro')")
    print("   3. Version number if this is an update")
    print()
    
    confirm = input("Continue with publishing? (y/N): ").strip().lower()
    if confirm != 'y':
        print("Publishing cancelled.")
        return False
    
    # Step 1: Check requirements
    if not check_requirements():
        print("❌ Failed to install requirements")
        return False
    
    # Step 2: Build package
    if not build_package():
        print("❌ Failed to build package")
        return False
    
    # Step 3: Upload to Test PyPI first
    print("\n🧪 Uploading to Test PyPI first (recommended)...")
    test_choice = input("Upload to Test PyPI first? (Y/n): ").strip().lower()
    
    if test_choice != 'n':
        if upload_to_pypi(test=True):
            print("✅ Successfully uploaded to Test PyPI!")
            print("🔗 Check your package at: https://test.pypi.org/project/finscraper-pro/")
            print("\n📥 Test installation with:")
            print("   pip install -i https://test.pypi.org/simple/ finscraper-pro")
            print()
            
            test_install = input("Upload to real PyPI now? (y/N): ").strip().lower()
            if test_install != 'y':
                print("Stopping at Test PyPI. Upload to real PyPI manually when ready.")
                return True
        else:
            print("❌ Failed to upload to Test PyPI")
            return False
    
    # Step 4: Upload to real PyPI
    print("\n🚀 Uploading to real PyPI...")
    final_confirm = input("Are you sure you want to upload to real PyPI? (y/N): ").strip().lower()
    
    if final_confirm == 'y':
        if upload_to_pypi(test=False):
            print("🎉 Successfully published to PyPI!")
            print("🔗 Check your package at: https://pypi.org/project/finscraper-pro/")
            print("\n📥 Anyone can now install with:")
            print("   pip install finscraper-pro")
            print("\n📖 And use the CLI:")
            print("   finscraper add AAPL")
            print("   finscraper show AAPL")
            print("   finscraper export --format xlsx")
            return True
        else:
            print("❌ Failed to upload to PyPI")
            return False
    else:
        print("Real PyPI upload cancelled.")
        return True

if __name__ == "__main__":
    success = main()
    if not success:
        sys.exit(1) 