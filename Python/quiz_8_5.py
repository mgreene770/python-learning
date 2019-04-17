#fname = input("Enter file name: ")
fname = 'mbox-short.txt'
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
lst = list()

for line in fh:
    if line.startswith('From:'):
        count = count + 1
        splt = line.split()
        lst.append(splt[1])

for item in lst:
    print(item)
    
print("There were", count, "lines in the file with From as the first word")
