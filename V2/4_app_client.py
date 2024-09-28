import streamlit as st
import mysql.connector
from langchain.llms import GooglePalm

# Set up Google PaLM with Langchain
api_key = "AIzaSyDzJsADKF9sS94Tz7GPvSLlOroyBcL3GVk"
llm = GooglePalm(google_api_key=api_key, temperature=0.6)

def get_palm_response(question):
    return llm(question)  # Generate a response using Google PaLM

def rephrase_with_palm(text):
    rephrase_prompt = f"Please rephrase the following text: '{text}'"
    return llm(rephrase_prompt)

# Streamlit app
st.title('Customer Support Chatbot')

# User input
user_question = st.text_input('Ask a question:')

if user_question:
    # Connect to MySQL
    conn = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='sanjaydchamp',
        database='chatbot_db'
    )
    cursor = conn.cursor(dictionary=True)

    # Fetch answer from the database
    cursor.execute("SELECT answer FROM faq WHERE question LIKE %s LIMIT 1", (f"%{user_question}%",))
    result = cursor.fetchone()

    if result:
        db_answer = result['answer']  # Fetch the answer from the database
        # Rephrase the answer using Google PaLM
        rephrased_answer = rephrase_with_palm(db_answer)
        answer = rephrased_answer
    else:
        # Use Google PaLM to generate an answer if not found in the database
        answer = get_palm_response(user_question)

        # Insert the new question and answer into the database
        cursor.execute("INSERT INTO faq (question, answer) VALUES (%s, %s)", (user_question, answer))
        conn.commit()

    st.write(f"Answer: {answer}")  # Display the rephrased or generated answer

    # Feedback mechanism
    feedback = st.radio("Was this answer helpful?", ('Yes', 'No'))
    if feedback == 'No':
        correct_answer = st.text_input('Please provide the correct answer:')
        if st.button('Submit'):
            cursor.execute("UPDATE faq SET answer = %s WHERE question = %s", (correct_answer, user_question))
            conn.commit()
            st.write('Thank you for your feedback!')

    cursor.close()
    conn.close()
