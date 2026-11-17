"""
Course      : AIP203 - Artificial Intelligence Lab
Experiment  : Build a Virtual Assistant (EDITH)
Module      : assistant.py
Description : Core assistant logic for EDITH: routes operational system
              commands and delegates AI questions to llm_engine.
"""

import re
from config import ASSISTANT_NAME, USER_NAME
import tools
import llm_engine
import voice_engine


class VirtualAssistant:
    def __init__(self, voice_enabled: bool = False):
        self.name = ASSISTANT_NAME
        self.user = USER_NAME
        self.voice_enabled = voice_enabled

    def speak(self, text: str):
        """Helper to speak text using the voice engine if enabled."""
        if self.voice_enabled:
            clean_text = re.sub(r"[*_#`|]", "", text)
            voice_engine.speak(clean_text, wait=False)

    def process_command(self, query: str) -> str:
        """
        Main routing function:
        - Operational system commands (clock, hardware, calc, notes, apps)
        - Conceptual / algorithmic queries -> llm_engine
        """
        if not query or not query.strip():
            return "Please enter a valid question or command."

        text = query.strip()
        q = text.lower()

        # 1. Greetings
        if q in ["hello", "hi", "hey", "greetings"]:
            msg = f"Hello! I am {self.name}, your Virtual Assistant. How can I assist you with your AI Lab questions today?"
            self.speak(msg)
            return msg

        if any(w in q for w in ["who are you", "what is your name"]):
            msg = f"I am {self.name} (Even Dead, I'm The Hero), your intelligent AI Virtual Assistant for the AIP203 Artificial Intelligence Lab."
            self.speak(msg)
            return msg

        # 2. Clock Time (Strict check to not collide with 'time complexity')
        clock_triggers = ["what is the time", "tell me the time", "what time is it", "current time", "time now"]
        if any(trig in q for trig in clock_triggers) and "complexity" not in q:
            msg = tools.get_current_time()
            self.speak(msg)
            return msg

        # 3. Calendar Date
        date_triggers = ["what is the date", "what is today's date", "todays date", "today's date", "current date"]
        if any(trig in q for trig in date_triggers):
            msg = tools.get_current_date()
            self.speak(msg)
            return msg

        # 4. System Diagnostics (CPU/RAM)
        if any(w in q for w in ["system status", "cpu usage", "ram usage", "memory usage", "system diagnostics"]):
            msg = tools.get_system_stats()
            self.speak(msg)
            return msg

        # 5. Launch Local Apps / URLs
        if q.startswith("open ") or q.startswith("launch "):
            target = q.replace("open", "").replace("launch", "").strip()
            if "youtube" in target:
                msg = tools.open_website("youtube.com", "YouTube")
            elif "google" in target:
                msg = tools.open_website("google.com", "Google")
            elif "calc" in target or "calculator" in target:
                msg = tools.launch_application("calc")
            elif "notepad" in target:
                msg = tools.launch_application("notepad")
            else:
                msg = tools.open_website(target, target)
            self.speak(msg)
            return msg

        # 6. Web Search
        if q.startswith("search ") or q.startswith("google "):
            term = re.sub(r"^(search|google)\s+(for\s+)?", "", q).strip()
            msg = tools.search_web(term)
            self.speak(msg)
            return msg

        # 7. Notes Management
        if q.startswith("save note ") or q.startswith("note that "):
            note_text = re.sub(r"^(save note|note that)\s+", "", text, flags=re.IGNORECASE).strip()
            msg = tools.save_note(note_text)
            self.speak("Note saved.")
            return msg

        if q in ["read notes", "show notes", "view notes", "my notes"]:
            msg = tools.read_notes()
            return msg

        # 8. Math Calculations
        if q.startswith("calculate ") or (q.startswith("what is ") and any(op in q for op in ["+", "-", "*", "/"]) and any(c.isdigit() for c in q)):
            expr = q.replace("calculate", "").replace("what is", "").strip()
            msg = tools.calculate(expr)
            self.speak(msg)
            return msg

        # 9. Syllabus Outline
        if q in ["syllabus", "lab syllabus", "show syllabus", "course content", "aip203 syllabus"]:
            msg = tools.get_syllabus_info()
            return msg

        # 10. Comprehensive AI Intelligence & LLM Engine
        response = llm_engine.ask_llm(text)
        self.speak(response)
        return response
