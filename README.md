<div align="center">

# 🤖 Path2AgenticAI

### My hands-on journey from zero to building Agentic AI systems — one concept at a time.

![Status](https://img.shields.io/badge/Status-🔴_Live_&_Ongoing-red?style=for-the-badge)
![Focus](https://img.shields.io/badge/Focus-LangChain_→_Agents-4F46E5?style=for-the-badge)
![Language](https://img.shields.io/badge/Language-Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

</div>

---

## 🌱 Why This Repo Exists

This is not a course. This is not a tutorial collection.

This is my **personal learning log** — a living record of me going deep into the LangChain ecosystem and the world of Agentic AI. Every folder is a concept I sat with, coded from scratch, broke, fixed, and finally understood.

The goal: to go from understanding how LLMs work in isolation → to building **autonomous AI agents** that can reason, plan, use tools, and act in the real world.

**This repo is still being written. Come back often.**

---

## 🗺️ The Learning Map

> Chapters are completed in order. Each builds on the last.

### 🔵 Phase 1 — LangChain Foundations
*Understanding the building blocks before assembling the machine.*

| # | Topic | What I Learned |
|---|-------|----------------|
| 01 | **LLMs** | How large language models work as the raw engine — direct text-in, text-out completions |
| 02 | **Chat Models** | The shift to message-based interaction (system / human / AI turns) and why it matters for agents |
| 03 | **Embedding Models** | Turning text into vectors — the math that makes semantic search and memory possible |
| 04 | **Prompts** | Prompt templates, few-shot prompting, dynamic prompt construction with variables |
| 05 | **Structured Output** | Forcing LLMs to return clean, typed data (JSON, Pydantic models) instead of raw text |
| 06 | **Output Parsers** | Parsing, validating, and transforming LLM responses into usable Python objects |

---

### 🟡 Phase 2 — Chains & The LCEL Way
*Composing components into intelligent pipelines.*

| # | Topic | What I Learned |
|---|-------|----------------|
| 07 | **Chains** | Chaining LLM calls together — sequential, parallel, and conditional logic |
| 08 | **Runnables** | LangChain Expression Language (LCEL) — the modern, composable way to build pipelines with `.pipe()` |

---

### 🟠 Phase 3 — RAG (Retrieval-Augmented Generation)
*Giving AI a long-term memory it can actually search.*

| # | Topic | What I Learned |
|---|-------|----------------|
| 09 | **Document Loaders** | Loading data from PDFs, web pages, text files, and other sources into LangChain |
| 10 | **Text Splitting** | Chunking strategies — why naive splitting breaks context and how to do it right |
| 11 | **Vector Stores** | Storing embeddings in ChromaDB, similarity search, and persistent vector databases |
| 12 | **Retrievers** | Querying vector stores intelligently — MMR, similarity thresholds, hybrid retrieval |

> 🗄️ **`my_chroma_db/`** — A persistent ChromaDB instance built during RAG experiments. Real data, real queries.

---

### 🔴 Phase 4 — Agentic AI *(Coming Soon)*
*This is where it gets serious.*

```
[ ] Tools & Tool Calling
[ ] ReAct Agents
[ ] LangGraph — Stateful, multi-step agent workflows
[ ] Memory Systems
[ ] Multi-Agent Architectures
[ ] Building a full Agentic system end-to-end
```

---

## 📁 Repo Structure

```
Path2AgenticAI/
│
├── 1.LLMs/                  # Raw LLM completions & model comparison
├── 2.ChatModels/            # Chat-based interaction patterns
├── 3.EmbeddedModels/        # Embedding generation & semantic similarity
├── 4.Prompts/               # Prompt templates & few-shot examples
├── 5.structured_output/     # Pydantic + with_structured_output()
├── 6.Output_Parsers/        # StrOutputParser, JsonOutputParser, etc.
├── 7.Chains/                # Sequential & parallel chains
├── 8.Runnabls/              # LCEL pipelines & RunnablePassthrough
├── 9.Document_Loaders/      # PDF, web, text loaders
├── 10.Text_Splitting/       # RecursiveCharacterTextSplitter & friends
├── 11.Vector_Stores/        # ChromaDB setup & embedding storage
├── 12.Retrievers/           # Retrieval strategies & RAG pipeline
└── my_chroma_db/            # Persistent vector store (local)
```

---

## 🛠️ Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=flat-square&logo=langchain&logoColor=white)
![ChromaDB](https://img.shields.io/badge/ChromaDB-Vector_Store-E8572A?style=flat-square)
![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=flat-square&logo=openai&logoColor=white)
![Groq](https://img.shields.io/badge/Groq-LLaMA-F54E00?style=flat-square)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=flat-square&logo=jupyter&logoColor=white)

---

## 💡 How to Use This Repo

Each folder is self-contained. You can clone and run any section independently.

```bash
git clone https://github.com/iamanu26/Path2AgenticAI.git
cd Path2AgenticAI

pip install langchain langchain-openai langchain-groq chromadb python-dotenv
```

Create a `.env` file in the root:
```env
OPENAI_API_KEY=your_key_here
GROQ_API_KEY=your_key_here
```

Then navigate to any folder and run the scripts.

---

## 🧠 The Bigger Picture

LangChain is just the foundation. The destination is **Agentic AI** — systems that don't just answer questions but can:

- Break down complex goals into sub-tasks
- Decide which tools to use and when
- Remember context across long interactions
- Collaborate with other agents
- Act in the real world via APIs and browsers

Every line of code in this repo is a step toward that.

---

<div align="center">

**⭐ Star this repo if you're on a similar path — let's learn in public.**

*Built by [Anurag Dubey](https://portfolio-iamanu26.vercel.app/) · Updated regularly*

</div>
