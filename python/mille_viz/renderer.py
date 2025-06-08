"""
Diagram Renderer Module

Handles the generation of infrastructure diagrams using the Diagrams library.
"""

from typing import Dict, List, Any, Optional
from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import VPC, Subnet
from diagrams.azure.compute import VirtualMachines
from diagrams.azure.database import SQLDatabases
from diagrams.gcp.compute import ComputeEngine
from diagrams.gcp.database import SQL


class DiagramRenderer:
    """
    Main class for rendering infrastructure diagrams from Terraform plan data.
    """
    
    def __init__(self, provider: str = "aws"):
        """
        Initialize the diagram renderer.
        
        Args:
            provider: Cloud provider (aws, azure, gcp)
        """
        self.provider = provider.lower()
        self.supported_providers = ["aws", "azure", "gcp"]
        
        if self.provider not in self.supported_providers:
            raise ValueError(f"Unsupported provider: {provider}. Supported: {self.supported_providers}")
    
    def render_diagram(self, plan_data: Dict[str, Any], output_file: str = "infrastructure", 
                      show: bool = False) -> str:
        """
        Render infrastructure diagram from Terraform plan data.
        
        Args:
            plan_data: Parsed Terraform plan data
            output_file: Output file name (without extension)
            show: Whether to display the diagram
            
        Returns:
            Path to the generated diagram file
        """
        with Diagram(f"{output_file.title()} Infrastructure", filename=output_file, show=show):
            resources = self._create_resources(plan_data)
            self._connect_resources(resources, plan_data)
        
        return f"{output_file}.png"
    
    def _create_resources(self, plan_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create diagram resources based on Terraform plan data.
        
        Args:
            plan_data: Parsed Terraform plan data
            
        Returns:
            Dictionary of created resources
        """
        resources = {}
        
        if "resource_changes" not in plan_data:
            return resources
        
        for resource in plan_data["resource_changes"]:
            resource_type = resource.get("type", "")
            resource_name = resource.get("name", "")
            
            if resource_type in self._get_resource_mapping():
                diagram_resource = self._get_resource_mapping()[resource_type]
                resources[f"{resource_type}.{resource_name}"] = diagram_resource(resource_name)
        
        return resources
    
    def _connect_resources(self, resources: Dict[str, Any], plan_data: Dict[str, Any]) -> None:
        """
        Connect resources based on dependencies in the plan data.
        
        Args:
            resources: Created diagram resources
            plan_data: Parsed Terraform plan data
        """
        # This would implement connection logic based on resource dependencies
        # For now, this is a placeholder for future implementation
        pass
    
    def _get_resource_mapping(self) -> Dict[str, Any]:
        """
        Get mapping of Terraform resource types to Diagrams components.
        
        Returns:
            Dictionary mapping resource types to diagram components
        """
        if self.provider == "aws":
            return {
                "aws_instance": EC2,
                "aws_db_instance": RDS,
                "aws_vpc": VPC,
                "aws_subnet": Subnet,
            }
        elif self.provider == "azure":
            return {
                "azurerm_virtual_machine": VirtualMachines,
                "azurerm_sql_database": SQLDatabases,
            }
        elif self.provider == "gcp":
            return {
                "google_compute_instance": ComputeEngine,
                "google_sql_database_instance": SQL,
            }
        
        return {}