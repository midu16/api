# ==============
#
# IDU MIHAI (c) 2018
#
# ==============
import os
import pyowm
import sys
# ==============
# Import the enviroment variables in this script
try:
	os.environ['OPENWEATHER_API_KEY']
	os.environ['CITY_NAME']
except KeyError:
	print 'Please set the following enviroment variable: OPENWEATHER_API_KEY and CITY_NAME'
	sys.exit(1)
# ==============
# Assign the enviroment variables values to variables
API_KEY =  os.environ['OPENWEATHER_API_KEY']
CITY = os.environ['CITY_NAME']
# ==============
# Test the format of the asssigned values
#print API_KEY
#print CITY
# ==============
owm = pyowm.OWM(API_KEY)
observation = owm.weather_at_place(CITY)
w = observation.get_weather()
# ==============
# Extract the informations from the weather API
wind = w.get_wind() 			#should display the speed of the wind
#print'The information regarding the humidity: ',
humidity = w.get_humidity() 		#should display the percentage of humidity
temperature = w.get_temperature('celsius') 	#should display the temperature in celsius
cloud = w.get_clouds()

# ==============
# Display the informations using stdout print function
print 'Source of the information is:','openweathermap'
print 'City is:',CITY
print 'Description is:'
print 'Speed of the wind is :', wind['speed'], 'meter per sec'
print 'Humidity is:', humidity, '%'
print 'The temperature is:', temperature['temp'], 'Celsius'
print 'Coulds over the city is:',cloud
# ================
