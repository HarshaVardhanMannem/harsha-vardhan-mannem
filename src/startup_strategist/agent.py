import os
import uuid
from google.adk.agents import Agent, SequentialAgent
from google.adk.tools import google_search
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


# Agent 1 - Clarify Idea Agent
clarify_idea_agent = Agent(
    name="clarify_idea_agent",
    model="gemini-2.0-flash",
    instruction="""
    You are a startup strategist. Clarify the user's business idea and rephrase it to be investor-ready.
    Keep it concise but compelling. Your goal is to define the startup vision in 1-2 sentences.
    Return only the refined idea, nothing else.
    """,
    output_key="refined_idea"
)

# Agent 2 - Problem Statement Agent
problem_statement_agent = Agent(
    name="problem_statement_agent",
    model="gemini-2.0-flash",
    tools=[google_search],
    instruction="""
    You have access to this refined idea: {refined_idea}
    
    Define the problem that this startup idea is solving. Focus on the pain points, scale of the problem, and who faces it.
    Research current market data if needed using google_search.
    Output just the problem statement in 2-3 clear sentences.
    """,
    output_key="problem"
)

# Agent 3 - Target Customer Agent
target_customer_agent = Agent(
    name="target_customer_agent",
    model="gemini-2.0-flash",
    tools=[google_search],
    instruction="""
    You have access to: {refined_idea}
    
    Identify the ideal target customer for this startup idea.
    Use demographic and behavioral characteristics. Who exactly would use this? Avoid generic audiences.
    Research market segments if needed using google_search.
    Provide a specific customer profile.
    """,
    output_key="customer"
)

# Agent 4 - MVP Planner Agent
mvp_planner_agent = Agent(
    name="mvp_planner_agent",
    model="gemini-2.0-flash",
    instruction="""
    You have access to:
    - Idea: {refined_idea}
    - Problem: {problem}
    - Target Customer: {customer}
    
    Based on this information, propose a simple MVP (Minimum Viable Product).
    List the key features and the simplest version of the product that can be shipped in 4-6 weeks.
    Focus on core functionality that addresses the main problem.
    """,
    output_key="mvp"
)

# Agent 5 - Competitor Analysis Agent
competitor_analysis_agent = Agent(
    name="competitor_analysis_agent",
    model="gemini-2.0-flash",
    tools=[google_search],
    instruction="""
    You have access to: {refined_idea}
    
    Find the top 3 existing competitors for this idea using google_search.
    Summarize their key features and how they solve the same problem.
    Output a short list with company names, brief descriptions, and their main strengths.
    """,
    output_key="competitors"
)

# Agent 6 - Monetization Agent
monetization_agent = Agent(
    name="monetization_agent",
    model="gemini-2.0-flash",
    instruction="""
    You have access to:
    - Idea: {refined_idea}
    - Competitors: {competitors}
    
    Propose 2-3 realistic ways this idea can make money. Be specific: subscriptions, transaction fees, licensing, freemium, etc.
    Consider what competitors are doing and identify potential revenue opportunities.
    Provide clear revenue model explanations.
    """,
    output_key="monetization"
)

# Agent 7 - Go-to-Market Agent
go_to_market_agent = Agent(
    name="go_to_market_agent",
    model="gemini-2.0-flash",
    instruction="""
    You have access to:
    - MVP: {mvp}
    - Target Customer: {customer}
    
    Propose a Go-To-Market (GTM) strategy focused on acquiring the first 100 users.
    Include specific channels (e.g., Reddit communities, LinkedIn, cold emails, content marketing).
    Provide actionable steps and timeline for customer acquisition.
    """,
    output_key="gtm"
)

# Agent 8 - Pitch Deck Agent
pitch_deck_agent = Agent(
    name="pitch_deck_agent",
    model="gemini-2.0-flash",
    instruction="""
    You have access to all previous outputs:
    - Refined Idea: {refined_idea}
    - Problem: {problem}
    - Target Customer: {customer}
    - MVP: {mvp}
    - Competitors: {competitors}
    - Monetization: {monetization}
    - GTM Strategy: {gtm}
    
    Create a comprehensive pitch deck outline using all this information.
    Structure it as a professional investor pitch with clear sections:
    1. Problem & Opportunity
    2. Solution (MVP)
    3. Target Market & Customer
    4. Competitive Landscape
    5. Revenue Model
    6. Go-to-Market Strategy
    7. Next Steps
    
    Make it investor-ready and compelling.
    """,
    output_key="pitch_deck"
)

# Agent 9 - Memory Agent
memory_agent = Agent(
    name="memory_agent",
    model="gemini-2.0-flash",
    instruction="""
    You have access to all previous outputs:
    """,
    output_key="memory"
)

# Create the main Sequential Agent that ADK web will use
root_agent = SequentialAgent(
    name="startup_strategist",
    description="A comprehensive startup strategist that transforms business ideas into investor-ready pitch decks through systematic analysis.",
    sub_agents=[
        clarify_idea_agent,
        problem_statement_agent,
        target_customer_agent,
        mvp_planner_agent,
        competitor_analysis_agent,
        monetization_agent,
        go_to_market_agent,
        pitch_deck_agent,
        memory_agent,
    ]
)

