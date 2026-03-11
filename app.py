import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Talking Rabbitt - Conversational Analytics")

uploaded_file = st.file_uploader("Upload your sales CSV", type=["csv"])

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    st.write("Data Preview")
    st.dataframe(df)

    question = st.text_input("Ask a question about your data")

    if question:

        if "highest revenue" in question.lower():

            region_revenue = df.groupby("Region")["Revenue"].sum()

            max_region = region_revenue.idxmax()

            st.success(f"Region with highest revenue is **{max_region}**")

            fig, ax = plt.subplots()
            region_revenue.plot(kind="bar", ax=ax)
            ax.set_ylabel("Revenue")

            st.pyplot(fig)

        elif "total revenue" in question.lower():

            total = df["Revenue"].sum()

            st.success(f"Total Revenue is **{total}**")

        else:

            st.write("Try asking: 'Which region has highest revenue?'")
