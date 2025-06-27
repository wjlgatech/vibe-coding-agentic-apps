"""
Main entry point for the Vibe Coding Agentic Apps.

This module bootstraps the agent registry, loads the agent_config.yaml,
initializes the orchestrator, and starts the FastAPI server.
"""

import os
import yaml
from fastapi import FastAPI
from src.orchestration.coordinator import Coordinator
from src.utils.logger import get_logger

# Initialize logger
logger = get_logger(__name__)

# Load agent configuration
AGENT_CONFIG_PATH = os.getenv("AGENT_CONFIG_PATH", "config/agent_config.yaml")
try:
    with open(AGENT_CONFIG_PATH, "r") as f:
        agent_config = yaml.safe_load(f)
    logger.info(f"Loaded agent configuration from {AGENT_CONFIG_PATH}")
except FileNotFoundError:
    logger.error(f"Agent configuration file not found at {AGENT_CONFIG_PATH}")
    agent_config = {} # Default to empty config
except Exception as e:
    logger.error(f"Error loading agent configuration: {e}")
    agent_config = {} # Default to empty config

# Initialize FastAPI app
app = FastAPI(
    title="Vibe Coding Agentic Apps",
    description="A multi-agent system for software development.",
    version="0.0.1",
)

# Initialize orchestrator
coordinator = Coordinator(agent_config=agent_config)

@app.get("/")
async def root():
    """
    Root endpoint for the API.
    """
    return {"message": "Vibe Coding Agentic Apps API is running!"}

# Example of how to run the app (for development)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
