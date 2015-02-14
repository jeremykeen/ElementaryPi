#!/usr/bin/env python
import sys
from twython import Twython
CONSUMER_KEY = 'DMW3P8IUjaL3e5AYsnCMepVjw'
CONSUMER_SECRET = '6DwcgPMgvhSsBS2yYF6zfaaytlWAn2r2K6ypsREYe3w3K6YPFb'
ACCESS_KEY = '3018880213-51Z1Q4ZoQGEGYVcVqPXCo9iI7wNAohUIVsunwtX'
ACCESS_SECRET = 'ggYYfPakn5MUHhfqu7FpN7KelCO2BVFhwUGgey6IjCkcj'

twitter = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)
twitter.send_direct_message(screen_name='@jeremykeen',text='test DM from keenestRPi')

