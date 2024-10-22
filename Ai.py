from openai import OpenAI
key = open("key1.py", "r").readline().strip('\n')
print(key)
client = OpenAI(api_key=key)

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Write a haiku about recursion in programming."
        }
    ]
)

print(completion.choices[0].message)
