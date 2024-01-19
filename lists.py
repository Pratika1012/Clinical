import streamlit as st

st.set_page_config(layout="wide")

st.markdown("""
 <style>
 .block-container {
 padding-top: 1rem;
 padding-bottom: 3rem;
 padding-right: 5rem;
 }
 </style>
 """, unsafe_allow_html=True)

st.markdown("<h2 style='text-align: center; color: darkBlue;'><b>Clinical Application of CURA-FILM <b/></h2>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: darkBlue;'><b>by Stellar BioMed<b/></h2>", unsafe_allow_html=True)
st.subheader(':red[HUMANS]')
# Add a subheader for "Burns"
st.markdown("<h4>Burns</h4>",unsafe_allow_html=True)

# List of burn scenarios
burn_scenarios = [
    "Burned Arm by hot milk",
    "Burned hand by hot oil",
    "Burned arm by steam car radiator",
    "Third degree Burn from walking on hot stones in temple",
    "Other"
]

# Display the list as clickable hyperlinks

for scenario in burn_scenarios:
    st.markdown(f"- [{scenario}](#{scenario.replace(' ', '-').lower()})")

# Display details for each burn scenario
# for scenario in burn_scenarios:
#     st.markdown(f"### {scenario.replace(' ', '-').lower()}")
#     st.write(f"Details for {scenario} go here.")
st.markdown("<h4>Ulcers</h4>",unsafe_allow_html=True)
ulcers_scenarios=[
    "Diabetic Ulcer",
    "Diabetic Ulcer suffering from ore than a Year",
    "Venous Ulcer",
] 

for scenario in ulcers_scenarios:
    st.markdown(f"- [{scenario}](#{scenario.replace(' ', '-').lower()})")

    
st.markdown("<h4>Others</h4>",unsafe_allow_html=True)
others_scenarios=[
    "Diabetic Bedsore",
    "gangreme",
    "Accident with industrial sugar came crusher",
    "Maggot infection"
] 
for scenario in others_scenarios:
    st.markdown(f"- [{scenario}](#{scenario.replace(' ', '-').lower()})")

st.subheader(':red[ANIMALS]')
Animals_scenarios=[
    "Jumping horse wounded with tractor Fork"
]
for scenario in Animals_scenarios:
    st.markdown(f"- [{scenario}](#{scenario.replace(' ', '-').lower()})")
