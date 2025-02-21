# Calories Advisor App

The Calories Advisor App is a Streamlit web application that allows users to upload an image of food items and receive information about the total calories, details of each food item with calorie intake, and whether the food is healthy or not. The app utilizes the Google Generative AI API to analyze images and generate content based on the input prompt provided by the user. Users can also receive suggestions for alternative healthy food items to include in their diet. The app aims to assist nutritionists and individuals in making informed decisions about their food choices and maintaining a healthy lifestyle.

Here's the link of the app if you want to play around with it - https://huggingface.co/spaces/Harsh12/nutritionist

## Libraries Used:
1. streamlit: Used for building the web application user interface and functionality.
2. google.generativeai: Utilized for accessing the Generative AI model for content generation.
3. os: Used for interacting with the operating system and environment variables.
4. dotenv: Used to load environment variables from a .env file. Contains the api key
5. PIL: Used for image processing and manipulation.
   
## There are 2 main functions defined to build the app:

#### get_gemini_response(input_prompt, image): 
This function takes an input prompt and an image as input parameters. It utilizes the Generative AI model called 'gemini-pro-vision' to generate content based on the input prompt and image. The function returns the generated text response.

#### input_image_setup(uploaded_file): 
This function takes an uploaded file as input and checks if a file has been uploaded. If a file is uploaded, it reads the file into bytes and creates a dictionary containing information about the image. And finally the function returns the image data.

## Work in Progress:
1. Sometimes the model doesn't accurately predict the items in the photos, because of which miscalculations happens in Calory Calculation. This can be prevented by more effective prompt engineering. Also we can fine tune the model on the data that contains image of the food items and the descriptions about the items in the food. By refining the model in this manner, we aim to enhance the effectiveness of food item prediction and ensure more accurate calorie calculations, ultimately providing users with reliable dietary information and promoting healthier eating habits.

