import streamlit as st
import requests
import pandas as pd

# Used the free RapidAI Endpoint: Random Dog Facts
url = 'https://random-dog-facts.p.rapidapi.com/'

headers = {
    "x-rapidapi-key": "b475f62f8fmsh74668022161a5b2p1f2114jsn7a14a3bfcab9",
    "x-rapidapi-host": "random-dog-facts.p.rapidapi.com"
}


def find_tail_tales():
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching data: {e}")
        return {}


st.title('Tail Tales: Facts and trivia about your four-legged friends ^_^')

# checkbox widget (1/1)
# selectbox widget (1/5)
more_tail_tales = st.checkbox('More tail wagging facts please!')

# numberbox widget (2/5)
num_box = st.number_input('Number of Tail Tales', min_value=1, max_value=50, value=5)

# text-input widget (3/5)
text_area = st.text_input('Search for a keyword')

# text-area widget (4/5)
feedback_area = st.text_area('How can we make this better? Feedback?')

# button-widget (1/1)
if st.button('Fetch Facts'):
    tail_tales = find_tail_tales()

    # keyword search based on text-input
    if text_area:
        tail_tales = [fact for fact in tail_tales if text_area.lower() in fact.lower()]

    # Check if data is received and contains the 'fact' field
    if tail_tales:
        # Success widget
        st.success('You got a tale!')

        # Display the dog fact(s)
        if more_tail_tales:

            st.subheader('Detailed View')
            for fact in tail_tales:
                st.write(f"**Dog Fact:** {fact}")
        else:
            # Convert facts list to DataFrame for interactive table
            facts_df = pd.DataFrame({'Fact': tail_tales})

            # Display interactive table
            st.dataframe(facts_df)
    else:
        # Warning widget
        st.warning("Sorry, no facts or tail tales")

# Display user comments or additional context
if feedback_area:
    st.write(f"*Woof, any feedback for us?:** {feedback_area}")
