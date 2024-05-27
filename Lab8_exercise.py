def find_first_repeating_character(t):
   
    char_count = {}
    
    for char in t:
        if char in char_count:
           
            print(f"First repeating character: {char}")
            print(f"Memory address: {id(char)}")
            return char, id(char)
        else:
         
            char_count[char] = 1
    
  
    return None


result = find_first_repeating_character("happiness")
if result:
    char, address = result
    print(f"The first repeating character is '{char}' having memory address {address}.")
else:
    print("No repeating character found!")