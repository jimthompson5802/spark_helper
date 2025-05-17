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
