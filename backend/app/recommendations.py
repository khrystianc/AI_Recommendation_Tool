import openai

openai.api_key = "your_openai_api_key"

def generate_recommendations(user_preferences):
    preferences = [pref.to_dict() for pref in user_preferences]
    response = openai.Completion.create(
        engine="davinci",
        prompt=f"Generate recommendations based on: {preferences}",
        max_tokens=50
    )
    return response.choices[0].text.strip()
