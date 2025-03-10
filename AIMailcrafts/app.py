# import streamlit as st
# import requests

# # def generate_email(api_url, api_token, recipient, topic, tone):
# #     headers = {"Authorization": f"Bearer {api_token}"}
# #     prompt = f"Generate a {tone} email for {recipient} about {topic}."
# #     payload = {"inputs": prompt}

# #     response = requests.post(api_url, headers=headers, json=payload)

# #     if response.status_code == 200:
# #         result = response.json()
# #         if isinstance(result, list) and "generated_text" in result[0]:
# #             return result[0]['generated_text']
# #         else:
# #             return "Error: API did not return the expected response."
# #     else:
# #         return f"Error {response.status_code}: {response.text}"




# def generate_email(api_url, api_token, recipient, topic, tone):
#     headers = {"Authorization": f"Bearer {api_token}"}
#     prompt = f"""
#     Write a detailed {tone} email to {recipient} about {topic}.
#     - **Start with a greeting** (e.g., "Dear [Recipient], I hope you're doing well.")
#     - **Introduce the purpose** of the email.
#     - **Provide key details** about {topic}.
#     - **Give action items or next steps**.
#     - **End with a closing statement** (e.g., "Looking forward to your response.")

#     The email should be at least **6-8 sentences long**.
#     """
    
#     payload = {"inputs": prompt}
#     response = requests.post(api_url, headers=headers, json=payload)
    
#     print("API Response:", response.text)  # Debugging output

#     if response.status_code == 200:
#         return response.json()[0]['generated_text']
#     else:
#         return f"Error: {response.status_code} - {response.text}"






# # Streamlit UI
# st.title("📧 Personalized Email Generator")
# st.write("Generate professional emails using AI!")

# api_url = api_url = api_url = "https://api-inference.huggingface.co/models/facebook/blenderbot-3B"

#   # Use a different model if needed
# api_token = st.text_input("Enter your Hugging Face API Token", type="password")

# recipient = st.text_input("Recipient's Name")
# topic = st.text_input("Email Topic")
# tone = st.selectbox("Select Email Tone", ["Professional", "Casual", "Friendly"])

# if st.button("Generate Email"):
#     if api_token and recipient and topic:
#         email_content = generate_email(api_url, api_token, recipient, topic, tone.lower())
#         st.subheader("Generated Email:")
#         st.write(email_content)
#     else:
#         st.warning("Please enter all required fields.")














# import streamlit as st
# import requests

# def generate_email(api_url, api_token, recipient, topic, tone,language):
#     headers = {"Authorization": f"Bearer {api_token}"}
    
#     # Shortened prompt to fit model limits
#     prompt = f"""
#     Write a professional {tone} email to {recipient} about {topic}. 
#     The email should be at least 6 sentences long, starting with a greeting and ending with a closing statement.
#     """
    
#     payload = {
#         "inputs": prompt,
#         "parameters": {"truncation": "only_first"}  # Avoids token overflow
#     }
    
#     response = requests.post(api_url, headers=headers, json=payload)
    
#     print("API Response:", response.text)  # Debugging

#     if response.status_code == 200:
#         return response.json()[0]['generated_text']
#     else:
#         return f"Error: {response.status_code} - {response.text}"

# # Streamlit UI
# st.title("📧 Personalized Email Generator")
# st.write("Generate  emails using AI!")

# api_url = "https://api-inference.huggingface.co/models/tiiuae/falcon-7b-instruct"
# api_token = st.text_input("Enter your Hugging Face API Token", type="password")

# recipient = st.text_input("Recipient's Name")
# topic = st.text_input("Email Topic")
# tone = st.selectbox("Select Email Tone", ["Professional", "Casual", "Friendly"])
# language = st.selectbox("Select Email language", ["English", "Telugu", "Hindi"])

# if st.button("Generate Email"):
#     if api_token and recipient and topic:
#         email_content = generate_email(api_url, api_token, recipient, topic, tone.lower(),language.lower())
#         st.subheader("Generated Email:")
#         st.write(email_content)
#     else:
#         st.warning("Please enter all required fields.")





# import streamlit as st
# import requests

# @st.cache_data
# def generate_email(api_url, api_token, recipient, topic, tone, language):
#     headers = {"Authorization": f"Bearer {api_token}"}
#     prompt = (
#         f"Write a {tone} email to {recipient} about {topic}. "
#         f"The email should be at least 6 sentences long, starting with a greeting and ending with a closing statement. "
#         f"Write the email in {language}. Make it sound natural and appropriate for a casual invitation."
#     )
    
#     payload = {"inputs": prompt}
#     response = requests.post(api_url, headers=headers, json=payload)
    
#     if response.status_code == 200:
#         result = response.json()
#         if isinstance(result, list) and len(result) > 0:
#             return result[0].get('generated_text', 'No valid response received.')
#         else:
#             return "Error: No valid response received."
#     elif response.status_code == 403:
#         return "Error: Invalid API token or permission issue."
#     elif response.status_code == 500:
#         return "Error: The model is too busy. Try again later."
#     else:
#         return f"Error: {response.status_code} - {response.text}"

# # Streamlit UI
# st.title("🌍 Multilingual Email Generator")
# st.write("Generate professional and natural emails in various languages using AI!")

# api_url = "https://api-inference.huggingface.co/models/tiiuae/falcon-7b-instruct"  # Update with your model URL
# api_token = st.text_input("Enter your Hugging Face API Token", type="password")

# recipient = st.text_input("Recipient's Name")
# topic = st.text_input("Email Topic")
# tone = st.selectbox("Select Email Tone", ["Professional", "Casual", "Friendly"])
# language = st.selectbox("Select Language", ["English", "Hindi", "Spanish", "French", "German", "Chinese", "Japanese", "Russian", "Arabic", "Portuguese"])

# if st.button("Generate Email"):
#     if api_token and recipient and topic:
#         with st.spinner("Generating email... Please wait."):
#             email_content = generate_email(api_url, api_token, recipient, topic, tone.lower(), language)
#         st.subheader("Generated Email:")
#         st.write(email_content)
#     else:
#         st.warning("Please enter all required fields.")


# import streamlit as st
# import requests
# from pymongo import MongoClient
# from datetime import datetime

# # MongoDB Connection
# client = MongoClient("mongodb://localhost:27017/AImailcrafts")  # Update with your MongoDB connection string if needed
# db = client["email_database"]
# collection = db["emails"]

# # Function to generate email using Hugging Face API
# def generate_email(api_url, api_token, recipient, topic, tone, language):
#     headers = {"Authorization": f"Bearer {api_token}"}
#     prompt = f"Write a {tone} email to {recipient} about {topic} in {language}."
    
#     payload = {"inputs": prompt}
#     response = requests.post(api_url, headers=headers, json=payload)
    
#     if response.status_code == 200:
#         return response.json()[0]['generated_text']
#     else:
#         return f"Error: {response.json().get('error', 'Unable to generate email.')}"

# # Streamlit UI
# st.title("📧 Multilingual Email Generator & Saver")
# st.write("Generate and save professional emails in various languages using AI!")

# api_url = "https://api-inference.huggingface.co/models/tiiuae/falcon-7b-instruct"  # You can change the model if needed
# api_token = st.text_input("Enter your Hugging Face API Token", type="password")

# recipient = st.text_input("Recipient's Name")
# topic = st.text_input("Email Topic")
# tone = st.selectbox("Select Email Tone", ["Professional", "Casual", "Friendly"])
# language = st.selectbox("Select Language", ["English", "Hindi", "Spanish", "French", "German", "Chinese"])

# if st.button("Generate Email"):
#     if api_token and recipient and topic:
#         email_content = generate_email(api_url, api_token, recipient, topic, tone.lower(), language)
        
#         # Save to MongoDB
#         email_data = {
#             "recipient": recipient,
#             "topic": topic,
#             "tone": tone,
#             "language": language,
#             "content": email_content,
#             "timestamp": datetime.now()
#         }
#         collection.insert_one(email_data)
        
#         st.subheader("Generated Email:")
#         st.write(email_content)
        
#         st.success("✅ Email successfully generated and saved to the database.")
#     else:
#         st.warning("Please enter all required fields.")




# import streamlit as st
# import requests
# from pymongo import MongoClient
# from datetime import datetime

# # MongoDB connection setup
# client = MongoClient("mongodb://localhost:27017/AImailcrafts")
# db = client["EmailDB"]
# collection = db["GeneratedEmails"]

# # Email generation function
# def generate_email(api_url, api_token, recipient, topic, tone, language):
#     headers = {"Authorization": f"Bearer {api_token}"}
#     prompt = f"Write a {tone} email to {recipient} about {topic}. The email should be in {language}."
#     payload = {"inputs": prompt}
    
#     response = requests.post(api_url, headers=headers, json=payload)
    
#     if response.status_code == 200:
#         generated_text = response.json()[0]['generated_text']
        
#         # Save to MongoDB
#         email_data = {
#             "recipient": recipient,
#             "topic": topic,
#             "tone": tone,
#             "language": language,
#             "email_content": generated_text,
#             "timestamp": datetime.now()
#         }
#         collection.insert_one(email_data)
        
#         return generated_text
#     else:
#         return f"Error: {response.status_code} - {response.json().get('error', 'Unknown error')}"

# # Streamlit UI
# st.title("🌍 Multilingual Email Generator")
# st.write("Generate emails in different languages using AI!")

# api_url = "https://api-inference.huggingface.co/models/tiiuae/falcon-7b-instruct"
# api_token = st.text_input("Enter your Hugging Face API Token", type="password")

# recipient = st.text_input("Recipient's Name")
# topic = st.text_input("Email Topic")
# tone = st.selectbox("Select Email Tone", ["Professional", "Casual", "Friendly"])
# language = st.selectbox("Select Language", ["English", "Hindi", "Spanish", "French", "German","Telugu"])

# if st.button("Generate Email"):
#     if api_token and recipient and topic:
#         email_content = generate_email(api_url, api_token, recipient, topic, tone.lower(), language)
#         st.subheader("Generated Email:")
#         st.write(email_content)
#     else:
#         st.warning("Please enter all required fields.")





import streamlit as st
import requests
from pymongo import MongoClient
from datetime import datetime

# MongoDB connection setup
client = MongoClient("mongodb://localhost:27017/")
db = client["EmailDB"]
collection = db["GeneratedEmails"]

# Email generation function
def generate_email(api_url, api_token, recipient, topic, tone, language):
    headers = {"Authorization": f"Bearer {api_token}"}
    prompt = f"Write a {tone} email to {recipient} about {topic}. The email should be in {language}."
    payload = {"inputs": prompt}
    
    response = requests.post(api_url, headers=headers, json=payload)
    
    if response.status_code == 200:
        generated_text = response.json()[0]['generated_text']
        
        # Save to MongoDB
        email_data = {
            "recipient": recipient,
            "topic": topic,
            "tone": tone,
            "language": language,
            "email_content": generated_text,
            "timestamp": datetime.now()
        }
        collection.insert_one(email_data)
        
        return generated_text
    else:
        return f"Error: {response.status_code} - {response.json().get('error', 'Unknown error')}"

# Streamlit UI
st.title("🌍 Multilingual Email Generator")
st.write("Generate emails in different languages using AI!")

api_url = "https://api-inference.huggingface.co/models/tiiuae/falcon-7b-instruct"
api_token = st.text_input("Enter your Hugging Face API Token", type="password")

recipient = st.text_input("Recipient's Name")
topic = st.text_input("Email Topic")
tone = st.selectbox("Select Email Tone", ["Professional", "Casual", "Friendly"])
language = st.selectbox("Select Language", ["English", "Hindi", "Spanish", "French", "German"])

if st.button("Generate Email"):
    if api_token and recipient and topic:
        email_content = generate_email(api_url, api_token, recipient, topic, tone.lower(), language)
        st.subheader("Generated Email:")
        st.write(email_content)
    else:
        st.warning("Please enter all required fields.")


