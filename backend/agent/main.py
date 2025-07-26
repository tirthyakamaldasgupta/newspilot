import tkinter as tk
from tkinter import scrolledtext
from graph import app
from state import AgentState


def run_agent():
    query = input_entry.get()
    input_entry.delete(0, tk.END)
    output_text.delete("1.0", tk.END)

    state = AgentState(query=query)

    for step in app.stream(state):
        output_text.insert(tk.END, f"{step}\n")
        output_text.see(tk.END)
        root.update_idletasks()

    output_text.insert(tk.END, "\n✅ Task completed.")
    output_text.see(tk.END)


root = tk.Tk()
root.title("News Assistant")

tk.Label(root, text="I can help you search news articles and email them to you.").pack(pady=5)

input_entry = tk.Entry(root, width=60)
input_entry.pack(padx=10, pady=5)

run_button = tk.Button(root, text="Submit", command=run_agent)
run_button.pack(pady=5)

output_text = scrolledtext.ScrolledText(root, width=80, height=20)
output_text.pack(padx=10, pady=10)

root.mainloop()
