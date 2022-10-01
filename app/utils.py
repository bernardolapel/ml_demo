import pandas as pd
import streamlit as st

@st.cache(suppress_st_warning=True)
def read_data(path):
    return pd.read_csv(path)
	
def head():
    st.markdown("""
        <h1 style='text-align: center; margin-bottom: -35px;'>
        Math Problem Generator
        </h1>
    """, unsafe_allow_html=True
    )
    
    st.caption("""
        <p style='text-align: center'>
        by <a href='https://medium.com/geoclid'>Geoclid</a>
        </p>
    """, unsafe_allow_html=True
    )
    
    st.write(
        "Feeling overwhelmed by your daily grind?",
        "Looking for something fun to do?",
        "Click the button for a random math problem \U0001F642."
    )
	
def body(sample):
    name = sample.iloc[0, 0]
    link = sample.iloc[0, 1]
    prob = sample.iloc[0, 2]
    st.info(f'### {name}')
    st.write(prob)
    st.caption(f'[source]({link})')
    st.markdown('---')