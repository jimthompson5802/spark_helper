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

    # Create a SparkSession using the config
    print("\nCreating SparkSession from config...")
    try:
        spark = create_spark_session(config_file)
        app_name = spark.conf.get('spark.app.name')
        print(f"Successfully created SparkSession with app name: {app_name}")
        print(f"Spark version: {spark.version}")

        # Show configured settings
        print("\nActive Spark configuration:")
        for item in sorted(spark.sparkContext.getConf().getAll()):
            print(f"  {item[0]}: {item[1]}")

        # Stop the session
        spark.stop()
    except Exception as e:
        print(f"Error creating SparkSession: {str(e)}")


if __name__ == "__main__":
    main()
