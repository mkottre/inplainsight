#!/usr/bin/python3

import http.client, random, sys, time

# A connection will be made at random between the following numbers
lower_limit = 0 # Set the lowest amount of time, in seconds, before calling random_connection()
upper_limit = 30 # Set the highest amount of time, in seconds, before calling random_connection()

def random_connection():
	random_number = random.randint(-1,(len(urls)-1)) # Generates a random number in the range 0 to the number of urls
	url = urls[random_number].strip('\n') # Uses the random number to choose a url and strips the new line character off of the end
	connection = http.client.HTTPConnection(url) # Creates a connection to the url
	connection.request("GET", "/index.html") # Makes the connection
	r1 = connection.getresponse() # Gets the response
	print(r1.status, r1.reason) # Prints the status of the connection
	print(url) # Prints the url
	connection.close() # Closes the connection

urls_file = open('urls', 'r') # Opens the urls file as read-only
urls = urls_file.readlines() # Creates an array out of the urls in the file
while True: # Runs a loop that creates a connection on a random interval
	interval_time = random.randint(lower_limit, upper_limit)
	random_connection()
	print(interval_time," seconds")
	time.sleep(interval_time)
