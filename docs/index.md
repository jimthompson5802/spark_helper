# Spark Helper Documentation

## Overview

Spark Helper is a Python package that provides utilities for working with Apache Spark configurations. It focuses on simplifying SparkSession creation through YAML-based configuration files, supporting both local development and cluster deployment with system-level default configurations that can be overridden by user settings.

## Installation

```bash
pip install spark-helper
```

Or for development:

```bash
pip install -e ".[dev]"
```

For more detailed setup instructions, see the [Getting Started Guide](getting_started.md).

## Core Features

### SparkSession Management

The `core.py` module provides utilities for creating SparkSessions from either YAML configuration files or dictionaries:

```python
from spark_helper.core import create_spark_session

# Create a SparkSession from a YAML configuration file
spark = create_spark_session("spark_config.yaml")

# OR create from a dictionary with 'type' parameter
spark = create_spark_session({
    "type": "local",  # Required to specify which template to use
    "appName": "MySparkApp",
    "spark.executor.memory": "2g"
})
```

### Configuration File Support

#### System-Level and User-Defined Configurations

The package provides a two-tier configuration system:
1. **System-level configurations**: Default settings for Spark that are applied automatically
2. **User-defined configurations**: Custom settings that override the system defaults

This approach ensures that important settings are always present while allowing for customization.

#### Generating Configuration Files

The package provides utilities to generate template configuration files for different Spark deployment types:

```python
from spark_helper.core import create_config_yaml

# Print a local template configuration to stdout
create_config_yaml(type="local")

# Save a local template configuration to a file
create_config_yaml(type="local", detail="user", file_name="my_local_config.yaml")

# Generate a cluster configuration with all settings (including system level)
create_config_yaml(type="cluster", detail="all", file_name="cluster_config.yaml")
```

The `create_config_yaml` function supports these parameters:
- `type`: The type of configuration template ("local" or "cluster")
- `detail`: Detail level ("user" for basic settings, "all" for including system-level settings)
- `file_name`: Optional path to save the configuration (if None, outputs to stdout)

You can also use the command-line tool:

```bash
# Print template to stdout
generate-spark-config

# Save local template to file
generate-spark-config --type local --file_path my_local_config.yaml

# Generate a cluster config with all details
generate-spark-config --type cluster --detail all --file_path cluster_config.yaml
```

#### Sample Configuration Files

##### Local Configuration

```yaml
# Spark Application Configuration Template for Local Spark
# Application information
appName: "SparkHelperApp"

# Spark Master 
master: "local[*]"

# deployment mode
spark.submit.deployMode: "client"  # or "cluster"
  
# Spark Driver settings
spark.driver.memory: "4g"
spark.driver.cores: 2
spark.driver.maxResultSize: "1g"
spark.driver.pythonVersion: "3.11"

# Spark Executor settings
spark.executor.memory: "4g"
spark.executor.cores: 2
spark.executor.instances: 2
spark.executor.pythonVersion: "3.11"
```

##### Cluster Configuration

```yaml
# Spark Application Configuration Template for Standalone Cluster
# Application information
appName: "SparkHelperApp"

# Spark Master 
master: "spark://spark-master:7077"

# deployment mode
spark.submit.deployMode: "client"  # or "cluster"
  
# Spark Driver settings
spark.driver.memory: "4g"
spark.driver.cores: 2
spark.driver.maxResultSize: "1g"
spark.driver.pythonVersion: "3.11"

# Spark Executor settings
spark.executor.memory: "4g"
spark.executor.cores: 2
spark.executor.instances: 2
spark.executor.pythonVersion: "3.11"
```

##### System-Level Configurations

These settings are applied by default unless overridden:

```yaml
# System related settings
spark.network.timeout: "300s"  # Network timeout for Spark jobs
spark.executor.heartbeatInterval: "60s"  # Heartbeat interval for executors
spark.broadcast.compress: "true"  # Enable compression for broadcast variables
spark.sql.adaptive.enabled: "true"  # Enable adaptive query execution
```

## Example Script

The package includes an example script demonstrating how to use the package:

```python
from spark_helper.core import create_config_yaml, create_spark_session

# Generate a config file
config_file = "custom_config.yaml"
create_config_yaml(config_file)

# Create a SparkSession using the config
spark = create_spark_session(config_file)

# Get configuration values
app_name = spark.conf.get('spark.app.name')
print(f"Created SparkSession with app name: {app_name}")

# View active configuration
for item in sorted(spark.sparkContext.getConf().getAll()):
    print(f"{item[0]}: {item[1]}")

# Stop the session
spark.stop()
```

You can run this example using:

```bash
python example.py
```

## Docker Integration

The package comes with Docker support for running a standalone Spark cluster for testing and development.

### Starting the Spark Cluster

```bash
docker-compose up -d
```

This command starts:
- A Spark master
- Multiple Spark worker nodes
- A Jupyterlab server accessible at `http://localhost:8888`

### Monitoring Your Application

Once a Spark application is running, you can monitor it through the Spark UI at `http://localhost:4040`.

### Stopping the Cluster

```bash
docker-compose down
```

## Development

### Running Tests

```bash
# Run all tests
pytest
```

### Code Style

This project uses:
- Black for code formatting
- isort for import sorting
- flake8 for linting
- mypy for type checking

Run them with:

```bash
black src tests
isort src tests
flake8 src tests
mypy src
```

## API Documentation

For detailed documentation of the package modules and functions, see [Module Reference](modules.md).
