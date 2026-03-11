total = 0

while True:
    number_input = input("Enter a number (0 to stop): ")
    number = int(number_input)  
    
    if number == 0:
        break  
    
    total += number  

print("Final sum:", total)