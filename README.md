# Gentopia

This project demonstrates the implementation of a multi-tool LLM agent capable of retrieving and synthesizing information from two key sources:\
Web Search (via Google Search API) \
PDF Document Parsing (via local PDF file processing)

The agent uses a tool-augmented LLM framework (Gentopia) to dynamically invoke the appropriate tools based on user input. This setup enables it to simulate real-world research assistance by answering queries from both the internet and uploaded documents.

# Features
PDF Reader Tool:
Extracts text and structured content from PDF files, enabling the agent to answer context-specific questions from documents.

Google Search Tool:
Leverages Google Search to find up-to-date and specific information, such as academic papers or recent trends.

Tool-Calling LLM Agent:
Uses reasoning chains to determine whether to invoke a tool (PDF or Web) and ask clarifying questions
