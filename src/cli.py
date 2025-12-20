"""CLI interface for AgentHR."""

import click
import asyncio
import json
from typing import Dict, Any

from .agents import (
    RecruitingAgent,
    OnboardingAgent,
    PayrollAgent,
    BenefitsAgent
)
from .config import settings


@click.group()
@click.version_option(version="0.1.0")
def cli():
    """AgentHR - AI-Native HCM Platform."""
    pass


@cli.command()
@click.option("--job-title", required=True, help="Job title to recruit for")
@click.option("--budget", required=True, type=float, help="Salary budget")
@click.option("--requirements", help="Job requirements (comma-separated)")
@click.option("--location", help="Job location")
@click.option("--output", default="json", type=click.Choice(["json", "table"]))
def recruiting(job_title: str, budget: float, requirements: str, location: str, output: str):
    """Execute recruiting agent."""
    click.echo(f"🚀 Starting recruiting for: {job_title}")
    
    task = {
        "job_title": job_title,
        "budget": budget,
        "location": location
    }
    
    if requirements:
        task["requirements"] = [r.strip() for r in requirements.split(",")]
    
    agent = RecruitingAgent()
    result = asyncio.run(agent.execute(task))
    
    if output == "json":
        click.echo(json.dumps(result, indent=2))
    else:
        click.echo(f"\n✅ Status: {result['status']}")
        click.echo(f"📊 Candidates Found: {result.get('candidates_found', 0)}")
        click.echo(f"💰 Pricing: ${result.get('pricing', 0):.2f}")


@cli.command()
@click.option("--employee-id", required=True, help="Employee ID")
@click.option("--employee-name", required=True, help="Employee name")
@click.option("--start-date", required=True, help="Start date (YYYY-MM-DD)")
@click.option("--department", help="Department")
@click.option("--role", help="Job role")
@click.option("--output", default="json", type=click.Choice(["json", "table"]))
def onboarding(employee_id: str, employee_name: str, start_date: str, 
               department: str, role: str, output: str):
    """Execute onboarding agent."""
    click.echo(f"👋 Onboarding: {employee_name} ({employee_id})")
    
    task = {
        "employee_id": employee_id,
        "employee_name": employee_name,
        "start_date": start_date
    }
    
    if department:
        task["department"] = department
    if role:
        task["role"] = role
    
    agent = OnboardingAgent()
    result = asyncio.run(agent.execute(task))
    
    if output == "json":
        click.echo(json.dumps(result, indent=2))
    else:
        click.echo(f"\n✅ Status: {result['status']}")
        click.echo(f"📄 Paperwork: {'Completed' if result.get('paperwork_completed') else 'Pending'}")
        click.echo(f"💻 Equipment: {'Provisioned' if result.get('equipment_provisioned') else 'Pending'}")


@cli.command()
@click.option("--period", default="monthly", help="Payroll period (monthly, biweekly, etc.)")
@click.option("--employee-ids", help="Employee IDs (comma-separated, optional)")
@click.option("--output", default="json", type=click.Choice(["json", "table"]))
def payroll(period: str, employee_ids: str, output: str):
    """Execute payroll agent."""
    click.echo(f"💰 Processing payroll for period: {period}")
    
    task = {"period": period}
    
    if employee_ids:
        task["employee_ids"] = [eid.strip() for eid in employee_ids.split(",")]
    
    agent = PayrollAgent()
    result = asyncio.run(agent.execute(task))
    
    if output == "json":
        click.echo(json.dumps(result, indent=2))
    else:
        click.echo(f"\n✅ Status: {result['status']}")
        click.echo(f"👥 Employees Processed: {result.get('employees_processed', 0)}")
        click.echo(f"💵 Total Amount: ${result.get('total_amount', 0):,.2f}")
        click.echo(f"💰 Pricing: ${result.get('pricing', 0):.2f}")


@cli.command()
@click.option("--action", default="enroll", type=click.Choice(["enroll", "claim", "query"]))
@click.option("--employee-id", required=True, help="Employee ID")
@click.option("--plan", help="Benefits plan")
@click.option("--output", default="json", type=click.Choice(["json", "table"]))
def benefits(action: str, employee_id: str, plan: str, output: str):
    """Execute benefits agent."""
    click.echo(f"🏥 Processing benefits {action} for employee: {employee_id}")
    
    task = {
        "action": action,
        "employee_id": employee_id
    }
    
    if plan:
        task["plan"] = plan
    
    agent = BenefitsAgent()
    result = asyncio.run(agent.execute(task))
    
    if output == "json":
        click.echo(json.dumps(result, indent=2))
    else:
        click.echo(f"\n✅ Status: {result['status']}")
        click.echo(f"📋 Action: {result.get('action', 'unknown')}")
        click.echo(f"💰 Pricing: ${result.get('pricing', 0):.2f}")


@cli.command()
def pricing():
    """Show pricing information."""
    click.echo("💰 AgentHR Pricing (Transaction-Based)\n")
    click.echo(f"Hiring: ${settings.pricing_hiring:.2f} per hire")
    click.echo(f"Payroll Run: ${settings.pricing_payroll:.2f} per run")
    click.echo(f"Benefits Enrollment: ${settings.pricing_benefits_enrollment:.2f} per enrollment")
    click.echo(f"Performance Review: ${settings.pricing_performance_review:.2f} per review")
    click.echo(f"Offboarding: ${settings.pricing_offboarding:.2f} per offboarding")


if __name__ == "__main__":
    cli()

