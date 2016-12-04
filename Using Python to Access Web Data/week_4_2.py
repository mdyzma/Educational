# Welcome Michal Dyzma from Using Python to Access Web Data

# Your current grade on this assignment is: 100%

# Following Links in Python

# In this assignment you will write a Python program that expands on http://www.pythonlearn.com/code/urllinks.py. The program will use urllib to read the HTML from the data files below, extract the href= vaues from the anchor tags, scan for a tag that is in a particular position relative to the first name in the list, follow that link and repeat the process a number of times and report the last name you find.

# We provide two files for this assignment. One is a sample file where we give you the name for your testing and the other is the actual data you need to process for the assignment

# Sample problem: Start at http://python-data.dr-chuck.net/known_by_Fikret.html 
# Find the link at position 3 (the first name is 1). Follow that link. Repeat this process 4 times. The answer is the last name that you retrieve.
# Sequence of names: Fikret Montgomery Mhairade Butchi Anayah 
# Last name in sequence: Anayah
# Actual problem: Start at: http://python-data.dr-chuck.net/known_by_Jennie.html 
# Find the link at position 18 (the first name is 1). Follow that link. Repeat this process 7 times. The answer is the last name that you retrieve.
# Hint: The first character of the name of the last page that you will load is: O
# Strategy
# The web pages tweak the height between the links and hide the page after a few seconds to make it difficult for you to do the assignment without writing a Python program. But frankly with a little effort and patience you can overcome these attempts to make it a little harder to complete the assignment without writing a Python program. But that is not the point. The point is to write a clever Python program to solve the program.

# Sample execution

# Here is a sample execution of a solution:

# $ python solution.py 
# Enter URL: http://python-data.dr-chuck.net/known_by_Fikret.html
# Enter count: 4
# Enter position: 3
# Retrieving: http://python-data.dr-chuck.net/known_by_Fikret.html
# Retrieving: http://python-data.dr-chuck.net/known_by_Montgomery.html
# Retrieving: http://python-data.dr-chuck.net/known_by_Mhairade.html
# Retrieving: http://python-data.dr-chuck.net/known_by_Butchi.html
# Retrieving: http://python-data.dr-chuck.net/known_by_Anayah.html
# The answer to the assignment for this execution is "Anayah".


# Imports
# ---------------------------------------
import urllib
import BeautifulSoup as bs
# ---------------------------------------

# Main page processing
# ---------------------------------------
url = raw_input('Enter URL: ')
count = int(raw_input('Enter count: '))
position = int(raw_input('Enter position: '))
# ---------------------------------------

myposition = int(position)-1
mycount = int(count)+1



# Links processing
names=list()
for i in range(int(mycount)):
    
    print "Retrieving: {}".format(url)
    html = urllib.urlopen(url).read()
    soup = bs.BeautifulSoup(html)
    tags = soup('a')
    tag = tags[myposition]
    names.append(tag.text)
    url = tags[myposition].get('href', None)


print names[-2]

