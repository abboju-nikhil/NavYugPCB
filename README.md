# NavYugPCB

> **AI-Powered Local Hardware Engineering Assistant for KiCad 10**

NavYugPCB is an AI-assisted Electronic Design Automation (EDA) project that converts natural language hardware design requirements into production-ready KiCad projects using a fully local AI pipeline.

The project combines Retrieval-Augmented Generation (RAG), local Large Language Models (LLMs), and deterministic Python code generation to create accurate, reproducible electronic designs while keeping all engineering data private.

---

# Features

* 🛡️ 100% Local AI (No cloud dependency)
* 📚 Local Engineering Knowledge Base (RAG)
* 🤖 Natural Language Circuit Design
* ⚡ Automatic KiCad 10 Project Generation
* 📖 Datasheet-Aware Component Selection
* 🔍 Semantic Search over Engineering Documents
* 🧩 Deterministic Schematic Generation
* 🚀 Designed for Production-Grade PCB Development

---

# Vision

Instead of manually drawing every schematic, an engineer can simply write:

> Design a 12V LED indicator using a 330Ω resistor.

NavYugPCB automatically:

```
Natural Language
        │
        ▼
Local AI Understanding
        │
        ▼
Engineering RAG Search
        │
        ▼
Circuit JSON
        │
        ▼
KiCad Project Generator
        │
        ▼
.kicad_pro
.kicad_sch
.kicad_pcb
```

---

# Project Goals

* Generate complete KiCad projects
* Eliminate hallucinated component selections
* Use engineering datasheets as the source of truth
* Produce deterministic CAD output
* Enable offline hardware design workflows

---

# Technology Stack

## Backend

* Python 3.14
* FastAPI
* Uvicorn

## AI

* Ollama
* Qwen3.5:4B

## RAG Pipeline

* PyMuPDF
* SentenceTransformers
* all-MiniLM-L6-v2
* ChromaDB

## EDA

* KiCad 10

---

# Project Architecture

```
                    User Prompt
                         │
                         ▼
                  FastAPI Backend
                         │
                         ▼
                 Retrieve RAG Context
                    (ChromaDB)
                         │
                         ▼
                Prompt + Engineering Data
                         │
                         ▼
                 Ollama (Qwen3.5)
                         │
              Intermediate Circuit JSON
                         │
                         ▼
           Deterministic Python Compiler
                         │
         ┌───────────────┴───────────────┐
         ▼                               ▼
   .kicad_pro                     .kicad_sch
                         │
                         ▼
                    .kicad_pcb
```

---

# Current Project Structure

```
NavYugPCB/

├── ai/
│   ├── llm.py
│   └── prompts.py
│
├── backend/
│   ├── app/
│   ├── kicad_generator.py
│   └── main.py
│
├── rag/
│   ├── pdf_reader.py
│   ├── chunker.py
│   ├── embeddings.py
│   └── vector_store.py
│
├── scripts/
│
├── tests/
│
├── knowledge/
│   ├── Datasheets/
│   ├── Application Notes/
│   ├── Books/
│   └── PCB Design/
│
├── output/
│
└── README.md
```

---

# Development Progress

## ✅ Phase 1

* Local Ollama integration
* FastAPI backend
* KiCad project generation
* Empty schematic generation
* Local RAG pipeline

---

## 🚧 Phase 2 (Current)

* AI Requirement Parser
* JSON Circuit Representation
* Component Extraction
* Netlist Generation
* Prompt Optimization

---

## 📋 Planned Phases

### Phase 3

* Deterministic KiCad Schematic Compiler

### Phase 4

* Footprint Assignment

### Phase 5

* PCB Placement

### Phase 6

* Routing

### Phase 7

* Design Rule Check (DRC)

### Phase 8

* Electrical Rule Check (ERC)

### Phase 9

* BOM Generation

### Phase 10

* Gerber Generation

---

# AI Design Philosophy

The Large Language Model is responsible only for **engineering reasoning**.

It does **not** generate KiCad files directly.

Instead, it produces an intermediate JSON representation.

Example flow:

```
Natural Language
      │
      ▼
AI Understanding
      │
      ▼
Circuit JSON
      │
      ▼
Python Compiler
      │
      ▼
KiCad Files
```

This separation minimizes hallucinations and ensures deterministic, valid KiCad output.

---

# Example Workflow

### Input

```
Design a 12V LED indicator.
```

### AI Output

```json
{
  "components": [
    {
      "type": "resistor",
      "value": "330"
    },
    {
      "type": "led",
      "color": "green"
    }
  ],
  "connections": [
    ["VIN","R1","1"],
    ["R1","2","D1","1"],
    ["D1","2","GND"]
  ]
}
```

### Python Output

```
LED Indicator.kicad_pro

LED Indicator.kicad_sch

LED Indicator.kicad_pcb
```

---

# Future Capabilities

* AI-assisted PCB layout
* Component recommendation
* Automatic ERC/DRC fixing
* LTspice simulation generation
* Power electronics design automation
* Multi-sheet schematic generation
* Multi-layer PCB support
* Manufacturing file generation
* Cost optimization
* Design optimization using datasheets

---

# Installation

Clone the repository:

```bash
git clone https://github.com/<username>/NavYugPCB.git
cd NavYugPCB
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it:

### Windows

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the FastAPI server:

```bash
uvicorn backend.app.main:app --reload
```

---

# License

This project is currently under active development.

License information will be added before the first public release.

---

# Author

**Abboju Nikhil**

M.Tech – Power Electronics Engineer

AI Hardware Engineer | PCB Designer | Power Electronics Developer

---

# Project Status

**Active Development** 🚧

Current milestone: **AI Requirement Parser → Deterministic KiCad Schematic Generation**
