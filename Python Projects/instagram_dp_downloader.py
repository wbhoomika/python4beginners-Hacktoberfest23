# Import the instaloader module 
import instaloader

# Get instance 
ig  = instaloader.Instaloader()

# Enter the username of the profile pic you want to download 
dp = input("Enter Insta username : ")

# Download the profile pic 
ig.download_profile(dp, profile_pic_only=True)