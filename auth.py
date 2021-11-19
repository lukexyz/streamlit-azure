import streamlit as st
import asyncio
from httpx_oauth.clients.google import GoogleOAuth2

from app import *
from config import *

def google_oauth():
    client = GoogleOAuth2(client_id, client_secret)
    authorization_url = asyncio.run(
        write_authorization_url(client=client,
                                redirect_uri=redirect_uri)
    )

    if 'token' not in st.session_state:
        st.session_state.token = None

    if st.session_state.token is None:
        try:
            code = st.experimental_get_query_params()['code']
        except:
            st.write(f'''
                Authorised Accounts Only: <a target="_self" href="{authorization_url}">Google OAuth Login</a>''',
                     unsafe_allow_html=True)
        else:
            # Verify token is correct:
            try:
                token = asyncio.run(
                    write_access_token(client=client,
                                       redirect_uri=redirect_uri,
                                       code=code))
            except:
                st.write(f'''<h2>
                    This account is not allowed or page was refreshed.
                    Please try again: <a target="_self"
                    href="{authorization_url}">Google Oauth Login</a></h2>''',
                         unsafe_allow_html=True)
            else:
                # Check if token has expired:
                if token.is_expired():
                    if token.is_expired():
                        st.write(f'''<h2>
                        Login session has ended,
                        please <a target="_self" href="{authorization_url}">
                        login</a> again.</h2>
                        ''')
                else:
                    st.session_state.token = token
                    user_id, user_email = asyncio.run(
                        get_email(client=client,
                                  token=token['access_token'])
                    )
                    st.session_state.user_id = user_id
                    st.session_state.user_email = user_email
                    main(user_id=st.session_state.user_id,
                         user_email=st.session_state.user_email)
    else:
        main(user_id=st.session_state.user_id,
             user_email=st.session_state.user_email)


async def write_authorization_url(client,
                                  redirect_uri):
    authorization_url = await client.get_authorization_url(
        redirect_uri,
        scope=["profile", "email"],
        extras_params={"access_type": "offline"},
    )
    return authorization_url


async def write_access_token(client,
                             redirect_uri,
                             code):
    token = await client.get_access_token(code, redirect_uri)
    return token


async def get_email(client,
                    token):
    user_id, user_email = await client.get_id_email(token)
    return user_id, user_email
