import pandas as pd
import time

wd    = '/Users/danielmsheehan/GitHub/amazon/tasks/201602_padatabase/'
inCSV = wd+'data/input/PADATABASE.CSV'

df = pd.read_csv(inCSV)
df = df.rename(columns=lambda x: x.lower())

print df.head(10)

print len(df.index)

df = df.fillna('')
df['full_address'] = df['address1'] + ' ' + df['city'] + ', ' + df['state'] + ' ' + df['zip']

addressList = df['full_address'].tolist()

from geopy.geocoders import Nominatim
geolocator = Nominatim()

geocodes = []



for i in addressList:
	try:
		print i
		temp = []
		location = geolocator.geocode(i)
		# #lat = location.latitude
		# #lon = location.longitude
		temp.append(i)
		# print location.latitude
		# print location.longitude
		temp.append(location)
		# #temp.append(location.longitude)
		geocodes.append(temp)
		time.sleep(2)
		print location
	except:
		print 'except'
		geocodes.append(i+' did not geocode')

print geocodes

dfg = DataFrame(geocodes)

ouCSV = wd+'data/processing/geocodes.csv'
dfg.to_csv(ouCSV)