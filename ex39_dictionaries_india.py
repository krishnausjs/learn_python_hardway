states = {
	'Andhra Pradesh': 'AP',
	'Karnataka' : 'KN',
	'Tamil Nadu' : 'TN',
	'Orissa' : 'OR',
	'Kashmir' : 'KR',
	'Kerala' : 'KL'
}

cities = {
	'AP' : 'Amaravathi',
	'TN' : 'Chennai',
	'KL' : 'Cochin',
	'KN' : 'Bangalore',
	'KR' : 'Shrinagar',
	'OR' : 'Bhuvaneswar'
}

cities['TL'] = 'Hyderabad'

print 30 * '-'
print "City of AP is %s" % cities['AP']
print 30 * '-'


print 30 * '-'
print "City of Tamil nadu is %s" % (cities[states['Tamil Nadu']])
print 30 * '-'
for state, abbrev in states.items():
	print "State is %s and abbrev is %s" % (state, abbrev)

for state, abbrev in states.items():
	print "City of state %s is %s" % (state, cities[abbrev])

city = cities.get('AP','Doesnt exist')
if not city:
	print "No city for AP exist"
else:
	print "City of AP is %s" % city

city = cities.get('ML', 'Doesnt exist')
if not city:
	print "No city for ML exist"
else:
	print "City of MP is %s" % city
