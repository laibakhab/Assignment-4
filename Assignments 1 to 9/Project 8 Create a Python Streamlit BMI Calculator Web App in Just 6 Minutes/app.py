# import streamlit as st
# import time
# st.set_page_config(page_title="BMI calculator" ,page_icon="" , layout="centered")

# st.title('BMI Calculator in python')

# st.markdown(
#     """      
# """
# )

# col_1 , col_2 = st.columns(2)

# with col_1:
#     weight = st.number_input('weight (kg) :' , min_value=1.0 , format='%.2f')\
    
# with col_1:
#     height = st.number_input('height (m) :' , min_value=1.0 , format='%.2f')    

# if height > 0 and weight > 0:
#     bmi = weight /(height **2)
#     st.subheader('BMI')
#     st.markdown(f'{bmi: .2f}' , unsafe_allow_html=True)

#     if bmi < 18.5:
#         st.error('underweight')
#     elif 18.5<= bmi <24.9:
#         st.success('normal weight') 
#     elif 25 <= bmi < 29.9:
#         st.warning('over weight')
#     else:
#         st.error('obsity')               
# else:
#     st.info('please enter a valid weight and height')        


import streamlit as st
import time

# Page config
st.set_page_config(page_title="BMI Calculator 🧮", page_icon="⚖️", layout="centered")

# Title and description
st.title('⚖️ BMI Calculator')
st.markdown(
    """<div style='text-align: center; font-size: 18px; color: grey;'>
    Calculate your Body Mass Index easily.
    </div>""",
    unsafe_allow_html=True
)

st.markdown("---")

# Input Section
st.header("Enter your details 👇")

col1, col2 = st.columns(2)

with col1:
    weight = st.number_input('Enter your weight (kg) :', min_value=1.0, format="%.2f", help="Example: 70.5 kg")
with col2:
    height = st.number_input('Enter your height (m) :', min_value=0.5, format="%.2f", help="Example: 1.75 m")

st.markdown("---")

# BMI Calculation
if height > 0 and weight > 0:
    bmi = weight / (height ** 2)
    st.subheader('Your BMI is:')
    st.success(f"**{bmi:.2f}**")

    # Category display
    if bmi < 18.5:
        st.error('🔵 Underweight')
    elif 18.5 <= bmi < 24.9:
        st.success('🟢 Normal weight')
    elif 25 <= bmi < 29.9:
        st.warning('🟠 Overweight')
    else:
        st.error('🔴 Obesity')
else:
    st.info('Please enter valid weight and height to calculate BMI.')

# Footer
st.markdown("---")
st.caption("Made with Laiba Asif using Streamlit")

