from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello this is your app running"

# import streamlit as st

# # ------------------------------------------------------
# st.title('Counter Example')
# # ------------------------------------------------------

# if 'count' not in st.session_state:
#     st.session_state.count = 0

# increment = st.button('Increment')
# if increment:
#     st.session_state.count += 1

# decrement = st.button('Decrement')
# if decrement:
#     st.session_state.count -= 1

# st.write(st.session_state.count)


# # ------------------------------------------------------
# st.title('Mirrored Widgets using Session State')
# # ------------------------------------------------------
# # https://blog.streamlit.io/session-state-for-streamlit/

# def update_first():
#     st.session_state.second = st.session_state.first

# def update_second():
#     st.session_state.first = st.session_state.second

# st.text_input(label='Textbox 1', key='first', on_change=update_first)
# st.text_input(label='Textbox 2', key='second', on_change=update_second)

