"""
Course      : AIP203 - Artificial Intelligence Lab
Experiment  : Build a Virtual Assistant
Module      : voice_engine.py
Description : Text-to-Speech (TTS) using Windows Native SAPI (win32com)
              with thread-safe COM initialization and graceful fallbacks.
"""

import sys
import threading

_pyttsx3_engine = None
try:
    import pyttsx3
    _pyttsx3_engine = pyttsx3.init()
except Exception:
    pass


def speak(text: str, wait: bool = False):
    """
    Thread-safe speech synthesis using Windows SAPI or pyttsx3.
    """
    if not text:
        return

    def _speak_worker():
        try:
            # Initialize COM for the current thread (required by Windows)
            import pythoncom
            pythoncom.CoInitialize()
        except Exception:
            pass

        try:
            import win32com.client
            speaker = win32com.client.Dispatch("SAPI.SpVoice")
            # 0 = synchronous within this worker thread
            speaker.Speak(str(text), 0)
        except Exception:
            try:
                if _pyttsx3_engine is not None:
                    _pyttsx3_engine.say(str(text))
                    _pyttsx3_engine.runAndWait()
            except Exception:
                pass

    if wait:
        _speak_worker()
    else:
        t = threading.Thread(target=_speak_worker, daemon=True)
        t.start()


def listen(timeout: int = 5, phrase_time_limit: int = 10) -> str:
    """
    Listens for speech input from the microphone.
    Falls back to console input if SpeechRecognition / PyAudio is unavailable.
    """
    try:
        import speech_recognition as sr
        recognizer = sr.Recognizer()
        recognizer.energy_threshold = 300
        recognizer.dynamic_energy_threshold = True

        with sr.Microphone() as source:
            print("[Listening... Speak now]")
            recognizer.adjust_for_ambient_noise(source, duration=0.8)
            audio = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)

        query = recognizer.recognize_google(audio)
        return query
    except Exception:
        # Fall back to keyboard input cleanly without crashing
        return input("[Type your query]: ").strip()
