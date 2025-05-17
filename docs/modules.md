# Module Reference

## `spark_helper.core`

The core module provides functions for creating and configuring SparkSessions.

### Functions

#### `create_spark_session(config_path: str) -> SparkSession`

Creates a SparkSession based on configuration from a YAML file.

**Parameters:**
- `config_path` (str): Path to the YAML configuration file

**Returns:**
- `SparkSession`: Configured Spark session

**Raises:**
- `FileNotFoundError`: If the config file doesn't exist
- `ValueError`: If the config file is invalid or missing required fields

**Example:**
```python
spark = create_spark_session("config.yaml")
```

#### `create_config_yaml(file_name: Optional[str] = None) -> None`

Generates a spark configuration YAML and write its contents to file_name or stdout.

**Parameters:**
- `file_name` (Optional[str]): Optional; the name of the generated config file. If None, output goes to stdout.

**Raises:**
- `FileNotFoundError`: If the specified file cannot be found in the package
- `ImportError`: If the specified package cannot be imported

**Example:**
```python
create_config_yaml()  # Output to stdout
create_config_yaml("custom_config.yaml")  # Write to file
```

## `spark_helper.generate_config`

Provides a command-line interface for generating Spark configuration templates.

### Functions

#### `main()`

Command line interface entry point for spark_helper.

**Returns:**
- `int`: Exit code (0 for success)

**Example Usage:**
```bash
generate-spark-config --file_path config.yaml
```

## Configuration Template

The default configuration template includes:

- Application name and master settings
- Driver configuration settings
- Executor configuration settings
- Python version settings

You can view the template with:
```bash
generate-spark-config
```
