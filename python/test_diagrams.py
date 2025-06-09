#!/usr/bin/env python3
"""Unit tests for Mille visualization utilities and diagrams."""

import unittest
from diagrams import Diagram
from diagrams.aws.compute import EC2


class TestDiagrams(unittest.TestCase):
    """Basic tests to ensure the diagrams environment works."""

    def test_basic_diagram(self):
        """Ensure a simple diagram can be created without errors."""
        with Diagram("Test", show=False):
            EC2("web")

    def test_mille_viz_import(self):
        """Ensure the mille_viz package can be imported."""
        from mille_viz import DiagramRenderer, parse_tf_plan, get_supported_providers  # noqa: F401

    def test_diagram_renderer(self):
        """Instantiate DiagramRenderer for all supported providers."""
        from mille_viz import DiagramRenderer
        for provider in ["aws", "azure", "gcp"]:
            DiagramRenderer(provider=provider)


class TestUtils(unittest.TestCase):
    """Tests for helper utilities."""

    def test_parse_tf_plan_missing_file(self):
        from mille_viz import parse_tf_plan
        with self.assertRaises(FileNotFoundError):
            parse_tf_plan("nonexistent.json")


if __name__ == "__main__":
    unittest.main()
