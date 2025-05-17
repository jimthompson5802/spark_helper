# Spark Helper Documentation

## Overview

Spark Helper is a Python package that provides utilities and helper functions for working with Apache Spark. It aims to simplify common Spark operations and provide an easier API for various tasks.

## Installation

```bash
pip install spark-helper
```

Or for development:

```bash
pip install -e ".[dev]"
```

## Core Features

### SparkSession Management

The `core.py` module provides utilities for creating and managing SparkSessions:

```python
from spark_helper.core import get_spark_session

# Create a basic SparkSession
spark = get_spark_session(app_name="MySparkApp")

# Create a SparkSession with custom configuration
config = {
    "spark.executor.memory": "4g",
    "spark.executor.cores": "2"
}
spark = get_spark_session(app_name="CustomSparkApp", config=config)
```

### Configuration File Support

You can also create a SparkSession from a YAML configuration file:

```python
from spark_helper.core import create_spark_session

# Create a SparkSession from a YAML configuration file
spark = create_spark_session("spark_config.yaml")
```

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
spark-config

# Save template to file
spark-config --file_path my_config.yaml
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

### Data Reading Utilities

```python
from spark_helper.core import read_csv

# Read a CSV file
df = read_csv(spark, "path/to/file.csv", header=True, infer_schema=True)
```

## Command Line Interface

Spark Helper includes a command-line interface for quick tasks:

```bash
python -m spark_helper.cli --app-name "MySparkApp"
```

## Development

### Running Tests

```bash
# Run all tests
pytest

# Run tests including those that require Spark
pytest --run-spark
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
