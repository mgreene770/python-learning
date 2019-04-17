largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" :
        break

    try :
        n = int(num)
    except:
        print('Invalid Input')
        continue

    if largest is None:
        largest = n
    elif n > largest:
        largest = n
    
    if smallest is None:
        smallest = n
    elif n < smallest:
        smallest = n
    

print("Maximum", largest)
print("Minimum", smallest)

##smallest = None
##value = 5
##
##if smallest is None :
##     smallest = value
##
##print(smallest, value)

##smallest_so_far = -1
##for the_num in [9, 41, 12, 3, 74, 15] :
##   if the_num < smallest_so_far :
##      smallest_so_far = the_num
##print(smallest_so_far)

##tot = 0 
##for i in [5, 4, 3, 2, 1] :
##    tot = tot + 1
##print(tot)

##def computepay(h,r):
##    if h <= 40:
##        pay = h * r
##    else:
##        pay = 40 * r
##        pay = pay + ((h - 40) * (r * 1.5))
##
##    return pay
##
##hrs = input("Enter Hours:")
##rate = input("Enter Pay:")
##p = computepay(float(hrs),float(rate))
##print("Pay",p)

##############################

##hrs = input("Enter Hours:")
##rate = input("Enter Rate:")
##
##h = float(hrs)
##r = float(rate)
##
##if h <= 40:
##    pay = h * r
##else:
##    pay = 40 * r
##    pay = pay + ((h - 40) * (r * 1.5))
##
##print (pay)
##

##############################
##score = input("Enter Score:")
##s = float(score)
##
##if s < 0.0:
##    print("Value out of range", s)
##elif s > 1.0:
##    print("Value out of range", s)
##elif s >= 0.9:
##    print("A")
##elif s >= 0.8:
##    print("B")
##elif s >= 0.7:
##    print ("C")
##elif s >= 0.6:
##    print("D")
##else:
##    print ("F")


    
