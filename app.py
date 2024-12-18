import streamlit as st

# Title of the website
st.title("My First Streamlit Website")

# Introduction Text
st.markdown("This is a simple website built using Streamlit. Let's see some cool features!")

# Adding a slider to get input from the user
st.subheader("Select your age:")
age = st.slider("Age", min_value=0, max_value=100, value=25)

# Display user input
st.write(f"You selected age: {age}")

# Adding a text input for the user
name = st.text_input("Enter your name:")

if name:
    st.write(f"Hello, {name}!")

# Add a button that displays a message when clicked
if st.button('Click Me'):
    st.write("Button clicked! You're awesome!")

# Displaying an image
st.subheader("Here's an image for you:")
st.image("https://www.streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.png", caption="Streamlit Logo", use_column_width=True)

# Adding a chart
st.subheader("A simple chart:")
import pandas as pd
import numpy as np

data = pd.DataFrame({
    'x': np.arange(1, 11),
    'y': np.random.randn(10)
})

st.line_chart(data)
