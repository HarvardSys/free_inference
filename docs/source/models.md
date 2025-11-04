# Available Models

HybridInference provides access to multiple state-of-the-art LLM models.

## Model Overview

| Model ID | Name | Context Length | Max Output | Pricing |
|----------|------|----------------|------------|---------|
| `llama-3.3-70b-instruct` | Llama 3.3 70B Instruct | 131K tokens | 8K tokens | Free |
| `llama-4-scout` | Llama 4 Scout | 128K tokens | 16K tokens | Free |
| `llama-4-maverick` | Llama 4 Maverick | 128K tokens | 16K tokens | Free |
| `glm-4.5` | GLM-4.5 | 128K tokens | 96K tokens | Free |
| `glm-4.5-air` | GLM-4.5-Air | 128K tokens | 96K tokens | Free |
| `glm-4.6` | GLM-4.6 | 200K tokens | 128K tokens | Free |
| `deepseek-r1` | DeepSeek R1 | 64K tokens | 8K tokens | Free |

## Model Details

### Llama 3.3 70B Instruct

**Model ID:** `llama-3.3-70b-instruct`

High-performance open-source model optimized for instruction following.

**Key Features:**
- Context length: 131,072 tokens
- Max output: 8,192 tokens
- Function calling support
- Structured output (JSON mode)
- Quantization: bf16
- Input modalities: text
- Output modalities: text

**Best For:**
- General purpose chat
- Long-form content generation
- Code generation
- Instruction following

**Example:**
```python
response = client.chat.completions.create(
    model="llama-3.3-70b-instruct",
    messages=[{"role": "user", "content": "Explain quantum computing"}],
    max_tokens=2048
)
```

---

### Llama 4 Scout

**Model ID:** `llama-4-scout`

Efficient MoE (Mixture of Experts) model for fast inference.

**Key Features:**
- Context length: 128,000 tokens
- Max output: 16,384 tokens
- Function calling support
- Structured output
- Quantization: fp8
- Input modalities: text
- Output modalities: text

**Best For:**
- Fast inference scenarios
- Cost-effective deployments
- Production workloads

---

### Llama 4 Maverick

**Model ID:** `llama-4-maverick`

Advanced MoE (Mixture of Experts) model with multimodal capabilities.

**Key Features:**
- Context length: 128,000 tokens
- Max output: 16,384 tokens
- Function calling support
- Structured output
- Quantization: fp8
- Input modalities: text, image
- Output modalities: text

**Best For:**
- Complex reasoning tasks
- Multimodal applications
- Long-form generation
- Production workloads with high quality requirements

---

### GLM-4.5

**Model ID:** `glm-4.5`

Bilingual model optimized for Chinese and English by Zhipu AI.

**Key Features:**
- Context length: 128,000 tokens
- Max output: 96,000 tokens
- Function calling support
- Structured output
- Quantization: fp8
- Input modalities: text
- Output modalities: text

**Best For:**
- Chinese language tasks
- Bilingual applications
- Cross-language translation
- General purpose chat in Chinese/English

---

### GLM-4.5-Air

**Model ID:** `glm-4.5-air`

Lightweight version of GLM-4.5 for faster inference.

**Key Features:**
- Context length: 128,000 tokens
- Max output: 96,000 tokens
- Function calling support
- Structured output
- Quantization: fp8
- Input modalities: text
- Output modalities: text

**Best For:**
- Fast Chinese/English chat
- High-throughput scenarios
- Cost-effective bilingual applications

---

### GLM-4.6

**Model ID:** `glm-4.6`

Latest generation Zhipu AI model with extended context and advanced features.

**Key Features:**
- Context length: 200,000 tokens
- Max output: 128,000 tokens
- Function calling support
- Structured output
- Thinking mode support
- Tool streaming
- Quantization: fp8
- Input modalities: text
- Output modalities: text

**Best For:**
- Long-context Chinese/English tasks
- Advanced reasoning
- Complex bilingual applications
- Production workloads requiring large context

---

### DeepSeek R1

**Model ID:** `deepseek-r1`

DeepSeek's reasoning model for complex problem solving.

**Key Features:**
- Context length: 64,000 tokens
- Max output: 8,000 tokens
- Function calling support
- Structured output
- Quantization: bf16
- Input modalities: text
- Output modalities: text

**Best For:**
- Reasoning tasks
- Mathematical problem solving
- Complex analytical tasks

---

## Using Different Models

Simply change the `model` parameter in your request:

```python
import openai

client = openai.OpenAI(
    base_url="https://freeinference.org/v1",
    api_key="your-api-key-here"
)

# Use Llama 3.3
response = client.chat.completions.create(
    model="llama-3.3-70b-instruct",
    messages=[{"role": "user", "content": "Hello!"}]
)

# Switch to Llama 4 Maverick
response = client.chat.completions.create(
    model="llama-4-maverick",
    messages=[{"role": "user", "content": "Hello!"}]
)

# Use GLM-4.6 for Chinese
response = client.chat.completions.create(
    model="glm-4.6",
    messages=[{"role": "user", "content": "你好！"}]
)
```

## Model Selection Guide

**For general chat and instructions:**
- `llama-3.3-70b-instruct` - Best balance of quality and speed
- `llama-4-maverick` - High quality, complex tasks with multimodal support

**For fast inference:**
- `llama-4-scout` - Optimized for speed
- `glm-4.5-air` - Fast bilingual inference

**For Chinese language:**
- `glm-4.6` - Latest generation with extended context
- `glm-4.5` - Stable bilingual support
- `glm-4.5-air` - Fast Chinese/English chat

**For advanced reasoning:**
- `deepseek-r1` - Specialized reasoning tasks
- `llama-3.3-70b-instruct` - Strong general reasoning

**For long-context tasks:**
- `glm-4.6` - 200K context window
- `llama-3.3-70b-instruct` - 131K context window
- `llama-4-scout` / `llama-4-maverick` - 128K context window

**For multimodal (text + image):**
- `llama-4-maverick` - Open-source multimodal with image support
