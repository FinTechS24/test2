import streamlit as st
import pandas as pd
import numpy as np
st.write("""
Hello world , its my very  first streamlit 
"""
         )
df = pd.read_csv("mushrooms.csv")
st.line_chart(df['season'])
