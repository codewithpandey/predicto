import re
import csv
import pandas as pd

f= open("data-errors.txt",'r')

fc = f.read()

fcbRegex = re.compile(r"line(\s\d+)")

clear = re.findall(fcbRegex,fc)

# cl = open("clean.txt",'w')

# clflag = cl.write("\n".join(clear))

for i in clear:
    print("lines",i)

arr=clear
print("array is",arr)

# with open("amazon_reviews_us_Watches_v1_00.tsv") as file:
#     tsv_file = csv.reader(file, delimiter="\t")
count = 1
reader = csv.reader(open('amazon_reviews_us_Watches_v1_00.tsv', 'r'), delimiter="\t")
writer = csv.writer(open('amazon_reviews_us_Watches_v1_00_clean.tsv', 'w'), delimiter="\t")
for row in reader:
    #  row1 = reader.next()
    if count in arr:
        print("skipping ", count)
        count += 1
        continue
    else:
        print("writting ", count)
        writer.writerow(row)
        count += 1
    # for line in tsv_file:
    #     if count in arr:
    #         continue
    #     count += 1
        
    #     newfile =open("clean.tsv",'w')

    #     newfileflag = newfile.write("\n".join(line))

     
        
    #    print(line)
    




