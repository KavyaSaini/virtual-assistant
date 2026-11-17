"""
=============================================================================
Course Name : Artificial Intelligence Lab (AIP203)
Experiment  : Build a Virtual Assistant (EDITH)
Submitted By: Student (Ayush Srivastava)
Semester/Yr : B.Tech CSE / AI Specialization
Description : EDITH - A Python virtual assistant capable of voice/text
              interaction, system utilities, and deep AI syllabus reasoning
              using the Google Gemini LLM API (with offline fallback).
=============================================================================
"""

import os
import sys
from pathlib import Path
from config import BASE_DIR, ENV_PATH
from assistant import VirtualAssistant
import voice_engine
import llm_engine


def setup_gemini_key():
    """Helper function to input and save the Gemini API key into .env"""
    print("\n--- Configure Google Gemini API Key ---")
    print("You can get a free key from: https://aistudio.google.com/app/apikey")
    key = input("Enter your Gemini API Key (or press Enter to skip): ").strip()
    if key:
        with open(ENV_PATH, "w", encoding="utf-8") as f:
            f.write(f"GEMINI_API_KEY={key}\nGEMINI_MODEL=gemini-2.5-flash\nASSISTANT_NAME=EDITH\n")
        os.environ["GEMINI_API_KEY"] = key
        print("[+] API Key saved to .env file successfully!\n")
    else:
        print("[!] No key entered. EDITH will run using offline knowledge.\n")


def print_lab_banner(voice_on: bool, llm_on: bool):
    print("=" * 60)
    print("   ARTIFICIAL INTELLIGENCE LAB - AIP203")
    print("   Experiment: Virtual Assistant (EDITH)")
    print("=" * 60)
    print(f" * Voice Output : {'ON (Windows SAPI)' if voice_on else 'OFF'}")
    print(f" * LLM Engine   : {'Google Gemini API (Active)' if llm_on else 'Offline Knowledge Engine'}")
    print("-" * 60)
    print(" Commands:")
    print("  'voice on' / 'voice off' : Toggle spoken speech")
    print("  'set key'                : Set Gemini API key")
    print("  'syllabus'               : Show AIP203 syllabus")
    print("  'exit'                   : Stop the assistant")
    print("=" * 60 + "\n")


def main():
    if not os.path.exists(ENV_PATH):
        with open(ENV_PATH, "w", encoding="utf-8") as f:
            f.write("GEMINI_API_KEY=\nGEMINI_MODEL=gemini-2.5-flash\nASSISTANT_NAME=EDITH\n")

    voice_enabled = False
    bot = VirtualAssistant(voice_enabled=voice_enabled)

    print_lab_banner(voice_on=voice_enabled, llm_on=llm_engine.is_llm_configured())
    print("EDITH: Hello! I am EDITH, your AI Lab assistant. Type your command or question:\n")

    while True:
        try:
            user_input = input("Student > ").strip()
            if not user_input:
                continue

            cmd = user_input.lower()

            if cmd in ["exit", "quit", "stop", "bye"]:
                print("EDITH: Goodbye! Good luck with your AI Lab experiments.")
                break

            if cmd == "voice on":
                bot.voice_enabled = True
                print("[+] Voice output turned ON.")
                bot.speak("Voice output is now active.")
                continue
            elif cmd == "voice off":
                bot.voice_enabled = False
                print("[-] Voice output turned OFF.")
                continue

            if cmd in ["set key", "setup key", "api key"]:
                setup_gemini_key()
                continue

            reply = bot.process_command(user_input)
            print(f"\nEDITH: {reply}\n")

        except KeyboardInterrupt:
            print("\n[!] Program interrupted. Exiting EDITH...")
            break
        except Exception as e:
            print(f"[!] Error: {e}\n")


if __name__ == "__main__":
    main()
