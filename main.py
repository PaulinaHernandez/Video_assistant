import streamlit as st
from dotenv import load_dotenv
import os
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi

st.set_page_config(layout="wide")

load_dotenv() ##load all the nevironment variables

genai.configure(api_key=os.getenv("key"))

## getting the transcript data from youtube videos
def extract_transcript_details(youtube_video_url):
    try:
        video_id=youtube_video_url.split("=")[1]
        
        transcript_text=YouTubeTranscriptApi.get_transcript(video_id)

        transcript = ""
        for i in transcript_text:
            transcript += " " + i["text"]

        return transcript

    except Exception as e:
        raise e
    
## getting the summary based on Prompt
def generate_gemini_content(transcript_text,prompt):

    prompt1="""You are Yotube video assistant. Given the following transcript text
summarize the entire video and prove the important summary in points
within 250 words."""
    model=genai.GenerativeModel("gemini-pro")
    response=model.generate_content(prompt+transcript_text)
    return response.text

def generate_answer(transcript_text, question):
    # You may adjust the prompt based on your model's requirements
    prompt2 = f"""Given the following transcript, answer the question: {question}\n\nTranscript:\n{transcript_text}\n\nAnswer:"""

    model = genai.GenerativeModel("gemini-pro") # Assuming using the same model; adjust if different
    response = model.generate_content(prompt2)
    return response.text

def generate_keywords_and_descriptions(transcript_text, model_name="gemini-pro"):
    prompt = f"Identify 5 - 8 important terms from the following transcript and provide a brief description for each term:\n\n{transcript_text}"

    # Configure the model
    model = genai.GenerativeModel(model_name)
    response = model.generate_content(prompt)
    
    # The response.text is expected to contain the keywords and their descriptions
    return response.text

#Streamlit 
st.title("Video Assistant")

if 'action' not in st.session_state:
    st.session_state['action'] = None
  
col1, col2, col3 = st.columns([1, 3, 1])

# Using this column for displaying outputs
with col1:
    youtube_link = st.text_input("Enter YouTube Video Link:", key="youtube_link")
    
    if youtube_link:
        video_id = youtube_link.split("=")[1]

    # Update session_state for buttons
    if st.button("Get a summary"):
        st.session_state['action'] = "summary"
    elif st.button("Show Transcript"):
        st.session_state['action'] = "transcript"
    elif st.button("Terminology"):
        st.session_state['action'] = "terminology"
    elif st.button("Ask question"):
        st.session_state['action'] = "ask_question"
    
    question = st.text_input("Ask a question about the video:", key="question")


# Using this column for displaying outputs
with col2:
    action = st.session_state.get('action', None)
    # Check which action to perform and display the corresponding output
    if 'action' in locals():
        if action == "summary":
            transcript_text = extract_transcript_details(youtube_link)
            if transcript_text:
                summary = generate_gemini_content(transcript_text, prompt1)
                st.markdown("## Detailed Notes:")
                st.write(summary)
        elif action == "transcript":
            transcript_text = extract_transcript_details(youtube_link)
            if transcript_text:
                st.markdown("## Video Transcript:")
                st.write(transcript_text)
            else:
                st.write("Sorry, we couldn't retrieve the transcript for this video.")
        elif action == "terminology":
            transcript_text = extract_transcript_details(youtube_link)
            if transcript_text:
                keywords_descriptions = generate_keywords_and_descriptions(transcript_text)
                st.markdown("## Terminology and Their Descriptions:")
                st.write(keywords_descriptions)
        elif action == "ask_question" and question:
            transcript_text = extract_transcript_details(youtube_link)
            if transcript_text:
                answer = generate_answer(transcript_text, question)
                st.markdown("## Answer:")
                st.write(answer)

# Using this column for the YouTube video thumbnail
with col3:
    if youtube_link:
        # Display the YouTube video thumbnail
        st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_column_width=True)
