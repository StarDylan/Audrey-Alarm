#!/usr/bin/python

import bluetooth
import time
import urllib
import sys




devices = []




#
# This file has all the UUIDs to check in the following format
#     00:00:00:0:00,name1
#     00:00:00:0:01,name2
#
with open ('btdevices.cfg', 'r') as f:
        for line in f:
                items = line.split(',')
                uuid = items[0].strip(' \t\n\r')

		try:
                	name = items[1].strip(' \t\n\r')
		except IndexError:
			name = None

                now = int(time.time())
                devices.append({ 'uuid' : uuid, 'name' : name, 'in_last_time' : now, 'out_last_time' : now, 'in_age' : 999, 'out_age' : 0})
                

while True:

    for device in devices:
        uuid = device['uuid']
        name = device['name']
        print('uuid = ' + uuid + " Name = " + name)
        
        if (device['in_age'] > 5):

            result = bluetooth.lookup_name(uuid, timeout=5) 
            if (result != None):  
                device['in'] = 1
                device['in_last_time'] = int(time.time())
                print "IN"
            else:
                device['in'] = 0
                device['out_last_time'] = int(time.time())
                print "OUT"

    
        
        

        now = int(time.time())
        device['out_age'] = now - device['in_last_time']  
        device['in_age'] = now - device['out_last_time']
    
            
        print 'InAge' + str(device['in_age']) + ' OutAge' + str(device['out_age'])
        time.sleep(0.5)

   
        


        if (device['name'] == 'Dylan iPhone' and device['in_age'] > 10):
            print'Device in Range!'

        else:
            print 'Device Not in Range!'


            
                
            
                
            
        

    
