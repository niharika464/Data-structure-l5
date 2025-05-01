number=int(input("Enter the number:"))

store=number
reverse=int(0)

while(number>0):
    rem=(number%10)
    reverse=reverse*10+rem
    number//=10

print("Reversed number is:", reverse)

if(store == reverse):
    print("\n no. is palindrome")
else:
    print("\n no. is not palindrome")