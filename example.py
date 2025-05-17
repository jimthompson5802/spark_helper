#!/usr/bin/env python
"""Example script demonstrating spark_helper package functionality."""

from spark_helper.core import create_config_yaml, create_spark_session


def main():
    """Run example operations with spark_helper."""
    # Generate a config file
    print("Generating config file...")
    config_file = "custom_config.yaml"
    create_config_yaml(config_file)
    print(f"Config file generated: {config_file}")
    
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