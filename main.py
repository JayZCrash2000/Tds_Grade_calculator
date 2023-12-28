import streamlit as st

st.text('')


st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("""
<h1 align="center">  TDS Grade Calculator </h1>
""", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

st.markdown("""
<h3 align="center"> Welcome this app is created  for calculating the final grade for TDS of september-2023 term, a Diploma level course for  BS IN DATA SCIENCE COURSE OFFERED BY IIT MADRAS 
""", unsafe_allow_html=True)



st.markdown("<hr>", unsafe_allow_html=True)


# Final course score T = 0.1GAA + 0.2 ROE1 + 0.2 P1 + 0.2P2 + 0.3F

def score_calculator(a,b,c,d,e):
  return(0.1*a + 0.2*b + 0.2*c + 0.2*d + 0.3*f)


st.markdown(""" <h5 align = "center">Enter the Graded assignment score:</h5>""", unsafe_allow_html=True)
a = st.number_input(" ")  # Using an empty string as label

st.markdown(""" <h5 align = "center">Enter the Programing quiz score:</h5>""", unsafe_allow_html=True)
b = st.number_input(" ")  # Using an empty string as label

st.markdown(""" <h5 align = "center">Enter the Course project one score:</h5>""", unsafe_allow_html=True)
c = st.number_input(" ")  # Using an empty string as label

st.markdown(""" <h5 align = "center">Enter the Course project two score:</h5>""", unsafe_allow_html=True)
d = st.number_input(" ")  # Using an empty string as label

st.markdown(""" <h5 align = "center">Enter the Endterm Exam score:</h5>""", unsafe_allow_html=True)
e = st.number_input(" ")  # Using an empty string as label

Total_score = score_calculator(a,b,c,d,e)

st.text(Total_score)

st.markdown(""" <h5 align = "center">f'{Total_score}'</h5>""", unsafe_allow_html=True)





