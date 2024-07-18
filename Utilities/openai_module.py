import openai

# Make sure to replace 'your-api-key-here' with your actual OpenAI API key
openai.api_key = 'your-api-key-here'

def get_response(prompt):
    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            max_tokens=60,
            n=1,
            stop=None,
            temperature=0.5,
        )
        return response.choices[0].text.strip()
    except Exception as e:
        print(f"Error getting response from OpenAI: {e}")
        return "Sorry, I couldn't process your message."
