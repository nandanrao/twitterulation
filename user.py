import numpy as np
from uuid import uuid4
from collections import namedtuple
import random

def gen_tweet_id():
    return uuid4().hex

Tweet = namedtuple('Tweet', ['id', 'retweeted_status_id', 'userid'])

class User():
    def __init__(self, userid, propensity):
        self.userid = userid
        self.propensity = propensity
        self.follows = set()
        self.tweets = set()
        self.retweets = set()

    def follow_user(self, userid):
        self.follows.add(userid)

    def _tweet(self):
        tweet = Tweet(gen_tweet_id(), None, self.userid)
        self.tweets.add(tweet.id)
        return tweet

    def _retweet(self, tweet):
        new_tweet = Tweet(gen_tweet_id(), tweet.id, self.userid)
        self.retweets.add(tweet.id)
        return new_tweet


    def _generate_timeline(self, prev_round):
        timeline = [tweet for user in self.follows
                        for tweet in prev_round.get(user, [])]

        # filter out tweets that I've retweeted
        timeline = [t for t in timeline
                    if t.retweeted_status_id not in self.tweets
                    and t.id not in self.retweets]

        return timeline

    def tweet(self, N):
        """ Returns N number of new tweets """
        return [self._tweet() for _ in range(N)]

    def retweet(self, tweets):
        """ returns the retweets of all given tweets """
        return [self._retweet(t) for t in tweets]

    def act(self, prev_round):
        if prev_round is None:
            # first round, everyone twets ?
            return self.tweet(1)

        else:
            # What should happen here? Can tweet more than once?
            # decide by propensity?
            if np.random.random() > self.propensity:
                timeline = self._generate_timeline(prev_round)

                # pick tweet to retweet (now is just totally random)
                to_retweet = [random.choice(timeline)] if timeline else []
                return self.retweet(to_retweet)

            else:

                # How many tweets to tweet?
                return self.tweet(1)
