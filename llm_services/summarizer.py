import openai

openai.api_key = "your-api-key"

def summarize_text(text: str) -> str:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{
            "role": "user",
            "content": f"Summarize the following research paper:\n\n{text}"
        }],
        max_tokens=700
    )
    return response["choices"][0]["message"]["content"]
