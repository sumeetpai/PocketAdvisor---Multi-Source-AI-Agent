from typing import Dict, Any

class PromptTemplates:
    """Container for all prompt templates used in the finance assistant."""

    # --- Reddit URL Analysis ---
    @staticmethod
    def reddit_url_analysis_system() -> str:
        return """You are a financial research assistant. 
Your task is to examine Reddit discussions and identify posts that give valuable insights about finance topics like investments, bank loan rates, or insurance.
Focus on:
- Posts where users share real financial experiences
- Comparisons of financial products (banks, loans, insurance)
- Community consensus and tips
Return the most relevant URLs."""

    @staticmethod
    def reddit_url_analysis_user(user_question: str, reddit_results: str) -> str:
        return f"""User Question: {user_question}

Reddit Results: {reddit_results}

Please analyze these Reddit results and identify the most valuable posts for answering the user's question."""

    # --- Google Analysis ---
    @staticmethod
    def google_analysis_system() -> str:
        return """You are a financial analyst. 
Analyze Google results to extract **official and reliable financial information**.
Focus on:
- Bank loan interest rates and terms
- Investment product details (mutual funds, SIPs, ETFs)
- Insurance provider offerings
- Authoritative sources like RBI, SEBI, banks, insurance companies
Explain findings in **simple words**."""

    @staticmethod
    def google_analysis_user(user_question: str, google_results: str) -> str:
        return f"""Question: {user_question}

Google Search Results: {google_results}

Please analyze these Google results and extract the key insights that help answer the question."""

    # --- Bing Analysis ---
    @staticmethod
    def bing_analysis_system() -> str:
        return """You are a financial analyst. 
Analyze Bing results to find **complementary financial insights**.
Focus on:
- News articles about banking and finance
- Comparisons across providers
- Technical/enterprise finance perspectives
Highlight **unique findings**."""

    @staticmethod
    def bing_analysis_user(user_question: str, bing_results: str) -> str:
        return f"""Question: {user_question}

Bing Search Results: {bing_results}

Please analyze these Bing results and extract insights that complement other search sources."""

    # --- Reddit Post Analysis ---
    @staticmethod
    def reddit_analysis_system() -> str:
        return """You are a financial assistant analyzing Reddit discussions.
Extract insights such as:
- Real user experiences with banks, loans, investments, insurance
- Community comparisons of financial products
- Positive and negative feedback
Quote relevant lines and explain in plain, simple terms."""

    @staticmethod
    def reddit_analysis_user(user_question: str, reddit_results: str, reddit_post_data: list) -> str:
        return f"""Question: {user_question}

Reddit Search Results: {reddit_results}

Detailed Reddit Post Data: {reddit_post_data}

Please analyze this Reddit content and extract community insights, user experiences, and relevant discussions."""

    # --- Synthesis ---
    @staticmethod
    def synthesis_system() -> str:
        return """You are an expert financial advisor. 
Combine Google, Bing, and Reddit analyses into a clear, easy-to-understand answer.
Your task:
- Compare financial options (banks, loans, insurance, investments)
- Break down complex terms into simple language
- Highlight pros/cons and intuitive comparisons
- Mention which insights come from official sources vs. community experiences
Make the advice **practical and beginner-friendly**."""

    @staticmethod
    def synthesis_user(
        user_question: str,
        google_analysis: str,
        bing_analysis: str,
        reddit_analysis: str,
    ) -> str:
        return f"""Question: {user_question}

Google Analysis: {google_analysis}

Bing Analysis: {bing_analysis}

Reddit Community Analysis: {reddit_analysis}

Please synthesize these analyses into a comprehensive answer that addresses the question from multiple perspectives."""


# --- Helper to create message pairs ---
def create_message_pair(system_prompt: str, user_prompt: str) -> list[Dict[str, Any]]:
    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ]


# --- Convenience functions ---
def get_reddit_url_analysis_messages(user_question: str, reddit_results: str) -> list[Dict[str, Any]]:
    return create_message_pair(
        PromptTemplates.reddit_url_analysis_system(),
        PromptTemplates.reddit_url_analysis_user(user_question, reddit_results),
    )


def get_google_analysis_messages(user_question: str, google_results: str) -> list[Dict[str, Any]]:
    return create_message_pair(
        PromptTemplates.google_analysis_system(),
        PromptTemplates.google_analysis_user(user_question, google_results),
    )


def get_bing_analysis_messages(user_question: str, bing_results: str) -> list[Dict[str, Any]]:
    return create_message_pair(
        PromptTemplates.bing_analysis_system(),
        PromptTemplates.bing_analysis_user(user_question, bing_results),
    )


def get_reddit_analysis_messages(user_question: str, reddit_results: str, reddit_post_data: list) -> list[Dict[str, Any]]:
    return create_message_pair(
        PromptTemplates.reddit_analysis_system(),
        PromptTemplates.reddit_analysis_user(user_question, reddit_results, reddit_post_data),
    )


def get_synthesis_messages(user_question: str, google_analysis: str, bing_analysis: str, reddit_analysis: str) -> list[Dict[str, Any]]:
    return create_message_pair(
        PromptTemplates.synthesis_system(),
        PromptTemplates.synthesis_user(user_question, google_analysis, bing_analysis, reddit_analysis),
    )
