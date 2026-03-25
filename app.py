import streamlit as st
from main import process_excel

st.title("AI Lead Intelligence System")

uploaded_file = st.file_uploader("Upload Excel File", type=["xlsx"])

if uploaded_file:
    st.write("Processing... please wait ⏳")

    df = process_excel(uploaded_file)

    st.success("Done!")

    st.write("### Results Preview")
    st.dataframe(df, use_container_width=True)

    if "Phone" in df.columns:
        df["Phone"] = df["Phone"].astype(str)
        df["Phone"] = df["Phone"].apply(lambda x: f"'{x}")

    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download Results",
        data=csv,
        file_name="results.csv",
        mime="text/csv"
    )