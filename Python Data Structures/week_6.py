# 10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.


name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
fh = open(name)



hours = []

for line in fh:
    if not line.startswith("From "): continue
    line.rstrip()
    hours.append(line.split()[5].split(":")[0])

counts = dict()

for hour in hours:
    counts[hour] = counts.get(hour, 0)+1


bcount = None
bword = None

for item, key in sorted(counts.items()):
    print item,key

