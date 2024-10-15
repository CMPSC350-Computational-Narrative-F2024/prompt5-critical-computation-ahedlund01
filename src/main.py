# Code to generate "text"

#!/usr/bin/python

import os
import openai
from dotenv import dotenv_values

# Set up OpenAI credentials

CONFIG = dotenv_values(".env")

OPEN_AI_KEY = CONFIG["KEY"] or os.environ["OPEN_AI_KEY"]
OPEN_AI_ORG = CONFIG["ORG"] or os.environ["OPEN_AI_ORG"]

openai.api_key = OPEN_AI_KEY
openai.organization = OPEN_AI_ORG

def load_file(filename: str = "") -> str:
    """Loads an arbitrary file name"""
    with open(filename, "r") as fh:
        return fh.read()
    
def main():

    # Load source file
    source_text = load_file("data/source.txt")

    # Prepare the messages for the chat completion with an enhanced prompt
    messages = [
        {"role": "system", "content": "You are a literary scholar and critical text analyst."},
        {"role": "user", "content": (
            "Please read the following text and perform an advanced chain-of-thought analysis. "
            "Delve deeply into the text's themes, structure, language, and stylistic devices. "
            "Identify and interpret metaphors, symbolism, and any literary techniques used. "
            "Explore the relationships between words and phrases, and discuss how they contribute to the overall meaning. "
            "Provide historical or cultural context if relevant. Offer a comprehensive, step-by-step explanation of your reasoning, "
            "revealing hidden nuances and underlying messages within the text.\n\n"
            f"Text:\n{source_text}\n\n"
            "Advanced Chain of Thought Analysis:"
        )}
    ]

    # Call the OpenAI API
    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        max_tokens=1500,
        temperature=0.7
    )

    # Extract the assistant's reply
    analysis = response.choices[0].message.content

    # Output the analysis
    print("Advanced Chain of Thought Analysis:\n", analysis)

    # Save the output to text.md
    with open('../writing/text.md', 'w') as f:
        f.write("# Advanced Chain of Thought Analysis\n\n")
        f.write(analysis)
    
if __name__ == "__main__":
    main()
