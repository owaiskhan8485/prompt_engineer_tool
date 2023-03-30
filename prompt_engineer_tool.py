import os
import openai
import tkinter as tk
from tkinter import ttk
from dotenv import load_dotenv

# Load API key from environment variable
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Set up the OpenAI API key
openai.api_key = "Your API Key here..."

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
    model = model_listbox.get(tk.ACTIVE)
    max_tokens = int(max_tokens_scale.get())
    temperature = float(temperature_scale.get())

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
model_listbox = tk.Listbox(window, height=3)
for item in ["text-davinci-002", "text-curie-001", "text-babbage-001"]:
    model_listbox.insert(tk.END, item)
model_listbox.activate(0)

max_tokens_label = ttk.Label(window, text="Max tokens:")
max_tokens_scale = tk.Scale(window, from_=10, to=1000, orient=tk.HORIZONTAL, length=200)

temperature_label = ttk.Label(window, text="Temperature:")
temperature_scale = tk.Scale(window, from_=0.1, to=1.0, orient=tk.HORIZONTAL, length=200, resolution=0.1)

# Create "Generate" button
generate_button = ttk.Button(window, text="Generate", command=on_generate_click)

# Create response text area
response_label = ttk.Label(window, text="Response:")
response_text = tk.Text(window, wrap=tk.WORD, width=60, height=10)

# Grid layout
prompt_label.grid(row=0, column=0, sticky="e")
prompt_entry.grid(row=0, column=1, padx=10)

model_label.grid(row=1, column=0, sticky="e")
model_listbox.grid(row=1, column=1)

max_tokens_label.grid(row=2, column=0, sticky="e")
max_tokens_scale.grid(row=2, column=1)

temperature_label.grid(row=3, column=0, sticky="e")
temperature_scale.grid(row=3, column=1)

generate_button.grid(row=4, column=1, pady=10)

response_label.grid(row=5, column=0, sticky="nw")
response_text.grid(row=5, column=1)

# Run the GUI
window.mainloop()
