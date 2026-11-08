import ollama


text = input("Paste your text: ")

stream = ollama.chat(
    model='gemma2',
    messages=[{
        'role': 'system',
        'content': f"You are an expert text summarizer and you ALWAYS summarize in this format: SUMMARY:\n2-4 short sentence summary \nKEY POINTS:\n1. \n2. \n3. \n4. \n5. \n ONE SENTENCE VERSION: \nOne sentence summary. Make sure to follow the format exactly and do NOT add any extra text. Here is the user's text: {text}"
    }],
    stream=True
)
print()
for chunk in stream:
    print(chunk['message']['content'], end='', flush=True)
