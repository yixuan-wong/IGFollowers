import tkinter as tk
from tkinter import filedialog
from bs4 import BeautifulSoup

def load_user_names_HTML(filename):
    """
    Loads usernames from an Instagram HTML file by detecting the file structure.
    1. For followers files, it extracts usernames from the href of <a> tags.
    2. For following files, it extracts usernames from the text of <h2> tags.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')

        # First, try to find usernames by parsing the href attribute in <a> tags.
        # This is the most reliable method for the followers list.
        usernames = []
        links = soup.find_all('a')
        
        # Heuristic to check if this file is in the followers format (contains profile links)
        if any('instagram.com/' in a.get('href', '') for a in links):
            for a in links:
                href = a.get('href')
                if href and 'instagram.com/' in href:
                    # Split the URL by '/' and get the last non-empty part, which is the username
                    # e.g., "https://www.instagram.com/samasteria/" -> "samasteria"
                    parts = [part for part in href.split('/') if part]
                    if parts and '?' not in parts[-1]: # Ensure it's a clean username
                        username = parts[-1]
                        usernames.append(username)

        # If no usernames were found using the <a> tag method,
        # it's likely the following list format which uses <h2> tags.
        if not usernames:
            h2_tags = soup.find_all('h2')
            usernames = [h2.text for h2 in h2_tags if h2.text]

        return usernames

def format_usernames(usernames):
    """Formats a list of usernames for printing."""
    # Sort the list alphabetically for easy reading
    return '\n'.join(sorted([f"@{username}" for username in usernames]))

def compare_followers_and_following(followers, following):
    """Compares follower and following lists and prints the differences."""
    followers_set = set(followers)
    following_set = set(following)

    # People who follow you, but you don't follow back
    not_followed_back = followers_set - following_set
    print(f"Accounts that follow you (but you don't follow back): {len(not_followed_back)}")
    if not_followed_back:
        print(format_usernames(not_followed_back))
    else:
        print("None")
    print("\n" + "="*40 + "\n") # Separator for clarity

    # People you follow, but who don't follow you back
    not_following_back = following_set - followers_set
    print(f"Accounts you follow (that don't follow you back): {len(not_following_back)}")
    if not_following_back:
        print(format_usernames(not_following_back))
    else:
        print("None")

# --- Main Program ---
root = tk.Tk()
root.withdraw()

print("Please select your FOLLOWERS HTML file.")
followers_file = filedialog.askopenfilename(title="Select Followers HTML File", filetypes=[("HTML Files", "*.html;*.htm")])
if not followers_file:
    print("Operation cancelled. Exiting.")
    exit()

print("Please select your FOLLOWING HTML file.")
following_file = filedialog.askopenfilename(title="Select Following HTML File", filetypes=[("HTML Files", "*.html;*.htm")])
if not following_file:
    print("Operation cancelled. Exiting.")
    exit()

print("\nProcessing files...\n")

followers = load_user_names_HTML(followers_file)
following = load_user_names_HTML(following_file)

if not followers or not following:
    print("Error: Could not extract usernames from one or both files.")
    print(f"Found {len(followers)} followers and {len(following)} accounts you follow.")
    print("Please ensure you have selected the correct HTML files.")
else:
    print(f"Found {len(followers)} followers and {len(following)} accounts you follow.\n")
    compare_followers_and_following(followers, following)