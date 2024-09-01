import streamlit as st
from string_calculator import StringCalculator

# Instantiate the StringCalculator class
calculator = StringCalculator()

# Streamlit app title
st.title("String Calculator")

# Input field for the numbers string
numbers_input = st.text_input("Enter numbers (e.g., '1,2,3'):")

st.success("""
To change the delimiter, the beginning of the string will contain a separate line that looks like this: 
"//[delimiter]\n[numbers…]". For example, "//;\n1;2" where the delimiter is ";" should return 3.
""")

# Perform the calculation when the button is pressed
if st.button("Calculate"):
    try:
        # Calculate the sum using the add method
        result = calculator.add(numbers_input)
        st.success(f"The sum is: {result}")
    except ValueError as e:
        # Handle and display errors (e.g., for negative numbers)
        st.error(str(e))
