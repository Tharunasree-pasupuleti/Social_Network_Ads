import streamlit as st
import joblib
model - joblib.load('Social_Network_Ads')
st.title('Social_Network_Ads CLASSIFIER')
ip = st.text_input('Enter Your Message')
op = model.predict([ip])
if st.button('predict'):
  st.title(op[0])
        
