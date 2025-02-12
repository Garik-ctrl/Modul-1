import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.DataFrame(
    np.random.randn(20,3),
    columns=["První","Druhý", "Třetí"]
)

st.line_chart(df)

st.header("Zapsané hodnoty")
st.table(df)