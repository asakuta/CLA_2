import math
import sys

def analyse():
    if len(sys.argv) > 1:
        File=sys.argv[1]
        handle=open(File, "r")
        text=handle.read()
        handle.close()
        lines=text.split("\n")
        categories=lines[0].split(",")
        nameColumn=0
        salColumn=0
        curColumn=0
        for x in range(0, len(categories)):
            if categories[x] == "Name":
                nameColumn=x
            if categories[x] == "Salary":
                salColumn=x
            if categories[x] == "Currency":
                curColumn=x
        firstLine=lines[1].split(",")
        salGBP=int(firstLine[salColumn])
        if firstLine[curColumn] != "GBP":
            value=salGBP
            rate=firstLine[curColumn]
            salGBP=convert(value, rate)
        winner=[{"name": firstLine[nameColumn], "salary": firstLine[salColumn], "GBP": salGBP}]
        for y in range(2, len(lines)-1):
            newLine=lines[y].split(",")
            salGBP=int(newLine[salColumn])
            name=newLine[nameColumn]
            if newLine[curColumn] != "GBP":
                value=salGBP
                rate=newLine[curColumn]
                salGBP=convert(value, rate)
            if salGBP > winner[0]["GBP"]:
                winner=[{"name": name, "salary": newLine[salColumn], "GBP": salGBP}]
            else:
                if salGBP == winner[0]["GBP"]:
                    winner.insert(len(winner), {"name": name, "salary": newLine[salColumn], "GBP": salGBP})
        print(winner)
    else:
        print("nope")

def convert(salary, rate):
    rates={"USD": 1.38, "JPY": 150.16, "HUF": 428.43} #as of 08.03.2021
    newSalary=salary/rates[rate]
    return(newSalary)

analyse()