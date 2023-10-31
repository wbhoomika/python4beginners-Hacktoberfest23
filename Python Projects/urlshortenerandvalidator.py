import pyshorteners
import validators
long_url = input("Enter the URL to shorten: ")



if not validators.url(long_url):
     print ("This input is invalid")

else:
     type_tiny = pyshorteners.Shortener()
     short_url = type_tiny.tinyurl.short(long_url)
     print("The Shortened URL is: " + short_url)
