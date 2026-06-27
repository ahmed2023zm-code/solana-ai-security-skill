# Solana Token Safety & Rugcheck AI Agent Skill

A highly optimized, production-ready AI Agent skill written in Python designed to empower Autonomous AI Agents (such as LangChain tools, LLM workflows, or Discord/Telegram bots) to dynamically inspect, analyze, and grade the security of any token contract on the Solana blockchain.

## Features
- **Automated Mint Audit:** Instantly verifies if the token contract creator has renounced ownership (Mint Authority).
- **Freeze Analysis:** Verifies whether the developer retains the ability to freeze user balances (Freeze Authority).
- **Algorithmic Safety Scoring:** Returns a granular safety indicator (0-100) and structured hazard levels (`LOW`, `MEDIUM`, `HIGH`).
- **Seamless Agent Integration:** Built cleanly to return dictionary formats that can be directly piped into OpenAI, Claude, or Llama prompt contexts.

## Architecture & Integration Setup


