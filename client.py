import ollama

response = ollama.chat(
    model="llama3.2:3b",
    messages=[
        {
            "role": "system",
            "content": "You are Jarvis, a helpful virtual assistant. Give clear, concise answers."
        },
        {
            "role": "user",
            "content": "What is coding?"
        }
    ]
)

print(response.message.content)

