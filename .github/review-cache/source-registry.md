# Source Registry

Use one row per canonical primary source that has already been fetched during review work.

## Column Guide

- `Source ID`: stable identifier used from topic files and findings.
- `URL`: canonical source URL.
- `Type`: `docs`, `blog`, `paper`, `repo`, `benchmark`, or similar.
- `Owner`: vendor, lab, or organization.
- `Topics`: comma-separated `Topic ID`s that reuse this source.
- `First seen`: first date this source entered the cache.
- `Last checked`: last date the source was explicitly re-verified.
- `Freshness class`: `static`, `slow`, `fast`, or `volatile`.
- `Status`: `current`, `stale`, `superseded`, `historical`.
- `Notes`: short note about why this source matters or what superseded it.

| Source ID | URL | Type | Owner | Topics | First seen | Last checked | Freshness class | Status | Notes |
|---|---|---|---|---|---|---|---|---|---|
| src-anthropic-models | https://platform.claude.com/docs/en/docs/about-claude/models | docs | Anthropic | anthropic-claude-family | 2026-04-11 | 2026-04-11 | fast | current | Canonical model list and pricing |
| src-anthropic-adaptive-thinking | https://platform.claude.com/docs/en/docs/build-with-claude/extended-thinking | docs | Anthropic | anthropic-claude-family | 2026-04-11 | 2026-04-11 | fast | current | Extended/adaptive thinking API |
| src-anthropic-glasswing | https://www.anthropic.com/research/the-model-behind-project-glasswing | blog | Anthropic | anthropic-claude-family | 2026-04-11 | 2026-04-11 | static | current | Mythos Preview benchmarks |
| src-anthropic-mcp | https://platform.claude.com/docs/en/docs/agents-and-tools/mcp-connector | docs | Anthropic | anthropic-claude-family, mcp-ecosystem | 2026-04-11 | 2026-04-11 | fast | current | MCP Connector beta |
| src-anthropic-batch | https://platform.claude.com/docs/en/docs/build-with-claude/batch-processing | docs | Anthropic | anthropic-claude-family | 2026-04-11 | 2026-04-11 | slow | current | Batch API limits |
| src-anthropic-caching | https://platform.claude.com/docs/en/docs/build-with-claude/prompt-caching | docs | Anthropic | anthropic-claude-family | 2026-04-11 | 2026-04-11 | slow | current | Prompt caching pricing |
| src-openai-models | https://developers.openai.com/api/docs/models | docs | OpenAI | openai-gpt5-family | 2026-04-11 | 2026-04-11 | fast | current | Model lineup overview |
| src-openai-pricing | https://openai.com/api/pricing/ | docs | OpenAI | openai-gpt5-family | 2026-04-11 | 2026-04-11 | fast | current | API pricing |
| src-openai-mcp | https://developers.openai.com/api/docs/guides/model-context-protocol | docs | OpenAI | openai-gpt5-family, mcp-ecosystem | 2026-04-11 | 2026-04-11 | fast | current | MCP in Responses API |
| src-openai-toolsearch | https://developers.openai.com/api/docs/guides/tools-overview | docs | OpenAI | openai-gpt5-family | 2026-04-11 | 2026-04-11 | fast | current | Tool search, defer_loading |
| src-openai-batch | https://developers.openai.com/api/docs/guides/batch | docs | OpenAI | openai-gpt5-family | 2026-04-11 | 2026-04-11 | slow | current | Batch API limits |
| src-google-gemini-models | https://ai.google.dev/gemini-api/docs/models | docs | Google | google-gemini-gemma | 2026-04-11 | 2026-04-11 | fast | current | Gemini model list |
| src-google-gemma-docs | https://ai.google.dev/gemma/docs | docs | Google | google-gemini-gemma | 2026-04-11 | 2026-04-11 | moderate | current | Gemma 4 family docs |
| src-google-gemini-diffusion | https://deepmind.google/technologies/gemini/diffusion/ | docs | Google | hybrid-architectures | 2026-04-11 | 2026-04-11 | slow | current | Experimental diffusion demo |
| src-qwen-github | https://github.com/QwenLM | repo | Alibaba | alibaba-qwen | 2026-04-11 | 2026-04-11 | moderate | current | Qwen open models |
| src-qwen-blog | https://qwenlm.github.io/blog/ | blog | Alibaba | alibaba-qwen | 2026-04-11 | 2026-04-11 | moderate | current | Model announcements |
| src-deepseek-docs | https://api-docs.deepseek.com/ | docs | DeepSeek | deepseek-family | 2026-04-11 | 2026-04-11 | moderate | current | API documentation |
| src-deepseek-github | https://github.com/deepseek-ai | repo | DeepSeek | deepseek-family | 2026-04-11 | 2026-04-11 | moderate | current | Open-weight models |
| src-deepseek-r1-paper | https://arxiv.org/abs/2501.12948 | paper | DeepSeek | deepseek-family | 2026-04-11 | 2026-04-11 | static | current | R1 paper (R1-Zero distinction) |
| src-xai-grok | https://docs.x.ai/docs/models | docs | xAI | xai-grok | 2026-04-11 | 2026-04-11 | moderate | current | Grok model docs |
| src-xai-docs | https://docs.x.ai/ | docs | xAI | xai-grok | 2026-04-11 | 2026-04-11 | moderate | current | xAI API reference |
| src-meta-llama | https://www.llama.com/ | docs | Meta | meta-llama | 2026-04-11 | 2026-04-11 | moderate | current | Llama 4 official site |
| src-meta-ai-blog | https://ai.meta.com/blog/ | blog | Meta | meta-llama | 2026-04-11 | 2026-04-11 | moderate | current | Model announcements |
| src-zhipu-glm | https://open.bigmodel.cn/ | docs | Zhipu AI | zhipu-glm | 2026-04-11 | 2026-04-11 | moderate | current | GLM-5.1 platform |
| src-minimax-hf | https://huggingface.co/MiniMaxAI | repo | MiniMax | minimax-m27 | 2026-04-11 | 2026-04-11 | moderate | partially_verified | M2.7 model card (details unverifiable) |
| src-mcp-spec | https://modelcontextprotocol.io/specification | docs | Anthropic | mcp-ecosystem | 2026-04-11 | 2026-04-11 | fast | current | MCP spec v2025-11-25 |
| src-mcp-docs | https://modelcontextprotocol.io/introduction | docs | Anthropic | mcp-ecosystem | 2026-04-11 | 2026-04-11 | fast | current | MCP overview and concepts |
| src-bitnet-paper | https://arxiv.org/abs/2402.17764 | paper | Microsoft | slm-edge | 2026-04-11 | 2026-04-11 | static | current | Ma et al. 2024, 1.58-bit |
| src-bitnet-repo | https://github.com/microsoft/BitNet | repo | Microsoft | slm-edge | 2026-04-11 | 2026-04-11 | slow | current | BitNet implementation |
| src-smollm-hf | https://huggingface.co/HuggingFaceTB/SmolLM3-3B | repo | HuggingFace | slm-edge | 2026-04-11 | 2026-04-11 | moderate | current | SmolLM3 model card |
| src-ai21-jamba | https://www.ai21.com/jamba | docs | AI21 Labs | hybrid-architectures | 2026-04-11 | 2026-04-11 | slow | current | Jamba 2 architecture |
| src-inception-mercury | https://www.inceptionlabs.ai/ | docs | Inception Labs | hybrid-architectures | 2026-04-11 | 2026-04-11 | slow | current | Mercury diffusion LLM |