## Twitter simulation framwork

The notebook `simulate.ipynb` should show you where to start.

Modify the `generate_users` function in the notebook to change how users are generated (right now the User only has one parameter: "propensity" to tweet vs. retweet)

`generate_users` generates users from a NetworkX graph, so you can make any NetworkX graph (directed) that represents the follower graph of the twitterverse you wish to simulate.

In `users.py`, the `User` class has a method called `act`. This is where one can change the choices to tweet, retweet, and how many tweets/retweets to use. Add any extra parameters needed to the constructor.

Let me know, I can add some stuff to visualize the results (in graph form or...???)
