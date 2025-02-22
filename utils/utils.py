# This module provides utility functions for the Nutrition App, including environment variable loading, image file handling, and a Streamlit sidebar widget for displaying information about the app.
# Functions:
#     load_return_env(variables: List[str]) -> Dict[str, str]:
#         Loads specified environment variables and returns them as a dictionary.
#     input_image_setup(uploaded_file):
#         Processes an uploaded image file and returns its MIME type and raw byte data.
#     about_widget() -> None:
#         Displays an "About" section in the Streamlit sidebar with information about the app.
# Constants:
#     CUSTOM_CSS (str): Custom CSS styles for the Streamlit app.

from typing import Dict, List
import streamlit as st
from dotenv import load_dotenv
import os

# load .env file to environment
load_dotenv()

def load_return_env(variables: List[str]) -> Dict[str, str]:
    return {var: os.getenv(var, None) for var in variables}

def input_image_setup(uploaded_file):

    # This function checks if the uploaded_file parameter is not None, which means that a file has been uploaded by the user. 
    # If a file has been uploaded, the code proceeds to read the file content into bytes using the getvalue() method of the uploaded_file object. 
    # This method returns the raw bytes of the uploaded file.
    
    # The bytes data obtained from the uploaded file is stored in a dictionary format under the key-value pair "mime_type" and "data". The "mime_type" key stores the MIME type of the uploaded file, 
    # which indicates the type of content (e.g., image/jpeg, image/png). The "data" key stores the raw bytes of the uploaded file.
    # The image data is then stored in a list named image_parts, which contains a dictionary with the MIME type and data of the uploaded file.
    
    if uploaded_file is not None:
        #Read the file into bytes

        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type":uploaded_file.type, #get the mime type of the uploaded file
                "data":bytes_data
            }
        ]

        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")

def about_widget() -> None:
    """Display an about section in the sidebar"""
    st.sidebar.markdown("---")
    st.sidebar.markdown("### ℹ️ About")
    st.sidebar.markdown("""
    This Calories Advisor Assistant helps you Know exactly what’s on your plate breakdown calories, macros, and nutrients with precision.

    Built with:
    - 🚀 Agno (Phidats)
    - 💫 Streamlit
    """)

CUSTOM_CSS = """
    <style>
    /* Main Styles */
   .main-title {
        text-align: center;
        background: linear-gradient(45deg, #FF4B2B, #FF416C);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3em;
        font-weight: bold;
        padding: 1em 0;
    }
    .subtitle {
        text-align: center;
        color: #666;
        margin-bottom: 2em;
    }
    .stButton button {
        width: 100%;
        border-radius: 20px;
        margin: 0.2em 0;
        transition: all 0.3s ease;
    }
    .stButton button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
    }
    .chat-container {
        border-radius: 15px;
        padding: 1em;
        margin: 1em 0;
        background-color: #f5f5f5;
    }
    .tool-result {
        background-color: #f8f9fa;
        border-radius: 10px;
        padding: 1em;
        margin: 1em 0;
        border-left: 4px solid #3B82F6;
    }
    .status-message {
        padding: 1em;
        border-radius: 10px;
        margin: 1em 0;
    }
    .success-message {
        background-color: #d4edda;
        color: #155724;
    }
    .error-message {
        background-color: #f8d7da;
        color: #721c24;
    }
    /* Dark mode adjustments */
    @media (prefers-color-scheme: dark) {
        .chat-container {
            background-color: #2b2b2b;
        }
        .tool-result {
            background-color: #1e1e1e;
        }
    }
    </style>
"""
