import pandas as pd
import mysql.connector

# Load CSV file
df = pd.read_csv('data/questions_answers.csv')

# Connect to MySQL
conn = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='sanjaydchamp',
    database='chatbot_db'
)
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS faq (
    id INT AUTO_INCREMENT PRIMARY KEY,
    question TEXT,
    answer TEXT
)
""")

# Insert data into table
for _, row in df.iterrows():
    cursor.execute("INSERT INTO faq (question, answer) VALUES (%s, %s)", (row['question'], row['answer']))

conn.commit()
cursor.close()
conn.close()
