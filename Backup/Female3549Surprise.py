#!/usr/bin/python

import time
import urllib2

print("sent Data to GA")
urllib2.urlopen("http://www.google-analytics.com/collect?v=1&tid=UA-47009702-1&cid=123&t=event&ec=Location%201&ea=Consumer%20Mood&el=Surprise")
urllib2.urlopen("http://www.google-analytics.com/collect?v=1&tid=UA-47009702-1&cid=123&t=event&ec=Location%201&ea=Total%20Consumer%20Views&el=Engagement%20Per%20Second")
urllib2.urlopen("http://www.google-analytics.com/collect?v=1&tid=UA-47009702-1&cid=123&t=event&ec=Location%201&ea=Gender&el=Female")
urllib2.urlopen("http://www.google-analytics.com/collect?v=1&tid=UA-47009702-1&cid=123&t=event&ec=Location%201&ea=Age%20Group&el=35%20to%2049").close