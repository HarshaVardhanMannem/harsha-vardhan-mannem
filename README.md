# Startup Strategist Agent

A comprehensive AI-powered startup strategist that transforms business ideas into investor-ready pitch decks through systematic analysis and market research.

## Overview

The Startup Strategist Agent is built using Google's Agent Development Kit (ADK) and leverages Gemini 2.0 Flash for intelligent analysis. It provides a structured approach to startup ideation by breaking down the process into 8 specialized agents, each focusing on a specific aspect of startup development.

## Features

- **Idea Clarification**: Refines raw business ideas into investor-ready concepts
- **Problem Analysis**: Identifies and validates market problems
- **Customer Profiling**: Defines target customer segments
- **MVP Planning**: Designs minimum viable products
- **Competitor Analysis**: Researches and analyzes market competition
- **Monetization Strategy**: Proposes revenue models
- **Go-to-Market Planning**: Creates customer acquisition strategies
- **Pitch Deck Generation**: Compiles comprehensive investor presentations

## Prerequisites

- Python 3.11 or higher
- Google Cloud Project with ADK enabled
- Google API credentials
- Internet connection for market research

## Installation

1. **Clone the repository**:
   ```bash
   git clone <your-repo-url>
   cd adk-project
   ```

2. **Create and activate virtual environment**:
   ```bash
   python -m venv adkenv
   # On Windows:
   adkenv\Scripts\activate
   # On macOS/Linux:
   source adkenv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install google-adk python-dotenv
   ```

4. **Set up environment variables**:
   Create a `.env` file in the root directory:
   ```
   GOOGLE_API_KEY=your_google_api_key_here
   GOOGLE_CLOUD_PROJECT=your_project_id
   ```

## Usage

### Option 1: ADK Web Interface
1. Navigate to the `startup_strategist` directory
2. Deploy using ADK web interface
3. Input your business idea
4. Receive comprehensive startup analysis

### Option 2: Command Line Interface
1. Navigate to the `startup_strategist` directory
2. Run the CLI version:
   ```bash
   python agent.py
   ```
3. Follow the interactive prompts

### Option 3: Direct Python Execution
```python
from startup_strategist.agent import agent

# Run the agent with your idea
result = await agent.run_async({
    "idea": "Your business idea here"
})
```

## Agent Architecture

The system consists of 8 specialized agents working sequentially:

1. **Clarify Idea Agent**: Refines raw ideas
2. **Problem Statement Agent**: Defines market problems
3. **Target Customer Agent**: Identifies customer segments
4. **MVP Planner Agent**: Designs minimum viable products
5. **Competitor Analysis Agent**: Researches competition
6. **Monetization Agent**: Proposes revenue models
7. **Go-to-Market Agent**: Plans customer acquisition
8. **Pitch Deck Agent**: Compiles final presentation

## Dependencies

- `google-adk`: Google's Agent Development Kit
- `python-dotenv`: Environment variable management
- `google-search`: Web search capabilities
- `gemini-2.0-flash`: AI model for analysis

## Configuration

### Environment Variables
- `GOOGLE_API_KEY`: Your Google API key
- `GOOGLE_CLOUD_PROJECT`: Your Google Cloud project ID

### Model Configuration
- Default model: `gemini-2.0-flash`
- Tools: Google Search for market research
- Output format: Structured JSON responses

## Troubleshooting

### Common Issues

1. **API Key Errors**: Ensure your Google API key is valid and has ADK permissions
2. **Import Errors**: Verify all dependencies are installed in your virtual environment
3. **Search Tool Failures**: Check internet connectivity and API quotas

### Debug Mode
Enable debug logging by setting:
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For issues and questions:
- Check the troubleshooting section
- Review the architecture documentation
- Open an issue on GitHub

## Roadmap

- [ ] Add more market research tools
- [ ] Implement financial modeling
- [ ] Add pitch deck template customization
- [ ] Integrate with CRM systems
- [ ] Add team collaboration features 