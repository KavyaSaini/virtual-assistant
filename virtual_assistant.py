import datetime
import os
import webbrowser
import wikipedia
import pywhatkit

NOTES_FILE = "assistant_notes.txt"


def speak(message):
    print("\nAssistant:", message)


def tell_time():
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    speak("The current time is " + current_time)


def tell_date():
    current_date = datetime.datetime.now().strftime("%d %B %Y")
    speak("Today's date is " + current_date)


def save_note():
    note = input("Enter your note: ").strip()

    if note == "":
        speak("You did not enter a note.")
        return

    with open(NOTES_FILE, "a", encoding="utf-8") as file:
        file.write(note + "\n")

    speak("Your note has been saved.")


def read_notes():
    if not os.path.exists(NOTES_FILE):
        speak("You do not have any saved notes.")
        return

    with open(NOTES_FILE, "r", encoding="utf-8") as file:
        notes = file.read().strip()

    if notes:
        speak("Here are your saved notes:\n" + notes)
    else:
        speak("You do not have any saved notes.")


def answer_common_questions(command):
    command = command.lower().strip()

    answers = {
        "capital of india": "The capital of India is New Delhi.",
        "what is the capital of india": "The capital of India is New Delhi.",
        "capital of france": "The capital of France is Paris.",
        "capital of japan": "The capital of Japan is Tokyo.",
        "what is ai": "Artificial Intelligence is a branch of computer science that makes machines perform tasks that normally require human intelligence.",
        "what is artificial intelligence": "Artificial Intelligence is a branch of computer science that makes machines perform tasks that normally require human intelligence.",
        "who is apj abdul kalam": "A. P. J. Abdul Kalam was an Indian aerospace scientist and the 11th President of India.",
        "who is mahatma gandhi": "Mahatma Gandhi was a leader of India's freedom movement and is widely known for his philosophy of non-violence."
    }

    if command in answers:
        speak(answers[command])
        return True

    return False


def search_web(query):
    if query:
        pywhatkit.search(query)
        speak("Here are the search results for " + query)
    else:
        speak("Please tell me what you want to search.")


def wikipedia_search(topic):
    if not topic:
        speak("Please provide a topic.")
        return

    try:
        result = wikipedia.summary(topic, sentences=3, auto_suggest=True)
        speak(result)
    except wikipedia.exceptions.DisambiguationError:
        speak("This topic has multiple meanings. Please make your search more specific.")
    except wikipedia.exceptions.PageError:
        speak("I could not find this topic on Wikipedia. I will search it on Google.")
        search_web(topic)
    except Exception:
        speak("I could not connect to Wikipedia. Please check your internet connection.")


def show_commands():
    speak(
        "You can try these commands:\n"
        "1. hello\n"
        "2. time\n"
        "3. date\n"
        "4. capital of india\n"
        "5. what is AI\n"
        "6. who is APJ Abdul Kalam\n"
        "7. open google\n"
        "8. open youtube\n"
        "9. open gmail\n"
        "10. search followed by a topic\n"
        "11. wikipedia followed by a topic\n"
        "12. save note\n"
        "13. read notes\n"
        "14. exit\n\n"
        "You can also type a general question, and I will try to find it on Wikipedia."
    )


def process_command(command):
    command = command.lower().strip()

    if command == "":
        return True

    if command in ["hello", "hi", "hey"]:
        speak("Hello! How can I help you?")

    elif "time" in command:
        tell_time()

    elif "date" in command or "today" in command:
        tell_date()

    elif answer_common_questions(command):
        pass

    elif command == "open google":
        webbrowser.open("https://www.google.com")
        speak("Opening Google.")

    elif command == "open youtube":
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube.")

    elif command == "open gmail":
        webbrowser.open("https://mail.google.com")
        speak("Opening Gmail.")

    elif command.startswith("search "):
        query = command[len("search "):].strip()
        search_web(query)

    elif command.startswith("wikipedia "):
        topic = command[len("wikipedia "):].strip()
        wikipedia_search(topic)

    elif command == "save note":
        save_note()

    elif command == "read notes":
        read_notes()

    elif command in ["help", "commands"]:
        show_commands()

    elif command in ["exit", "quit", "stop", "bye"]:
        speak("Goodbye! Have a nice day.")
        return False

    else:
        # If no built-in command matches, try searching the question on Wikipedia.
        wikipedia_search(command)

    return True


def main():
    print("=" * 50)
    print("             PYTHON VIRTUAL ASSISTANT")
    print("=" * 50)

    speak("Hello! I am your virtual assistant.")
    speak("Type help to see the available commands.")

    running = True

    while running:
        command = input("\nYou: ")
        running = process_command(command)


if __name__ == "__main__":
    main()
