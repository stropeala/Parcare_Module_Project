import datetime
import time
from random import randint


def countdown_draft():
    start_s = str(datetime.datetime.now())
    start = {"Intrare in parcare": str(datetime.datetime.now())}

    t = randint(0, 2)
    while t:
        time.sleep(1)
        t -= 1

    end_s = str(datetime.datetime.now())
    end = {"Parcarea a expirat": str(datetime.datetime.now())}

    timp = start | end

    print(type(end_s))
    print(timp)
    print(eval(f"{end_s} - {start_s}"))
