class Twitter():
    def __init__(self):
        self.rounds = []

    def tweet(self, tweet):
        try:
            self.current_round[tweet.userid].append(tweet)
        except KeyError:
            self.current_round[tweet.userid] = [tweet]

    def round(self, users):
        self.current_round = {}
        self.rounds.append(self.current_round)

        prev_round = self.rounds[-2] if len(self.rounds) > 1 else None

        tweets = [t for u in users
                  for t in u.act(prev_round)]

        for t in tweets:
            self.tweet(t)


    def simulate(self, users, rounds):
        for i in range(rounds):
            self.round(users)
