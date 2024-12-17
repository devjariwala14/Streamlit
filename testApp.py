import streamlit as st
import pandas as pd
st.title('Streamlit Test App')
uploaded_file = st.file_uploader('Drop your file here', type=None, accept_multiple_files=False, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="visible")

if uploaded_file is not None:
    st.write(f"Filename: {uploaded_file.name}")

    if uploaded_file.type == "text/csv":
        
        df = pd.read_csv(uploaded_file)
        st.write(df.head())
        
        options = st.multiselect("Choose the columns you want to set as indepandant variable",df.columns)
        button = st.button("qwerty")
        print(button)
        if st.button("Submit"):
            for x in options:
                st.write(x)

    elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
        # Read Excel file
        df = pd.read_excel(uploaded_file)
        st.write(df)
    else:
        # Handle other file types as needed
        st.text("File type not supported for preview.")