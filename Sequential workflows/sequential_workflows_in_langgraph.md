# Sequential workflows in langgraph

## 📌 Overview
This guide provides a comprehensive walkthrough for building **Sequential Workflows** using LangGraph. A sequential workflow is a linear process where tasks (nodes) are connected back-to-back without any conditional branching or parallel execution. 

By following this guide, you will learn the core syntax of LangGraph and how to construct both standard Python-based graphs and LLM-powered chains.

## 🛠️ Environment Setup & Installation

Before building workflows, you need to configure your Python environment and install the required dependencies.

### 1. Create a Virtual Environment
It is highly recommended to isolate your project dependencies.
```bash
# Create the virtual environment
python -m venv myenv

# Activate it (Windows)
myenv\Scripts\activate  

# Activate it (Mac/Linux)
source myenv/bin/activate
```

### 2. Install Packages
Install LangGraph, LangChain, and the necessary OpenAI integrations. (Jupyter tools are included if you plan to visualize the graphs in notebooks).
```bash
pip install langgraph langchain langchain-openai python-dotenv ipykernel
```

### 3. API Key Configuration
Create a `.env` file in the root directory of your project and add your OpenAI API key:
```env
OPENAI_API_KEY="sk-your-openai-api-key-here"
```

---

## 🧠 Core LangGraph Concepts

To build sequential workflows, you must understand the following foundational components:

*   **State (`TypedDict`):** The shared data structure (dictionary) passed between every node in your graph. Nodes read from this state, perform operations, and return updates to it.
*   **StateGraph:** The core engine that orchestrates the workflow. You initialize it by passing your State definition.
*   **Nodes:** Standard Python functions that represent individual steps. A node always takes the `state` as an argument and returns a dictionary of state updates.
*   **Edges:** The connections that define the flow. In a sequential workflow, edges simply connect `Node A` -> `Node B` -> `Node C`. Special edges connect to `START` and `END`.
*   **Compile & Invoke:** Once edges and nodes are defined, the graph is compiled into a runnable application. You start the workflow by invoking it with an initial state payload.

---

## 🚀 Detailed Workflow Implementations

### 1. The BMI Calculator Workflow (Non-LLM)
This workflow is perfect for understanding LangGraph's mechanics without the added complexity of language models.

*   **Purpose:** Calculate a user's Body Mass Index (BMI) and categorize it.
*   **State Schema:**
    *   `weight` (float)
    *   `height` (float)
    *   `bmi` (float)
    *   `category` (string)
*   **Nodes:** 
    1.  **`calculate_bmi`:** Reads `weight` and `height` from the state, calculates `bmi = weight / (height ** 2)`, and returns the `bmi` value.
    2.  **`label_bmi`:** Reads the newly calculated `bmi` from the state, determines the category (Underweight, Normal, Overweight, Obese), and returns the `category`.
*   **Graph Flow:** `START` ➔ `calculate_bmi` ➔ `label_bmi` ➔ `END`

### 2. Simple LLM QA Workflow
This workflow introduces basic LLM integration within the graph structure.

*   **Purpose:** Ask a question and get an answer from an OpenAI model.
*   **State Schema:**
    *   `question` (string)
    *   `answer` (string)
*   **Nodes:** 
    1.  **`llm_qa`:** Takes the `question` from the state, formats a prompt, invokes `ChatOpenAI()`, and returns the model's response to update the `answer` state.
*   **Graph Flow:** `START` ➔ `llm_qa` ➔ `END`

### 3. Prompt Chaining (Blog Generation)
This is an advanced sequential workflow that breaks a complex LLM task into smaller, manageable steps (Prompt Chaining). 

*   **Purpose:** Generate a high-quality blog post by first drafting an outline, then writing the content based on that outline.
*   **State Schema:**
    *   `topic` (string)
    *   `outline` (string)
    *   `content` (string)
*   **Nodes:**
    1.  **`generate_outline`:** Uses the `topic` to prompt the LLM to write a structural outline. Updates the `outline` state.
    2.  **`generate_blog`:** Uses *both* the `topic` and the newly generated `outline` to prompt the LLM for the final blog post. Updates the `content` state.
*   **Graph Flow:** `START` ➔ `generate_outline` ➔ `generate_blog` ➔ `END`
*   **Why use LangGraph for this?** Unlike traditional LCEL (LangChain Expression Language) chains that only return the final output, LangGraph's stateful nature means that after execution, you have access to the initial topic, the intermediate outline, *and* the final blog content.

---

## 📝 Practice Exercise

To test your understanding, try extending the **Prompt Chaining** workflow:

1.  **Define a new State Attribute:** Add a `score` (integer) to your State schema.
2.  **Create an Evaluator Node:** Build a third node called `evaluate_blog`.
3.  **Prompt Engineering:** Inside this node, pass the `outline` and `content` to the LLM and prompt it to: *"Act as an editor. Based on the provided outline, evaluate the final blog content and return an integer score out of 10."*
4.  **Update the Graph:** Wire the edges so the graph flows: `generate_blog` ➔ `evaluate_blog` ➔ `END`.