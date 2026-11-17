"""
Course      : AIP203 - Artificial Intelligence Lab
Experiment  : Build a Virtual Assistant
Module      : llm_engine.py
Description : Comprehensive intelligence engine answering all conceptual,
              algorithmic, complexity, implementation, and comparison
              questions across the entire AI Lab syllabus.
"""

import os
import json
import urllib.request
from config import GEMINI_API_KEY, GEMINI_MODEL

SYSTEM_INSTRUCTION = (
    "You are an expert academic AI professor and tutor for the AIP203 Artificial Intelligence Lab. "
    "When answering any student question, do NOT just provide a one-line definition. "
    "Provide a detailed, well-structured explanation covering: "
    "1. Intuition and Core Concept "
    "2. Algorithm Steps or Working Principle "
    "3. Time and Space Complexity with reasons "
    "4. Key Formulas / Heuristics / Proofs (if applicable) "
    "5. Pros, Cons, and Practical Applications. "
    "Format clearly with headings and bullet points."
)


def is_llm_configured():
    """Returns True if user has configured an active Gemini API key."""
    key = os.getenv("GEMINI_API_KEY", "").strip()
    return bool(key and key != "YOUR_GEMINI_API_KEY_HERE")


def query_gemini_api(prompt, api_key):
    """
    Queries Google Gemini API for deep generative answers.
    """
    try:
        from google import genai
        client = genai.Client(api_key=api_key)
        res = client.models.generate_content(
            model=GEMINI_MODEL,
            contents=prompt,
            config={"system_instruction": SYSTEM_INSTRUCTION}
        )
        if res and res.text:
            return res.text.strip()
    except Exception:
        pass

    try:
        endpoint = f"https://generativelanguage.googleapis.com/v1beta/models/{GEMINI_MODEL}:generateContent?key={api_key}"
        headers = {"Content-Type": "application/json"}
        payload = {
            "contents": [
                {"role": "user", "parts": [{"text": f"{SYSTEM_INSTRUCTION}\n\nStudent Query: {prompt}"}]}
            ]
        }
        req = urllib.request.Request(endpoint, data=json.dumps(payload).encode("utf-8"), headers=headers, method="POST")
        with urllib.request.urlopen(req, timeout=15) as response:
            result = json.loads(response.read().decode("utf-8"))
            return result["candidates"][0]["content"]["parts"][0]["text"].strip()
    except Exception as e:
        return f"Gemini API request error: {e}"


# ==============================================================================
# COMPREHENSIVE AI LAB KNOWLEDGE REASONING ENGINE
# Covers all aspects: concepts, algorithms, complexities, code, comparisons
# ==============================================================================

def answer_ai_query(q: str) -> str:
    """
    Comprehensive rule-based knowledge engine covering every sub-question
    about BFS, DFS, IDS, Simulated Annealing, Hill Climbing, 8-Puzzle,
    Wumpus World, Towers of Hanoi, A*, D*, Bayesian Networks, EM, and HMM.
    """
    lower = q.lower()

    # --------------------------------------------------------------------------
    # 1. BFS vs DFS / Comparisons
    # --------------------------------------------------------------------------
    if ("bfs" in lower and "dfs" in lower) or ("difference" in lower and ("bfs" in lower or "dfs" in lower)):
        return (
            "### Comparison: Breadth-First Search (BFS) vs Depth-First Search (DFS)\n\n"
            "| Parameter | BFS | DFS |\n"
            "| :--- | :--- | :--- |\n"
            "| **Data Structure** | FIFO Queue | LIFO Stack (or Recursion) |\n"
            "| **Traversal Strategy** | Explores level by level | Explores branch to deepest node before backtracking |\n"
            "| **Time Complexity** | O(V + E) or O(b^d) | O(V + E) or O(b^m) |\n"
            "| **Space Complexity** | O(b^d) (High memory consumption) | O(bm) or O(d) (Very memory efficient) |\n"
            "| **Completeness** | Complete (guaranteed to find goal if b is finite) | Incomplete in infinite depth graphs |\n"
            "| **Optimality** | Optimal for unweighted graphs (finds shallowest goal) | Not optimal (may return a deeper non-optimal path) |\n\n"
            "**When to use which?**\n"
            "- Use **BFS** when the target is likely close to the root or when the shortest path is strictly required.\n"
            "- Use **DFS** when memory is constrained, when tree depth is bounded, or for topological sorting and maze traversal."
        )

    # --------------------------------------------------------------------------
    # 2. Depth-First Search (DFS)
    # --------------------------------------------------------------------------
    if "dfs" in lower or "depth first" in lower:
        if any(w in lower for w in ["complexity", "time complexity", "space complexity"]):
            return (
                "### Complexity Analysis of Depth-First Search (DFS)\n\n"
                "- **Time Complexity**: **O(V + E)** for graphs represented using Adjacency Lists, or **O(b^m)** for search trees, "
                "where `b` is the branching factor and `m` is the maximum depth of the state space.\n"
                "- **Space Complexity**: **O(V)** for storing visited vertices, or **O(b * m)** on the recursion stack. "
                "DFS requires significantly less memory than BFS because it only retains the current branch and its sibling alternatives."
            )
        if any(w in lower for w in ["code", "implementation", "python", "pseudocode"]):
            return (
                "### Python Implementation of Depth-First Search (DFS)\n\n"
                "```python\n"
                "def dfs(graph, start, visited=None):\n"
                "    if visited is None:\n"
                "        visited = set()\n"
                "    visited.add(start)\n"
                "    print(start, end=' ')\n\n"
                "    for neighbor in graph.get(start, []):\n"
                "        if neighbor not in visited:\n"
                "            dfs(graph, neighbor, visited)\n"
                "    return visited\n\n"
                "# Example Graph Representation:\n"
                "# graph = {'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['F'], 'D': [], 'E': [], 'F': []}\n"
                "# dfs(graph, 'A') -> Output: A B D E C F\n"
                "```"
            )
        return (
            "### Depth-First Search (DFS)\n\n"
            "**1. Core Intuition:**\n"
            "DFS explores as far as possible along each branch before backtracking. It operates using a **LIFO Stack** "
            "(either explicitly or via Python recursion).\n\n"
            "**2. Algorithm Steps:**\n"
            "1. Push starting node onto the stack and mark it as visited.\n"
            "2. While the stack is not empty, pop the top node.\n"
            "3. If the node is the goal, terminate and return success.\n"
            "4. Otherwise, for each unvisited neighbor, mark as visited and push to the stack.\n"
            "5. If no unvisited neighbors exist, backtrack to the previous node.\n\n"
            "**3. Properties:**\n"
            "- **Time Complexity**: O(V + E) or O(b^m)\n"
            "- **Space Complexity**: O(b * m) (Memory friendly)\n"
            "- **Completeness**: Incomplete in infinite depth trees or cycles (unless visited set is used)\n"
            "- **Optimality**: Not optimal (does not guarantee the shortest path)."
        )

    # --------------------------------------------------------------------------
    # 3. Breadth-First Search (BFS)
    # --------------------------------------------------------------------------
    if "bfs" in lower or "breadth first" in lower:
        if any(w in lower for w in ["complexity", "time complexity", "space complexity"]):
            return (
                "### Complexity Analysis of Breadth-First Search (BFS)\n\n"
                "- **Time Complexity**: **O(V + E)** for adjacency lists, or **O(b^d)** in a search tree where `b` is branching factor "
                "and `d` is the depth of the shallowest solution.\n"
                "- **Space Complexity**: **O(b^d)**. The queue must hold all nodes at the current frontier level. "
                "Because exponential memory is required, space is usually the primary bottleneck in BFS rather than execution time."
            )
        if any(w in lower for w in ["code", "implementation", "python", "pseudocode"]):
            return (
                "### Python Implementation of Breadth-First Search (BFS)\n\n"
                "```python\n"
                "from collections import deque\n\n"
                "def bfs(graph, start):\n"
                "    visited = set([start])\n"
                "    queue = deque([start])\n\n"
                "    while queue:\n"
                "        node = queue.popleft()\n"
                "        print(node, end=' ')\n\n"
                "        for neighbor in graph.get(node, []):\n"
                "            if neighbor not in visited:\n"
                "                visited.add(neighbor)\n"
                "                queue.append(neighbor)\n"
                "```"
            )
        return (
            "### Breadth-First Search (BFS)\n\n"
            "**1. Core Intuition:**\n"
            "BFS explores the state space systematically in concentric layers. It visits all immediate neighbors (depth 1) "
            "before moving to depth 2, using a **FIFO Queue**.\n\n"
            "**2. Algorithm Steps:**\n"
            "1. Enqueue root node and mark as visited.\n"
            "2. Dequeue front node from queue.\n"
            "3. If node is the goal state, return success.\n"
            "4. Enqueue all unvisited adjacent neighbors and mark them as visited.\n"
            "5. Repeat until queue is empty or goal is found.\n\n"
            "**3. Properties:**\n"
            "- **Time Complexity**: O(b^d)\n"
            "- **Space Complexity**: O(b^d) (Exponential memory)\n"
            "- **Completeness**: Complete if branching factor `b` is finite.\n"
            "- **Optimality**: Guaranteed optimal for unweighted graphs (finds the path with fewest edges)."
        )

    # --------------------------------------------------------------------------
    # 4. Iterative Deepening Search (IDS / IDDFS)
    # --------------------------------------------------------------------------
    if "iterative deepening" in lower or "ids" in lower or "iddfs" in lower:
        return (
            "### Iterative Deepening Search (IDS / IDDFS)\n\n"
            "**1. What is IDS?**\n"
            "Iterative Deepening Search is a hybrid strategy that combines the **optimality and completeness of BFS** "
            "with the **space efficiency of DFS**.\n\n"
            "**2. How it works:**\n"
            "It repeatedly executes Depth-Limited Search (DLS), starting at depth limit 0 and incrementing the limit by 1 each iteration:\n"
            "- Iteration 0: DLS(depth=0)\n"
            "- Iteration 1: DLS(depth=1)\n"
            "- Iteration d: DLS(depth=d) until goal is found.\n\n"
            "**3. Complexity:**\n"
            "- **Time Complexity**: O(b^d). Although nodes in top levels are regenerated, the bottom level contains b^d nodes, "
            "so the regeneration overhead is only around 1/(1 - 1/b), which is asymptotically identical to BFS.\n"
            "- **Space Complexity**: **O(b * d)** (Linear memory like DFS, solving the BFS memory bottleneck!).\n"
            "- **Completeness & Optimality**: Complete and optimal for uniform step costs."
        )

    # --------------------------------------------------------------------------
    # 5. A* Algorithm
    # --------------------------------------------------------------------------
    if "a*" in lower or "a star" in lower:
        if any(w in lower for w in ["admissible", "heuristic", "proof", "optimality", "consistent"]):
            return (
                "### A* Search: Admissibility and Consistency\n\n"
                "**1. Evaluation Function:**\n"
                "`f(n) = g(n) + h(n)`\n"
                "- `g(n)` = exact cost incurred from start node to current node `n`.\n"
                "- `h(n)` = estimated heuristic cost from `n` to the goal.\n\n"
                "**2. Admissible Heuristic (Tree Search Optimality):**\n"
                "A heuristic is **admissible** if it never overestimates the true cost to reach the goal: `0 <= h(n) <= h*(n)`.\n"
                "If h(n) is admissible, A* tree search is guaranteed to return the optimal cost solution.\n\n"
                "**3. Consistent Heuristic (Graph Search Optimality):**\n"
                "A heuristic is **consistent (monotonic)** if for every node `n` and successor `n'` generated by action `a`:\n"
                "`h(n) <= c(n, a, n') + h(n')` (satisfies Triangle Inequality).\n"
                "Consistency guarantees that the first time a state is expanded in graph search, its optimal path is already found!"
            )
        if any(w in lower for w in ["dijkstra", "difference", "compare"]):
            return (
                "### A* Search vs Dijkstra's Algorithm\n\n"
                "- **Dijkstra's Algorithm** evaluates nodes based solely on `f(n) = g(n)`. It expands blindly in all directions like a circle.\n"
                "- **A* Search** adds an informed heuristic: `f(n) = g(n) + h(n)`. The heuristic directs the search beam towards the goal, "
                "greatly reducing the number of nodes expanded.\n"
                "- When `h(n) = 0` for all nodes, A* becomes identical to Dijkstra's algorithm."
            )
        return (
            "### A* Search Algorithm\n\n"
            "**1. Overview:**\n"
            "A* is the most widely used informed, best-first graph traversal algorithm in artificial intelligence. "
            "It computes an evaluation function for every node:\n"
            "`f(n) = g(n) + h(n)`\n\n"
            "**2. Algorithm Execution:**\n"
            "1. Maintain an `Open Set` (Priority Queue ordered by lowest `f(n)`) and a `Closed Set` (visited nodes).\n"
            "2. Initialize `Open Set` with start node `s` (`f(s) = g(s) + h(s) = 0 + h(s)`).\n"
            "3. Extract node `n` with smallest `f(n)`.\n"
            "4. If `n` is goal, reconstruct path and return.\n"
            "5. Add `n` to `Closed Set`.\n"
            "6. For each neighbor `m` of `n`, compute `g(m) = g(n) + cost(n, m)`. If `m` is unvisited or has a lower cost path, update its `f(m)`.\n\n"
            "**3. Complexity:**\n"
            "- **Time Complexity**: O(b^d) in worst case (exponential), but linear when heuristic error is bounded by O(log h*).\n"
            "- **Space Complexity**: O(b^d) because all explored nodes must be held in memory."
        )

    # --------------------------------------------------------------------------
    # 6. D* Algorithm (Dynamic A*)
    # --------------------------------------------------------------------------
    if "d*" in lower or "d star" in lower or "dynamic a*" in lower:
        return (
            "### D* Search Algorithm (Dynamic A*)\n\n"
            "**1. What is D*?**\n"
            "D* (Dynamic A*) is an informed incremental search algorithm designed by Anthony Stentz for real-time mobile robot navigation "
            "in unknown, dynamic, or changing environments.\n\n"
            "**2. The Key Problem It Solves:**\n"
            "If an autonomous vehicle plans a route with A*, and suddenly encounters an unexpected road blockage, re-running A* from scratch "
            "is computationally expensive. D* modifies previously computed cost estimates locally and replans paths in real-time.\n\n"
            "**3. How it operates:**\n"
            "- Plans backward from goal to start.\n"
            "- Maintains state tags: `NEW`, `OPEN`, `CLOSED`.\n"
            "- Uses key values to propagate cost changes only through affected regions rather than re-evaluating the entire graph."
        )

    # --------------------------------------------------------------------------
    # 7. Simulated Annealing
    # --------------------------------------------------------------------------
    if "simulated annealing" in lower or "annealing" in lower:
        return (
            "### Simulated Annealing Algorithm\n\n"
            "**1. Physical Analogy:**\n"
            "Simulated Annealing is inspired by the metallurgy process of annealing: heating a metal to high temperature "
            "and cooling it slowly to form defect-free crystalline structures with minimal energy.\n\n"
            "**2. Overcoming Local Extrema:**\n"
            "Standard hill climbing only takes uphill (better) steps and easily gets trapped in local maxima. "
            "Simulated Annealing escapes local extrema by probabilistically accepting downhill (worse) moves:\n"
            "`P(accept) = exp(-ΔE / T)`\n"
            "- `ΔE` is the difference in evaluation score (`E_next - E_current`).\n"
            "- `T` is the current Temperature parameter.\n\n"
            "**3. Temperature Schedule:**\n"
            "- At **high T** (early stages), the system accepts worse moves readily, allowing broad global exploration.\n"
            "- As **T cools down** (geometric cooling: `T = T * alpha`, e.g., alpha = 0.95), acceptance of bad moves approaches zero, "
            "converting the algorithm into fine-grained local hill climbing."
        )

    # --------------------------------------------------------------------------
    # 8. Hill Climbing
    # --------------------------------------------------------------------------
    if "hill climbing" in lower:
        return (
            "### Hill Climbing Algorithm\n\n"
            "**1. Working Principle:**\n"
            "Hill Climbing is a greedy local search algorithm. Starting from an initial state, it continuously moves in the direction "
            "of steepest ascent (highest evaluation value) among its neighboring states. It terminates when no neighbor has a higher value.\n\n"
            "**2. Major Limitations:**\n"
            "1. **Local Maxima**: A peak that is higher than neighboring states but lower than the global maximum.\n"
            "2. **Ridges**: A sequence of local maxima where sides are steep, causing the algorithm to oscillate.\n"
            "3. **Plateaus / Flat Local Maxima**: Flat areas where all neighbors have the same score, making gradient direction zero.\n\n"
            "**3. Solutions & Variants:**\n"
            "- **Random-Restart Hill Climbing**: Runs series of hill climbing searches from random starting positions until global optimum is reached.\n"
            "- **Stochastic Hill Climbing**: Chooses randomly among uphill moves weighted by slope steepness."
        )

    # --------------------------------------------------------------------------
    # 9. 8-Puzzle Problem
    # --------------------------------------------------------------------------
    if "8 puzzle" in lower or "eight puzzle" in lower:
        if any(w in lower for w in ["heuristic", "manhattan", "misplaced"]):
            return (
                "### Heuristics for the 8-Puzzle Problem\n\n"
                "**1. Misplaced Tiles Heuristic (h1):**\n"
                "- Counts how many numbered tiles are not in their final goal position.\n"
                "- **Admissibility**: Admissible because each misplaced tile must move at least once (`h1 <= h*`).\n\n"
                "**2. Manhattan Distance Heuristic (h2):**\n"
                "- Computes the sum of absolute horizontal and vertical grid distances for each tile from its target position:\n"
                "  `h2 = sum(|x_current - x_goal| + |y_current - y_goal|)`\n"
                "- **Dominance**: `h2` dominates `h1` (`h2(n) >= h1(n)` for all states), meaning A* with Manhattan distance expands "
                "significantly fewer states while retaining optimal guarantees!"
            )
        return (
            "### 8-Puzzle Problem Formulation\n\n"
            "**1. Problem Description:**\n"
            "A 3x3 board containing 8 numbered square tiles (1 through 8) and 1 blank space. "
            "The objective is to slide tiles into the blank space to transform an initial configuration into a goal configuration.\n\n"
            "**2. State Space:**\n"
            "- Total tile permutations: `9! = 362,880`.\n"
            "- Reachable state space: Exactly half are reachable from any valid starting position (`9! / 2 = 181,440` states).\n\n"
            "**3. Problem Elements:**\n"
            "- **States**: Location of each tile on the 3x3 board.\n"
            "- **Operators (Actions)**: Move blank tile [Left, Right, Up, Down].\n"
            "- **Goal Test**: Current board configuration matches target state.\n"
            "- **Path Cost**: Each move has a unit cost of 1."
        )

    # --------------------------------------------------------------------------
    # 10. Wumpus World
    # --------------------------------------------------------------------------
    if "wumpus" in lower:
        return (
            "### Wumpus World Problem (Knowledge-Based Reasoning)\n\n"
            "**1. Environment Characteristics (PEAS):**\n"
            "- **Performance Measure**: +1000 for climbing out with gold, -1000 for falling in pit or eaten by Wumpus, -1 per step, -10 for shooting arrow.\n"
            "- **Environment**: 4x4 grid of rooms surrounded by walls.\n"
            "- **Actuators**: Forward, TurnLeft, TurnRight, Grab (gold), Shoot (arrow), Climb (out of cave).\n"
            "- **Sensors (5 Percepts)**:\n"
            "  1. `Stench`: Sensed in square containing Wumpus and directly adjacent squares (not diagonally).\n"
            "  2. `Breeze`: Sensed in squares directly adjacent to a Pit.\n"
            "  3. `Glitter`: Sensed when standing on the square containing Gold.\n"
            "  4. `Bump`: Sensed when walking into a wall.\n"
            "  5. `Scream`: Heard anywhere when the Wumpus is killed by an arrow.\n\n"
            "**2. Logical Inference Strategy:**\n"
            "The agent uses Propositional Logic. If room [1,1] has no breeze and no stench, [1,2] and [2,1] are proven 100% safe. "
            "By combining logical rules (e.g., `B_1,2 <=> (P_1,1 v P_2,2 v P_1,3)`), the agent proves which rooms are safe before moving."
        )

    # --------------------------------------------------------------------------
    # 11. Towers of Hanoi
    # --------------------------------------------------------------------------
    if "hanoi" in lower or "towers of hanoi" in lower:
        return (
            "### Towers of Hanoi Problem\n\n"
            "**1. Objective & Rules:**\n"
            "Move `n` disks of differing sizes from a Source peg (A) to a Destination peg (C) using an Auxiliary peg (B), subject to:\n"
            "1. Only one disk can be moved at a time.\n"
            "2. Only the uppermost disk from any peg can be removed.\n"
            "3. No larger disk may ever be placed on top of a smaller disk.\n\n"
            "**2. Recurrence Relation & Complexity:**\n"
            "- Recurrence: `T(n) = 2T(n-1) + 1` with base condition `T(1) = 1`.\n"
            "- Minimum moves required: **2^n - 1**.\n"
            "- **Time Complexity**: **O(2^n)** (Exponential).\n"
            "- **Space Complexity**: **O(n)** (Recursion stack depth).\n\n"
            "**3. Recursive Logic:**\n"
            "1. Move `n-1` disks from Source to Auxiliary using Destination peg.\n"
            "2. Move `n-th` largest disk directly from Source to Destination.\n"
            "3. Move `n-1` disks from Auxiliary to Destination using Source peg."
        )

    # --------------------------------------------------------------------------
    # 12. Bayesian Networks
    # --------------------------------------------------------------------------
    if "bayesian" in lower or "bayes" in lower:
        return (
            "### Bayesian Networks (Probabilistic Graphical Models)\n\n"
            "**1. Definition:**\n"
            "A Bayesian Network is a Directed Acyclic Graph (DAG) that represents a set of random variables and their "
            "conditional dependencies via directed edges.\n\n"
            "**2. Mathematical Foundation:**\n"
            "- **Bayes' Rule**: `P(A | B) = [P(B | A) * P(A)] / P(B)`\n"
            "- **Chain Rule for Joint Probability**:\n"
            "  `P(X_1, X_2, ..., X_n) = Product_{i=1 to n} P(X_i | Parents(X_i))`\n\n"
            "**3. Key Concepts:**\n"
            "- **Conditional Probability Table (CPT)**: Quantifies the probability distribution of each variable given all combinations of its parents.\n"
            "- **Conditional Independence & D-Separation**: If two nodes are conditionally independent given evidence variables, "
            "their joint distribution factors, drastically simplifying probabilistic inference from exponential to polynomial."
        )

    # --------------------------------------------------------------------------
    # 13. Expectation-Maximization (EM) Algorithm
    # --------------------------------------------------------------------------
    if "em algorithm" in lower or "expectation maximization" in lower or "expectation-maximization" in lower:
        return (
            "### Expectation-Maximization (EM) Algorithm\n\n"
            "**1. Purpose:**\n"
            "The EM algorithm is an iterative optimization technique to calculate Maximum Likelihood Estimates (MLE) "
            "in statistical models with unobserved (latent) variables or missing data.\n\n"
            "**2. The Two Alternating Steps:**\n"
            "1. **E-Step (Expectation)**: Calculates the expected value of the complete-data log-likelihood with respect to the "
            "conditional distribution of latent variable `Z` given observed data `X` and current parameter estimates `theta^(t)`:\n"
            "   `Q(theta | theta^(t)) = E_{Z|X, theta^(t)} [ log P(X, Z | theta) ]`\n"
            "2. **M-Step (Maximization)**: Updates model parameters by maximizing the expectation function `Q`:\n"
            "   `theta^(t+1) = argmax_{theta} Q(theta | theta^(t))`\n\n"
            "**3. Applications:**\n"
            "- Gaussian Mixture Models (GMM) clustering\n"
            "- Training Hidden Markov Models (Baum-Welch algorithm)\n"
            "- Medical diagnosis with incomplete patient records."
        )

    # --------------------------------------------------------------------------
    # 14. Hidden Markov Models (HMM)
    # --------------------------------------------------------------------------
    if "hmm" in lower or "hidden markov" in lower:
        return (
            "### Hidden Markov Model (HMM)\n\n"
            "**1. Core Architecture:**\n"
            "An HMM is a bivariate discrete-time stochastic process where the system state `X_t` is hidden/unobservable, "
            "but emits observable observations `Y_t` governed by probabilistic laws.\n\n"
            "**2. The Five Tuples (S, V, A, B, pi):**\n"
            "- `S`: Set of hidden states.\n"
            "- `V`: Set of observation symbols.\n"
            "- `A`: Transition Probability Matrix `A = {a_ij = P(X_{t+1}=s_j | X_t=s_i)}`.\n"
            "- `B`: Emission Probability Matrix `B = {b_j(k) = P(Y_t=v_k | X_t=s_j)}`.\n"
            "- `pi`: Initial state distribution `pi_i = P(X_1 = s_i)`.\n\n"
            "**3. The 3 Canonical Problems & Algorithms:**\n"
            "1. **Evaluation**: Given observation sequence `O` and model `lambda`, find `P(O | lambda)`.\n"
            "   -> Solved by **Forward-Backward Algorithm**.\n"
            "2. **Decoding**: Given `O`, find the single most probable sequence of hidden states.\n"
            "   -> Solved by **Viterbi Algorithm** (Dynamic Programming).\n"
            "3. **Learning**: Optimize model parameters `lambda = (A, B, pi)` given observations.\n"
            "   -> Solved by **Baum-Welch Algorithm** (an EM algorithm variant)."
        )

    # Default general fallback
    return (
        f"### Academic AI Inquiry: '{q}'\n\n"
        "I can answer conceptual, mathematical, complexity, and algorithmic questions across your AI Lab curriculum, including:\n"
        "- **Uninformed Search**: DFS, BFS, Iterative Deepening Search (IDS).\n"
        "- **Informed Search**: A* Search, Admissibility/Consistency proofs, D* Algorithm.\n"
        "- **Local Search**: Hill Climbing, Simulated Annealing.\n"
        "- **Constraint & Logic Problems**: 8-Puzzle heuristics (Manhattan vs Misplaced), Wumpus World agent, Towers of Hanoi.\n"
        "- **Probabilistic Models**: Bayesian Networks, Expectation-Maximization (EM), and Hidden Markov Models (HMM).\n\n"
        "Try asking: *'What is time complexity of BFS vs DFS?'*, *'Explain Manhattan distance heuristic'*, or *'How does Viterbi algorithm work in HMM?'*."
    )


def ask_llm(prompt: str) -> str:
    """
    Main entry point:
    If Gemini API key is configured, queries the Gemini LLM.
    Otherwise, uses the built-in comprehensive academic AI reasoning engine.
    """
    key = os.getenv("GEMINI_API_KEY", "").strip()
    if key and key != "YOUR_GEMINI_API_KEY_HERE":
        ans = query_gemini_api(prompt, key)
        if not ans.startswith("Gemini API request error"):
            return ans

    # Comprehensive multi-angle knowledge engine
    return answer_ai_query(prompt)
