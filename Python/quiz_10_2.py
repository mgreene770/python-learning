#name = input("Enter file:")
name = "mbox-short.txt"
if len(name) < 1 : name = "mbox-short.txt"
fh = open(name)
times = dict()

for line in fh:    
    if line.startswith('From'):        
        idx = line.find(':')        
        if idx > 4:
            time = line[idx-2:idx]
            times[time] = times.get(time, 0) + 1
            
for k, v in sorted( times.items()):
    print(k, v)

#print('Sorted Reverse:', sorted(times.items(), reverse=True))

