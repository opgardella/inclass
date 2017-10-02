import re

values = []
with open("mbox-short.txt",'r') as data:
    for line in data:
        if re.findall('X-DSPAM-Confidence:', line):
            #print (line)
            values.append(re.findall((":(.\S+)"), line))

print (values)
print ("Number of values:" + str(len(values)))
print ("Maximum:" + str(max(values)[0]))
print ("Minimum:" + str(min(values)[0]))
