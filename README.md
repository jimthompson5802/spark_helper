# Spark Helper

A Python package to simplify working with Apache Spark.

## Features

- Easy SparkSession creation with customizable configurations
- YAML-based configuration for Spark applications
- Helper functions for common Spark operations
- Command-line interface for basic Spark tasks

## Installation

### From source

```bash
# Clone the repository
git clone https://github.com/yourusername/spark_helper.git
cd spark_helper

# Install the package in development mode
pip install -e .

# Or install with development dependencies
pip install -e ".[dev]"
```

## Usage

### Basic usage

```python
from spark_helper.core import get_spark_session

# Create a basic SparkSession
spark = get_spark_session(app_name="MySparkApp")

# Create a SparkSession with custom configuration
config = {
    "spark.executor.memory": "4g",
    "spark.executor.cores": "2",
    "spark.driver.memory": "2g"
}
spark = get_spark_session(app_name="CustomSparkApp", config=config)

# Use helper functions
from spark_helper.core import read_csv
df = read_csv(spark, "path/to/data.csv")
```

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
spark-config --file_path my_config.yaml
```

### Command Line Interface

```bash
# Run the CLI tool
python -m spark_helper.cli --app-name "MySpark"
```

## Development

### Set up development environment

```bash
# Install development dependencies
pip install -e ".[dev]"

# Run tests
pytest

# Run tests including those that require Spark
pytest --run-spark

# Format code
black src tests
isort src tests
```

## License

MIT
