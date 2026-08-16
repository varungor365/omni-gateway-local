<div align="center">

# 🌐 omni-gateway-local

**A single, unified API gateway for all local and remote LLMs.**

[![PyPI version](https://badge.fury.io/py/omni-gateway-local.svg)](https://badge.fury.io/py/omni-gateway-local)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

<br/>

</div>

---

## ✨ Why this exists

If you're building AI applications, you probably have API keys for OpenAI, Anthropic, Gemini, and maybe a local Ollama instance running `llama3`. Managing all these endpoints in your code is a nightmare.

**omni-gateway-local** solves this. It exposes a single OpenAI-compatible `/v1/chat/completions` endpoint. You point your apps to `http://localhost:8000`, and it routes the request to the correct provider based on the `model` parameter.

### Features
- 🔄 **Universal Compatibility:** Speak to Claude, Gemini, and Llama using the standard OpenAI SDK.
- ⚡ **Lightning Fast:** Built on `FastAPI` and `LiteLLM`.
- 🌊 **Streaming Support:** Full support for Server-Sent Events (SSE) streaming.

---

## 🚀 Quickstart

### Install
```bash
pip install omni-gateway-local
```

### Configure
Set your API keys in the environment:
```bash
export OPENAI_API_KEY="sk-..."
export ANTHROPIC_API_KEY="sk-ant-..."
export GEMINI_API_KEY="AIza..."
```

### Run
```bash
omni-gateway --port 8000
```

### Test
```python
from openai import OpenAI

client = OpenAI(base_url="http://localhost:8000/v1", api_key="dummy")

response = client.chat.completions.create(
    model="claude-3-sonnet-20240229", # Gateway routes this to Anthropic!
    messages=[{"role": "user", "content": "Hello!"}]
)
```

---

## 🤖 AI Agent Context

See [CLAUDE.md](CLAUDE.md) for contribution guidelines.

---

## 📄 License

MIT © Varun Ruhella. See [LICENSE](LICENSE) for details.

## Who this is for

Omni Gateway Local gives developers one interface for working with local and remote LLM providers. It is intended for provider switching, local-model experiments, and applications that benefit from a unified API boundary.

## Why star this repository

Star this project if you integrate multiple LLM providers, build local AI applications, or want a small gateway layer to extend.
