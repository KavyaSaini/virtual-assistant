"""
Configuration settings for AI Virtual Assistant (EDITH).
Supports loading environment variables from .env file.
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Base directory
BASE_DIR = Path(__file__).resolve().parent

# Load .env file
ENV_PATH = BASE_DIR / ".env"
load_dotenv(dotenv_path=ENV_PATH)

# Assistant settings
ASSISTANT_NAME = os.getenv("ASSISTANT_NAME", "EDITH")
USER_NAME = os.getenv("USER_NAME", "Student")

# LLM API Configuration
# Default to Google Gemini API
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "").strip()
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")

# Audio Settings
SPEECH_RATE = int(os.getenv("SPEECH_RATE", "175"))
SPEECH_VOLUME = float(os.getenv("SPEECH_VOLUME", "1.0"))
VOICE_ENABLED_DEFAULT = os.getenv("VOICE_ENABLED", "false").lower() in ("true", "1", "yes")

# Notes storage path
NOTES_FILE = BASE_DIR / "notes.txt"
