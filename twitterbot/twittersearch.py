
#!/usr/bin/env python
import sys
from twython import Twython
CONSUMER_KEY = 'QZuyCzb6QtYkjqCpgJ00PzqDk'
CONSUMER_SECRET = 'QmdViQqo8AjssPER8XiVoxKZSRFB9iLT1adl4qkn7GVE1KDukI'
ACCESS_KEY = '16248994-P7Xho81dRzn8szzfXjxYsQyd8BHmdiiZ1Z3PHd9eC'
ACCESS_SECRET = 'Z5L2B8bfNGmIrApBp5WHvPwki43geA3823K2UVRCdhGlP'

twitter = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)
query= sys.argv[1]

print "searching twitter for: %s" % query

search = twitter.cursor(twitter.search,q=query)
for result in search:
    print result
