import sys
import tweepy
import time
reload(sys)
sys.setdefaultencoding('utf-8')

ConsumerKey = '6C5ssisX3BR0uArUObjv7GjH5'
ConsumerSecret = 'O4GXWtOpOlE2HAKVjmX1O5kltSclT7cxxxxxxxxxxxxxxxxxxxx'
AccessToken = '844973212291256320-PW4lPhggG5ZtQIssExxxxxxxxxxxxxxxxxx'
AccessTokenSecret = 'ttcZUJBirpZKTZMWCD2arCNRknPE1xxxxxxxxxxxxxxxxxxx'

auth = tweepy.OAuthHandler(ConsumerKey, ConsumerSecret)
auth.set_access_token(AccessToken, AccessTokenSecret)

api = tweepy.API(auth)

tweet = tweepy.Cursor(api.followers_ids, id = 'TheAcademy', count = 5000).pages()
try:
    while True:
        try:
            AcademyFollower = open('/home/jiangnan/Desktop/AcademyFollower', 'a')
            AcademyFollower.write(str(tweet.next()))
            AcademyFollower.write('\n\n')
            AcademyFollower.close()
        except tweepy.TweepError:
            time.sleep(15 * 60 + 10) % sleep scheme due to Twitter API rate limitation
            continue
except:
    print "End"