# Free Inference

OpenRouter-compatible API for accessing multiple LLM models.

## Documentation

Visit our documentation at: https://harvardsys.github.io/free_inference/

## Quick Start

```python
import openai

client = openai.OpenAI(
    base_url="https://freeinference.org/v1",
    api_key="your-api-key-here"
)

response = client.chat.completions.create(
    model="llama-3.3-70b-instruct",
    messages=[{"role": "user", "content": "Hello!"}]
)

print(response.choices[0].message.content)
```

## Available Models

- Llama 3.3 70B Instruct
- Llama 4 Scout & Maverick
- Gemini 2.5 Flash
- GPT-5
- Claude Opus 4.1
- GLM-4.5

See the [Models documentation](https://harvardsys.github.io/free_inference/models.html) for the complete list.
