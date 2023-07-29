import streamlit as st
from streamlit.components.v1 import IFrame
from datetime import datetime

def main():
    st.title("Health Predictor: Deep Learning and Data Mining Project for Personalized Health Risk Assessment")
    
    # Adding subtitles
    st.subheader("By Mushtari Khan")

    # Display current date and time
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    st.write("Current Date & Time:", current_datetime)
 
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

    # Add an iframe that points to your Google Colab notebook
    colab_url = "https://colab.research.google.com/drive/1TGaSLNcVtCKfWYYm3QvSg1J4gIq7sqJl"
    IFrame(colab_url, width=800, height=600)

if __name__ == "__main__":
    main()

