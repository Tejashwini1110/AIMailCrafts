from pymongo import MongoClient

client = MongoClient("mongodb:// 127.0.0.1:27017/AImailcrafts")
db = client["email_generator"]
collection = db["generated_emails"]

if st.button("Save Email to Database"):
    email_data = {
        "recipient": recipient,
        "topic": topic,
        "tone": tone,
        "email_content": email_content
    }
    collection.insert_one(email_data)
    st.success("Email saved to database successfully!")
