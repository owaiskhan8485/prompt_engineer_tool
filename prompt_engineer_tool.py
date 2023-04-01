import os
import openai
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from dotenv import load_dotenv
import threading

# Load API key from environment variable
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Set up the OpenAI API key
openai.api_key = "your_api_key_here"

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

def generate_response_on_click():
    generate_button.config(state="disabled")
    progress_bar["value"] = 0
    progress_bar.start(10)
    prompt = prompt_entry.get()
    model = model_listbox.get(tk.ACTIVE)
    max_tokens = int(max_tokens_scale.get())
    temperature = float(temperature_scale.get())

    try:
        threading.Thread(target=generate_response_thread, args=(prompt, model, max_tokens, temperature)).start()
    except Exception as e:
        response_text.delete(1.0, tk.END)
        response_text.insert(tk.END, f"Error: {e}")
        progress_bar.stop()
        generate_button.config(state="normal")

def generate_response_thread(prompt, model, max_tokens, temperature):
    response = generate_response(prompt, model, max_tokens, temperature)
    response_text.delete(1.0, tk.END)
    response_text.insert(tk.END, response)
    progress_bar.stop()
    progress_bar["value"] = 100
    generate_button.config(state="normal")

def save_prompt():
    prompt = prompt_entry.get()
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    if file_path:
        with open(file_path, "w") as file:
            file.write(prompt)

def load_prompt():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, "r") as file:
            prompt = file.read()
        prompt_entry.delete(0, tk.END)
        prompt_entry.insert(0, prompt)

def create_menu(window):
    menu = tk.Menu(window)
    window.config(menu=menu)

    file_menu = tk.Menu(menu)
    menu.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="Save Prompt", command=save_prompt)
    file_menu.add_command(label="Load Prompt", command=load_prompt)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=window.quit)

def create_widgets(window):
    global prompt_entry, model_listbox, max_tokens_scale, temperature_scale
    global generate_button, progress_bar, response_text

    prompt_label = ttk.Label(window, text="Prompt:")
    prompt_entry = ttk.Entry(window, width=50)

    model_label = ttk.Label(window, text="Model:")
    model_listbox = tk.Listbox(window, height=6)
    model_listbox_scrollbar = ttk.Scrollbar(window, orient="vertical", command=model_listbox.yview)
    model_listbox.config(yscrollcommand=model_listbox_scrollbar.set)
    for item in ["text-davinci-003", "text-davinci-002", "text-curie-001", "text-babbage-001"]:
        model_listbox.insert(tk.END, item)
    model_listbox.activate(0)

    max_tokens_label = ttk.Label(window, text="Max tokens:")
    max_tokens_scale = tk.Scale(window, from_=10, to=1000, orient=tk.HORIZONTAL, length=200)

    temperature_label = ttk.Label(window, text="Temperature:")
    temperature_scale = tk.Scale(window, from_=0.1, to=1.0, orient=tk.HORIZONTAL, length=200, resolution=0.1)

    generate_button = ttk.Button(window, text="Generate", command=generate_response_on_click)

    progress_bar = ttk.Progressbar(window, orient="horizontal", length=250, mode="determinate")

    response_label = ttk.Label(window, text="Response:")
    response_text = tk.Text(window, wrap=tk.WORD, width=60, height=10)
    response_text_scrollbar = ttk.Scrollbar(window, orient="vertical", command=response_text.yview)
    response_text.config(yscrollcommand=response_text_scrollbar.set)

    setup_grid(prompt_label, prompt_entry, model_label, model_listbox, model_listbox_scrollbar, max_tokens_label,
               max_tokens_scale, temperature_label, temperature_scale, generate_button, progress_bar, response_label,
               response_text, response_text_scrollbar)



def setup_grid(prompt_label, prompt_entry, model_label, model_listbox, model_listbox_scrollbar, max_tokens_label,
               max_tokens_scale, temperature_label, temperature_scale, generate_button, progress_bar, response_label,
               response_text, response_text_scrollbar):

    prompt_label.grid(row=0, column=0, sticky="e")
    prompt_entry.grid(row=0, column=1, padx=10)

    model_label.grid(row=1, column=0, sticky="e")
    model_listbox.grid(row=1, column=1)
    model_listbox_scrollbar.grid(row=1, column=2, sticky="ns")

    max_tokens_label.grid(row=2, column=0, sticky="e")
    max_tokens_scale.grid(row=2, column=1)

    temperature_label.grid(row=3, column=0, sticky="e")
    temperature_scale.grid(row=3, column=1)

    generate_button.grid(row=4, column=1, pady=10)

    progress_bar.grid(row=5, column=0, columnspan=2)

    response_label.grid(row=6, column=0, sticky="nw")
    response_text.grid(row=6, column=1)
    response_text_scrollbar.grid(row=6, column=2, sticky="ns")

def main():
    window = tk.Tk()
    window.title("Prompt Engineer Tool")
    window.geometry("600x600")

    create_menu(window)
    create_widgets(window)

    window.mainloop()

if __name__ == "__main__":
    main()

