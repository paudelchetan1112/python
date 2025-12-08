def profile_info(username, followers=1500):
    print(f"Username:{username}")
    print(f"Followers:{followers}")

profile_info('user1')
profile_info(followers=2500, username="user2")