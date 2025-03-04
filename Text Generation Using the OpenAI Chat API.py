import openai

# Set your OpenAI API key
openai.api_key = "YOUR_OPENAI_API_KEY"

def generate_story(prompt: str) -> str:
    response = openai.ChatCompletion.create(
        model="gpt-4",  # You can use "gpt-3.5-turbo" if preferred
        messages=[
            {"role": "system", "content": "You are a creative storyteller who writes engaging short stories."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.8,
        max_tokens=250,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=["\n"]
    )
    return response.choices[0].message["content"].strip()

if __name__ == "__main__":
    prompt = "Write a short, imaginative story about a robot that discovers its passion for painting."
    story = generate_story(prompt)
    print("Generated Story:\n", story)
