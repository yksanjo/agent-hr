"""FastAPI application for AgentHR."""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict, Any, Optional
import uvicorn

from ..agents import (
    RecruitingAgent,
    OnboardingAgent,
    PayrollAgent,
    BenefitsAgent
)
from ..config import settings

app = FastAPI(
    title="AgentHR API",
    description="AI-Native HCM Platform - Transaction-based pricing",
    version="0.1.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class TaskRequest(BaseModel):
    """Task request model."""
    task_type: str
    parameters: Dict[str, Any]


class TaskResponse(BaseModel):
    """Task response model."""
    status: str
    result: Dict[str, Any]
    pricing: float


@app.get("/")
async def root():
    """Root endpoint."""
    return {
        "name": "AgentHR",
        "version": "0.1.0",
        "description": "AI-Native HCM Platform",
        "pricing_model": "transaction-based"
    }


@app.get("/health")
async def health():
    """Health check endpoint."""
    return {"status": "healthy"}


@app.post("/api/v1/tasks/execute", response_model=TaskResponse)
async def execute_task(request: TaskRequest):
    """
    Execute an HR task using the appropriate agent.
    
    Supported task types:
    - recruiting: Recruiting agent
    - onboarding: Onboarding agent
    - payroll: Payroll agent
    - benefits: Benefits agent
    """
    task_type = request.task_type.lower()
    parameters = request.parameters
    
    # Select and initialize agent
    agent = None
    if task_type == "recruiting":
        agent = RecruitingAgent()
    elif task_type == "onboarding":
        agent = OnboardingAgent()
    elif task_type == "payroll":
        agent = PayrollAgent()
    elif task_type == "benefits":
        agent = BenefitsAgent()
    else:
        raise HTTPException(
            status_code=400,
            detail=f"Unknown task type: {task_type}"
        )
    
    try:
        # Execute task
        result = await agent.execute(parameters)
        pricing = agent.get_pricing()
        
        return TaskResponse(
            status="success",
            result=result,
            pricing=pricing
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/v1/pricing")
async def get_pricing():
    """Get pricing information for all agents."""
    return {
        "pricing": {
            "recruiting": settings.pricing_hiring,
            "payroll": settings.pricing_payroll,
            "benefits_enrollment": settings.pricing_benefits_enrollment,
            "performance_review": settings.pricing_performance_review,
            "offboarding": settings.pricing_offboarding
        },
        "model": "transaction-based",
        "currency": "USD"
    }


@app.get("/api/v1/agents")
async def list_agents():
    """List available agents."""
    return {
        "agents": [
            {
                "name": "recruiting",
                "description": "Automated candidate sourcing, screening, and scheduling",
                "pricing": settings.pricing_hiring
            },
            {
                "name": "onboarding",
                "description": "Automated new hire paperwork, provisioning, and training",
                "pricing": 0.0  # Included in hiring
            },
            {
                "name": "payroll",
                "description": "Automated payroll processing, tax compliance, and payments",
                "pricing": settings.pricing_payroll
            },
            {
                "name": "benefits",
                "description": "Automated benefits enrollment, claims processing, and queries",
                "pricing": settings.pricing_benefits_enrollment
            }
        ]
    }


if __name__ == "__main__":
    uvicorn.run(
        "src.api.main:app",
        host=settings.api_host,
        port=settings.api_port,
        reload=settings.api_debug
    )

