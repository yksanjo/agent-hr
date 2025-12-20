# AgentHR - AI-Native HCM Platform

> Autonomous HR agents that automate recruiting, onboarding, payroll, and benefits—priced per transaction, not per employee. Directly disrupts Workday's seat-based revenue model.

[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

## 🎯 Overview

AgentHR is an AI-native HCM platform with autonomous agents that automate HR tasks, enabling leaner organizations with fewer employees. Unlike Workday's seat-based pricing, AgentHR charges per transaction (hiring, payroll run, benefits enrollment), directly attacking Workday's revenue model.

**Why This Disrupts Workday:**
- **Transaction-Based Pricing**: Pay per hiring ($50), payroll run ($2), benefits enrollment ($1) instead of per employee
- **Enables Leaner Organizations**: AI automation reduces headcount, shrinking Workday's revenue base
- **AI-Native Architecture**: Built for AI agents from day one, not a retrofit like Workday Illuminate™
- **60-80% Cost Savings**: Compared to Workday's seat-based pricing
- **Multi-Platform**: Works with existing HR systems, not a replacement

## 🤖 Core Agents

### 1. **Recruiting Agent**
- Automated candidate sourcing (LinkedIn, job boards, referrals)
- AI-powered resume screening and ranking
- Automated interview scheduling (calendar integration)
- Candidate communication (email, SMS, chatbot)
- Offer letter generation and negotiation
- Background check coordination
- Onboarding handoff

### 2. **Onboarding Agent**
- Automated new hire paperwork (I-9, W-4, benefits enrollment)
- Equipment provisioning (laptop, access cards, software)
- Training assignment and tracking
- Buddy/mentor matching
- First-day/week/month check-ins
- Knowledge base access setup

### 3. **Payroll Agent**
- Automated payroll processing (calculations, deductions, taxes)
- Tax compliance (federal, state, local)
- Direct deposit setup and management
- Pay stub generation and distribution
- Year-end tax forms (W-2, 1099)
- Payroll reconciliation

### 4. **Benefits Agent**
- Benefits enrollment automation
- Claims processing and tracking
- Open enrollment management
- Benefits queries (chatbot)
- COBRA administration
- Wellness program coordination

### 5. **Performance Agent**
- 360 review collection and analysis
- Goal setting and tracking
- Continuous feedback collection
- Performance review generation
- Development plan recommendations
- Promotion/compensation recommendations

### 6. **Offboarding Agent**
- Exit interview automation
- Knowledge transfer documentation
- Access revocation (systems, buildings)
- Final paycheck and benefits processing
- Alumni network invitation

## ✨ Key Features

- **Transaction-Based Pricing**: Pay per transaction, not per employee
- **AI-Native Architecture**: Microservices, API-first, event-driven
- **Multi-Platform Integration**: Works with existing HR systems, Slack, Teams, email
- **Real-Time Processing**: Instant responses, not batch
- **Autonomous Workflows**: End-to-end automation, minimal human intervention
- **Compliance Built-In**: SOC 2, GDPR, HIPAA, labor law compliance

## 🚀 Quick Start

```bash
# Install AgentHR
pip install agent-hr

# Configure API keys
export OPENAI_API_KEY=your_key
export ANTHROPIC_API_KEY=your_key

# Initialize Recruiting Agent
agent-hr recruiting init --company "Acme Corp"

# Start automated recruiting
agent-hr recruiting start --job-title "Software Engineer" --budget 100000

# Process payroll
agent-hr payroll process --period monthly

# Enroll employee in benefits
agent-hr benefits enroll --employee-id 12345 --plan "Health Plan A"
```

## 💰 Pricing Model

### Transaction-Based
- **Hiring**: $50 per hire
- **Payroll Run**: $2 per payroll run
- **Benefits Enrollment**: $1 per enrollment
- **Performance Review**: $10 per review
- **Offboarding**: $25 per offboarding

### Agent Subscription
- **Per Agent**: $500-$5,000/month (unlimited transactions)
- **Full Platform**: $10,000-$50,000/month (all agents)

### Enterprise License
- **Unlimited Transactions**: $50K-$500K/year
- **Premium Support**: 24/7 SLA, dedicated account manager
- **Custom Agents**: Tailored to your needs

## 📊 Market Opportunity

- **Workday HCM Revenue**: ~$8-10B/year
- **Target Market Share**: 2-5% = $160M-$500M opportunity
- **Key Advantage**: Transaction-based pricing enables leaner organizations, directly reducing Workday's revenue base

## 🛠️ Tech Stack

- **Backend**: Python (FastAPI), Node.js (microservices)
- **AI/ML**: OpenAI GPT-4, Anthropic Claude, LangChain, LlamaIndex
- **Frontend**: React, TypeScript
- **Database**: PostgreSQL, Redis (caching)
- **Message Queue**: RabbitMQ, Kafka
- **Container**: Kubernetes, Docker
- **Integration**: REST APIs, webhooks, Zapier, n8n

## 🎯 Target Customers

1. **Workday Customers Reducing Headcount**
   - Companies automating HR functions
   - Organizations with AI initiatives
   - Cost-conscious enterprises
   - Contract renewal windows

2. **Mid-Market Enterprises**
   - Workday is too expensive
   - Need enterprise features
   - Willing to try alternatives
   - Growth companies (headcount scaling = Workday costs scaling)

3. **Startups/Scale-ups**
   - Don't want Workday lock-in
   - Cost-conscious
   - Modern tech stack preferred
   - Transaction-based pricing aligns with growth

## 🚀 Go-to-Market Strategy

1. **Target Workday Customers Reducing Headcount**
   - Companies automating HR functions
   - Organizations with AI initiatives
   - Cost-conscious enterprises

2. **Offer Free Migration Assessment**
   - Analyze current Workday usage
   - Identify automation opportunities
   - Calculate cost savings
   - Provide migration roadmap

3. **Lead with ROI**
   - "Reduce HR headcount by 30-50% through automation"
   - "Pay per transaction, not per employee"
   - "60-80% cost savings vs. Workday seat-based pricing"
   - "Built for AI agents, not retrofitted"

4. **Partner with HR Consultants**
   - Deloitte, PwC, Accenture HR practices
   - HR transformation consultants
   - AI implementation partners

## 📈 Competitive Advantages

- **60-80% Cost Savings**: Transaction-based vs. Workday's seat-based pricing
- **AI-Native Architecture**: Built for AI agents from day one, not a retrofit
- **Multi-Platform**: Works with existing HR systems, not a walled garden
- **Faster Innovation**: Weekly releases vs. Workday's quarterly releases
- **Enables Leaner Organizations**: Fewer employees = less Workday revenue

## 📝 License

Apache 2.0

## 🔗 Related Products

- [AgentFinance](./../agent-finance) - AI-Native Finance Platform
- [WorkdayExit](./../workday-exit) - Workday Migration Platform
- [LeanOrg](./../lean-org) - Organizational Efficiency Platform
- [OpenHR](./../open-hr) - Open-Source HR Agent Platform

