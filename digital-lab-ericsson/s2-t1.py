from timeit import default_timer as timer

start = timer()

ledState = 0
interval = 1
pauseMillis = 0

while True:
    timeMillis = timer() 
    print("timeMillis",timeMillis)
	
    if timeMillis-pauseMillis >= interval:
        pauseMillis = timeMillis

        if ledState == 0:
            ledState = 1
            print("ledState",ledState)
        else:
            ledState = 0
            print("ledState",ledState)