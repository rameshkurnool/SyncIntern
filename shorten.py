import pyshorteners
# initialize the Shortener object
s = pyshorteners.Shortener()

# enter the URL to be shortened
url = input("Enter the URL to shorten: ")

# use the Shortener object to shorten the URL
short_url = s.tinyurl.short(url)

# print the shortened URL
print("Shortened URL:", short_url)
