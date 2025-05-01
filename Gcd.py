#program to find HCF/GCD

#using Eucliden Algorithms
def hcf(numberSmallest,numberLargest):
    while(numberSmallest):
        numberStore=numberSmallest
        numberSmallest = numberLargest % numberSmallest
        numberLargest = numberStore
        return numberLargest
    
# Enter 2 numbers
numberLargest = int(input("Enter the largest number: "))
numberSmallest = int(input("Enter the smallest number: "))

# LCM equal products of numbers divide hcf of the numbers
lcm = int((numberSmallest / hcf(numberSmallest,numberLargest)) * numberLargest)
print("LCM is:",lcm)
