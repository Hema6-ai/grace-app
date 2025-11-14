import streamlit as st
import matplotlib.pyplot as plt
from figures import fig8, fig9, fig10, fig11, fig12

st.title("GRACE Constellation Optimization Dashboard")

option = st.selectbox(
    "Select Figure",
    ["Figure 8", "Figure 9", "Figure 10", "Figure 11", "Figure 12"]
)

if option == "Figure 8":
    st.header("Constellation Population (Generations 1, 3, 20)")
    fig = fig8()
    st.pyplot(fig)

elif option == "Figure 9":
    st.header("Pareto Curves")
    fig = fig9()
    st.pyplot(fig)

elif option == "Figure 10":
    st.header("Average Degree Variances (Pareto 1,10,48)")
    fig = fig10()
    st.pyplot(fig)

elif option == "Figure 11":
    st.header("Family of 10 Constellations on Pareto Front")
    fig = fig11()
    st.pyplot(fig)

elif option == "Figure 12":
    st.header("1-day Degree Variances (c01–c10)")
    fig = fig12()
    st.pyplot(fig)
