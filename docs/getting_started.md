# Getting Started with Spark Helper

This guide walks through the basic steps to set up and use the Spark Helper package.

## Installation

Install the package from source:

```bash
# Clone the repository
git clone https://github.com/yourusername/spark_helper.git
cd spark_helper

# Install the package in development mode with development dependencies
pip install -e ".[dev]"
```

## Basic Usage

### Step 1: Generate a Configuration File

Generate a template Spark configuration file:

```python
from spark_helper.core import create_config_yaml

# Write a local configuration to a file
create_config_yaml(type="local", detail="user", file_name="my_spark_config.yaml")

# Or a cluster configuration with all details
create_config_yaml(type="cluster", detail="all", file_name="cluster_config.yaml")
```

Alternatively, use the command-line tool:

```bash
# Generate local configuration
generate-spark-config --type local --file_path my_spark_config.yaml

# Generate cluster configuration with all details
generate-spark-config --type cluster --detail all --file_path cluster_config.yaml
```

### Step 2: Customize the Configuration

Edit the generated YAML file to match your Spark environment requirements:

```yaml
# Example customizations
appName: "MySparkApplication"
master: "local[4]"  # Use 4 local cores
spark.driver.memory: "8g"
spark.executor.memory: "6g"
spark.executor.cores: 2
```

### Step 3: Create a SparkSession

You can create a SparkSession in two ways:

#### Option 1: From a configuration file

Use the configuration file to create a SparkSession:

```python
from spark_helper.core import create_spark_session

# Create a SparkSession using the config file
spark = create_spark_session("my_spark_config.yaml")

# Use the SparkSession
df = spark.read.csv("path/to/data.csv", header=True)
df.show()

# Stop the session when done
spark.stop()
```

#### Option 2: From a configuration dictionary

Create a SparkSession directly from a configuration dictionary:

```python
from spark_helper.core import create_spark_session

# Create a SparkSession using a dictionary
config = {
    "type": "local",  # Required - specifies which template to use
    "appName": "MySparkApplication",
    "master": "local[4]",
    "spark.driver.memory": "8g",
    "spark.executor.memory": "6g",
    "spark.executor.cores": 2
}
spark = create_spark_session(config)

# Use the SparkSession
df = spark.read.csv("path/to/data.csv", header=True)
df.show()

# Stop the session when done
spark.stop()
```

Note: The `type` key is required in the configuration dictionary to specify which template to use (either "local" or "cluster"). Your custom settings will override any template defaults.

## Next Steps

- Check the [Module Reference](modules.md) for detailed API documentation
- Run the example script to see the package in action: `python example.py`
- Look at the tests to understand expected behavior: `pytest tests/`
