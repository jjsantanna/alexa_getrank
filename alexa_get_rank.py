#Script written by Jair Santanna
#input: tested_url
#output:#c1:tested_url 
	#c2:timestamp
	#c3:popularity
	#c4:reach_rank
	#c5:rank_delta"

#!/usr/bin/env python
import sys
import re
import urllib2
import time

measurement_time = time.time()

def get_alexa_rank(url):
    try:
        data = urllib2.urlopen('http://data.alexa.com/data?cli=10&dat=snbamz&url=%s' % (url)).read()

        popularity_rank = re.findall("POPULARITY[^\d]*(\d+)", data)
        if popularity_rank: popularity_rank = popularity_rank[0]
        else: popularity_rank = -1

        reach_rank = re.findall("REACH[^\d]*(\d+)", data)
        if reach_rank: reach_rank = reach_rank[0]
        else: reach_rank = -1
        
        popularity_delta = re.findall("DELTA[^\d]*(\d+)", data)
        if popularity_delta: popularity_delta = popularity_delta[0]
        else: popularity_delta = -1
        #print popularity_delta #for debug purpose

        return int(popularity_rank), int(reach_rank), int(popularity_delta)

    except (KeyboardInterrupt, SystemExit):
        raise
    # except:
    #     return None

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print 'usage: python %s <site-url>' % (sys.argv[0])
        sys.exit(2)

    url = sys.argv[1]
    data = get_alexa_rank(url)
    #print data #for debug purpose

    popularity_rank, reach_rank, popularity_delta = -1, -1, -1
    if data:
        popularity_rank, reach_rank, popularity_delta = data

    #print "#c1:url\t#c2:timestamp\t#c3:popularity\t#c4:reach_rank\t#c5:rank_delta" #for debug purpose
    print url+";"+str(measurement_time)+";"+str(popularity_rank)+";"+str(reach_rank)+";"+str(popularity_delta)

