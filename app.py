import streamlit as st
import joblib
model = joblib.load('Social_Network_Ads')
st.title('SOCIAL_NETWORK_ADS CLASSIFIER')
ip = st.text_input('Enter the Message')
op = model.predict([ip])
if st.button('predict'):
  st.title(op[0])
                                                
                                                    
                                                                               
                                                
                                                                 
                       
            
                    
                   
                                   
       
