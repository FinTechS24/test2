import streamlit as st
import pandas as pd
import numpy as np
st.write("""
Hello world , its my second streamlit test
"""
         )
df = pd.read_csv("mushrooms.csv")
st.line_chart(df['season'])
