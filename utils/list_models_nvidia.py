import os
from dotenv import load_dotenv
from langchain_nvidia_ai_endpoints import ChatNVIDIA

# Load the NVIDIA_API_KEY from your .env file
load_dotenv()

# Initialize the ChatNVIDIA client
# It automatically picks up the API key from the environment
llm = ChatNVIDIA()

# Fetch and print the available models
print("Available NVIDIA Models:")
for model in llm.get_available_models():
    print(model.id)

"""
openai/gpt-oss-20b
nvidia/nemotron-3-nano-omni-30b-a3b-reasoning
google/gemma-4-31b-it
meta/muse-glimmer-30b
moonshotai/kimi-k3



nvidia/nemotron-3-ultra-550b-a55b
meta/llama-3.2-11b-vision-instruct
nvidia/nemotron-3-super-120b-a12b


"""


# meta/llama-3.1-8b-instruct (Fastest & Lowest Cost) -Best for: Fast RAG retrieval generation, query rewriting, intent classification, and simple decision nodes in LangGraph.
# meta/llama-3.3-70b-instruct (Best Overall Agent Model) - Best for: Core LangGraph agents, complex tool/function calling, multi-step planning, and synthesising answers from large retrieved documents.
# deepseek-ai/deepseek-r1-distill-qwen-32b (Best for Complex Reasoning) - Best for: Multi-step logical reasoning nodes, mathematical evaluation, and complex decision-tree routing inside agentic graphs.

"""
Top 3 Embedding Models for RAG
The ChatNVIDIA().get_available_models() command only lists conversational endpoints. For vector retrieval in RAG, use NVIDIA’s dedicated embedding endpoints via NVIDIAEmbeddings.

1. nvidia/nv-embedqa-e5-v5 (Best overall for QA & RAG)
Best for: Dense retrieval across asymmetric question-answer pairs.

Why: Top-ranked model on MTEB benchmarks specifically optimized for retrieval-augmented generation.

2. baai/bge-m3 (Best for Multi-lingual & Hybrid Search)
Best for: Projects requiring multi-lingual support or dense + sparse retrieval.

Why: High speed, low memory footprint, and strong performance across long context inputs.

3. snowflake/arctic-embed-l (Best Enterprise Benchmark)
Best for: Enterprise document search, code retrieval, and tabular data embeddings.

Why: Fast execution speed with high retrieval accuracy.
"""

"""
Top 3 Image Generation Models (NVIDIA API)
Image generation models operate on dedicated API endpoints rather than chat interfaces. You can access these via standard HTTP requests or the NVIDIA client using your NVIDIA_API_KEY.

1. black-forest-labs/flux.1-dev (Highest Quality)
Best for: High-detail, prompt-adherent image generation with complex text layout capabilities.

Why: Current state-of-the-art open image generation architecture.

2. black-forest-labs/flux.1-schnell (Fastest & Lowest Cost)
Best for: Real-time visual generation and agentic workflows requiring rapid image creation.

Why: Optimized to produce outputs in 1–4 inference steps.

3. stabilityai/stable-diffusion-3-medium (Balanced Performance)
Best for: General visual asset creation and styled image outputs.

Why: Low latency with broad artistic versatility.
"""

