# streamlit-azure
Template code for deploying streamlit to azure web app.

# Setup 
App Service > Settings > Configuration > Startup Command
> `streamlit run --server.port 8080 --server.enableCORS false app.py`