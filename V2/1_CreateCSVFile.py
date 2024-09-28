import pandas as pd

data = {
    "question": [
        "What is the price of the AI course?",
        "How can I access the course materials?",
        "What is the refund policy?",
        "How do I contact support?",
        "Do you offer group discounts?",
        "Are there any prerequisites for the data science course?",
        "What payment methods do you accept?",
        "How long do I have access to the course materials?",
        "Can I get a certificate after completing the course?",
        "Is there any support available during the course?"
    ],
    "answer": [
        "The price of the AI course is $199.",
        "You can access the course materials from your dashboard.",
        "You can request a refund within 30 days of purchase if you are not satisfied with the course.",
        "You can contact support by emailing support@example.com or calling 123-456-7890.",
        "Yes, we offer group discounts for purchases of 5 or more licenses. Please contact sales@example.com for more details.",
        "Basic knowledge of programming and statistics is recommended for the data science course.",
        "We accept all major credit cards, PayPal, and bank transfers.",
        "You will have lifetime access to the course materials.",
        "Yes, you will receive a certificate of completion after finishing the course.",
        "Yes, you will have access to our support team via email and live chat during the course."
    ]
}

df = pd.DataFrame(data)
df.to_csv("questions_answers.csv", index=False)
