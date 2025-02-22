"""
This module provides functionality to analyze food items from an image and calculate their total calories,
along with detailed nutritional information. It uses Google's Generative AI to process the image and generate
the required nutritional details.

Functions:
    get_response(image): Analyzes the food items in the provided image and returns a detailed nutritional report.

Constants:
    GOOGLE_API_KEY: The API key for accessing Google's Generative AI services.

Dependencies:
    os: Provides a way of using operating system dependent functionality.
    google.generativeai: Google's Generative AI library.
    utils.utils: Custom utility functions, specifically for loading environment variables.
"""

import os
import google.generativeai as genai 

from utils.utils import (
    load_return_env
)


input_prompt = """
    You are an expert nutritionist where you need to see the food items from given image and calculate 
    the total calories, also provide the details of every food items with calories intake in the
    below format
            1. Item 1 - no of calories
            2. Item 2 - no of calories
            ----
            ----
    Finally you can mention whether the food is healthy or not and also mention the percentage split 
    of protein, carbohydrates, fats, fibers, sugarand other important nutrient required in our diet. 
    If you find that food is not healthy then you must provide some alternative healthy food items that user can have in diet.
"""

GOOGLE_API_KEY = load_return_env(["GOOGLE_API_KEY"])["GOOGLE_API_KEY"]

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_response(image):
    model = genai.GenerativeModel('gemini-2.0-flash')
    response = model.generate_content([input_prompt, image[0]])
    return response.text