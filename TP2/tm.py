import time

def update_time():
    localtime = time.localtime()
    result = time.strftime("%I:%M:%S %p", localtime)
    return result