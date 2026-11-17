# 🤖 EDITH — Artificial Intelligence Virtual Assistant

> **Course**: AIP203 — Artificial Intelligence Laboratory  
> **Credit**: 1 (L-T-P: 0-0-2)  
> **Student Name**: Ayush Srivastava  
> **Technologies**: Python 3, FastAPI, Uvicorn, Google Gemini LLM API, Windows SAPI, Web Speech API  

---

## 📖 Table of Contents
1. [Overview](#-overview)
2. [Key Capabilities](#-key-capabilities)
3. [Syllabus Coverage](#-syllabus-coverage-aip203)
4. [System Architecture](#-system-architecture)
5. [Directory Structure](#-directory-structure)
6. [Getting Started](#-getting-started)
   - [Option 1: Web Interface (Localhost)](#option-1-web-interface-localhost)
   - [Option 2: Terminal Interface (CLI)](#option-2-terminal-interface-cli)
7. [Configuring Google Gemini API Key](#-configuring-google-gemini-api-key)
8. [Sample Test Queries](#-sample-test-queries)
9. [Academic Lab Evaluation Notes](#-academic-lab-evaluation-notes)

---

## 🌟 Overview

**EDITH** (*Even Dead, I'm The Hero*) is a modular, hybrid AI Virtual Assistant engineered for academic evaluation in the **AIP203 Artificial Intelligence Laboratory**.

It bridges the gap between **deterministic operational tools** (system hardware monitoring, application launching, calendar/clock, mathematical calculations) and **generative artificial intelligence** (Google Gemini LLM API), complemented by an extensive offline reasoning engine covering the complete AI lab curriculum.

---

## ⚡ Key Capabilities

- **Dual User Interfaces**:
  - **Modern Web Application**: Clean, responsive web portal hosted locally at `http://localhost:8000`.
  - **Console / CLI App**: Interactive terminal loop for command-line grading (`python main.py`).
- **Comprehensive AI Domain Knowledge**:
  - Detailed answers to complex questions on search algorithms, heuristics, game agents, and probabilistic models.
  - Generates algorithm steps, time and space complexity proofs, comparison tables, and Python implementations.
- **Speech Interaction (STT & TTS)**:
  - **Speech-to-Text**: Voice dictation through the browser's Web Speech API.
  - **Text-to-Speech**: Speech synthesis powered by native Windows SAPI (`win32com.client.Dispatch("SAPI.SpVoice")`).
- **Operating System & Tool Integration**:
  - **Hardware Diagnostics**: Real-time CPU and RAM utilization metrics via `psutil`.
  - **Web Navigation**: Automated searches and website launch (Google, YouTube, GitHub).
  - **Utility Launchers**: Instant access to Calculator and Notepad.
  - **Persistent Notes**: Save and retrieve timestamped notes in `notes.txt`.
  - **Safe Math Engine**: Evaluation of mathematical expressions.
- **Fail-Safe Offline Mode**:
  - Operates reliably even without an internet connection or API key, answering all syllabus questions with complete accuracy.

---

## 📚 Syllabus Coverage (AIP203)

| Lab Unit | Curriculum Experiment | EDITH Capability |
| :--- | :--- | :--- |
| **Labs 1 to 3** | DFS, BFS, Iterative Deepening Search (IDS), Simulated Annealing | Explains traversal orders, queue/stack usage, complexity derivations, temperature cooling schedules, and code. |
| **Labs 4 to 5** | Wumpus World Problem, 8-Puzzle, Towers of Hanoi | Knowledge-based inference rules, Manhattan vs Misplaced heuristics, $2^n - 1$ recurrence relations. |
| **Labs 6 to 7** | A\*, D\*, and Hill Climbing Algorithm | Admissibility/consistency proofs, dynamic path cost replanning, local maxima/ridge escape strategies. |
| **Labs 8 to 10** | Bayesian Networks, EM Algorithm, Hidden Markov Models (HMM) | Bayes' theorem, CPT tables, E-step & M-step formulations, Forward-Backward, Viterbi decoding, and Baum-Welch learning. |
| **Labs 11 to 12** | **Build a Virtual Assistant** | **The EDITH Assistant System** (this project). |

---

## 🏗️ System Architecture

```
                      +---------------------------------------+
                      |         Student / User Input          |
                      |    (Web Portal / Terminal / Voice)    |
                      +-------------------+-------------------+
                                          |
                                          v
                      +---------------------------------------+
                      |           EDITH Orchestrator          |
                      |            (assistant.py)             |
                      +-------------------+-------------------+
                                          |
                   +----------------------+----------------------+
                   |                                             |
                   v                                             v
       [Operational Tool Intent?]                   [Conceptual / AI Query]
                   |                                             |
        +----------+----------+                                  v
        |                     |                     +---------------------------+
        v                     v                     |    Intelligence Engine    |
  [Local Tools]       [System Automation]           |      (llm_engine.py)      |
  • Clock Time        • Open Browser/YouTube        +-------------+-------------+
  • Calendar Date     • Launch Calculator/Notepad                 |
  • Math Calculator   • Note Taking (notes.txt)                   v
  • System Status     • Syllabus Information             [API Key Present?]
        |                     |                            /             \
        +----------+----------+                          YES              NO
                   |                                      |                |
                   v                                      v                v
        +---------------------+                   [Gemini API]    [Knowledge Engine]
        |  Formatted Response |                           \                /
        +----------+----------+                            \              /
                   |                                        +------+-----+
                   v                                               |
        +----------------------------------------------------------+
        |                 Output Presentation Handler              |
        |      • Web Chat Bubble (Markdown + Tables + Code)        |
        |      • Spoken Audio (Windows SAPI / Browser TTS)         |
        +----------------------------------------------------------+
```

---

## 📁 Directory Structure

```
.
├── main.py              # Interactive CLI entry point
├── server.py            # Localhost FastAPI web server
├── assistant.py         # Intent classification & action router
├── llm_engine.py        # Gemini LLM client & syllabus knowledge engine
├── tools.py             # System hardware metrics, browser, calculator, notes
├── voice_engine.py      # Thread-safe Windows SAPI voice synthesizer
├── config.py            # Configuration & environment variable loader
├── requirements.txt     # Python dependency specifications
├── .env                 # Environment variables (API keys)
├── .env.example         # Environment template
├── notes.txt            # Local storage for student notes
├── web/
│   └── index.html       # Clean student web portal
└── LAB_MANUAL.md        # Formal academic lab report & Viva Voce Q&A
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10+ (tested on Python 3.14)
- Google Chrome or Microsoft Edge (for microphone dictation)

### Dependencies Installation
All core dependencies (`fastapi`, `uvicorn`, `python-dotenv`, `psutil`, `pywin32`, `requests`, `google-genai`) are specified in `requirements.txt`:
```bash
pip install -r requirements.txt
```

---

### Option 1: Web Interface (Localhost)

To launch the web interface:
```bash
python server.py
```
Open your browser and navigate to:
👉 **`http://localhost:8000`**

- **Mic Dictation (🎙️)**: Click the microphone button in the input bar to speak.
- **Voice Output (🔊)**: Toggle the voice button in the top right to enable/disable spoken answers.
- **Sample Queries**: Click any pre-configured question on the left sidebar for instant testing.

---

### Option 2: Terminal Interface (CLI)

For command-line execution and demonstration:
```bash
python main.py
```

**Commands inside CLI**:
- `voice on` / `voice off` — Enable or mute spoken speech output.
- `set key` — Paste your Gemini API key directly into the terminal.
- `syllabus` — Display the AIP203 laboratory curriculum.
- `exit` — Exit the program.

---

## 🔑 Configuring Google Gemini API Key

EDITH is fully integrated with **Google Gemini**. A free API key can be obtained in seconds without a credit card:

1. Visit **Google AI Studio**:  
   👉 `https://aistudio.google.com/app/apikey`
2. Sign in with your Google account.
3. Click **"Create API Key"** and copy the generated key string (`AIzaSy...`).
4. Paste it into your [.env](file:///c:/Users/Ayush%20Srivastava/Downloads/New%20folder%20(2)/.env) file:
   ```env
   GEMINI_API_KEY=AIzaSyYourKeyHere
   GEMINI_MODEL=gemini-2.5-flash
   ASSISTANT_NAME=EDITH
   ```
*(Note: If no API key is configured, EDITH seamlessly falls back to its comprehensive offline syllabus reasoning engine with zero errors.)*

---

## 🧪 Sample Test Queries

| Query Type | Input | What EDITH Does |
| :--- | :--- | :--- |
| **Complexity Analysis** | `"What is the time complexity of BFS vs DFS?"` | Provides a comparison table detailing data structures, time complexities, and memory usage. |
| **Heuristics & Proofs** | `"Why is A* admissible and consistent?"` | Explains $f(n) = g(n) + h(n)$, tree search admissibility, and graph search triangle inequality. |
| **8-Puzzle Problem** | `"Explain Manhattan distance in 8 puzzle"` | Formulates $h_2$, explains absolute coordinate distances, and proves dominance over misplaced tiles. |
| **Wumpus World** | `"How does the Wumpus World agent reason?"` | Outlines percepts (`[Stench, Breeze, Glitter, Bump, Scream]`) and propositional inference rules. |
| **Local Search** | `"How does Simulated Annealing escape local maxima?"` | Explains the cooling schedule and probability equation $P = e^{-\Delta E / T}$. |
| **Probabilistic Models** | `"Explain the 3 main problems in HMM"` | Details the Forward-Backward evaluation, Viterbi decoding, and Baum-Welch training algorithms. |
| **Hardware Diagnostics** | `"system status"` | Reads live CPU percentage and RAM usage through `psutil`. |
| **Math Calculations** | `"calculate (45 * 2) + 15"` | Evaluates the expression safely and returns `105`. |
| **Note Taking** | `"save note Submit AI Lab record on Friday"` | Appends timestamped entry to `notes.txt`. |

---

## 🎓 Academic Lab Evaluation Notes

For formal lab submissions, project reports, and viva preparation, refer to:
👉 **[LAB_MANUAL.md](file:///c:/Users/Ayush%20Srivastava/Downloads/New%20folder%20(2)/LAB_MANUAL.md)**

It contains:
- Complete Experiment Abstract & Objectives
- Theoretical Foundation (NLP, Search Algorithms, Large Language Models)
- Viva Voce Questions & Answers frequently asked by university examiners
