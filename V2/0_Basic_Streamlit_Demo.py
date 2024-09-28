import streamlit as st
import pandas as pd

# Title of the app
st.title('Basic Streamlit Demo')

# Text input
user_name = st.text_input('Enter your name:')

# Displaying text based on input
if user_name:
    st.write(f'Hello, {user_name}!')

# Slider input
age = st.slider('Select your age:', 0, 100, 25)

# Displaying selected age
st.write(f'You are {age} years old.')

# Checkbox input
agree = st.checkbox('I agree')

if agree:
    st.write('Thank you for agreeing!')

# Button
if st.button('Click Me'):
    st.write('Button clicked!')

# Radio buttons
option = st.radio(
    "What's your favorite color?",
    ('Red', 'Green', 'Blue'))

if option:
    st.write(f'Your favorite color is {option}.')

# Select box
selectbox_option = st.selectbox(
    'Select a number',
    [1, 2, 3, 4, 5])

st.write(f'You selected: {selectbox_option}')

# Creating a simple dataframe
data = {
    'Column 1': [1, 2, 3, 4],
    'Column 2': [10, 20, 30, 40]
}
df = pd.DataFrame(data)

# Displaying the dataframe
st.write('Here is a simple dataframe:')
st.write(df)

# Displaying a dataframe with st.dataframe (allows interaction like sorting)
st.dataframe(df)

# Displaying a static table with st.table
st.table(df)

# Line chart
st.line_chart(df)

# Bar chart
st.bar_chart(df)

# Area chart
st.area_chart(df)

# Display an image
st.image('https://www.streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.png', caption='Streamlit Logo')

# Displaying Markdown text
st.markdown('This is **Markdown** text.')

# Displaying LaTeX
st.latex(r'''
     a^2 + b^2 = c^2
     ''')
