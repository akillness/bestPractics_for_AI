#!/usr/bin/env python3
"""
Simplified Lemonade SDK Demo
This example demonstrates how to directly use the Lemonade SDK without the server
"""

import sys
import os

# Add lemonade SDK to path
sys.path.insert(0, '/Users/jangyoung/.pyenv/versions/3.11.5/lib/python3.11/site-packages')

def demo_lemonade_tools():
    """Demonstrate lemonade tools directly"""
    print("🍋 Lemonade SDK Direct Usage Demo")
    print("=" * 40)
    
    try:
        # Import lemonade API
        import lemonade
        print("✅ Lemonade SDK imported successfully!")
        print(f"Version: {lemonade.__version__ if hasattr(lemonade, '__version__') else 'Unknown'}")
        
        # List available tools
        print("\n🔧 Available lemonade tools:")
        # Use the CLI interface to show available tools
        os.system('lemonade --help')
        
        return True
        
    except ImportError as e:
        print(f"❌ Failed to import lemonade: {e}")
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def demo_server_info():
    """Show server-related information and commands"""
    print("\n🖥️  Lemonade Server Commands:")
    print("-" * 30)
    
    # Show server help
    print("Available server commands:")
    os.system('lemonade-server-dev --help')
    
    print("\n📋 Available models:")
    os.system('lemonade-server-dev list')

def main():
    """Main demo function"""
    print("🍋 Lemonade SDK Comprehensive Demo")
    print("=" * 50)
    
    # Demonstrate direct SDK usage
    success = demo_lemonade_tools()
    
    if success:
        print("\n" + "=" * 50)
        # Show server information
        demo_server_info()
        
        print("\n🎯 Summary:")
        print("✅ Lemonade SDK has been successfully installed and configured")
        print("✅ Direct SDK tools are available via 'lemonade' command")
        print("✅ Server tools are available via 'lemonade-server-dev' command")
        print("\n📚 To get started:")
        print("1. Download a model: lemonade-server-dev pull <model-name>")
        print("2. Start server: lemonade-server-dev run <model-name>") 
        print("3. Use the OpenAI-compatible API at http://localhost:8000/api/v1")
        
        return True
    else:
        print("❌ Demo failed - SDK not properly installed")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)