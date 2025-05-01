ln=int(input("Enter the largest number: "))
sm= int(input("Enter the smallest number:"))

while sm:
    store=sm
    sm=ln
    ln=store

print("HCF is:",ln)    