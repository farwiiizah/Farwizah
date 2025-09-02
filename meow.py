# streamlit_app.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.title("📊 Simple Streamlit App")

# Sidebar input
st.sidebar.header("User Input")
name = st.sidebar.text_input("Enter your name:", "Guest")
num_points = st.sidebar.slider("Number of Data Points", min_value=10, max_value=100, value=50)

# Display greeting
st.write(f"Hello, **{name}**! 👋")

# Generate random data
data = pd.DataFrame({
    'x': np.arange(num_points),
    'y': np.random.randn(num_points).cumsum()
})

# Show data
st.subheader("📈 Generated Data")
st.dataframe(data)

# Plot data
st.subheader("📉 Line Chart")
fig, ax = plt.subplots()
ax.plot(data['x'], data['y'], marker='o')
ax.set_title("Random Cumulative Data")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
st.pyplot(fig)
