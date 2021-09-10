import requests

print( "The requests library version:", requests.__version__ )

print( "GET the google homepage:", requests.get( 'http://www.google.com/' ) )

print( "Print my script on Github:", requests.get( 'https://github.com/TheOnlyMiki/CMPUT-404---Lab-1/lab1.py' ).text )

