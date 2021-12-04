import streamlit as st
import pandas as pd

import matplotlib.pyplot as plt

import matplotlib

matplotlib.use("Agg")

# Load data
@st.cache
def load_data(data):
    df=pd.read_csv(data,index_col=False)
    return df

def run_eda_app():
    st.title("Exploratory Data Analysis")
    df=load_data("./parkinson.csv")
    df_new=load_data("./parkinson_upsample.csv")
    #df_encoded=load_data("./data/diabetes_data_upload_clean.csv") 
    #freq_df=load_data("./data/freqdist_of_age_data.csv")
    
    submenu=st.sidebar.selectbox("Submenu",["Descriptive","Plots"])
    if submenu=="Descriptive":
        st.subheader("Descriptive Data")
        st.dataframe(df)
        with st.expander("Data Types"):
            st.dataframe(df.dtypes.astype(str))
        with st.expander("Descriptive Summary"):
            st.dataframe(df.describe().astype(str))
        
        col1,col2=st.columns([2,1])
        with col1:
            with st.expander("Before Upsampling"):
                st.dataframe(df["Target"].value_counts().astype(str))
        with col2:
            with st.expander("After Upsampling"):
                st.dataframe(df_new["Target"].value_counts().astype(str))
        pass


    elif submenu=="Plots":
        st.subheader("Plots")
        # Layout
        
        with st.expander("Dist Plot of Target values : "):
            
            st.image("./Images/Imbalance.png",use_column_width=True,caption="1-Pakinson's   2-Healthy")
            
        with st.expander("Skewness in the datafrane"):
            st.image("./Images/Skewed.png",use_column_width=True , caption="Red line denotes the Mean of the data")
            pass
            # with st.expander(""):
                
            #     pass
            
        with st.expander("Correlation Plot"):
            st.image("./Images/corr.png")                
            pass    
        
        # Outlier Detection
        with st.expander("Outlier Detection Plot"):
            st.image("./Images/outlier.png")

        with st.expander("Important Features"):
            st.image("./Images/feature_imp.png")
        pass    
        pass


