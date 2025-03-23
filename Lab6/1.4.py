import time

x = int(input("Enter a number: "))
mms = int(input("Enter milliseconds: "))
time.sleep(mms / 1000)

print("Square root of", x,  "after", mms, "milliseconds is", pow(x, 0.5))