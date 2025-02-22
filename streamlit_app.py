"""
Sets up the Streamlit interface for the Food Calories Calculator application.

This module implements a Streamlit web application for calculating food calories from an uploaded image.

The application allows users to upload an image of food, processes the image to extract relevant data,
and then uses a pre-trained model to provide a breakdown of the calories, macros, and nutrients present in the food.

Modules and functions used:
- PIL.Image: For handling image uploads and processing.
- agent.kcal_agent.get_response: For getting the calorie breakdown response from the model.
- utils.utils: Contains utility functions and custom CSS for the application.
- nest_asyncio: To apply asyncio event loop patching for compatibility with Streamlit.
- streamlit: For building the web application interface.

Functions:
- main(): The main function that sets up the Streamlit interface, handles image uploads, and displays the calorie breakdown response.

Usage:
Run this script to start the Streamlit web application. Users can upload an image of food and get a detailed breakdown of its nutritional content.

"""

from PIL import Image
from agent.kcal_agent import get_response
from utils.utils import (
    CUSTOM_CSS,
    input_image_setup
)

import nest_asyncio
import streamlit as st

nest_asyncio.apply()


st.set_page_config(
    page_title="Know exactly what’s on your plate breakdown calories, macros, and nutrients with precision.",
    page_icon="🥗",
)

# Add custom CSS
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

"""
This function creates the main layout of the web application, allowing users to upload an image of food,
and then processes the image to provide a detailed breakdown of its nutritional content including calories,
macros, and nutrients.

The interface includes:
- A title and a file uploader for users to upload an image.
- A button to submit the image for processing.
- A section to display the uploaded image.
- A section to display the nutritional breakdown response.

The function uses the following components:
- input_image_setup: A utility function to prepare the uploaded image for processing.
- get_response: A function to get the nutritional breakdown from the pre-trained model.

Note:
- The function uses Streamlit's container, columns, and markdown features to create the layout.
- Custom CSS is applied to style the interface.

Returns:
None
"""
def main():
    with st.container(border=True):
        st.markdown("<h1 class='main-title'>Food Calories Calculator</h1>", unsafe_allow_html=True)
        st.markdown("---")

        col1, col2 = st.columns([1,1])
        with col1:
            image = ""
            uploaded_file = st.file_uploader(
                "Choose an image...", type=["jpg", "jpeg", "png"],key="file_upload")

            if uploaded_file is not None:
                image = Image.open(uploaded_file)
                st.image(image, caption="Uploaded Image", use_container_width=True)

            submit = st.button("Tell me about the total calories")

        with col2:
            ####################################################################
            # About section
            ####################################################################
            # about_widget()

            if submit:
                image_data = input_image_setup(uploaded_file)
                response = get_response(image_data)
                st.markdown("### The Response Is")
                st.write(response)

main()
