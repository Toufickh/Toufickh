
fringo = False
marra = 1

while fringo == False and marra < 4: 
  print("Please select one of the following formulas to do: \n")
  print("1: Add two numbers \n")
  print("2: Check if a number is odd or even \n")
  print("3: Reverse a number \n")
  vari = int (input("Value: "))
  print("\n")

  if vari == 1:
    x = int (input("Enter the first number \n" ))
    y = int (input("Enter the second number \n"))
    sum = sum([x,y])
    print("Sum of", x, "and", y, "is", sum)
    fringo = True
  elif vari == 2:
    x = int (input("Enter the number that you want to check \n" ))
    if x % 2 ==0:
      print("Number is Even")
      fringo = True
    else:
      print("Number is Odd")
      fringo = True
  elif vari == 3:
    bromo = int(input("Please input the number to rotate: "))
    baram = 0
    while (bromo > 0):
      remainder = bromo % 10
      baram = (baram * 10) + remainder
      bromo = bromo // 10
    print("The reversed number is:", baram)
    print("\n")
    fringo = True
  else:
    print("This input is not acceptable \n")
    fringo = False
    marra = marra +1
    if marra == 4:
      print("You have exceeded the number of retries, the program will exit now!\n")         
