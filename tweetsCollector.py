followerID = open('FollowerID')
followerlist = followerID.read().split()

followerTwitter = open('FollowerTwitter', 'w')
ZombieID = open('ZombieID','w')
IgnoredID = open('DataMiningProject1/IgnoredID1','w')
NotAuthorized = open('NotAuthorized','w')

for follower in followerlist:
    try:
        twitterlist = api.user_timeline(follower, count = 200)
        if len(twitterlist) == 0:
            ZombieID.write(follower)
            ZombieID.write('\n')
            continue
        else:
            userinformation = follower + ',' \
                              + str(twitterlist[0]._json['user']['statuses_count']) + ',' \
                              + str(twitterlist[0]._json['user']['friends_count']) + '\n'
            followerTwitter.write(userinformation)
            for status in twitterlist:
                followerTwitter.write(status.text + '\n')
            followerTwitter.write('\n\n\n####################\n\n\n')
    except tweepy.error.TweepError, argument:
        if (argument.__str__()) == "Not authorized.":
            NotAuthorized.write(follower)
            NotAuthorized.write('\n')
            continue
        if argument.__str__() == "[{u'message': u'Rate limit exceeded', u'code': 88}]":
            time.sleep(15 * 60 + 3)
            continue
        if argument.__str__() == "[{u'message': u'Internal error', u'code': 131}]":
            IgnoredID.write(follower)
            IgnoredID.write('\n')
            continue
        else:
            IgnoredID.write(follower)
            IgnoredID.write('\n')
            continue

followerID.close()
followerTwitter.close()
ZombieID.close()
IgnoredID.close()
NotAuthorized.close()