# Module Reference

## `spark_helper.core`

The core module provides functions for creating and configuring SparkSessions.

### Functions

#### `create_spark_session(config: Union[str, Dict[str, Any]]) -> SparkSession`

Creates a SparkSession based on configuration from either a YAML file or a configuration dictionary.

**Parameters:**
- `config` (Union[str, Dict[str, Any]]): 
  - If a string: Path to the YAML configuration file
  - If a dictionary: Configuration parameters (must include "type" key specifying which template to use)

**Returns:**
- `SparkSession`: Configured Spark session

**Raises:**
- `FileNotFoundError`: If the configuration file or template resource doesn't exist
- `ValueError`: If the YAML configuration cannot be parsed or if the required "type" key is missing from the dictionary
- `TypeError`: If the config is neither a string nor a dictionary

**Examples:**
```python
# From a YAML file
spark = create_spark_session("config.yaml")

# From a dictionary (must include 'type' key)
spark = create_spark_session({
    "type": "local",  # Required to specify which template to use
    "appName": "MySparkApp",
    "master": "local[*]",
    "spark.executor.memory": "2g"
})
```

#### `create_config_yaml(type: str = "local", detail: str = "user", file_name: Optional[str] = None) -> None`

Creates a Spark configuration YAML file from a template resource.

**Parameters:**
- `type` (str, optional): The type of Spark configuration template to use (e.g., "local", "cluster"). Defaults to "local".
- `detail` (str, optional): The level of detail to include ("user" or "all"). If "all", appends system-level config. Defaults to "user".
- `file_name` (Optional[str], optional): The path to the output file. If None, outputs to stdout. Defaults to None.

**Raises:**
- `ImportError`: If the 'spark_helper' package cannot be imported
- `FileNotFoundError`: If the specified template resource is not found in the package
- `RuntimeError`: If any other error occurs while accessing or writing the resource

**Examples:**
```python
# Output local template to stdout
create_config_yaml()  

# Write local template to file
create_config_yaml(type="local", file_name="local_config.yaml")  

# Generate a cluster configuration with all settings (including system level)
create_config_yaml(type="cluster", detail="all", file_name="cluster_config.yaml")
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

## Configuration Templates

The package includes multiple configuration templates:

### Local Template

The local configuration template includes:
- Application name and master settings for local execution
- Driver configuration settings
- Executor configuration settings
- Python version settings

You can view the local template with:
```bash
generate-spark-config --type local
```

### Cluster Template

The cluster configuration template includes:
- Application name and master settings for cluster execution 
- Driver configuration settings optimized for distributed computing
- Executor configuration settings for cluster deployment
- Network and resource management settings

You can view the cluster template with:
```bash
generate-spark-config --type cluster
```

### System-Level Configurations

When using the "all" detail level, system-level configurations will be included, such as:
- Network timeout settings
- Executor heartbeat intervals
- Broadcast compression settings
- Adaptive query execution settings

View these configurations with:
```bash
generate-spark-config --type cluster --detail all
```
