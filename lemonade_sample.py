#!/usr/bin/env python3
"""
Lemonade SDK Sample Code
This example demonstrates how to use the Lemonade SDK to interact with local LLMs
through OpenAI-compatible API.
"""

from openai import OpenAI
import requests
import time
import sys

def check_server_status():
    """Check if the Lemonade server is running"""
    try:
        response = requests.get("http://localhost:8000/api/v1/models", timeout=5)
        return response.status_code == 200
    except:
        return False

def main():
    print("🍋 Lemonade SDK Sample Application")
    print("=" * 40)
    
    # Check if server is running
    print("Checking if Lemonade server is running...")
    if not check_server_status():
        print("❌ Lemonade server is not running!")
        print("Please start the server with: lemonade-server run <model-name>")
        print("Example: lemonade-server run Llama-3.2-1B-Instruct-Hybrid")
        return False
    
    print("✅ Lemonade server is running!")
    
    # Initialize OpenAI client
    client = OpenAI(
        base_url="http://localhost:8000/api/v1",
        api_key="lemonade"  # Default API key for Lemonade
    )
    
    # Get available models
    try:
        print("\nFetching available models...")
        models = client.models.list()
        print(f"Available models: {len(models.data)}")
        for model in models.data:
            print(f"  - {model.id}")
    except Exception as e:
        print(f"Error fetching models: {e}")
        return False
    
    # Use the first available model
    if not models.data:
        print("No models available!")
        return False
    
    model_name = models.data[0].id
    print(f"\nUsing model: {model_name}")
    
    # Sample conversations
    test_prompts = [
        "What is the capital of France?",
        "Explain quantum computing in simple terms.",
        "Write a short Python function to calculate factorial."
    ]
    
    print("\n🤖 Starting conversations...")
    print("=" * 40)
    
    for i, prompt in enumerate(test_prompts, 1):
        print(f"\nQuery {i}: {prompt}")
        print("-" * 30)
        
        try:
            # Create completion
            completion = client.chat.completions.create(
                model=model_name,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=200,
                temperature=0.7
            )
            
            response = completion.choices[0].message.content
            print(f"Response: {response}")
            
            # Show token usage if available
            if completion.usage:
                print(f"Tokens used: {completion.usage.total_tokens}")
                
        except Exception as e:
            print(f"❌ Error: {e}")
        
        # Small delay between requests
        time.sleep(1)
    
    print("\n✅ Sample completed successfully!")
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)