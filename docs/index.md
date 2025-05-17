# Spark Helper Documentation

## Overview

Spark Helper is a Python package that provides utilities for working with Apache Spark configurations. It focuses on simplifying SparkSession creation through YAML-based configuration files.

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

The `core.py` module provides utilities for creating SparkSessions from YAML configuration files:

```python
from spark_helper.core import create_spark_session

# Create a SparkSession from a YAML configuration file
spark = create_spark_session("spark_config.yaml")
```

### Configuration File Support

#### Generating Configuration Files

The package provides utilities to generate template configuration files:

```python
from spark_helper.core import create_config_yaml

# Print a template configuration to stdout
create_config_yaml()

# Save a template configuration to a file
create_config_yaml("my_config.yaml")
```

You can also use the command-line tool:

```bash
# Print template to stdout
generate-spark-config

# Save template to file
generate-spark-config --file_path my_config.yaml
```

#### Sample Configuration

```yaml
# Application information
appName: "SparkHelperApp"

# Spark Master 
master: "local[*]"

# deployment mode
spark.submit.deployMode: "client"  # or "cluster"
  
# Spark Driver settings
spark.driver.memory: "4g"
spark.driver.cores: 2

# Spark Executor settings
spark.executor.memory: "4g"
spark.executor.cores: 2
spark.executor.instances: 2
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
