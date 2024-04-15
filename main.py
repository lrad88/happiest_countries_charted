import streamlit as st
import plotly.express as px
import pandas as pd

happy = pd.read_csv("happy.csv")

st.title("In search of Happiness")

st.markdown("<p style='color: green; font-size: 20px;'>"
            "Does a countries GDP or social support affect its overall "
            "happiness ?</p>",
            unsafe_allow_html=True)

zhe = st.selectbox("Select the data for the X axis",
                   ("Happiness", "Life_Expectancy", "Corruption", "GDP",
                    "Social_Support", "Generosity",
                    "Freedom_to_make_life_choices"))
yo = st.selectbox("Select the data for the Y axis",
                  ("Happiness", "Life_Expectancy", "Corruption", "GDP",
                   "Social_Support", "Generosity",
                   "Freedom_to_make_life_choices"))

# match cases are used to match the choices in the select box to
# the data in the csv so that it an be displayed in in the graph

country = happy["country"]

match zhe:
    case "Happiness":
        x = happy["happiness"]
    case "Life_Expectancy":
        x = happy["lifeexpectancy"]
    case "Corruption":
        x = happy["corruption"]
    case "GDP":
        x = happy["gdp"]
    case "Social_Support":
        x = happy["social_support"]
    case "Generosity":
        x = happy["generosity"]
    case "Freedom_to_make_life_choices":
        x = happy["freedom_to_make_life_choices"]

match yo:
    case "Happiness":
        y = happy["happiness"]
    case "Life_Expectancy":
        y = happy["lifeexpectancy"]
    case "Corruption":
        y = happy["corruption"]
    case "GDP":
        y = happy["gdp"]
    case "Social_Support":
        y = happy["social_support"]
    case "Generosity":
        y = happy["generosity"]
    case "Freedom_to_make_life_choices":
        y = happy["freedom_to_make_life_choices"]

st.subheader(f"{zhe} and {yo}")

show_names = st.checkbox("Show country names", value=False)

if show_names:
    figure = px.scatter(x=x, y=y, text=country, labels={"x": zhe, "y": yo})
    st.plotly_chart(figure)

else:
    figure = px.scatter(x=x, y=y, labels={"x": zhe, "y": yo},
                        hover_data={"Country": country})
    st.plotly_chart(figure)
