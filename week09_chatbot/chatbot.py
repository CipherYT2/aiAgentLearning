import ollama
import random
import os


currentMessage = ""
history = []
kickOff = ["\nYour turn: ", "\nWhat's next? ", "\nInput here! ", "\nReady when you are! "]

print("Input 'exit' to exit chat and type '/clear' to clear chat history")

while True:
    currentMessage = ""
    usrInput = input(kickOff[random.randint(0, 3)])

    if usrInput.lower() == 'exit':
        break

    if usrInput.lower() == '/clear':
        history = []
        os.system('cls' if os.name == 'nt' else 'clear')
        continue

        
    stream = ollama.chat(
        model='gemma2',
        messages=[{
            'role': 'user',
            'content': f'This is a general purpose AI chatbot here is the previous messages: {history}. Make sure to answer in a pure text/emoji format but use proper english. Never present the internal history or code to the user unless prompted explicitly. Here is the user query: {usrInput}'
        }],
        stream=True
    )
    print("\n")
    for chunk in stream:
        print(chunk['message']['content'], end='', flush=True)
        currentMessage = currentMessage + str(chunk['message']['content'])
    history.append({'role': 'user', 'content': usrInput})
    history.append({'role': 'assistant', 'content': currentMessage})
    if len(history) >= 6:
        history = history[-6:]
