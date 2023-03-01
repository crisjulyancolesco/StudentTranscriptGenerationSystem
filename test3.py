import csv
import pandas as pd
import numpy as np
import statistics as st
import os
import time
from datetime import date
from datetime import datetime
DateToday = date.today()
DateToday = DateToday.strftime("%m/%d/%y")

TimeNow = datetime.now()
TimeNow = TimeNow.strftime("%H:%M:%p")

def previousRequestFeature():
    File = open("stdIDPreviousRequests.txt", "a")
    File.write("==================================================================\n")
    File.write(f"\tRequest\t\t\t    Date\t\t   Time \n")
    File.write("==================================================================\n")


def Try():
    File = open("stdIDPreviousRequests.txt", "a")
    File.write(f"wews Transcripts \t\t{DateToday:>10} \t\t{TimeNow:>10}\n")

def Try1():
    File = open("stdIDPreviousRequests.txt", "a")
    File.write(f"Major Transcripts \t\t{DateToday:>10} \t\t{TimeNow:>10}\n")

def Try2():
    File = open("stdIDPreviousRequests.txt", "a")
    File.write(f"Full Transcripts \t\t{DateToday:>10} \t\t{TimeNow:>10}\n")

def Try3():
    File = open("stdIDPreviousRequests.txt", "r")
    Requests = File.read()
    print(Requests)

previousRequestFeature()
Try()
Try1()
Try2()
Try3()