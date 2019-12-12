from retweeting import *

def test_add_followers():
    user = User(1, 0.5)
    user_b = User(2, 0.5)
    user.follow_user(user_b.userid)
    assert user.follows == { 2 }

def test_generate_timeline_only_followed_users():
    user = User(1, 0.5)
    user_b = User(2, 0.5)

    user.follow_user(user_b.userid)
    timeline = user._generate_timeline({ 2: [Tweet('foo', None, 2)],
                                         3: [Tweet('bar', None, 3)]})

    assert timeline == [Tweet('foo', None, 2)]

def test_generate_timeline_no_tweet_ive_tweeted():
    user = User(1, 0.5)
    user_b = User(2, 0.5)

    tw = user.tweet(1)[0]
    timeline = user._generate_timeline({ 2: [Tweet('foo', tw.id, 2)]})
    assert timeline == []


def test_generate_timeline_no_tweet_ive_retweeted():
    user = User(1, 0.0)
    user_b = User(2, 0.5)

    tw = user_b.tweet(1)
    user.retweet(tw)

    # simulate next round
    timeline = user._generate_timeline({ 2: tw })

    # no tweets in timeline as only tweet was already retweeted
    assert timeline == []


# def test_first_round_tweets():
#     twitter = Twitter()
#     user = User(1, 0.5)
#     tw = user.round(None)
#     assert twitter.rounds[0] == { 1: [tw] }
