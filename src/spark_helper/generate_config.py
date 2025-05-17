#!/usr/bin/env python
"""CLI interface for spark_helper."""

import argparse
import sys

from spark_helper.core import create_config_yaml


def main():
    """Command line interface for spark_helper."""
    parser = argparse.ArgumentParser(description="Spark Configuration Generator")
    parser.add_argument(
        "--file_path", default=None, help="Optional file path for configuration (default: None)"
    )
    args = parser.parse_args()

    create_config_yaml(file_name=args.file_path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
