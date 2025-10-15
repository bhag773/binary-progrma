def toBinary(integer):
    while num != 0:
        output = []
    if integer % 2 == 1 :
        output.insert(0, "1")
    elif integer % 2 == 0:
        output.insert(0, "0")
        num = num // 2
    binaryString = " ".join(output) 
    return binaryString 
       
      






int_ = int(input("Enter a number between 1 and 255: "))

print(toBinary(int_))
