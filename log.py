import time

startTime = 0
endTime = 0

def start():
    global startTime
    startTime = time.perf_counter()
    return startTime

def end():
    global endTime
    endTime = time.perf_counter()
    elapsed = endTime - startTime
    return elapsed
