#!/usr/bin/env python
"""Example script demonstrating spark_helper package functionality."""

import argparse
from spark_helper.core import create_spark_session


def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="Run Spark Helper example")
    parser.add_argument(
        "--config-file",
        type=str,
        default="local_config.yaml",
        help="Path to the config file (default: local_config.yaml)"
    )
    return parser.parse_args()


def main():
    """Run example operations with spark_helper."""
    # Parse command line arguments
    args = parse_args()
    config_file = args.config_file

    # Method 1: Create a SparkSession from a config file
    print("\nCreating SparkSession from config file...")
    try:
        spark_from_file = create_spark_session(config_file)
        app_name = spark_from_file.conf.get('spark.app.name')
        print(f"Successfully created SparkSession with app name: {app_name}")
        print(f"Spark version: {spark_from_file.version}")

        # Show configured settings
        print("\nActive Spark configuration (from file):")
        for item in sorted(spark_from_file.sparkContext.getConf().getAll()):
            print(f"  {item[0]}: {item[1]}")

        # do some operations
        rdd = spark_from_file.sparkContext.parallelize(range(10))
        print("Sample operation result:", rdd.map(lambda x: x*x).collect())

        # Stop the session
        spark_from_file.stop()
        print("Session from file closed successfully")

        # Method 2: Create a SparkSession directly from a dictionary
        print("\nCreating SparkSession from dictionary...")
        config_dict = {
            "appName": "SparkHelperDictExample",
            "master": "local[*]",
            "spark.executor.memory": "2g",
            "spark.driver.memory": "1g",
            "spark.sql.shuffle.partitions": "8",
        }

        spark_from_dict = create_spark_session(config_dict)
        app_name = spark_from_dict.conf.get('spark.app.name')
        print(f"Successfully created SparkSession with app name: {app_name}")
        print(f"Spark version: {spark_from_dict.version}")

        # Show configured settings
        print("\nActive Spark configuration (from dictionary):")
        for item in sorted(spark_from_dict.sparkContext.getConf().getAll()):
            print(f"  {item[0]}: {item[1]}")

        # do some operations
        rdd = spark_from_dict.sparkContext.parallelize(range(5, 15))
        print("Sample operation result:", rdd.map(lambda x: x*2).collect())

        # Stop the session
        spark_from_dict.stop()
    except Exception as e:
        print(f"Error creating SparkSession: {str(e)}")


if __name__ == "__main__":
    main()
