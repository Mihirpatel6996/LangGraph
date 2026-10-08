import time
from langchain_nvidia_ai_endpoints import ChatNVIDIA
from dotenv import load_dotenv

# Load your NVIDIA_API_KEY
load_dotenv()

# Your complete list of models pasted as a multi-line string
raw_model_list = """
openai/gpt-oss-20b
nvidia/nemotron-3-nano-omni-30b-a3b-reasoning
google/gemma-4-31b-it
meta/muse-glimmer-30b
moonshotai/kimi-k3
nvidia/nemotron-3-ultra-550b-a55b
meta/llama-3.2-11b-vision-instruct
nvidia/nemotron-3-super-120b-a12b
"""

# Clean up the list by splitting on newlines and removing empty spaces
all_models = [m.strip() for m in raw_model_list.strip().split("\n") if m.strip()]

active_models = []
print(f"Starting test for {len(all_models)} models. This will take about {(len(all_models)*2)/60:.1f} minutes...")

for model_id in all_models:
    try:
        # Initialize with max_tokens=5 to keep the test ultra-fast and cheap
        llm = ChatNVIDIA(
    model=model_id,
    max_completion_tokens=5
)
        
        start = time.perf_counter()

        response = llm.invoke("Hi")

        elapsed = time.perf_counter() - start
        print(f"✅ ACTIVE: {model_id} (Response Time: {elapsed:.2f}s)")
        active_models.append(model_id)
        
    except Exception as e:
        if "410" in str(e):
            print(f"❌ EOL (410 Gone): {model_id}")
        elif "429" in str(e):
            print(f"⚠️ RATE LIMIT HIT (429): {model_id} - Consider increasing the sleep time.")
        else:
            print(f"⚠️ FAILED (Other): {model_id} - {e}")
    
    # Pause for 2 seconds to guarantee you stay under 40 RPM (60 / 40 = 1.5 seconds)
    time.sleep(3)

# Save the survivors to a text file for easy reference
with open("active_nvidia_models.txt", "w") as f:
    f.write("--- Verified Active Models ---\n")
    for am in active_models:
        f.write(f"{am}\n")

print("\n🎉 Test complete! All active models have been saved to 'active_nvidia_models.txt'.")