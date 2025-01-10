import streamlit as st
import pandas as pd

# Variables initialization
df = pd.DataFrame()

def Home_screen():
# Main function
    title,space,logoutBtn = st.columns([1,1,0.25],vertical_alignment="bottom",border=False)
    with title:
        st.title('ModelXpert')
    with space:
        st.write(" ")  
    with logoutBtn:
        # st.Page(logout, title="Log out", icon=":material/logout:")
        st.button("",on_click=logout,icon=":material/logout:")
    
    uploaded_file = st.file_uploader(
        'Upload your dataset here',
        type=['csv', 'xlsx'],
        accept_multiple_files=False,
        label_visibility="visible",
    )

    if uploaded_file:
        checkDoc(uploaded_file)

    if not df.empty:
        labels = radioButton()
        submitButton(labels)
    # check = st.button("Check")
    # if check:
    #     st.switch_page("pages/check.py")

def logout():
    st.session_state.logged_in = False

def submitButton(labelSelection):
# Target varaible , Indepandent Variable and Submit Button
    if labelSelection=="Manual":
        targetVariable = st.selectbox("Choose Target Variable",df.columns)
        options = st.multiselect("Choose the columns you want to set as indepandant variable",df.columns)
        button = st.button("Submit")
        if button:
            for x in options:
                st.write(x)
        return targetVariable
 
    elif labelSelection=="Automatic":
        # targetVariable = st.selectbox("Choose Target Variable",df.columns)
        # options = st.multiselect("Choose the columns you want to set as independant variable",df.columns)
        button = st.button("Submit")


def radioButton():
#label selection radio button
    labelSelection = st.radio(
        "Select Labels",
        ["Automatic","Manual"], 
        captions=["Completely automatic","Manually select the labels"]
    )
    return labelSelection


def checkDoc(uploaded_file):
# Check the document
    global df  
    st.write(f"Filename: {uploaded_file.name}")

    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
        st.write("CSV file loaded successfully!")

    elif uploaded_file.name.endswith('.xlsx'):
        df = pd.read_excel(uploaded_file)
        st.write("Excel file loaded successfully!")

    else:
        st.error("File type not supported for preview.")
    
    st.write(df.head())


if __name__ == "__main__":
    Home_screen()
