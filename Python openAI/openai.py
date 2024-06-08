
print ("Please select one of the following formulas to do: \n")
print("1: Add two numbers \n")
print("2: odd or even numbers \n")
vari = int (input(" Value: \n"))

if vari == 1:
  x = int (input("Enter the first number \n" ))
  y = int (input("Enter the second number \n"))
  sum = sum([x,y])
  print("Sum of", x, "and", y, "is", sum)
elif vari == 2:
  x = int (input("Enter the number that you want to Check \n" ))
  if x % 2 ==0:
    print("Number is Even")
  else:
    print("Number is Odd")