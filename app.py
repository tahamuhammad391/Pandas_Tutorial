import streamlit as st
import pandas as pd
import plotly.express as px


st.title("Cric info app")

def load_data(file_path):
    df=pd.read_csv(file_path)
    return df


data_path="./newcricinfo.csv"

df=load_data(data_path)

st.dataframe(df)

country_matches =df.groupby("country")["Matches"].sum().sort_values().reset_index().head(5)

fig_country = px.pie(
    country_matches,
    names="country",
    values="Matches",
    title="Country wise Matches"
)


total_hundred = df["100"].sum()
total_player = df["Player"].nunique()
total_Matches = df["Matches"].sum()
total_Sixes = df["6s"].sum()
total_runs = df["Runs"].sum()

col1,col2,col3,col4,col5 = st.columns(5)

with col1:
    st.metric(label="Total Runs" , value = total_runs)
with col2:
    st.metric(label="Total Hundred" , value = total_hundred)
with col3:
    st.metric(label="Total Matches" , value = total_Matches)
with col4:
    st.metric(label="Sixes" , value = total_Sixes)
with col5:
    st.metric(label="Players" , value = total_player)
st.plotly_chart(fig_country)