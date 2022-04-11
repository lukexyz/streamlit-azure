# streamlit-azure

Template code for deploying streamlit to azure web app.

## 1. Create new App

- Create new project on 🌐 [Azure App Service](https://portal.azure.com/#blade/HubsExtension/BrowseResource/resourceType/Microsoft.Web%2Fsites)
- Select appropriate `subscription` and `resource group`

## 2. CICD Instance

- Publish: ✔️ `code`
- Runtime stack `python 3.9`
- Operating system `Linux`

## 3. App Service Plan

- Sku and size: `B1`
  - `1.75 GB Memory`
  - `$13.14 USD/Month` (first month free)

## 4. Deployment

- Continuous deployment: ✔️ `Enable`
- Link github account and select
  - `Organisation` > `Repository` > `Branch`

## 5. Networking

- (Optional) Enable network injection if internal `virtual network` is desired.

Click through final options > and click `create`.

> 🏆 Now your app service is up and running.

# Setup Continuous Deployment

In the Azure portal navigate to

- App Service > Settings (left column) > `Configuration`
  - General settings (tab) > `Startup Command`

> `python -m streamlit run --server.port 8000 app.py`

Automatically run virtual env and pip requirements on rebuild:

- App Service > Configuration > `Application settings` (on by default)

> `SCM_DO_BUILD_DURING_DEPLOYMENT = true`

✔️ Save changes

# Monitor

App Service > Monitoring > Log stream

# Authentication

App Service > Authentication > Identity Provider

# Custom Domains

App Service > Settings > Custom domains

# Networking

Specify IP endpoints in virtual network.
