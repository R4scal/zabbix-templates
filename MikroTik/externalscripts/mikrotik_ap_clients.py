#!/usr/bin/python

import netsnmp
import binascii
import sys

# Get data from snmp
def getmac(host, community):
    oid = netsnmp.VarList(netsnmp.Varbind('.1.3.6.1.4.1.14988.1.1.1.2.1.1'))
    res = netsnmp.snmpwalk(oid, Version = 2, DestHost=host,
                           Community=community)
    return res


args = sys.argv

if len(args) < 3:
   print "Usage: ", sys.argv[0], "HOST COMMINITY"
else:
   items = getmac(sys.argv[1], sys.argv[2])
   count = len(items) - 1

   print '{'
   print ' "data": ['
   for (n, item) in enumerate(items):
      # convert binary to ASCII
      mac = binascii.b2a_hex(item)
      # convert to mac format
      mac = ':'.join(mac[i:i+2] for i in range(0, len(mac), 2)).strip()
      # get oid
      segments = mac.split(":")
      segments = [ str(int(x, 16)) for x in segments ]
      oid = '.'.join(segments).strip()
      # Print discovery item
      print '  {'
      print "   \"{#MACADDRESS}\": \"%s\"," % mac
      print "   \"{#OID}\": \"%s\"" % oid
      if n == count:
         print '  }'
      else:
         print '  },'
   print ' ]'
   print '}'
