from insta_bot import InstaFollower

USERNAME = 'pythoncode58'
PASSWORD = 'superman2'
SIMILAR_ACCOUNT = 'cristiano'
bot = InstaFollower(username=USERNAME, password=PASSWORD, similar_account=SIMILAR_ACCOUNT)
bot.login()
bot.find_followers()
bot.follow()