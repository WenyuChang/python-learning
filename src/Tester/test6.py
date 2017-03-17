import uuid,datetime


u = uuid.UUID('94d8b0df-fcb4-11e5-9774-07dcdcc484fc')
print '%s: %s' % (str(u), datetime.datetime.fromtimestamp((u.time - 0x01b21dd213814000L)*100/1e9))
s = 1460028822650 / 1000.0
print datetime.datetime.fromtimestamp(s).strftime('%Y-%m-%d %H:%M:%S.%f')


#94e4498f-fcb4-11e5-97a5-0050568e09f9



u = uuid.UUID('94e708b1-fcb4-11e5-b520-59caf0a5d51a')
print '%s: %s' % (str(u), datetime.datetime.fromtimestamp((u.time - 0x01b21dd213814000L)*100/1e9))
s = 1460028822744 / 1000.0
print datetime.datetime.fromtimestamp(s).strftime('%Y-%m-%d %H:%M:%S.%f')







print
print



u = uuid.UUID('9df01421-fd17-11e5-b5e2-1feb8eb8dd16')
print '%s: %s' % (str(u), datetime.datetime.fromtimestamp((u.time - 0x01b21dd213814000L)*100/1e9))
s = 1460071358144 / 1000.0
print datetime.datetime.fromtimestamp(s).strftime('%Y-%m-%d %H:%M:%S.%f')


print
print
print


u = uuid.UUID('9d5c86b1-fd17-11e5-9bdb-eb87f71e60b2')
print '%s: %s' % (str(u), datetime.datetime.fromtimestamp((u.time - 0x01b21dd213814000L)*100/1e9))
s = 1460071358144 / 1000.0
#print datetime.datetime.fromtimestamp(s).strftime('%Y-%m-%d %H:%M:%S.%f')