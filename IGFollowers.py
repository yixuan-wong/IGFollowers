import tkinter as tk
from tkinter import filedialog
from bs4 import BeautifulSoup

def load_user_names_HTML(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')

        usernames = [a.text for a in soup.find_all('a') if a.text]

        return usernames
    
def format_usernames(usernames):
    return '\n'.join([f"@{username}" for username in usernames])

def compare_followers_and_following(followers, following):
    followers_set = set(followers)
    following_set = set(following)

    # People you are not following back 
    not_followed_back = followers_set - following_set
    print(f"Not followed back: {len(not_followed_back)}")
    if not_followed_back: 
        print(format_usernames(not_followed_back))
    else:
        print("None") 
    print("\n")

    # People that are not following you back
    not_following_back = following_set - followers_set
    print(f"Not following back: {len(not_following_back)}")
    if not_following_back:
        print(format_usernames(not_following_back))
    else:
        print("None")

root = tk.Tk()
root.withdraw()

followers_file = filedialog.askopenfilename(title = "Select Followers HTML File", filetype = [("HTML Files", "*.html;*.htm")])
following_file = filedialog.askopenfilename(title = "Select Following HTML File", filetype = [("HTML Files", "*.html;*.htm")])

followers = load_user_names_HTML(followers_file)
following = load_user_names_HTML(following_file)

compare_followers_and_following(followers, following)