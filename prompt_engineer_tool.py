import os
import openai
import tkinter as tk
from tkinter import ttk
from dotenv import load_dotenv

# Load API key from environment variable
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Set up the OpenAI API key
openai.api_key = "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"

def generate_response(prompt, model="text-davinci-002", max_tokens=100, temperature=0.5):
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=max_tokens,
        n=1,
        stop=None,
        temperature=temperature,
    )
    return response.choices[0].text.strip()

def on_generate_click():
    prompt = prompt_entry.get()
    model = model_entry.get() or "text-davinci-002"
    max_tokens = int(max_tokens_entry.get() or 100)
    temperature = float(temperature_entry.get() or 0.5)

    response = generate_response(prompt, model, max_tokens, temperature)

    response_text.delete(1.0, tk.END)
    response_text.insert(tk.END, response)

# Create main window
window = tk.Tk()
window.title("Prompt Engineer Tool")

# Create input fields and labels
prompt_label = ttk.Label(window, text="Prompt:")
prompt_entry = ttk.Entry(window, width=50)

model_label = ttk.Label(window, text="Model:")
model_entry = ttk.Entry(window, width=50)

max_tokens_label = ttk.Label(window, text="Max tokens:")
max_tokens_entry = ttk.Entry(window, width=50)

temperature_label = ttk.Label(window, text="Temperature:")
temperature_entry = ttk.Entry(window, width=50)

# Create "Generate" button
generate_button = ttk.Button(window, text="Generate", command=on_generate_click)

# Create response text area
response_label = ttk.Label(window, text="Response:")
response_text = tk.Text(window, wrap=tk.WORD, width=60, height=10)

# Grid layout
prompt_label.grid(row=0, column=0, sticky="e")
prompt_entry.grid(row=0, column=1, padx=10)

model_label.grid(row=1, column=0, sticky="e")
model_entry.grid(row=1, column=1)

max_tokens_label.grid(row=2, column=0, sticky="e")
max_tokens_entry.grid(row=2, column=1)

temperature_label.grid(row=3, column=0, sticky="e")
temperature_entry.grid(row=3, column=1)

generate_button.grid(row=4, column=1, pady=10)

response_label.grid(row=5, column=0, sticky="nw")
response_text.grid(row=5, column=1)

# Run the GUI
window.mainloop()
