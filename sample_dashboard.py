import streamlit as st
import pandas as pd
import plotly.express as px


st.title("📊 Sample Data Dashboard")
st.write("This app visualizes data from the sample dataset.")

@st.cache_data
def get_data():
    
    data = {
        'item': ['A', 'B', 'C', 'D', 'E'],
        'quantity': [10, 20, 30, 40, 50],
        'value': [45, 65, 25, 80, 55]
    }
    return pd.DataFrame(data)

df = get_data()


st.success(f"✅ Rows loaded: {df.shape[0]}")


threshold = st.slider("Show rows where 'value' > x", min_value=0, max_value=100, value=50)


if 'value' in df.columns:
    filtered = df[df['value'] > threshold]
else:
    filtered = df


if {'quantity', 'value'}.issubset(df.columns):
    fig = px.scatter(
        filtered,
        x='quantity',
        y='value',
        text='item',
        title='Quantity vs Value'
    )
    fig.update_traces(marker=dict(size=10, color='orange'), textposition='top center')
    st.plotly_chart(fig)


st.dataframe(filtered)
