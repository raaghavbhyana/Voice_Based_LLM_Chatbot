import streamlit as st
import speech_recognition as sr
import pyttsx3
import google.generativeai as genai

st.title("Voice Operated Chatbot for Restaurants")

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

### Write Message History
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.chat_message(msg["role"], avatar="🧑‍💻").write(msg["content"])
    else:
        st.chat_message(msg["role"], avatar="🤖").write(msg["content"])

def generate_response(query):
    genai.configure(api_key="Enter Your Api Key Here")
    model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",system_instruction="Welcome! to AAR Restaurant.You are  Chatbot assisting  at a restaurant.Your name is TopC.Explain information about dished in about 15-20 words")
    response = model.generate_content(query,stream=True)
    response.resolve()
    engine=pyttsx3.init()
    engine.say(response.text)
    engine.runAndWait()
    return response.text

def speech_to_text():
    """Captures microphone input and performs speech recognition."""

    r = sr.Recognizer()
    with sr.Microphone() as source:
        
        audio = r.listen(source,10)

    try:
        text = r.recognize_google(audio)  # Use Google Speech-to-Text by default
        st.success("You said: " + text)
        return text
    except sr.UnknownValueError:
        st.error("Speech Recognition could not understand audio")
        return ""
    except sr.RequestError as e:
        st.error("Could not request results from Google Speech Recognition service; {0}".format(e))
        return ""

if st.button("Speak"):
    prompt = speech_to_text()
elif prompt := st.chat_input("Type or speak"):
    pass  # Keep prompt if user typed or previous speech input was successful

# Process prompt if available
if prompt :
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user", avatar="🧑‍💻").write(prompt)
    st.session_state["full_message"] = generate_response(prompt)
    st.chat_message("assistant", avatar="🤖").write(st.session_state["full_message"])
    st.session_state.messages.append({"role": "assistant", "content": st.session_state["full_message"]})
