# Spark Helper

A Python package to simplify working with Apache Spark by providing utilities to generate user modifiable Spark configuration parameters and SparkSession creation.

## Features

- Simple SparkSession creation from YAML configuration files
- Generate template YAML configuration files for different Spark deployment types (local, cluster)
- Command-line interface for generating Spark configurations with customizable detail levels
- System-level default configurations that can be overridden by user settings
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

### Creating SparkSession

You can create a SparkSession in two ways:

1. From a YAML configuration file:

```python
from spark_helper.core import create_spark_session

# Create a SparkSession from a YAML configuration file
spark = create_spark_session("config.yaml")
```

2. Directly from a configuration dictionary:

```python
from spark_helper.core import create_spark_session

# Create a SparkSession from a dictionary
config = {
    "type": "local",  # Required to specify which template to use
    "appName": "MySparkApp",
    "master": "local[*]",
    "spark.executor.memory": "2g",
    "spark.driver.memory": "1g"
}
spark = create_spark_session(config)
```

### Generating Configuration Templates

Generate template configuration files:

```python
from spark_helper.core import create_config_yaml

# Generate a local Spark configuration template and save it to a file
create_config_yaml(type="local", detail="user", file_name="my_config.yaml")

# Generate a cluster configuration with all settings (including system level)
create_config_yaml(type="cluster", detail="all", file_name="cluster_config.yaml")

# Print a configuration template to stdout
create_config_yaml(type="local")
```

Or use the command-line tool:

```bash
generate-spark-config --help
usage: generate-spark-config [-h] [--type TYPE] [--detail DETAIL] [--config CONFIG] [--file_path FILE_PATH]

Spark Configuration Generator

options:
  -h, --help            show this help message and exit
  --type TYPE           Type of Spark session to create (default: local), valid options: local, cluster
  --detail DETAIL       Detail level of the configuration (default: user), valid options: user, all
  --config CONFIG       Configuration type (default: default), valid options: default, custom
  --file_path FILE_PATH
                        Optional file path for configuration (default: None)
```

**Example command-line usage:**

```bash
# Generate a local config file
generate-spark-config --type local --file_path my_config.yaml

# Generate a cluster config with all details
generate-spark-config --type cluster --detail all --file_path cluster_config.yaml
```

#### Sample Configuration Files

**Local Spark Configuration**

```bash
generate-spark-config
```

```yaml
# Spark Application Configuration Template for Local Spark
# This template provides common configuration parameters for Spark applications

# User-specific configurations
# Application information
appName: "SparkHelperApp"

# Local Spark Master 
# "local"       Run Spark locally with one worker thread (i.e. no parallelism at all).
# "local[K]"    Run Spark locally with K worker threads (ideally, set this to the number of cores on your machine).
# "local[K,F]"  Run Spark locally with K worker threads and F maxFailures (see spark.task.maxFailures for an explanation of this variable).
# "local[*]"    Run Spark locally with as many worker threads as logical cores on your machine.
# "local[*,F]"  Run Spark locally with as many worker threads as logical cores on your machine and F maxFailures.
# "local-cluster[N,C,M]"        Local-cluster mode is only for unit tests. It emulates a distributed cluster in a single JVM with N number of workers, C cores per worker and M MiB of memory per worker.

master: "local[*]"

```

**Standalone Cluster Configuration with full details**

```bash
generate-spark-config --type cluster --detail all
```

```yaml
# Spark Application Configuration Template for Standalone Cluster
# This template provides common configuration parameters for Spark applications

# User-specific configurations
# Application information
appName: "SparkHelperApp"

# Spark Master 
# for standalone mode, use spark://spark-master:7077
# for yarn mode, use yarn
master: "spark://spark-master:7077" 

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

### Standalone Spark Cluster

To bring up the environment, run the following command:

```bash
docker-compose up -d
```
This command will start the Spark cluster and Jupyterlab server in detached mode. The Jupyterlab server will be accessible at `http://localhost:8888` in your web browser.  Expected output:

```bash
Mac:jim spark_sandbox[504]$ docker compose up -d
[+] Running 7/7
 ✔ Network spark_sandbox_spark-network  Created                          0.0s 
 ✔ Container spark-master               Started                          0.1s 
 ✔ Container spark-worker-2             Started                          0.3s 
 ✔ Container spark-worker-4             Started                          0.2s 
 ✔ Container jupyterlab                 Started                          0.2s 
 ✔ Container spark-worker-3             Started                          0.2s 
 ✔ Container spark-worker-1             Started                          0.2s
```


Connecting to the Juypterlab server via the web browser or from Visual Studio code use the following URL: `http://localhost:8888`. For ease of testing, the Jupyterlab server is configured to allow access without a password or token. However, in a production environment, it is recommended to set up authentication and secure access to the Jupyterlab server.

Once a Spark Applicaiton is running, the application UI will be accessible at `http://localhost:4040`. You can monitor the Spark cluster's status and job progress through this interface.

To stop the environment, run:

```bash
docker-compose down
```
This command will stop and remove the containers, networks, and volumes defined in the `docker-compose.yml` file.  The expected output is:

```bash
+] Running 7/7
 ✔ Container spark-worker-2             Removed                         10.3s 
 ✔ Container spark-worker-4             Removed                         10.4s 
 ✔ Container jupyterlab                 Removed                          0.3s 
 ✔ Container spark-worker-3             Removed                         10.2s 
 ✔ Container spark-worker-1             Removed                         10.2s 
 ✔ Container spark-master               Removed                         10.2s 
 ✔ Network spark_sandbox_spark-network  Removed                          0.2s 
Mac:jim spark_sandbox[506]$ 
```



## Documentation

- [User Guide](docs/index.md)
- [Getting Started](docs/getting_started.md)
- [Module Reference](docs/modules.md)

## License

MIT
