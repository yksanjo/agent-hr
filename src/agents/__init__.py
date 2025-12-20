"""HR Agents module."""

from .base_agent import BaseAgent
from .recruiting_agent import RecruitingAgent
from .onboarding_agent import OnboardingAgent
from .payroll_agent import PayrollAgent
from .benefits_agent import BenefitsAgent

__all__ = [
    "BaseAgent",
    "RecruitingAgent",
    "OnboardingAgent",
    "PayrollAgent",
    "BenefitsAgent",
]

