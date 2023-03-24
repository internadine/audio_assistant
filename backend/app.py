import speech_recognition as sr
import openai
import pyttsx3

# Set up OpenAI API
openai.api_key = "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"


# Set up speech-to-text
recognizer = sr.Recognizer()

# Set up text-to-speech
engine = pyttsx3.init()

def listen_and_transcribe():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio)
        print(f"User: {text}")
        return text
    except Exception as e:
        print("Error:", e)
        return None


def generate_gpt3_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What's the weather like today?"},
        {"role": "assistant", "content": "The current temperature is 75 degrees Fahrenheit. The sky is mostly sunny with a few clouds"},
        {"role": "user", "content": prompt}
         ],
        max_tokens=100,
        temperature=0.5,
    )
    message = response.choices[0].message.content
    return message

def speak(text):
    engine.say(text)
    engine.runAndWait()

def main():
    print("Audio Assistant is ready to listen...")
    user_input = listen_and_transcribe()
    print(f"You said: {user_input}")
    response = generate_gpt3_response(user_input)
    print(f"Assistant's response: {response}")
    speak(response)


if __name__ == "__main__":
    main()
