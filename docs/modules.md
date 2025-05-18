# Module Reference

## `spark_helper.core`

The core module provides functions for creating and configuring SparkSessions.

### Functions

#### `create_spark_session(config: Union[str, Dict[str, Any]]) -> SparkSession`

Creates a SparkSession based on configuration from either a YAML file or a configuration dictionary.

**Parameters:**
- `config` (Union[str, Dict[str, Any]]): Path to the YAML configuration file or a dictionary of configuration parameters

**Returns:**
- `SparkSession`: Configured Spark session

**Raises:**
- `FileNotFoundError`: If a config file path is provided but doesn't exist
- `ValueError`: If a config file path is provided but the file is invalid
- `TypeError`: If the config is neither a string nor a dictionary

**Examples:**
```python
# From a YAML file
spark = create_spark_session("config.yaml")

# From a dictionary
spark = create_spark_session({
    "appName": "MySparkApp",
    "master": "local[*]",
    "spark.executor.memory": "2g"
})
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
