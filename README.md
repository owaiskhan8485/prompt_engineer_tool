# Prompt Engineer Tool

A Python application that generates AI responses using OpenAI's GPT models. This application provides a graphical user interface to facilitate the input of prompts and generate the response. The user can input the desired prompt, model, maximum tokens, and temperature to generate responses.
## Requirements

-Python 3.6 or higher
-Tkinter (usually comes pre-installed with Python, but you can install it with pip install tk if it's missing)
-OpenAI Python library: pip install openai
-Python-dotenv library: pip install python-dotenv

## Setup

1. Sign up for an OpenAI API key if you don't have one already: https://beta.openai.com/signup/
2. Create a `.env` file in the same directory as your `prompt_engineer_tool.py` script.
3. Add your OpenAI API key to the `.env` file like this:

    OPENAI_API_KEY=your_api_key_here

Replace `your_api_key_here` with your actual OpenAI API key.

## Usage

1. Run the `prompt_engineer_tool.py` script:

   python prompt_engineer_tool.py

2. Enter the following values in the GUI:

- **Model**: The name of the AI model you want to use (e.g.,"text-davinci-003", "text-davinci-002", "text-curie-002", "text-babbage-002", or "text-ada-002").
- **Max tokens**: The maximum number of tokens (words or word pieces) in the generated response (e.g., 100).
- **Temperature**: A value between 0 and 1 that controls the randomness of the generated response (e.g., 0.5).

3. Click the "Generate" button to generate the AI response based on your input.

## Troubleshooting

If the application is not working as expected or not showing any output, make sure you have installed all the required libraries, set up your `.env` file with the correct API key, and entered valid values for the Model, Max tokens, and Temperature fields.

If you still encounter issues, please check the Python console for any error messages or traceback information that may help diagnose the problem.

