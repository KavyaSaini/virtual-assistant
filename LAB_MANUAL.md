# Artificial Intelligence Laboratory (AIP203)
## Lab Experiment Record

* **Course Code**: AIP203  
* **Course Title**: Artificial Intelligence Laboratory  
* **Credit**: 1 (0-0-2)  
* **Student Name**: Ayush Srivastava  
* **Experiment**: Build a Virtual Assistant — EDITH (Labs 11 & 12)  

---

### 1. Objective
To design and implement **EDITH**, a modular Virtual Assistant in Python demonstrating natural language interaction, local task execution (system diagnostics, web automation, note taking, calculations), and integration with a Large Language Model (Google Gemini API) alongside an offline domain knowledge base.

---

### 2. Theory & System Design

#### A. Architecture Overview
The system follows a modular client-server and multi-tiered agent design:
1. **User Interface Layer**:
   - **Web Interface**: Lightweight client connecting to a local FastAPI server (`http://localhost:8000`).
   - **Command-Line Interface**: Terminal interaction via standard I/O (`python main.py`).
2. **Intent & Decision Layer (`assistant.py`)**:
   - Checks user queries against known operational intents (time, date, hardware diagnostics, calculator, note management, lab syllabus).
   - Unmatched queries are routed to the Large Language Model layer.
3. **LLM & Reasoning Layer (`llm_engine.py`)**:
   - Connects to Google's Gemini LLM API using secure authentication via `.env`.
   - In offline mode (or when no API key is supplied), a domain-specific fallback module handles questions related to AI search strategies (DFS, BFS, A*), adversarial/logic problems (Wumpus World, 8-Puzzle), and probabilistic models (Bayesian Networks, HMM, EM).
4. **Voice Synthesizer Layer (`voice_engine.py`)**:
   - Uses the native Windows Speech API (`SAPI.SpVoice`) via COM dispatch (`win32com.client`) with thread-safe `pythoncom` initialization for hardware-accelerated text-to-speech.

---

### 3. Implementation Modules

| File | Role |
|---|---|
| `server.py` | FastAPI backend server serving static portal and chat APIs on `localhost:8000`. |
| `main.py` | Standalone CLI entry point for console lab evaluation. |
| `assistant.py` | Rule-based intent recognition and delegation logic for EDITH. |
| `llm_engine.py` | Gemini API connection and syllabus knowledge engine. |
| `tools.py` | System hardware monitoring (`psutil`), calculator, note logging, and syllabus dictionary. |
| `voice_engine.py` | Windows SAPI audio synthesis engine. |
| `web/index.html` | Clean student web portal interface. |

---

### 4. Sample Test Logs

#### Test 1: Algorithm Query (DFS vs BFS)
* **Student Query**: `"What is the time complexity of BFS vs DFS?"`  
* **EDITH Response**: 
  *"Breadth-First Search (BFS) operates on a FIFO Queue with Time Complexity $O(V+E)$ or $O(b^d)$ and Space Complexity $O(b^d)$. Depth-First Search (DFS) operates on a LIFO Stack with Time Complexity $O(V+E)$ or $O(b^m)$ and Space Complexity $O(bm)$."*

#### Test 2: System Diagnostic Check
* **Student Query**: `"system status"`  
* **EDITH Response**: `"System Status: CPU usage is 10.2% | RAM usage is 68.1% (10950 MB / 16091 MB)."`

#### Test 3: Math Evaluation
* **Student Query**: `"calculate (45 * 2) + 15"`  
* **EDITH Response**: `"The result of (45 * 2) + 15 is 105."`

#### Test 4: Note Taking
* **Student Query**: `"save note Review A* heuristic proofs before lab exam"`  
* **EDITH Response**: `"Saved note: 'Review A* heuristic proofs before lab exam'"`

---

### 5. Viva Voce Questions & Answers

**Q1: What is the benefit of a hybrid architecture in EDITH?**  
*Answer*: Pure rule-based systems are deterministic and fast for exact commands (e.g., launching apps, checking system CPU), but cannot handle freeform language. Pure LLM systems can hallucinate and have network latency. A hybrid architecture combines the speed and security of local rules with the general intelligence of an LLM.

**Q2: How does EDITH handle lack of internet or missing API keys?**  
*Answer*: EDITH includes an offline fallback module (`llm_engine.answer_ai_query`) containing comprehensive representations of all course concepts (BFS, DFS, A*, 8-Puzzle, Wumpus World, Bayesian Networks, HMM, EM), preventing crashes when network or API keys are unavailable.

**Q3: What makes A\* search optimal?**  
*Answer*: A* search is guaranteed to find the optimal path if its heuristic function $h(n)$ is **admissible** (it never overestimates the true cost to reach the goal) for tree search and **consistent** (monotonicity condition: $h(n) \le c(n, a, n') + h(n')$) for graph search.
