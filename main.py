import os
import tweepy
from pprint import pprint
from dotenv import load_dotenv
load_dotenv()

# 認証　
API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')
BEARER_TOKEN = os.getenv('BEARER_TOKEN')

def ClientInfo():
    client = tweepy.Client(
        consumer_key=API_KEY,
        consumer_secret=API_SECRET,
        access_token=ACCESS_TOKEN,
        access_token_secret=ACCESS_TOKEN_SECRET,
        bearer_token=BEARER_TOKEN
    )
    
    return client

# 特定のツイートからいいねしたユーザー情報を取得
def Get_Liking_Users(tweet_id):
    # メソッド実行
    users = ClientInfo().get_liking_users(id=int(tweet_id)).data
    
    # 結果加工
    result = []
    if users !=  None:
        for i in range(len(users)):
            obj = {}
            obj["user_id"]  = users[i].id
            obj["name"]     = users[i].name
            obj["username"] = users[i].username
            result.append(obj)
    else:
        result.append("")
    
    
    # 出力
    return result

# 特定のユーザーIDからフォロワー情報取得
def GetUser_Follower(user_id):
    # メソッド
    following = ClientInfo().get_users_followers(id=int(user_id))
    
    # 取得したデータ加工
    results     = []
    follow_data = following.data

    # tweet検索結果取得
    if follow_data != None:
        for tweet in follow_data:
            obj = {}
            obj["user_id"]  = tweet.id       # User_ID
            obj["name"]     = tweet.name     # Name
            obj["username"] = tweet.username #username
            results.append(obj)
    else:
        results.append('')

    # 結果出力
    return results

if __name__ == "__main__":
    tweet_id = 'ツイートID'
    # user_id = 'ユーザーID'
    pprint(Get_Liking_Users(tweet_id))
    # pprint(GetUser_Follower(user_id))