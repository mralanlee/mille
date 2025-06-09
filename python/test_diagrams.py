#!/usr/bin/env python3
"""
Test script to verify Diagrams library functionality.

This script creates a simple diagram to ensure the Diagrams library
and Graphviz are properly installed and working.
"""

from diagrams import Diagram
from diagrams.aws.compute import EC2

def test_basic_diagram():
    """Test basic diagram creation."""
    try:
        with Diagram("Test", show=False):
            EC2("web")
        print("✓ Basic diagram test passed - Diagrams library is working!")
        return True
    except Exception as e:
        print(f"✗ Basic diagram test failed: {e}")
        return False

def test_mille_viz_import():
    """Test importing the mille_viz module."""
    try:
        from mille_viz import DiagramRenderer, parse_tf_plan, get_supported_providers
        print("✓ Mille visualization module import test passed!")
        return True
    except Exception as e:
        print(f"✗ Mille visualization module import test failed: {e}")
        return False

def test_diagram_renderer():
    """Test the DiagramRenderer class."""
    try:
        from mille_viz import DiagramRenderer
        
        # Test creating renderer for each supported provider
        for provider in ["aws", "azure", "gcp"]:
            renderer = DiagramRenderer(provider=provider)
            print(f"✓ DiagramRenderer for {provider} created successfully!")
        
        return True
    except Exception as e:
        print(f"✗ DiagramRenderer test failed: {e}")
        return False

def main():
    """Run all tests."""
    print("Running Mille visualization environment tests...\n")
    
    tests = [
        ("Basic Diagrams functionality", test_basic_diagram),
        ("Mille viz module import", test_mille_viz_import),
        ("DiagramRenderer class", test_diagram_renderer),
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"Running {test_name}...")
        if test_func():
            passed += 1
        print()
    
    print(f"Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! Python visualization environment is ready.")
        return 0
    else:
        print("❌ Some tests failed. Please check the installation.")
        return 1

if __name__ == "__main__":
    exit(main())
