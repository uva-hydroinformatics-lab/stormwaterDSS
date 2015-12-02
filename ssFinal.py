# -*- coding: utf-8 -*-
import json
import urllib2
import time
import speedtestUpdate

"""
Author: Stuart Sheffield (sfs8cq@virginia.edu)
Last modified: November 23, 2015.
"""

wshedDel = ['wshedDel']
basinChar = ['basinChar']
totalTime = ['total']

print time.strftime("%c")
for i in range(100):
    speedtestUpdate.speedtest()
    
    lat = 38.0656515783
    lon = -78.4799437051
    
    delineateUrl = "http://streamstatsags.cr.usgs.gov/streamstatsservices/watershed.json?" \
        + "rcode=VA" \
        + "&xlocation=%s"%(lon) \
        + "&ylocation=%s"%(lat) \
        + "&crs=4326&includeparameters=false&includeflowtypes=false" \
        + "&includefeatures=true&simplify=true"
        
    t1 = time.time()
    
    response1 = urllib2.urlopen(delineateUrl, timeout=10000).read()
    
    t2 = time.time()
    
    data1 = json.loads(response1)
    
    wspace = data1['workspaceID']
    
    basinUrl = "http://streamstatsags.cr.usgs.gov/streamstatsservices/parameters.json?" \
            + "rcode=VA" \
            + "&workspaceID=%s"%(wspace) \
            + "&includeparameters=false"
    
    response2 = urllib2.urlopen(basinUrl, timeout=10000).read()

    data2 = json.loads(response2)
    t3 = time.time()
    
    wshedDel.append(t2-t1)
    basinChar.append(t3-t2)
    totalTime.append(t3-t1)
    
for i in range(len(wshedDel)):
    print '%s,%s,%s'%(wshedDel[i],basinChar[i],totalTime[i])