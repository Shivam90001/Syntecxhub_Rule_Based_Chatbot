import tkinter as tk
from tkinter import scrolledtext, filedialog
from datetime import datetime

knowledge_base = {
    "what is ai": "Artificial Intelligence enables machines to perform tasks that normally require human intelligence.",
    "what is machine learning": "Machine Learning is a subset of AI that learns patterns from data.",
    "what is deep learning": "Deep Learning uses neural networks with multiple layers to learn complex patterns.",
    "what is python": "Python is a popular programming language used in AI, web development, automation and data science.",
    "who created python": "Python was created by Guido van Rossum.",
    "what is data science": "Data Science combines statistics, programming and domain knowledge to extract insights from data.",
    "what is chatbot": "A chatbot is a software application that interacts with users through text or voice.",
    "what is nlp": "Natural Language Processing helps computers understand and process human language.",
    "what is computer vision": "Computer Vision enables computers to understand images and videos.",
    "what is neural network": "A neural network is a machine learning model inspired by the human brain.",
    "what is cloud computing": "Cloud Computing provides computing resources over the internet.",
    "what is cybersecurity": "Cybersecurity protects systems, networks and data from cyber threats.",
    "what is data mining": "Data Mining is the process of discovering patterns from large datasets.",
    "what is automation": "Automation uses technology to perform tasks with minimal human intervention.",
    "what is generative ai": "Generative AI creates new content such as text, images, audio and code."
}

def save_history(user_text, bot_text):
    with open("chat_history.txt", "a", encoding="utf-8") as file:
        file.write(f"\n[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]\n")
        file.write(f"User: {user_text}\n")
        file.write(f"Bot: {bot_text}\n")

def get_response(message):
    msg = message.lower().strip()

    if msg in ["hi", "hello", "hey", "hii"]:
        return "Hello! Welcome. How can I help you today?"

    elif "help" in msg:
        return "You can ask me questions about AI, Python, Machine Learning, Cybersecurity, NLP, Cloud Computing and more."

    elif "how are you" in msg:
        return "I am doing great. Thanks for asking."

    elif "your name" in msg:
        return "My name is Syntecx AI Assistant."

    elif "joke" in msg:
        return "Why do programmers prefer dark mode? Because light attracts bugs."

    elif "thank" in msg:
        return "You're welcome."

    elif "bye" in msg or "goodbye" in msg:
        return "Goodbye. Have a wonderful day."

    elif msg in knowledge_base:
        return knowledge_base[msg]

    else:
        return "Sorry, I don't have an answer for that. Please try another question."

def send_message():
    user_text = entry.get().strip()

    if user_text == "":
        return

    time_now = datetime.now().strftime("%H:%M")

    chat_area.insert(tk.END, f"\n[{time_now}] You: {user_text}\n")

    bot_reply = get_response(user_text)

    chat_area.insert(tk.END, f"[{time_now}] Bot: {bot_reply}\n")

    save_history(user_text, bot_reply)

    chat_area.see(tk.END)

    entry.delete(0, tk.END)

def clear_chat():
    chat_area.delete("1.0", tk.END)
    chat_area.insert(
        tk.END,
        "Bot: Welcome to Syntecx AI Assistant\nAsk your questions below.\n"
    )

def save_chat():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")]
    )

    if file_path:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(chat_area.get("1.0", tk.END))

root = tk.Tk()
root.title("Syntecx AI Chatbot")
root.geometry("750x550")
root.resizable(False, False)

title = tk.Label(
    root,
    text="Syntecx AI Chatbot",
    font=("Arial", 18, "bold")
)
title.pack(pady=10)

chat_area = scrolledtext.ScrolledText(
    root,
    wrap=tk.WORD,
    font=("Arial", 11)
)
chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

chat_area.insert(
    tk.END,
    "Bot: Welcome to Syntecx AI Assistant\nAsk your questions below.\n"
)

bottom_frame = tk.Frame(root)
bottom_frame.pack(fill=tk.X, padx=10, pady=5)

entry = tk.Entry(
    bottom_frame,
    font=("Arial", 12)
)
entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))

send_button = tk.Button(
    bottom_frame,
    text="Send",
    width=10,
    command=send_message
)
send_button.pack(side=tk.LEFT)

clear_button = tk.Button(
    root,
    text="Clear Chat",
    width=15,
    command=clear_chat
)
clear_button.pack(pady=5)

save_button = tk.Button(
    root,
    text="Save Chat",
    width=15,
    command=save_chat
)
save_button.pack(pady=5)

entry.bind("<Return>", lambda event: send_message())

root.mainloop()