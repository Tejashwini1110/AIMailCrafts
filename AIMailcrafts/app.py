# import streamlit as st
# import requests

# # def generate_email(api_url, api_token, recipient, topic, tone):
# #     headers = {"Authorization": f"Bearer {api_token}"}
# #     prompt = f"Generate a {tone} email for {recipient} about {topic}."
    
# #     payload = {"inputs": prompt}
# #     response = requests.post(api_url, headers=headers, json=payload)
    
# #     if response.status_code == 200:
# #         return response.json()[0]['generated_text']
# #     else:
# #         return "Error: Unable to generate email."

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














import streamlit as st
import requests

def generate_email(api_url, api_token, recipient, topic, tone):
    headers = {"Authorization": f"Bearer {api_token}"}
    
    # Shortened prompt to fit model limits
    prompt = f"""
    Write a professional {tone} email to {recipient} about {topic}. 
    The email should be at least 6 sentences long, starting with a greeting and ending with a closing statement.
    """
    
    payload = {
        "inputs": prompt,
        "parameters": {"truncation": "only_first"}  # Avoids token overflow
    }
    
    response = requests.post(api_url, headers=headers, json=payload)
    
    print("API Response:", response.text)  # Debugging

    if response.status_code == 200:
        return response.json()[0]['generated_text']
    else:
        return f"Error: {response.status_code} - {response.text}"

# Streamlit UI
st.title("📧 Personalized Email Generator")
st.write("Generate professional emails using AI!")

api_url = "https://api-inference.huggingface.co/models/tiiuae/falcon-7b-instruct"
api_token = st.text_input("Enter your Hugging Face API Token", type="password")

recipient = st.text_input("Recipient's Name")
topic = st.text_input("Email Topic")
tone = st.selectbox("Select Email Tone", ["Professional", "Casual", "Friendly"])

if st.button("Generate Email"):
    if api_token and recipient and topic:
        email_content = generate_email(api_url, api_token, recipient, topic, tone.lower())
        st.subheader("Generated Email:")
        st.write(email_content)
    else:
        st.warning("Please enter all required fields.")
