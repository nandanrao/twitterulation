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

        prev_rounds = self.rounds if len(self.rounds) > 0 else None

        tweets = [t for u in users
                  for t in u.act(prev_rounds)]

        for t in tweets:
            self.tweet(t)

        self.rounds.append(self.current_round)


    def simulate(self, users, rounds):
        for i in range(rounds):
            self.round(users)
