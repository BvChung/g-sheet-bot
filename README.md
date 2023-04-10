# Leetbot

## Overview

LeetBot is a personal leetcode problem and solution tracker discord bot integrated with Google Sheets using Google Sheets API and Gspread Python API.

## Table of Contents

- [Tech](#tech)<br/>
- [Setting Up](#setting-up)<br/>
- [Development](#development)<br/>
- [Demos](#demo-gifs)<br/>

## Tech

- [Python](https://www.python.org/)

## Setting Up

1. Create project on [Google Cloud](https://console.cloud.google.com)
2. Go to API's & Services and enable Google Sheets API + Google Drive API
3. Go to Google Sheets API and create a service account -> Keys tab -> Add Key -> Create Key -> Export as JSON
4. Go to your Google Sheets spreadsheet
5. Share with "client_email" in the JSON file

## Development

1. Install dependencies

```
pip install -r requirements.txt
```

2. Create .env

```
Discord Information
TOKEN = 
MY_GUILD = 

Google Sheets Information
CREDENTIALS_JSON = JSON name
SHEET_NAME = 
```

## Demo GIFs
**Viewing**

![All](https://github.com/BvChung/leetbot/blob/main/botdemogifs/viewall.gif)

![Topics](https://github.com/BvChung/leetbot/blob/main/botdemogifs/viewtopic.gif)

**Creating**

![Creation](https://github.com/BvChung/leetbot/blob/main/botdemogifs/creating.gif)

**Updating**

![Update](https://github.com/BvChung/leetbot/blob/main/botdemogifs/update.gif)

**Deleting**

![Deletion](https://github.com/BvChung/leetbot/blob/main/botdemogifs/deleting.gif)


