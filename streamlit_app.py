import streamlit as st
import google.generativeai as genai 
import os 
from dotenv import load_dotenv
load_dotenv()
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input_prompt, image):
    model = genai.GenerativeModel('gemini-2.0-flash')
    response = model.generate_content([input_prompt, image[0]])
    return response.text

def input_image_setup(uploaded_file):

    '''
    This function checks if the uploaded_file parameter is not None, which means that a file has been uploaded by the user. 
    If a file has been uploaded, the code proceeds to read the file content into bytes using the getvalue() method of the uploaded_file object. 
    This method returns the raw bytes of the uploaded file.
    
    The bytes data obtained from the uploaded file is stored in a dictionary format under the key-value pair "mime_type" and "data". The "mime_type" key stores the MIME type of the uploaded file, 
    which indicates the type of content (e.g., image/jpeg, image/png). The "data" key stores the raw bytes of the uploaded file.
    The image data is then stored in a list named image_parts, which contains a dictionary with the MIME type and data of the uploaded file.
    
    '''
    #check if file has been uploaded
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
    
## initialising the streamlit app
    
st.set_page_config(page_title="Calories Advisor App")

st.header("Calories Advisor App")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

image = ""

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)

submit = st.button("Tell me about the total calories")

input_prompt = """
You are an expert nutritionist where you need to see the food items from the image and calculate 
the total calories, also provide the details of every food items with calories intake in the
below format
        1. Item 1 - no of calories
        2. Item 2 - no of calories
        ----
        ----
Finally you can slo mention whether the food is healthy or not and also mention the
percentage split ration of carbohydrates, fats, fibers, sugar, protein and other important
things required in our diet. If the If you find that food is not healthy then you must provide
some alternative healthy food items that user can have in diet.

"""


if submit:
    image_data = input_image_setup(uploaded_file)
    response = get_gemini_response(input_prompt, image_data)
    st.header("The Response is: ")
    st.write(response)
