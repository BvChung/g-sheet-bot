# AutomateBot

## Overview

Automate uploading information to Google Sheets using Google Sheets API and Gspread Python API.

## Table of Contents

- [Tech](#tech)<br/>
- [Setting Up](#setting-up)<br/>
- [Development](#development)<br/>

## Tech

- [Python](https://www.python.org/)

## Setting Up

1. Create project on [Google Cloud](https://console.cloud.google.com)
2. Go to API's & Services and enable Google Sheets API + Google Drive API
3. Go to Google Sheets API and create a service account -> Keys tab -> Add Key -> Create Key -> Export as JSON
4. Go to your Google Sheets spreadsheet and Share with the "client_email" in the JSON file

## Development

1. Install dependencies

```
pip install -r requirements.txt
```

2. Can either use JSON file with Google Sheets API or create a .env file with the information

3. Example .env

```
Discord Information
TOKEN =
MY_GUILD =

Google Sheets Information
CREDENTIALS_JSON =
SHEET_NAME =
TYPE =
PROJECT_ID =
PRIVATE_KEY_ID =
PRIVATE_KEY =
CLIENT_EMAIL =
CLIENT_ID =
AUTH_URI =
TOKEN_URI =
AUTH_PROVIDER_X509_CERT_URL =
CLIENT_X509_CERT_URL =
```
