Video Assistant
Overview

Video Assistant is a Streamlit-based application designed to enhance your video watching experience by providing a comprehensive suite of tools that leverage the power of AI. It allows users to input a YouTube video link and offers the following features:

    Video Summary: Generates a concise summary of the video content.
    Transcript Display: Shows the complete transcript of the video.
    Terminology Extraction and Description: Identifies key terms within the transcript and provides descriptions.
    Question Answering: Answers user queries based on the video's content.

This application is perfect for learners, researchers, and anyone looking to quickly grasp the essence of a video, understand its key terminology, or seek answers to specific questions.


Installation

Before running the application, ensure you have Python installed on your system. This project is built using Python 3.8 or newer.

git clone <repository-url>
cd <project-directory>

Install dependencies:

Ensure you are in the project directory and run:

bash

    pip install -r requirements.txt


To start the application, run the following command in your terminal:

streamlit run app.py

Navigate to the provided URL in your web browser to interact with the application.
Features

    Enter YouTube Video Link: Paste the URL of the YouTube video you want to analyze in the input field.

    Get a Summary: Click the "Get a Summary" button to generate and display a concise summary of the video.

    Show Transcript: Click the "Show Transcript" button to display the video's full transcript.

    Terminology: Click the "Terminology" button to extract and explain key terms found in the transcript.

    Ask a Question: Enter your question in the provided text input and click the "Ask question" button to get answers based on the video's content.

Configuration

The application uses environmental variables to manage sensitive information such as API keys. Ensure you have a .env file in your project directory with the following content:

KEY= your-api-key

Replace <your-api-key> with your actual API key for the services used by the application.

Contributing

Contributions to the Video Assistant project are welcome! Please refer to the CONTRIBUTING.md file for guidelines on how to make a contribution.
