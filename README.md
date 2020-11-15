# URLCheck

# Note
Shitty Code. Made it for personal Use(testing). Might break. Might give Errors. Might not work. 

# Description
Checking URL Response Codes to see if Domain is Live, Responding and is in Prod.   

# Usage
`python3 -f <file-with-URLs/Domains> -t <No. of Threads(Default=2)>` 

# Concept and Output
1. Checks if the Response Code for the given URL is 200.
2. Then appends `/zz11(random stuff)` to the URL and checks if the response code is still 200.
3. If both the response codes are 200 OK, domain is most likely Dead or Non-Prod. (Note: Could be throwing Custom errors with 200 OK responses as well)
4. Saves all the Dead ones to Dead-Domains.txt and the Live ones to Live-Domains.txt
