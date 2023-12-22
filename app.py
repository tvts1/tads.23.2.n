import streamlit as st
from plot.interactive import plt_line_i

st.title('Stock Price App')

#sidebar
symbol = st.sidebar.text_input('Enter stock symbol:', 'AAPL')

#plt
fig = plt_line_i(symbol)
st.plotly_chart(fig)

