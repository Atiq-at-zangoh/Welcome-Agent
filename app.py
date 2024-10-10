import streamlit as st
from utility import create_csv, update_csv

def main():
    st.set_page_config("Welcome AI Assistant")
    st.header("--> Welcome AI Assistant <--")
    
    with st.form("visitor_details"):
        st.write("Enter Your details: ")

        name = st.text_input(" Name")
        phone = st.number_input(" Contact Number")
        email = st.text_input(" Email ")
        company = st.text_input(" Company")
        designation = st.text_input(" Designation")

        submitted = st.form_submit_button("Submit")
        if submitted:
            ## Update in csv
            new_entry = [name, phone, email, company, designation]
            create_csv()
            update_csv(new_visitor=new_entry)
            
            ## Send an email
            

            st.write("Hi "+name+", Thanks for filling this form.")
            st.write("Please check "+email+" for invitation.")
            
            ## Send message on linkedin



    
        
if __name__ == "__main__":
    main()