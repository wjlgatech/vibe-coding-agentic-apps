"""
BaseAgent: Defines the interface for all agents in the system.
"""

from abc import ABC, abstractmethod

class BaseAgent(ABC):
    """
    Abstract base class for all agents.

    Agents are responsible for planning, executing, and reflecting on tasks.
    """

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    @abstractmethod
    def plan(self, task: str) -> str:
        """
        Generates a plan to accomplish the given task.

        Args:
            task: The task to be planned.

        Returns:
            A string representing the plan.
        """
        pass

    @abstractmethod
    def execute(self, plan: str) -> str:
        """
        Executes the given plan.

        Args:
            plan: The plan to be executed.

        Returns:
            A string representing the result of the execution.
        """
        pass

    @abstractmethod
    def reflect(self, original_task: str, plan: str, execution_result: str) -> str:
        """
        Reflects on the execution of a task and suggests improvements.

        Args:
            original_task: The original task given to the agent.
            plan: The plan that was executed.
            execution_result: The result of the plan execution.

        Returns:
            A string representing the reflection and suggested improvements.
        """
        pass
