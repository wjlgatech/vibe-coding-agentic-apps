"""
Logger utility: Wrapper around Python’s logging module.
"""

import logging
import logging.config
import os
import yaml

def get_logger(name: str) -> logging.Logger:
    """
    Configures and returns a logger instance.

    Loads logging configuration from `logging.yaml` specified by the
    `LOGGING_CONFIG` environment variable. If the file is not found or an
    error occurs, a basic console logger is configured.

    Args:
        name: The name of the logger (usually __name__ of the calling module).

    Returns:
        A configured logging.Logger instance.
    """
    log_config_path = os.getenv("LOGGING_CONFIG", "config/logging.yaml")

    if os.path.exists(log_config_path):
        try:
            with open(log_config_path, "r") as f:
                config = yaml.safe_load(f)
            logging.config.dictConfig(config)
            print(f"Loaded logging configuration from {log_config_path}") # For initial debugging
        except Exception as e:
            print(f"Error loading logging configuration from {log_config_path}: {e}")
            logging.basicConfig(level=logging.INFO) # Fallback to basic config
    else:
        print(f"Logging configuration file not found at {log_config_path}. Using basic configuration.")
        logging.basicConfig(level=logging.INFO) # Fallback to basic config

    return logging.getLogger(name)
