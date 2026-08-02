# omni-gateway-local - AI Agent Guidelines

## Agent Context
If a user asks you to add new features to this gateway:
1. Try to rely on `litellm`'s native capabilities before writing custom routing logic.
2. Ensure the `/v1/chat/completions` endpoint always maintains strict OpenAI API schema compatibility.
3. Keep the server lightweight; do not add heavy dependencies like PyTorch or Transformers.
