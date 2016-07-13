#!/usr/bin/python
#
# author: Denny R S Vriesman


import json 
import sys
import urllib2
import datetime

jenkinsUrl = "http://jenkins/job/"


if len( sys.argv ) > 1 :
    jobName = sys.argv[1]
else :
    print "Job Name required"
    sys.exit(-9)

try:
    jenkinsStream   = urllib2.urlopen( jenkinsUrl + jobName + "/lastBuild/api/json" )
except urllib2.HTTPError, e:
    print "Error: " + str(e.code) 
    sys.exit(-8)

try:
    result = json.load( jenkinsStream )
except:
    print "Failed to parse"
    sys.exit(-7)

if result.has_key( "result" ) and result["result"]:      

    date = datetime.datetime.fromtimestamp(result["timestamp"]/1000).strftime('%Y-%m-%d %H:%M:%S')

    print "[" + jobName + "] date: " + date + " build number: " + result["displayName"] + " build status: " + result["result"]
 
    if result["result"] != "SUCCESS" :
        exit(-1)
else:
    sys.exit(-6)

sys.exit(0)
