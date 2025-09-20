# PocketAdvisor – Multi-Source AI Agent

**PocketAdvisor** is a powerful, AI-driven financial assistant that aggregates, analyzes, and synthesizes financial data from multiple sources—including Google, Bing, and Reddit—to provide users with actionable insights. It simplifies complex financial concepts, compares financial products, and helps users make informed decisions in investments, loans, and insurance.  

---

## 🔹 Key Features

1. **Multi-Source Research**
   - Fetches information from:
     - **Google** for official and reliable financial information.
     - **Bing** for complementary insights and additional perspectives.
     - **Reddit** for community discussions and real user experiences.
   - Ensures accurate and diverse financial information.

2. **Automated Data Analysis**
   - Uses AI (Gemini-2 / OpenAI) to analyze content from all sources.
   - Extracts key insights, comparisons, and user experiences.

3. **Structured Synthesis**
   - Combines analyses from all sources into a single, coherent answer.
   - Highlights pros, cons, and intuitive comparisons.
   - Provides explanations in **simple, beginner-friendly language**.

4. **Extensible Architecture**
   - Modular Python codebase with clear separation of:
     - Web operations (`web_operations.py`)
     - Snapshot handling (`snapshot_operations.py`)
     - Prompt templates (`prompts.py`)
     - Orchestrator and workflow (`main.py` using LangGraph)
   - Easy to add new data sources or domains.

5. **Parallel & Graph-Based Workflow**
   - Uses `LangGraph` to orchestrate search, analysis, and synthesis tasks.
   - Supports parallel execution of multiple sources for faster insights.

---

## 🔹 Supported Financial Domains

- **Investments**
  - Mutual funds, SIPs, ETFs
  - Equity vs debt funds
  - Portfolio guidance

- **Bank Loans**
  - Home loans, personal loans, car loans
  - Interest rate comparison
  - Loan tenure and EMI analysis

- **Insurance**
  - Health and life insurance providers
  - Term vs ULIP comparison
  - Policy benefits and exclusions

- **General Finance Guidance**
  - Simplified explanations of financial products
  - Beginner-friendly tips
  - Community-based insights

---

## 🔹 Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/PocketAdvisor.git
cd PocketAdvisor
```
### Create virtual environment
```bash
uv venv
source .venv/bin/activate   # Linux/macOS
.venv\Scripts\activate      # Windows
```
### Install dependencies
```bash
uv add -r requirements.txt
```
### Set up environment variables
### Create a .env file and add:
```bash
GEMINI_API_KEY=<your_google_gemini_key>
BRIGHTDATA_API_KEY=<your_brightdata_key>
```

# 🔹 Usage
Run the chatbot interface:

```bash
uv run main.py
```
## Example interactions:

```bash
Ask me anything: How do floating vs fixed home loan rates work?
```
PocketAdvisor will:

Search Google for official financial information.

Search Bing for complementary insights.

Retrieve Reddit posts discussing similar queries.

Analyze each source using AI.

Synthesize a comprehensive, easy-to-understand recommendation.

# 🔹 Code Structure
bash
Copy code
PocketAdvisor/
│
├─ main.py                  # Entry point & graph orchestration
├─ prompts.py               # LLM prompt templates and message helpers
├─ web_operations.py        # Web search & data retrieval functions
├─ snapshot_operations.py   # BrightData snapshot polling & download
├─ .env                     # Environment variables for API keys
├─ requirements.txt         # Python dependencies
└─ README.md

# 🔹 Technical Highlights
LangGraph: Orchestrates nodes (search, analysis, synthesis) and edges (workflow) for structured execution.

LLM Integration: Gemini-2 or OpenAI LLMs for structured and natural language outputs.

Structured Prompts: Ensures accurate and domain-specific AI responses.

BrightData API: Real-time, reliable scraping of web and Reddit data.

Parallel & Modular Design: Each source is analyzed independently and concurrently.

# 🔹 Future Enhancements
Add more financial websites or blogs for deeper insights.

Integrate real-time stock market data or mutual fund NAVs.

Add personalized advice based on user profile and risk preferences.

Build web or mobile UI for better user interaction.

# 🔹 Skills Demonstrated
Python, API integration, data pipelines

LLM orchestration & structured prompt engineering

Web scraping and data aggregation

Modular software design & workflow automation

Multi-source knowledge synthesis

# 🔹 License
MIT License – Open for personal and educational use.