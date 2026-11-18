import streamlit as st
import pandas as pd

df = pd.DataFrame({
'uf': ["MG", "BA", "CE", "PR"],
'Lingua portuguesa insuficiente': [0.3211, 0.487, 0.3588, 0.23],
'matematica insuficiente': [0.5677, 0.7309, 0.6122, 0.4857]
})
df 