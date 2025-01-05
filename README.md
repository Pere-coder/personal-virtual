# **Voice Assistant with PDF Extraction & AI Responses**

## **Description**

This project integrates voice recognition, text-to-speech, and AI-based question answering. It utilizes the `speech_recognition` library to listen to user input through the microphone, the `pyttsx3` library for text-to-speech output, and the `langchain_ollama` model to generate intelligent responses. Additionally, it can extract text from PDF documents and respond to questions based on the content of the document.

The AI model, **Ollama**, has been downloaded locally from [Ollama.com](https://ollama.com/), and the project uses this locally hosted model for generating responses based on user input or document content.
I used Ollama 3.2
---

## **Features**

- **Voice Interaction**: Converts spoken commands into text and provides audible responses.
- **AI-Powered Responses**: Uses the Ollama model to generate responses based on user input or document context.
- **PDF Text Extraction**: Extracts text from PDFs and answers questions based on the content of the PDF document.
- **Error Handling**: Robust error handling for microphone issues, Google speech recognition failures, and file-related errors.

---

## **Installation**

To set up this project locally, follow these steps:

### Prerequisites

Make sure that you have Python 3.x installed on your machine and that you have downloaded the Ollama model locally.

1. **Download Ollama Model**: 
   - Go to [Ollama.com](https://ollama.com/) and download the Ollama model.
   - Follow the setup instructions on the website to install Ollama on your machine.

2. **Clone the repository**:

   ```bash
   git clone https://github.com/Pere-coder/personal-virtual.git
   cd personal-virtual
