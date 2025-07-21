"""
Configuration module for GuitarTrainer project.

Provides hierarchical, consolidated access to all project configuration settings.
Configuration files are organized by type (10-19 for project, 20-29 for infrastructure)
and consolidated into unified configuration objects.
"""

from .config_manager import (
    ConfigDict,
    ProjectConfig,
    InfrastructureConfig,
    ProjectConfigManager,
    InfrastructureConfigManager,
    get_project_config,
    get_infrastructure_config
)

__all__ = [
    'ConfigDict',
    'ProjectConfig',
    'InfrastructureConfig',
    'ProjectConfigManager',
    'InfrastructureConfigManager',
    'get_project_config',
    'get_infrastructure_config'
]
