"""Core functionality for the spark_helper package."""

from typing import Optional
import importlib
import importlib.resources
import os
import sys
import yaml
from textwrap import dedent

from pyspark.sql import SparkSession


# these are system-level default configurations
# that can be overridden by user-defined configurations
SYSTEM_LEVEL_CONFIG_YAML = dedent("""
    # System related settings
    spark.network.timeout: "300s"  # Network timeout for Spark jobs
    spark.executor.heartbeatInterval: "60s"  # Heartbeat interval for executors
    spark.broadcast.compress: "true"  # Enable compression for broadcast variables
    spark.sql.adaptive.enabled: "true"  # Enable adaptive query execution
""")

ENDING_CONFIG_YAML = dedent("""
    # additional Spark configuration can be added here
    # Example: Enable Hive support
    # spark.sql.catalogImplementation: "hive"
""")


def create_spark_session(config_path: str) -> SparkSession:
    """
    Create a SparkSession using configuration from a YAML file.

    Loads Spark configuration from the specified YAML file, applies user-defined and system-level
    settings, and returns a configured SparkSession. User-defined settings in the YAML file take
    precedence over system-level defaults.

    Args:
        config_path (str): Path to the YAML configuration file.

    Returns:
        SparkSession: A configured SparkSession instance.

    Raises:
        FileNotFoundError: If the configuration file does not exist.
        ValueError: If the YAML configuration cannot be parsed.

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

    builder = SparkSession.builder

    # App name and master
    app_name = config.pop("appName", "DefaultSparkApp")
    builder = builder.appName(app_name)

    master = config.pop("master", "local[*]")
    builder = builder.master(master)

    # Set system-level configurations
    system_level_config = yaml.safe_load(SYSTEM_LEVEL_CONFIG_YAML)
    for key, value in system_level_config.items():
        # check if the key is already in the config, i.e., user-defined config
        # takes precedence over system-level config
        if key not in config:
            config[key] = value

    # Set other configurations
    builder = builder.config(map=config)

    # Create and return the SparkSession
    return builder.getOrCreate()


def create_config_yaml(type: str = "local", detail: str = "user", file_name: Optional[str] = None) -> None:
    """
    Creates a Spark configuration YAML file from a template resource.

    This function loads a YAML template resource from the 'spark_helper' package, optionally appends system-level
    configuration, and writes the result to a specified file or outputs it to stdout.

    Args:
        type (str, optional): The type of Spark configuration template to use (e.g., "local"). Defaults to "local".
        detail (str, optional): The level of detail to include in the configuration ("user" or "all"). If "all",
            appends system-level config. Defaults to "user".
        file_name (Optional[str], optional): The path to the output file. If None, outputs to stdout. Defaults to None.

    Raises:
        ImportError: If the 'spark_helper' package cannot be imported.
        FileNotFoundError: If the specified template resource is not found in the package.
        RuntimeError: If any other error occurs while accessing or writing the resource.

    Examples:
        >>> create_config_yaml(type="local", detail="user", file_name="config.yaml")
        >>> create_config_yaml(type="local", detail="all")
    """

    try:
        # Import the package and spark config template
        package = importlib.import_module("spark_helper")
        resource_name = f"spark_config_{type}_template.yaml"
        resource = importlib.resources.files(package).joinpath(resource_name)

        # Check if the resource exists
        if not resource.is_file():
            raise FileNotFoundError(f"Resource '{resource_name}' not found in package 'spark_helper'")

        # read the spark config template
        with resource.open("r", encoding="utf-8") as f:
            content = f.read()

            # add system-level config if detail is "all"
            if type != "local" and detail == "all":
                content = content + "\n" + SYSTEM_LEVEL_CONFIG_YAML

            # add ending comment about adding additional configurations
            if type != "local":
                content = content + "\n" + ENDING_CONFIG_YAML

            # write to file or stdout
            if file_name:
                with open(file_name, "w", encoding="utf-8") as out_file:
                    out_file.write(content)
            else:
                sys.stdout.write(content)

    except ImportError:
        raise ImportError("Could not import package 'spark_helper'")
    except Exception as e:
        raise RuntimeError(f"Error accessing resource: {str(e)}")
