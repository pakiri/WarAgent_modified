import openai
import os

# Replace 'your-api-key' with your actual OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')

def test_openai_api():
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Task: You plan to visit 3 European cities for 14 days in total. You only take direct flights to commute between cities. You would like to visit Florence for 6 days. You want to meet a friend in Florence between day 9 and day 14. You would like to visit Barcelona for 5 days. You would like to visit Helsinki for 5 days. Here are the cities that have direct flights: Barcelona and Florence, Helsinki and Barcelona. Find a trip plan of visiting the cities for 14 days by taking direct flights to commute between them."}
            ]
        )
        print("API call successful. Response:")
        print(response.choices[0].message['content'].strip())
    except Exception as e:
        print(f"API call failed: {e}")

if __name__ == "__main__":
    test_openai_api()
