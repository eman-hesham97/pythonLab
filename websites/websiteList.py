import webbrowser
import random
Website_list = ["https://www.google.com", "https://www.facebook.com", "https://www.youtube.com", "https://www.twitter.com"]
selectedWebsite = random.choice(Website_list)
webbrowser.open(selectedWebsite, new=2)