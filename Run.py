# streamlit_read_csv.py

import streamlit as st
import pandas as pd

# Title
st.title("Finance Data Viewer")

# URL to CSV
csv_url = (
    "https://raw.githubusercontent.com/farwiiizah/Farwizah/refs/heads/main/Finance_data.csv"
)

# Read CSV
@st.cache_data
def load_data(url):
    try:
        df = pd.read_csv(url)
        return df
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return None

df = load_data(csv_url)

if df is not None:
    # Display raw data
    st.subheader("Raw Data")
    st.dataframe(df)

    # Show basic stats
    st.subheader("Summary statistics")
    st.write(df.describe(include='all'))

    # Column selection
    st.subheader("Interactive Plot")
    numeric_cols = df.select_dtypes(include=["number"]).columns.tolist()
    if numeric_cols:
        x_col = st.selectbox("Select X-axis column", numeric_cols, index=0)
        y_col = st.selectbox("Select Y-axis column", numeric_cols, index=1 if len(numeric_cols) > 1 else 0)

        # Scatter plot
        st.write(f"### {y_col} vs {x_col}")
        st.altair_chart(
            st.altair_chart(
                st.altair_chart(
                    st.altair_chart(
                        __import__('altair').Chart(df).mark_point().encode(
                            x=x_col, y=y_col
                        )
                    )
                )
            ),
            use_container_width=True,
        )

    # Filtering example
    st.subheader("Filter by Gender")
    if "gender" in df.columns:
        chosen = st.multiselect(
            "Choose gender(s):",
            options=df["gender"].unique(),
            default=df["gender"].unique(),
        )
        filtered = df[df["gender"].isin(chosen)]
        st.dataframe(filtered)

else:
    st.write("No data loaded.")
