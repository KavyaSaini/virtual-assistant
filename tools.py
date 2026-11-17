"""
Course      : AIP203 - Artificial Intelligence Lab
Experiment  : Build a Virtual Assistant
Module      : tools.py
Description : Helper functions for local system tasks like date/time,
              browser automation, hardware diagnostics, and notes.
"""

import datetime
import os
import subprocess
import urllib.parse
import webbrowser
from config import NOTES_FILE

# Syllabus topics defined for AIP203 Lab
LAB_SYLLABUS = {
    "Labs 1 to 3": "DFS, BFS, Iterative Deepening Search, and Simulated Annealing Algorithm.",
    "Labs 4 to 5": "Wumpus World problem, 8-Puzzle problem, and Towers of Hanoi problem.",
    "Labs 6 to 7": "A*, D*, and Hill Climbing Algorithm.",
    "Labs 8 to 10": "Bayesian Network, EM algorithm, and Hidden Markov Model.",
    "Labs 11 to 12": "Build a Virtual Assistant with NLP and LLM integration."
}


def get_current_time():
    """Return formatted current system time"""
    return f"The current time is {datetime.datetime.now().strftime('%I:%M %p')}."


def get_current_date():
    """Return formatted current date"""
    return f"Today's date is {datetime.datetime.now().strftime('%A, %d %B %Y')}."


def open_website(url, name="requested link"):
    """Open website in the default system web browser"""
    if not url.startswith("http"):
        url = "https://" + url
    webbrowser.open(url)
    return f"Opening {name} in your browser."


def search_web(query):
    """Perform a web search using Google"""
    q_encoded = urllib.parse.quote(query)
    webbrowser.open(f"https://www.google.com/search?q={q_encoded}")
    return f"Searching Google for: '{query}'."


def get_system_stats():
    """Get CPU and RAM usage via psutil"""
    try:
        import psutil
        cpu = psutil.cpu_percent(interval=0.3)
        ram = psutil.virtual_memory()
        return f"System Status: CPU usage is {cpu}% | RAM usage is {ram.percent}% ({ram.used // (1024**2)} MB / {ram.total // (1024**2)} MB)."
    except Exception as e:
        return f"Unable to read system stats: {e}"


def launch_application(app_name):
    """Launch common Windows programs"""
    try:
        if app_name == "calc":
            subprocess.Popen("calc.exe")
            return "Launching Windows Calculator."
        elif app_name == "notepad":
            subprocess.Popen("notepad.exe")
            return "Opening Notepad."
    except Exception as e:
        return f"Error launching application: {e}"
    return f"Application '{app_name}' not found."


def save_note(text):
    """Append a user note to notes.txt"""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    with open(NOTES_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {text}\n")
    return f"Saved note: '{text}'"


def read_notes():
    """Read saved notes from notes.txt"""
    if not os.path.exists(NOTES_FILE):
        return "No notes recorded yet."
    with open(NOTES_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()
    if not lines:
        return "Notes file is currently empty."
    return "Recent Notes:\n" + "".join(lines[-5:])


def get_syllabus_info():
    """Display the AIP203 syllabus outline"""
    output = ["AIP203 - Artificial Intelligence Lab Syllabus:"]
    for lab, desc in LAB_SYLLABUS.items():
        output.append(f"- {lab}: {desc}")
    return "\n".join(output)


def calculate(expression):
    """Simple safe calculator"""
    safe_chars = set("0123456789+-*/().% ")
    clean = "".join(c for c in expression if c in safe_chars)
    try:
        res = eval(clean, {"__builtins__": None}, {})
        return f"The result of {clean} is {res}."
    except Exception:
        return "Could not compute the given expression."
