import streamlit as st

def main():
    st.title("Mushtari Khan's Data Mining Project")

    st.write("Dataset source: https://data.cdc.gov/Behavioral-Risk-Factors/Behavioral-Risk-Factor-Surveillance-System-BRFSS-P/dttw-5yxu")

   # Text box
    user_input = st.text_input("Enter some text:", "")

    # Select option
    option = st.selectbox("Select an option:", ["Option 1", "Option 2", "Option 3"])

    # Display the user input and selected option
    st.write("You entered:", user_input)
    st.write("You selected:", option)

if __name__ == "__main__":
    main()

