import requests
import sys
import pdb
import random
import copy

# For actual use in functioning version
apikey = '&appid=dbf5bbbaeef83b5dccc8aa6dab999515'
options = '&units=imperial'
url = 'https://api.openweathermap.org/data/2.5/weather?q='


# Shell for mocked up responses
json_response_shell = {
    'main': {
        'temp' : ''
    },
    'name' : ''
}

# holds our random responses
# max of 10, and popped off as requests are made
randomResponses = []

# Generate random responses
def generateRandoms():
    rands = []
    random.seed()
    # random city names for generation
    cityNames = ['Milwaukee','Chicago','New York','Anaheim','Toronto','Madison',
                'birmingham','Washington D.C.','Atlanta','Seattle','Green Bay',
                'Bern','London','Berlin','Paris','Tokyo']    
    for i in range(10):
        random.shuffle(cityNames)
        new = copy.deepcopy(json_response_shell)
        new['name'] = cityNames.pop()
        new['main']['temp'] = random.randint(-100,130)

        rands.append(new)
    
    global randomResponses 
    randomResponses = copy.deepcopy(rands)
        
# Calls API and 
def fetchWeather(city):
    try:
        
        queryUrl = url + str(city) + options + apikey
    # commented out for mocked responses
        #response = requests.get(queryUrl)
        #if response.ok:
            #return response.json()    
        #else:
            #return None
        response = randomResponses.pop()
        return response

    except KeyboardInterrupt:
        raise
    except:
        e = sys.exc_info()
        sys.stderr.write("Error: " + str(e))

def getTemp(resp):
    return resp['main']['temp']

def fetchMultiple(cityList):
    retList = []
    for city in cityList:
        tmp = fetchWeather(city)
        cityPair = (tmp['name'],tmp['main']['temp'])
        retList.append(cityPair)
    return retList

def tempsort(responses,reverse=False,prettyprint=False):
    if reverse is True:
        responses.sort(key=getTemp,reverse=True)
    else:
        responses.sort(key=getTemp)

    if prettyprint:
        print("Sorted:")
        for resp in responses:
            print (resp['name'] + ' : ' + str(resp['main']['temp']))
    return responses
    