# IGFollowers

## Overview

**IGFollowers** is a Python application designed to help users analyze their Instagram followers and following lists. The app allows users to easily identify who is not following them back and who they are not following back by comparing their followers and following data.

## Features

- **User-Friendly Interface**: Utilizes Tkinter for a simple and intuitive file selection interface.
- **HTML Parsing**: Extracts usernames from HTML files containing follower and following lists using BeautifulSoup.
- **Comparison Analysis**: Provides insights on:
  - Users who do not follow you back.
  - Users you do not follow back.
- **Output Summary**: Displays results in a clear and concise format.

## Prerequisites

To run the IGFollowers application, you'll need the following:

- Python 3.x installed on your machine.
- The following Python libraries:
  - `BeautifulSoup`
  - `tkinter`

You can install the required libraries using pip:

```bash
pip install beautifulsoup4
```
## How to Use IGFollowers

Follow these steps to use the IGFollowers application:

### Step 1: Prepare Your HTML Files

- Ensure you have two HTML files:
  - **Followers List**: An HTML file containing the list of users who follow you.
  - **Following List**: An HTML file containing the list of users you follow.

### Step 2: Run the Application

1. **Open a Terminal or Command Prompt**:  
   Navigate to the directory where the IGFollowers project is located.

2. **Run the Application**:  
   Execute the following command to start the application:

   ```bash
   python IGFollow.py
   ```
### Step 3: Select Your Files

- When prompted, select your HTML files:
  - **Select the Followers File**: Choose the HTML file that contains your followers.
  - **Select the Following File**: Choose the HTML file that contains the users you are following.

### Step 4: View the Results

- After the application processes the files, it will display the results in the terminal. The output will include:
  - **Not Following Back**: The number of users who do not follow you back, along with their usernames.
  - **Not Followed Back**: The number of users you do not follow back, along with their usernames.
