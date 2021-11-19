import streamlit as st
import pandas as pd
import altair as alt
from collections import namedtuple
import math

import os

from auth import *
from config import *


def main(user_id, user_email):
    st.write(f"You're logged in as {user_email}")

    if user_email.split('@')[1] == domain:
        st.success('Login Successful')
        st.title('Secret Algorithm 🤫 ')

        # Altair showcase
        with st.echo(code_location='below'):
            # Secret Algorithm

            total_points = st.slider("Number of points in spiral", 1, 5000, 2000)
            num_turns = st.slider("Number of turns in spiral", 1, 100, 9)
            Point = namedtuple('Point', 'x y')
            data = []
            points_per_turn = total_points / num_turns
            for curr_point_num in range(total_points):
                curr_turn, i = divmod(curr_point_num, points_per_turn)
                angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
                radius = curr_point_num / total_points
                x = radius * math.cos(angle)
                y = radius * math.sin(angle)
                data.append(Point(x, y))
            st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
                .mark_circle(color='#0068c9', opacity=0.5)
                .encode(x='x:Q', y='y:Q'))

    else:
        st.error('Login Rejected')
        st.text(f'No secrets for you, {user_email}.')




if __name__ == '__main__':
    st.set_page_config(
    page_title="Internal App",     # String or None. Strings get appended with "• Streamlit". 
    page_icon="🦄",                # String, anything supported by st.image, or None.
    layout="centered",             # Can be "centered" or "wide". In the future also "dashboard", etc.
    initial_sidebar_state="auto")  # Can be "auto", "expanded", "collapsed"

    # Initialise OAuth login
    google_oauth()
