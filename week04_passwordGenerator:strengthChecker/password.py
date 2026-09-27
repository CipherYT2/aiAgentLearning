import ollama

def checkPasswordStrength(password):
    stream = ollama.chat(
        model='gemma2',
        messages=[{
            'role': 'user',
            'content': f'Check the strength of the password provided at the end of the line. Make sure your output is only Password strength followed bylow, moderate, or high, high being the highest security. Inputted password: {password}'
        }],
        stream=True
    )
    for chunk in stream:
        print(chunk['message']['content'], end='', flush=True)

def generatePassword(length, easyRememberance):
    full_response = ""
    stream = ollama.chat(
        model='gemma2',
        messages=[{
            'role': 'user',
            'content': f'Generate a password where the length is {length} and how easy it is to remember to a human brain is {easyRememberance}, 10 is the easiest to remember and 0 is the absolute securest you can make. Do NOT generate any additional text. After that generate the strength of the password. Make the strength formated like in a new line and like: Generated password strength: low, medium or high. The format in which you should print is: Generated password: [password]'
        }],
        stream=True
    )
    for chunk in stream:
         content = chunk.message.content
         print(content, end='', flush=True)
         full_response += content
    return full_response.replace("Generated password: ", "")
while True:
    mode = input("1. Check password strength \n2. Generate password \n3. Exit \nInput: ")

    if mode == '3':
        break
    
    if mode == '2':
        print("PASSWORD GENERATOR \n")
        try:
            length, remember = input("Input the length, and how easy you want the password to be(10 is the easiest, 0 most secure). Format is (length, rememberance): ").split(', ')
            generatePassword(length, remember)
        except Exception as e:
            print("Unsupported Format.")

    if mode == '1':
        print("PASSWORD STRENGTH CHECKER \n")
        password = input("Input your password: ")
        checkPasswordStrength(password)

