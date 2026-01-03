import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# App title
st.title("ReLU Activation Function")

# Define ReLU function
def relu(x):
    return np.maximum(0, x)

# Generate input values
x = np.linspace(-10, 10, 100)
y = relu(x)

# Plot the ReLU function
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_xlabel("Input")
ax.set_ylabel("Output")
ax.set_title("ReLU Function")

# Display plot in Streamlit
st.pyplot(fig)
