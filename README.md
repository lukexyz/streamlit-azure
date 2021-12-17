# streamlit-azure
Template code for deploying streamlit to azure web app.

# CIDI
Add github repo details to Azure App Service.

# Setup 
App Service > Configuration > Startup Command
> `streamlit run --server.port 8080 --server.enableCORS false app.py`

Automatically run virtual env and pip requirements
App Service > Configuration > Application settings (on by default)
> `SCM_DO_BUILD_DURING_DEPLOYMENT = true`

# Authentication
App Service > Authentication > Identity Provider

# Custom Domains
App Service > Settings > Custom domains

# Networking
Specify IP endpoints in virtual network.

