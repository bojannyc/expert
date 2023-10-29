import streamlit as st
import json


# Load decision tree from a JSON file
def load_decision_tree(filename):
    with open(filename, 'r') as f:
        return json.load(f)
      
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
        st.header("Recommendation")
        st.info(node)


def main():
    st.title("Demandey Expert Advisor")
    option = st.selectbox( 'Please select Decision Tree?', ('TV Simple', 'TV Complex', 'Refrigiator'))
    st.divider()
    if option == "TV Simple":
        file="tv1.json"
    elif option == "TV Complex":
        file="tv2.json" 
    else:
        file="refrigiator.json" 
    # Initialize the DECISION_TREE from the file
    DECISION_TREE = load_decision_tree(file) 
    st.header("Questions")  
    display_question(DECISION_TREE)
    st.divider()

    st.header("Decision Tree JSON")
    
    st.json(DECISION_TREE)

    svg_str = create_svg_tree(DECISION_TREE)
    st.markdown(f'<div style="border:1px solid #ccc">{svg_str}</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
