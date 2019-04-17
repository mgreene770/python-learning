#name = input("Enter file:")
name = "mbox-short.txt"
if len(name) < 1 : name = "mbox-short.txt"
names = dict()
fh = open(name)
max_count = 0
max_name = ''

for line in fh:
    if line.startswith('From:'):
        splt = line.split()
        email = splt[1]
        names[email] = names.get(email, 0) + 1

##for key in names:
##    if names[key] > max_count:    
##        max_count = names[key]
##        max_name = key

for k,v in names.items():
    if v > max_count:
        max_count= v
        max_name = k
print (max_name, names[max_name])

print(sorted( [ (v, k) for k, v in names.items() ]))

