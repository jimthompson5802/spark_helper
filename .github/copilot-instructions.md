<!-- Use this file to provide workspace-specific custom instructions to Copilot. For more details, visit https://code.visualstudio.com/docs/copilot/copilot-customization#_use-a-githubcopilotinstructionsmd-file -->

# Spark Helper Package

This workspace contains a Python package for working with Apache Spark. The package focuses on providing helper functions and utilities to streamline common Spark operations.

## Project Structure

- `src/spark_helper/`: Contains the main package code
  - `core.py`: Core functionality for working with Spark
  - `cli.py`: Command-line interface
- `tests/`: Contains test files
- `docs/`: Documentation

## Code Style

- Follow PEP 8 guidelines
- Use type hints for all function parameters and return values
- Maximum line length is 100 characters (Black formatter's default)
- Use docstrings for all public functions, classes, and methods
- Write comprehensive tests for all functionality

## Development Conventions

- Use pytest for testing
- Format code with Black
- Sort imports with isort
- Use flake8 for linting 
- Use mypy for type checking
