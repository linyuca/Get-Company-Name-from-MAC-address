#!/usr/bin/env python

from maclookup import ApiClient
import sys
import json
import os

mykey=os.environ.get('MY_KEY')
if mykey == None:
    mykey="at_EYedF482zqmiTdQyerFKVsBKlFNfc"

#Get the movie name 
mac_addr = sys.argv[1]
if len(mac_addr) == 0 :
    print ("Mac address missing")
    sys.exit()

client = ApiClient(mykey)

try:
  #vendor = client.get_vendor(mac_addr)
  #print ("Mac address: {} is for vendor: {}".format(mac_addr, vendor))

  response = client.get_raw_data(mac_addr, 'json')

  json_text = json.loads(response)

  vendor = json_text['vendorDetails']['companyName']
  if (len(vendor) > 0) :
    print ("Mac address: {} is for vendor: {}".format(mac_addr, vendor))
  else:
    print ("Mac address: {} does not match to any vendor".format(mac_addr))
except Exception as e:
  print ("Error: get_vendor with erro: {}".format(str(e))) 

