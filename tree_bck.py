import streamlit as st
import json

DECISION_TREE = {
    "question": "Which screen size are you looking for?",
    "options": ["< 40 inches", "40-55 inches", "55+ inches"],
    "next": [
        {
            "question": "Is space a constraint?",
            "options": ["Yes", "No"],
            "next": [
                "Consider the CompactModel 37S -a wall-mountable TV to save space.",
                "Consider the SlimSeries 38P -compact stands and slim designs perfect for smaller spaces."
            ]
        },
        {
            "question": "Are you interested in a Smart TV?",
            "options": ["Yes", "No"],
            "next": [
                {
                    "question": "Any specific streaming platform preference?",
                    "options": ["Netflix", "Amazon Prime", "No preference"],
                    "next": [
                        "Consider the StreamMax 45N - comes with a built-in Netflix app.",
                        "Consider the PrimeView 46A - comes with a built-in Amazon Prime app.",
                        "Consider the SmartChoice 48B - supports all major streaming platforms."
                    ]
                },
                "Consider the ClassicView 47X - a high-quality non-smart TV. Pair it with your favorite streaming device."
            ]
        },
        {
            "question": "What's more important to you?",
            "options": ["Picture Quality", "Sound Quality", "Both"],
            "next": [
                {
                    "question": "OLED or QLED?",
                    "options": ["OLED", "QLED"],
                    "next": [
                        "Consider the UltraView O65 - offers unparalleled black levels and contrast with OLED technology.",
                        "Consider the BrightSeries Q66 - QLED tech for brighter visuals, especially in well-lit rooms."
                    ]
                },
                {
                    "question": "Do you plan on using an external sound system?",
                    "options": ["Yes", "No"],
                    "next": [
                        "Consider the SoundFlex 60E - packed with necessary audio outputs.",
                        "Consider the DolbyDream 61D - with built-in Dolby Atmos support for an immersive audio experience."
                    ]
                },
                "Consider the PremiumPro 70P - a top-tier model that delivers both stunning visuals and outstanding sound."
            ]
        }
    ]
}

def display_question(node):
    """Recursive function to display questions based on user's choice."""
    if "question" in node:
        option = st.selectbox(node["question"], node["options"])
        # Get the next node based on user's answer
        next_node = node["next"][node["options"].index(option)]
        # Display the next question or result
        display_question(next_node)
    else:
        # If there's no question, it's a final result
        st.info(node)

def main():
    st.title("Demandey TV Recommendation")
    display_question(DECISION_TREE)

if __name__ == "__main__":
    main()
