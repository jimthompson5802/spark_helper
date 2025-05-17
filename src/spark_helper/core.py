"""Core functionality for the spark_helper package."""

from typing import Optional
import importlib
import importlib.resources
import os
import sys
import yaml

from pyspark.sql import SparkSession


def create_spark_session(config_path: str) -> SparkSession:
    """
    Create a SparkSession based on configuration from a YAML file.

    This function reads a YAML configuration file and uses it to configure and create a
    SparkSession. The YAML file should contain Spark configuration parameters as shown in the
    template.

    Args:
        config_path: Path to the YAML configuration file

    Returns:
        SparkSession: Configured Spark session

    Raises:
        FileNotFoundError: If the config file doesn't exist
        ValueError: If the config file is invalid or missing required fields

    Examples:
        >>> spark = create_spark_session("config.yaml")
    """
    # Check if file exists
    if not os.path.isfile(config_path):
        raise FileNotFoundError(f"Configuration file not found: {config_path}")

    # Read the YAML file
    try:
        with open(config_path, "r") as f:
            config = yaml.safe_load(f)
    except Exception as e:
        raise ValueError(f"Failed to parse YAML configuration: {str(e)}")

    # Start building SparkSession
    builder = SparkSession.builder

    # Set app name if provided
    app_name = config.get("appName", "SparkApplication")
    builder = builder.appName(app_name)

    # Set master if provided
    master = config.get("master")
    if master:
        builder = builder.master(master)

    # Apply all other Spark configurations
    for key, value in config.items():
        # Skip non-configuration keys that we handle separately
        if key in ["appName", "master"]:
            continue

        # Check if it's a direct spark configuration (starts with 'spark.')
        if isinstance(key, str) and key.startswith("spark."):
            builder = builder.config(key, value)

    # Create and return the SparkSession
    return builder.getOrCreate()


def create_config_yaml(file_name: Optional[str] = None) -> None:
    """
    Generates a spark configuration YAML and write its contents to file_name or stdout.

    If file_name is None, output goes to stdout.

    Args:
        file_name: Optional; the name of the generated config file.

    Raises:
        FileNotFoundError: If the specified file cannot be found in the package
        ImportError: If the specified package cannot be imported

    Examples:
        >>> create_config_yaml()
        >>> create_config_yaml("custom_config.yaml")
    """
    try:
        package = importlib.import_module("spark_helper")
        resource_name = "spark_config_template.yaml"

        resource = importlib.resources.files(package).joinpath(resource_name)
        if not resource.is_file():
            raise FileNotFoundError(f"Resource '{resource_name}' not found in package 'spark_helper'")
        with resource.open("r", encoding="utf-8") as f:
            content = f.read()
            if file_name:
                with open(file_name, "w", encoding="utf-8") as out_file:
                    out_file.write(content)
            else:
                sys.stdout.write(content)
    except ImportError:
        raise ImportError("Could not import package 'spark_helper'")
    except Exception as e:
        raise RuntimeError(f"Error accessing resource: {str(e)}")
