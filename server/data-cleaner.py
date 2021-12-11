import re
import csv
import pandas as pd

f= open("data-errors.txt",'r',encoding="utf8")

fc = f.read()

fcbRegex = re.compile(r"line(\s\d+)")

clear = re.findall(fcbRegex,fc)

for i in clear:
    print("lines",i)

arr=clear
print("array is",arr)

count = 1
reader = csv.reader(open('amazon_reviews_us_Watches_v1_00.tsv', 'r',encoding="utf8"), delimiter="\t")
writer = csv.writer(open('amazon_reviews_us_Watches_v1_00_clean.tsv', 'w',encoding="utf8"), delimiter="\t")
for row in reader:
    if count in arr:
        print("skipping ", count)
        count += 1
        continue
    else:
        print("writting ", count)
        writer.writerow(row)
        count += 1
    




