
# Voice Operated Chatbot for Restaurants

This Streamlit application implements a voice-operated chatbot for restaurants. Users can interact with the chatbot through voice commands or by typing text messages. The chatbot utilizes Google Generative AI to provide informative responses about restaurant dishes.

**Features:**

- Speech recognition for capturing user voice input.
- Text-based input for users who prefer typing.
- Chat interface for displaying conversation history.
- Integration with Google Generative AI for generating responses about dishes.
- Text-to-speech functionality for voice output from the chatbot.

**Requirements:**

- Python 3.x
- Streamlit (`pip install streamlit`)
- SpeechRecognition (`pip install SpeechRecognition`)
- pyttsx3 (`pip install pyttsx3`)
- Google Generative AI API (requires a Google Cloud Platform project and API key)(`pip install google-generativeai`)

**Installation:**

1. Create a Google Cloud Platform project and enable the Google Generative AI API.
2. Obtain an API key for the project.
3. Install the required Python libraries using `pip`.

**Usage:**

1. Run the script using `python your_script_name.py`.
2. The Streamlit app will launch in your web browser.
3. Click the "Speak" button to activate voice recognition.
4. Alternatively, type a message in the text input field.
5. The chatbot will respond to your input with information about dishes.

## Acknowledgments
- Google Generative AI for providing the AI model and API.
- Streamlit for the framework to build interactive and beautiful web applications.

