
import streamlit as st

st.text('')


st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("""
<h1 align="center">  MAD1 Grade Calculator </h1>
""", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

st.markdown("""
<h2 align="center"> "We should focus on something which we can't achieve." - Narendra Modi</h2>
""", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

st.markdown("""
<h3 align="center"> Welcome to the MAD1 Grade Calculator app, this app is created  for calculating the final grade for MAD! of september-2023 term, a Diploma level course for  BS IN DATA SCIENCE COURSE OFFERED BY IIT MADRAS 
""", unsafe_allow_html=True)



st.markdown("<hr>", unsafe_allow_html=True)


# Final course score T = 0.1GAA + 0.2 ROE1 + 0.2 P1 + 0.2P2 + 0.3F
def best_calcular(d,e): 
  return g=max(d,e)
def max_calculator(f,d,e,g):
  return c=max(0.35f + 0.2d + 0.25e, 0.4f + 0.3g)

def score_calculator(a,b,c):
  return 0.15*a + 0.05*b + c


def Grade_calculator(total_score):
  
  if total_score >= 90:
    return 'S'
  
  elif total_score >= 80:
    return 'A'

  elif total_score >= 70:
    return 'B'

  elif total_score >= 60:
    return 'C'

  elif total_score >= 50:
    return 'D'

  elif total_score >= 40:
    return 'E'

  else:
    return 'F'


st.markdown(""" <h5 align = "center">Enter the Graded Lab Assignment Score:</h5>""", unsafe_allow_html=True)
a = st.number_input(label = " " , key="first_digit_input") 

st.markdown(""" <h5 align = "center">Enter the Graded assignment score:</h5>""", unsafe_allow_html=True)
b = st.number_input(label = " " , key="second_digit_input")  # Using an empty string as label

st.markdown(""" <h5 align = "center">Enter the quiz 1 score:</h5>""", unsafe_allow_html=True)
d = st.number_input(label = " " , key="third_digit_input")  # Using an empty string as label

st.markdown(""" <h5 align = "center">Enter the Course quiz 2 score:</h5>""", unsafe_allow_html=True)
e = st.number_input(label = " " , key="fourth_digit_input")  # Using an empty string as label

st.markdown(""" <h5 align = "center">Enter the Endterm Exam score:</h5>""", unsafe_allow_html=True)
f = st.number_input(label = " " , key="fifth_digit_input")  # Using an empty string as label

Total_score = score_calculator(a,b,c)

grade = Grade_calculator(Total_score)



if st.button('Start Calculating!'):
  
  st.markdown(f"""
  <h3 align="center">Your Total Score : {Total_score:.2f} 
  """, unsafe_allow_html=True)
  st.markdown(f"""
  <h3 align="center">Your Grade for TDS is : {grade} 
  """, unsafe_allow_html=True)

st.markdown("""
<h2 align="center"> Created by JayZCrash </h2>
""", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

st.markdown("""
<h4 align="center"> Dedicating this app to IITM for giving such a good learning experience to us. Also to the instructors for their selfless dedication towards teaching us the concepts in depth , friendly and in an easily understandable way </h4>
""", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)




       






