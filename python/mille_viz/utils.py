"""
Utility functions for the Mille visualization package.

Contains helper functions for parsing Terraform plans and other common operations.
"""

import json
from typing import Dict, List, Any, Optional


def parse_tf_plan(plan_file_path: str) -> Dict[str, Any]:
    """
    Parse a Terraform plan JSON file.
    
    Args:
        plan_file_path: Path to the Terraform plan JSON file
        
    Returns:
        Parsed plan data as a dictionary
        
    Raises:
        FileNotFoundError: If the plan file doesn't exist
        ValueError: If the file contains invalid JSON
    """
    try:
        with open(plan_file_path, 'r', encoding='utf-8') as f:
            plan_data = json.load(f)
        return plan_data
    except FileNotFoundError:
        raise FileNotFoundError(f"Terraform plan file not found: {plan_file_path}")
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON in plan file {plan_file_path}: {e}") from e


def get_supported_providers() -> List[str]:
    """
    Get list of supported cloud providers.
    
    Returns:
        List of supported provider names
    """
    return ["aws", "azure", "gcp"]


def extract_resources(plan_data: Dict[str, Any]) -> List[Dict[str, Any]]:
    """
    Extract resource information from Terraform plan data.
    
    Args:
        plan_data: Parsed Terraform plan data
        
    Returns:
        List of resource dictionaries
    """
    resources = []
    
    if "resource_changes" in plan_data:
        for resource_change in plan_data["resource_changes"]:
            if resource_change.get("change", {}).get("actions") == ["create"]:
                resources.append({
                    "type": resource_change.get("type"),
                    "name": resource_change.get("name"),
                    "address": resource_change.get("address"),
                    "values": resource_change.get("change", {}).get("after", {}),
                })
    
    return resources


def get_resource_dependencies(plan_data: Dict[str, Any]) -> Dict[str, List[str]]:
    """
    Extract resource dependencies from Terraform plan data.
    
    Args:
        plan_data: Parsed Terraform plan data
        
    Returns:
        Dictionary mapping resource addresses to their dependencies
    """
    dependencies = {}
    
    if "resource_changes" in plan_data:
        for resource_change in plan_data["resource_changes"]:
            address = resource_change.get("address", "")
            change = resource_change.get("change", {})
            
            # Extract dependencies from before_sensitive, after_sensitive, etc.
            # This is a simplified approach and may need refinement
            deps = []
            if "after" in change and isinstance(change["after"], dict):
                for key, value in change["after"].items():
                    if isinstance(value, str) and value.startswith("${"):
                        # This is a Terraform interpolation, extract referenced resources
                        # This is a basic implementation and would need more sophisticated parsing
                        deps.append(value)
            
            dependencies[address] = deps
    
    return dependencies


def validate_plan_format(plan_data: Dict[str, Any]) -> bool:
    """
    Validate that the plan data has the expected Terraform format.
    
    Args:
        plan_data: Parsed plan data to validate
        
    Returns:
        True if the format is valid, False otherwise
    """
    required_fields = ["format_version", "terraform_version"]
    
    for field in required_fields:
        if field not in plan_data:
            return False
    
    # Check for either planned_values or resource_changes
    if "planned_values" not in plan_data and "resource_changes" not in plan_data:
        return False
    
    return True