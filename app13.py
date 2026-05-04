import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import os

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(layout="wide")

# -----------------------------
# IMAGE
# -----------------------------
image_path = "Leao.jpg"

def load_image(path):
    try:
        if os.path.exists(path):
            return Image.open(path)
        return None
    except:
        return None

image = load_image(image_path)

# -----------------------------
# HEADER
# -----------------------------
col1, col2 = st.columns([1, 3])

with col1:
    if image:
        st.image(image, width=180)
    else:
        st.warning("Image not found")

with col2:
    st.title("Rafael Leão")
    st.markdown("### Left Winger | Inside Forward")
    st.markdown("---")

# -----------------------------
# KPIs (YOUR DATA)
# -----------------------------
total_goals = 9
total_xg = 9.27
total_xa = 4.44
total_shots = 60

col1, col2, col3, col4 = st.columns(4)

col1.metric("Goals", total_goals, round(total_goals - total_xg, 2))
col2.metric("xG", total_xg)
col3.metric("xA", total_xa)
col4.metric("Shots", total_shots)

st.markdown("---")

# -----------------------------
# ATTRIBUTES
# -----------------------------
st.markdown("### Player Attributes")

attributes = {
    "Ball Carrying": 95,
    "1v1 Ability": 94,
    "Explosiveness": 92,
    "Decision Making": 78,
    "Finishing": 80,
    "Creativity": 75
}

for attr, value in attributes.items():
    st.markdown(f"**{attr}**")
    st.progress(value / 100)

st.markdown("---")

st.markdown("### Tactical Profile")

st.markdown("""
- Transition-driven attacker  
- Right-foot dominant finisher  
- Open-play shot creator  
- High-volume dribbler  
- Penalty area focused attacker  
""")

# -----------------------------
# DATA
# -----------------------------
zone_df = pd.DataFrame({
    "zone": ["Out of box", "Penalty area", "Six-yard box"],
    "shots": [14, 39, 7],
    "goals": [3, 5, 1],
    "xG": [0.79, 5.17, 3.31]
})

type_df = pd.DataFrame({
    "type": ["Right foot", "Left foot", "Head"],
    "shots": [38, 14, 8],
    "goals": [7, 1, 1],
    "xG": [6.88, 1.93, 0.45]
})

situation_df = pd.DataFrame({
    "situation": ["Open play", "From corner", "Penalty", "Set piece"],
    "shots": [53, 3, 2, 2],
    "goals": [5, 1, 2, 1],
    "xG": [7.54, 0.12, 1.52, 0.09]
})

position_df = pd.DataFrame({
    "role": ["Starter", "Sub"],
    "shots90": [2.92, 4.74],
    "xG90": [0.47, 0.32]
})

# -----------------------------
# SIDEBAR
# -----------------------------
section = st.sidebar.radio("Navigate", [
    "Overview",
    "Shot Zones",
    "Shot Types",
    "Situations",
    "Role Analysis",
    "Scouting Summary"
])

# -----------------------------
# OVERVIEW
# -----------------------------
if section == "Overview":

    st.header("Performance Overview")

    col1, col2, col3 = st.columns(3)
    col1.metric("Goals", total_goals)
    col2.metric("xG", total_xg)
    col3.metric("Shots", total_shots)

    fig, ax = plt.subplots()
    ax.bar(["Goals", "xG"], [total_goals, total_xg])
    ax.set_title("Goals vs xG")
    st.pyplot(fig)

# -----------------------------
# SHOT ZONES
# -----------------------------
elif section == "Shot Zones":

    st.header("Shot Zone Analysis")

    zone_df["xG/shot"] = zone_df["xG"] / zone_df["shots"]

    fig, ax = plt.subplots()
    ax.bar(zone_df["zone"], zone_df["shots"])
    ax.set_title("Shot Distribution")
    plt.xticks(rotation=20)
    st.pyplot(fig)

    fig2, ax2 = plt.subplots()
    ax2.bar(zone_df["zone"], zone_df["xG"])
    ax2.set_title("xG by Zone")
    plt.xticks(rotation=20)
    st.pyplot(fig2)

    st.dataframe(zone_df)

# -----------------------------
# SHOT TYPES
# -----------------------------
elif section == "Shot Types":

    st.header("Shot Type Breakdown")

    type_df["xG/shot"] = type_df["xG"] / type_df["shots"]

    fig, ax = plt.subplots()
    ax.bar(type_df["type"], type_df["shots"])
    ax.set_title("Shots by Type")
    plt.xticks(rotation=20)
    st.pyplot(fig)

    st.dataframe(type_df)

# -----------------------------
# SITUATIONS
# -----------------------------
elif section == "Situations":

    st.header("Situation Analysis")

    fig, ax = plt.subplots()
    ax.pie(situation_df["shots"], labels=situation_df["situation"], autopct="%1.1f%%")
    st.pyplot(fig)

    st.dataframe(situation_df)

# -----------------------------
# ROLE ANALYSIS
# -----------------------------
elif section == "Role Analysis":

    st.header("Role-Based Output")

    fig, ax = plt.subplots()
    ax.bar(position_df["role"], position_df["shots90"])
    ax.set_title("Shots/90 by Role")
    st.pyplot(fig)

    fig2, ax2 = plt.subplots()
    ax2.bar(position_df["role"], position_df["xG90"])
    ax2.set_title("xG/90 by Role")
    st.pyplot(fig2)

    st.dataframe(position_df)

# -----------------------------
# 🔥 SCOUTING SUMMARY (DYNAMIC)
# -----------------------------
elif section == "Scouting Summary":

    st.header("Scouting Report")

    # Dynamic logic
    main_zone = zone_df.loc[zone_df["xG"].idxmax(), "zone"]
    main_type = type_df.loc[type_df["xG"].idxmax(), "type"]
    main_situation = situation_df.loc[situation_df["xG"].idxmax(), "situation"]

    st.markdown(f"""
    ### Player Profile
    - Direct wide attacker  
    - Transition-based threat  
    - Shot creation through ball carrying  

    ### Strengths
    - Generates most xG from **{main_zone}**
    - Primary threat via **{main_type}**
    - Majority of output in **{main_situation}**

    ### Weaknesses
    - Limited aerial impact  
    - Not a consistent six-yard box presence  
    - Some inefficiency from distance  

    ### Tactical Insight
    - Most dangerous when cutting inside from the left  
    - Relies on right-foot finishing actions  
    - Thrives in open-play attacking transitions  

    ### Analyst Verdict
    > Rafael Leão is a high-impact wide attacker whose output is driven by  
    > **{main_type.lower()} shots in {main_situation.lower()} from the {main_zone.lower()}**,  
    > making him a transition-focused offensive weapon rather than a traditional striker.
    """)