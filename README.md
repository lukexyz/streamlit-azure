# streamlit-azure
Template code for deploying streamlit to azure web app.

# CIDI
Add github repo details to Azure App Service.

# Setup 
App Service > Configuration > Startup Command
> `python -m streamlit run --server.port 8000 app.py`

Automatically run virtual env and pip requirements
App Service > Configuration > Application settings (on by default)
> `SCM_DO_BUILD_DURING_DEPLOYMENT = true`

# Monitor 
App Service > Monitoring > Log stream

# Authentication
App Service > Authentication > Identity Provider

# Custom Domains
App Service > Settings > Custom domains

# Networking
Specify IP endpoints in virtual network.

