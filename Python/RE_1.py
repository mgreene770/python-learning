import re
#name = input("Enter file:")
name = "mbox-short.txt"
if len(name) < 1 : name = "mbox-short.txt"
fh = open(name)
times = dict()

for line in fh:    
    line = line.rstrip()
    if re.search('^From:', line):
        print(line)

# dot (.) = wildcard, any character
# asterisk = 0 or more

# ^X-\S+:
# starts-with X-, /S = any non-whitespace characters, + = 1+ times, followed by a colon at the end
