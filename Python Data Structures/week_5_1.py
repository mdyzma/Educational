# 9.4 Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
fh = open(name)

emails = []

for line in fh:
    if not line.startswith("From "): continue
    line.rstrip()
    emails.append(line.split()[1])

counts = dict()

for email in emails:
    counts[email] = counts.get(email, 0)+1


bcount = None
bword = None

for item, key in counts.items():
    if bcount is None or key>bcount:
        bcount = key
        bword = item


#x = max(counts, key=counts.get)

print bword, bcount
