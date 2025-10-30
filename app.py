import streamlit as st

# App title
st.set_page_config(page_title="Calculator App", page_icon="🧮", layout="centered")
st.title("🧮 Simple Calculator")

# Input fields
st.write("### Enter two numbers:")
num1 = st.number_input("First number", value=0.0)
num2 = st.number_input("Second number", value=0.0)

# Select operation
operation = st.selectbox("Choose an operation", ["Addition (+)", "Subtraction (-)", "Multiplication (×)", "Division (÷)"])

# Calculate result
if st.button("Calculate"):
    if operation == "Addition (+)":
        result = num1 + num2
        st.success(f"Result: {num1} + {num2} = {result}")
    elif operation == "Subtraction (-)":
        result = num1 - num2
        st.success(f"Result: {num1} - {num2} = {result}")
    elif operation == "Multiplication (×)":
        result = num1 * num2
        st.success(f"Result: {num1} × {num2} = {result}")
    elif operation == "Division (÷)":
        if num2 != 0:
            result = num1 / num2
            st.success(f"Result: {num1} ÷ {num2} = {result}")
        else:
            st.error("Error: Division by zero is not allowed.")

# Footer
st.markdown("---")
st.caption("Built with ❤️ using Streamlit")
