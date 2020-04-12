
score = float(input("Enter Score: "))
if score < 1 and score > 0:
    if score >= 0.9:
            print('A')
    elif score >= 0.8:
        print('B')
    elif score >= 0.7:
        print('C')
    elif score >= 0.6:
        print('D')
    else:
        print('F')
else:
    print('Value of score is out of range.')


largest = None
smallest = None


while True:
    num = input("Enter a number: ")
    if num == "done" : break
    try:
    	num = int(num)
    except:
        print('Invalid input')
        continue
    if largest is None:
        largest = num
    elif num > largest:
        largest = num
    elif smallest is None:
        smallest = num
    elif num < smallest:
        smallest = num
    #print(num)

print("Maximum is", largest)
print('Minimum is', smallest)




def computepay(h,r):
    if h <= 40:
    	pay = h * r
    else:
    	h1 = h - 40
    	pay = 40 * r + h1 *(r * 1.5)
    return pay

hrs = input("Enter Hours:")
rate = input('Enter Rate:')

h = float(hrs)
r = float(rate)

p = computepay(h,r)
print("Pay",p)
