# Sophia AI Assistant
Sophia is a desktop AI assistant built using Python that can perform various tasks such as answering questions like ChatGPT, opening desktop applications, browsing websites, and even making phone and WhatsApp calls. This project is designed to be versatile and extensible, with the ability to add more functionalities easily. It integrates the Hugging Face API, a free ChatGPT alternative to simulate conversation, and offers multiple activation methods for user commands.

## Demo Video
You can check out the demo by clicking on the below image

[![Demo Video](https://github.com/user-attachments/assets/b54a65c4-1deb-40e1-b957-772285d14c54)](https://youtu.be/dgCYDETwjcs)


## Features

* **Voice Activation:** Activate Sophia by saying "Sophia."
* **Text Input:** Type your queries and press enter to receive a response.
* **App Control:** Open applications like Notepad and OneNote.
* **Website Navigation:** Open websites like YouTube and Canva.
* **Multimedia Control:** Search and play specific videos on YouTube.
* **Phone and WhatsApp Communication:** Make calls or send messages.

## Technology Used:
- #### Languages:
  - ![PYTHON](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=darkgreen)
  - ![HTML](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
  - ![CSS](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
  - ![JAVASCRIPT](https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E)
- #### FrameWork:
  - ![BOOTSTRAP](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)
- #### Database:
  - ![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)
- #### API used for:
  - Hugging Face API ![Hugging Face API](https://github.com/user-attachments/assets/17108a47-2fbf-4ea7-bac7-b66e3fafe9e0)

## Installation

### Prerequisites
Make sure you have Python installed. Then, install the following packages:

```bash
beautifulsoup4==4.12.3
blinker==1.8.2
bottle @ git+https://github.com/bottlepy/bottle.git@3fdb8b2a2e0d1641374b53ef2b051fe7f54508b5
bottle-websocket==0.2.9
certifi==2024.7.4
cffi==1.16.0
charset-normalizer==3.3.2
click==8.1.7
colorama==0.4.6
comtypes==1.4.4
Eel==0.16.0
enum34==1.1.10
Flask==3.0.3
future==1.0.0
gevent==24.2.1
gevent-websocket==0.10.1
greenlet==3.0.3
hugchat==0.4.8
idna==3.7
itsdangerous==2.2.0
Jinja2==3.1.4
MarkupSafe==2.1.5
MouseInfo==0.1.3
numpy==2.0.0
pillow==10.4.0
playsound==1.2.2
pocketsphinx==5.0.3
psutil==6.0.0
pvporcupine==1.9.5
PyAudio==0.2.14
PyAutoGUI==0.9.54
pycparser==2.22
PyGetWindow==0.0.9
PyMsgBox==1.0.9
pyparsing==3.1.2
pyperclip==1.9.0
pypiwin32==223
PyRect==0.2.0
PyScreeze==0.1.30
pyttsx3==2.90
pytweening==1.2.0
pywhatkit==5.4
pywin32==306
requests==2.32.3
requests-toolbelt==1.0.0
setuptools==70.2.0
sounddevice==0.4.7
soupsieve==2.5
SpeechRecognition==3.10.4
typing_extensions==4.12.2
urllib3==2.2.2
Werkzeug==3.0.3
whichcraft==0.6.1
wikipedia==1.4.0
zope.event==5.0
zope.interface==6.4.post2
```

### Setup Instructions

**Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/sophia-ai-assistant.git
   cd sophia-ai-assistant
```
__To install the necessary dependencies and set up the API and database, I recommend checking out my YouTube tutorial series where I walk you through the entire process of building an AI assistant.__

### 📺 [Watch the Full YouTube Tutorial Series](https://www.youtube.com/playlist?list=PLoGk-8pBKSRVWvGN372yBzrF15tSv22KY)

## Usage

### Activating the Assistant
There are several ways to activate Sophia:

- **Voice Activation:** Simply say "Sophia."
- **Text Input:** Type your query in the input box (e.g., "How are you?").
- **Keyboard Shortcut:** Press `Window + J` to activate the assistant.

### Supported Commands

#### Query Answering
Ask Sophia questions, and she'll answer using the Hugging Face API, a free ChatGPT alternative.
**Example:** "Tell me about yourself"

#### Opening Applications
- "Open Notepad"
- "Open OneNote"

#### Website Navigation
- "Open YouTube"
- "Open Canva"

#### Multimedia Search
- "Play the video of the 99 names of Allah on YouTube"

#### Phone and Messaging
- "Sophia, make a phone call to Ali Hassan"
- "Sophia, send a message to Ali Hassan"
- "Sophia, make a video call on WhatsApp"

### Future Enhancements
- **Custom Application and Website Management:** Users will be able to add their applications and websites without needing to work with databases or SQL.
- **Expanded Application Support:** Add support for more desktop and web applications.
- **Customizable Settings:** Implement user-configurable settings for a more personalized experience.

## Contributing
Feel free to open issues or submit pull requests to improve the project. Contributions are welcome, whether it’s adding new features, fixing bugs, or improving documentation.

## Feedback
If you have any suggestions or want to request additional features, leave a comment on the YouTube tutorial series. Your feedback is highly appreciated!
