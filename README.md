# Spark Helper

A Python package to simplify working with Apache Spark by providing utilities for SparkSession creation and configuration management.

## Features

- Simple SparkSession creation from YAML configuration files
- Generate template YAML configuration files for Spark applications
- Command-line interface for generating Spark configurations
- Type hints and comprehensive documentation throughout

## Installation

### From source

```bash
# Clone the repository
git clone https://github.com/yourusername/spark_helper.git
cd spark_helper

# create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install the package in development mode
pip install -e .

# Or install with development dependencies
pip install -e ".[dev]"
```

## Usage

### Configuration File Support

Create a SparkSession using a YAML configuration file:

```python
from spark_helper.core import create_spark_session

# Create a SparkSession from a YAML configuration
spark = create_spark_session("config.yaml")
```

Generate a template configuration file:

```python
from spark_helper.core import create_config_yaml

# Generate and save a template configuration
create_config_yaml("my_config.yaml")
```

Or use the command-line tool:

```bash
# Generate a config file
generate-spark-config --file_path my_config.yaml
```

#### Default Confguration File

```yaml
# Spark Application Configuration Template
# This template provides common configuration parameters for Spark applications

# User-specific configurations
# Application information
appName: "SparkHelperApp"

# Spark Master 
# Use local[*] for local development
# for standalone mode, use spark://spark-master:7077
# for yar
master: "local[*]"

# deployment mode
spark.submit.deployMode: "client"  # or "cluster"
  
# Spark Driver settings
spark.driver.memory: "4g" # Memory allocated for the driver
spark.driver.cores: 2 # Number of cores for the driver
spark.driver.maxResultSize: "1g" # Maximum size of the result that can be collected to the driver
spark.driver.pythonVersion: "3.11"  # Python version for PySpark

# Spark Executor settings
spark.executor.memory: "4g" #
spark.executor.cores: 2 # Number of cores per executor
spark.executor.instances: 2 # Number of executors
spark.executor.pythonVersion: "3.11"  # Python version for PySpark

# System related settings
spark.network.timeout: "300s"  # Network timeout for Spark jobs
spark.executor.heartbeatInterval: "60s"  # Heartbeat interval for executors
spark.broadcast.compress: "true"  # Enable compression for broadcast variables
spark.sql.adaptive.enabled: "true"  # Enable adaptive query execution
  
# additional Spark configuration can be added here
# Example: Enable Hive support
# spark.sql.catalogImplementation: "hive"
```

The user is now able to modify the configuration file to suit their needs. Using the function `create_spark_session()` the user starts a SparkSession passing in the configuration file with the desired settings

### Example Script

The package includes an example script that demonstrates how to use the package:

```bash
# Run the example script
python example.py
```

This will:
1. Generate a custom configuration file
2. Create a SparkSession using that configuration
3. Display information about the SparkSession and its configuration

## Development

### Set up development environment

```bash
# Install development dependencies
pip install -e ".[dev]"

# Run tests
pytest

# Format code
black src tests
isort src tests

# Lint code
flake8 src tests

# Check types
mypy src
```

## Documentation

- [User Guide](docs/index.md)
- [Getting Started](docs/getting_started.md)
- [Module Reference](docs/modules.md)

## License

MIT
