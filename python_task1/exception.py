#exception handling
try:
    x = int(input("Enter number: "))
    print(10 / x)

except:
    print("Error occurred")

finally:
    print("Done")
