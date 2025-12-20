"""Base agent class for all HR agents."""

from abc import ABC, abstractmethod
from typing import Dict, Any, Optional
from datetime import datetime
import uuid


class BaseAgent(ABC):
    """Base class for all HR agents."""
    
    def __init__(self, agent_name: str, config: Optional[Dict[str, Any]] = None):
        self.agent_name = agent_name
        self.config = config or {}
        self.agent_id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
    
    @abstractmethod
    async def execute(self, task: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute the agent's main task.
        
        Args:
            task: Task parameters
            
        Returns:
            Execution results
        """
        pass
    
    @abstractmethod
    def get_pricing(self) -> float:
        """
        Get the pricing for this agent's transaction.
        
        Returns:
            Price in USD
        """
        pass
    
    def validate_task(self, task: Dict[str, Any]) -> bool:
        """
        Validate task parameters.
        
        Args:
            task: Task parameters
            
        Returns:
            True if valid, False otherwise
        """
        return True
    
    def get_metadata(self) -> Dict[str, Any]:
        """Get agent metadata."""
        return {
            "agent_id": self.agent_id,
            "agent_name": self.agent_name,
            "created_at": self.created_at.isoformat(),
            "config": self.config
        }

