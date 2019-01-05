import pdb
import service as svc
import random

# Print debug statements
DEBUG = False

def test_tempsort(testCount,mode):

    # Randomly tests the tempsort function (ascending and descending)
    # Tests are done against a list sorted by the sort() method built in to Python

    if mode == 1:
        print("Testing ascending sort")
    else:
        print("Testing descending sort")
    
    numErrors = 0
    for t in range(testCount):

        # generate random responses
        svc.generateRandoms()
        
        # hold the random responses
        responses = []
        
        # hold city,temp pairs for testing
        pairs = []
        
        # fetch 10 responses
        for i in range(10):
            responses.append(svc.fetchWeather(None))
            pairs.append((responses[i]['name'],responses[i]['main']['temp'])) 

        if DEBUG:
            print('Before sorting: ')
            print(pairs)
            print(responses)
        if mode == 1:    
            # sort with built-in sort
            pairs.sort(key=lambda tup: tup[1])
        
            # sort with service.tempsort
            svc.tempsort(responses, prettyprint=True)
        else:
            # sort with built-in sort
            pairs.sort(key=lambda tup: tup[1], reverse=True)
        
            # sort with service.tempsort
            svc.tempsort(responses, reverse=True, prettyprint=True)   

        if DEBUG:
            print('After sorting: ')
            print(pairs)
            print(responses)

        # Confirm the built in Python sorted list matches our sorted list
        for i in range(len(responses)):
            desired = pairs[i][0]
            actual = responses[i]['name']
            try:
                assert desired == actual, "Mismatch"
            except AssertionError:
                numErrors += 1

    print ("Number of errors: %d"% numErrors) 


test_tempsort(1,0)