import instaloader  # type: ignore
import getpass

def get_followers(username, password, target_username):
    
    L = instaloader.Instaloader()

    try:
        
        L.login(username, password)
    except instaloader.exceptions.ConnectionException as e:
        print("Login failed:", e)
        return

    try:
        # Load the profile
        profile = instaloader.Profile.from_username(L.context, target_username)

        # Get the list of followers
        followers = profile.get_followers()
        count = 0

        # Store the followers in a list
        followers_list = []
        for follower in followers:
            followers_list.append(follower.username)
            count += 1

        # Print the followers
        print("Followers:", followers_list)

        # Save followers to a text file
        with open('followers_list.txt', 'w') as file:
            for follower in followers_list:
                file.write(follower + '\n')
        print(count)
    except instaloader.exceptions.ProfileNotExistsException:
        print("Profile does not exist.")
    except instaloader.exceptions.ConnectionException as e:
        print("Connection error:", e)
    except Exception as e:
        print("An error occurred:", e)

def get_following(username, password, target_username):
   
    L = instaloader.Instaloader()

    try:
        
        L.login(username, password)
    except instaloader.exceptions.ConnectionException as e:
        print("Login failed:", e)
        return 
    try:
        
        profile = instaloader.Profile.from_username(L.context, target_username)

       
        followees = profile.get_followees()
        followees_count=0

        
        followees_list = []
        for followee in followees:
            followees_list.append(followee.username)
            followees_count+=1  

        # Print the followees
        print("Following:", followees_list)

        # Save followees to a text file
        with open('followees_list.txt', 'w') as file:
            for followee in followees_list:
                file.write(followee + '\n')
        print(followees_count)        
    except instaloader.exceptions.ProfileNotExistsException:
        print("Profile does not exist.")
    except instaloader.exceptions.ConnectionException as e:
        print("Connection error:", e)
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    
    username = input("Enter your Instagram username: ")
    password = getpass.getpass("Enter your Instagram password: ")

    target_username = input("Enter the target Instagram username: ")

    get_followers(username, password, target_username)
    get_following(username, password, target_username)
