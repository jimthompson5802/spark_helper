"""Tests for the spark_helper package."""

import os
import pytest
import yaml
import sys
from tempfile import NamedTemporaryFile
from io import StringIO

from spark_helper.core import create_spark_session, create_config_yaml


def test_create_spark_session_from_file():
    """Test creating a SparkSession from a YAML config file."""
    # Create a temporary config file
    config = {
        "appName": "TestYamlSession",
        "master": "local[*]",
        "spark.executor.memory": "3g",
        "spark.driver.memory": "2g",
        "spark.sql.shuffle.partitions": "10",
    }

    with NamedTemporaryFile(suffix=".yaml", mode="w") as temp_file:
        yaml.dump(config, temp_file)
        temp_path = temp_file.name

        # Create SparkSession from the config file
        spark = create_spark_session(temp_path)

        # Verify the session was created with correct configuration
        assert spark is not None
        assert spark.conf.get("spark.app.name") == "TestYamlSession"
        assert spark.conf.get("spark.master") == "local[*]"
        assert spark.conf.get("spark.executor.memory") == "3g"
        assert spark.conf.get("spark.driver.memory") == "2g"
        assert spark.conf.get("spark.sql.shuffle.partitions") == "10"

        spark.stop()


def test_create_spark_session_from_dict():
    """Test creating a SparkSession from a dictionary config."""
    # Create a config dictionary
    config = {
        "type": "local",
        "appName": "TestDictSession",
        "master": "local[*]",
        "spark.executor.memory": "4g",
        "spark.driver.memory": "2g",
        "spark.sql.shuffle.partitions": "12",
    }

    # Create SparkSession directly from the config dictionary
    spark = create_spark_session(config)

    # Verify the session was created with correct configuration
    assert spark is not None
    assert spark.conf.get("spark.app.name") == "TestDictSession"
    assert spark.conf.get("spark.master") == "local[*]"
    assert spark.conf.get("spark.executor.memory") == "4g"
    assert spark.conf.get("spark.driver.memory") == "2g"
    assert spark.conf.get("spark.sql.shuffle.partitions") == "12"

    spark.stop()


def test_create_spark_session_file_not_found():
    """Test that create_spark_session raises the correct exception for missing files."""
    with pytest.raises(FileNotFoundError):
        create_spark_session("nonexistent_config.yaml")


def test_create_spark_session_invalid_type():
    """Test that create_spark_session raises the correct exception for invalid input type."""
    with pytest.raises(TypeError):
        create_spark_session(123)  # Not a string or dictionary


@pytest.mark.parametrize("detail", ["user", "all"])
def test_create_config_yaml_stdout(detail):
    """Test that create_config_yaml writes to stdout when no file name is provided."""
    # Redirect stdout to capture the output
    old_stdout = sys.stdout
    mystdout = StringIO()
    sys.stdout = mystdout

    try:
        create_config_yaml(type="cluster", detail=detail)
        output = mystdout.getvalue()

        # Check if output contains some expected YAML content
        assert "appName:" in output
        assert "SparkHelperApp" in output
        assert "spark.driver.memory" in output
        assert "spark.executor.cores" in output
        if detail == "all":
            assert "spark.network.timeout" in output
        else:
            assert "spark.network.timeout" not in output
    finally:
        # Restore stdout
        sys.stdout = old_stdout


def test_create_config_yaml_file():
    """Test that create_config_yaml writes to a file when a file name is provided."""
    with NamedTemporaryFile(suffix=".yaml") as temp_file:
        temp_path = temp_file.name

        create_config_yaml(type="local", file_name=temp_path)

        # Check if the file was created and contains expected content
        assert os.path.exists(temp_path)

        with open(temp_path, "r") as f:
            content = f.read()
            assert "appName:" in content
            assert "master" in content

        # Create SparkSession from the config
        spark = create_spark_session(temp_path)

        # Verify the session was created with correct configuration
        assert spark is not None
        assert spark.conf.get("spark.app.name") == "SparkHelperApp"

        spark.stop()


@pytest.mark.parametrize("type", [("local", "local[*]"), ("cluster", "spark://spark-master:7077")])
def test_create_config_yaml_type(type):
    """Test that create_config_yaml handles different types correctly."""
    with NamedTemporaryFile(suffix=".yaml") as temp_file:
        temp_path = temp_file.name

        create_config_yaml(type=type[0], file_name=temp_path)

        # Check if the file was created and contains expected content
        assert os.path.exists(temp_path)

        # load the YAML file
        with open(temp_path, "r") as f:
            content = yaml.safe_load(f)
            assert content["appName"] == "SparkHelperApp"
            assert content["master"] == type[1]

            if type[0] == "local":
                assert "spark.driver.memory" not in content.keys()
            elif type[0] == "cluster":
                assert "spark.driver.memory" in content.keys()
                assert "spark.executor.cores" in content.keys()
                assert "spark.executor.instances" in content.keys()
