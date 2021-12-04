import streamlit as st

from eda_app import run_eda_app
from ml_app import run_ml_app

st.set_page_config(page_title="Parkinson's Disease Prediction",
                        page_icon="🦍")




def main():
    menu=["Home","EDA","ML Model","About"]
    choice=st.sidebar.selectbox("Menu", menu)
    if choice=="Home":
        st.title("Parkinson's Disease Prediction App")
        st.image("./Images/disease.jpg", width=450)
        st.write("""
			
			The Dataset was a part of a ML Challange and was provided by Siddhardhan S. 
             

			#### App Content
				- EDA Section: Exploratory Data Analysis of Data
				- ML Section: ML Predictor App

			""")
        pass
    elif choice=="EDA":
        run_eda_app()

        pass
    elif choice=="ML Model":
        run_ml_app()
        pass
    else:
        st.title("About")
        st.subheader("Durgance Gaur")
        st.subheader("NIT Silchar")

        st.markdown("""
        * ### Description :

            * ##### The dataset was in the form of text file.
            * ##### The challenge required to convert text file to usable dataframe.
            * ##### Working on data preprocessing, data analysis and working with NULL values.


        * ### Metadata :

            * ##### The dataset was in the form of text file .
            * ##### It has 195 observations and 24 features.
            """)

    
if __name__=="__main__":
    main()