import streamlit as st
from datetime import datetime

def main():
    st.title("Health Predictor: Deep Learning and Data Mining Project for Personalized Health Risk Assessment")
    # Adding subtitles
    st.subheader("By Mushtari Khan")

    # Display current date and time
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    st.write("Current Date & Time:", current_datetime)

    # Option to switch between dark and light mode
    theme_mode = st.radio("Select Theme Mode:", ["Light", "Dark"])
    if theme_mode == "Dark":
        st.experimental_set_query_params(theme="dark")
    else:
        st.experimental_set_query_params(theme="default")
    
    #st.write("Dataset source: https://data.cdc.gov/Behavioral-Risk-Factors/Behavioral-Risk-Factor-Surveillance-System-BRFSS-P/dttw-5yxu")

    # Inserting page description using Markdown
    st.markdown("""
   The app will utilize separate deep learning models trained on the Behavioral Risk Factor Surveillance System (BRFSS) 
   dataset for each health condition. By inputting their information through the app, users will receive personalized predictions and 
   gain insights into potential health risks, empowering them to make informed decisions about their well-being. The project aims to provide a valuable tool for 
   individuals to assess their health and facilitate early intervention, promoting a proactive approach to healthcare management.

    You can find the source code for this app on [GitHub](https://github.com/your-username/your-repo).

    Dataset source: https://data.cdc.gov/Behavioral-Risk-Factors/Behavioral-Risk-Factor-Surveillance-System-BRFSS-P/dttw-5yxu
    MetaData Source: https://chronicdata.cdc.gov/Behavioral-Risk-Factors/Behavioral-Risk-Factor-Surveillance-System-BRFSS-H/iuq5-y9ct/data
    """)

   # Text box
    user_input = st.text_input("Enter your Name:", "")

    # Select option
    option = st.selectbox("Select an option:", ["Option 1", "Option 2", "Option 3"])

    # Display the user input and selected option
    st.write("You entered:", user_input)
    st.write("You selected:", option)

if __name__ == "__main__":
    main()

