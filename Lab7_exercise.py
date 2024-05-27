def reverse_string(s):
   
    if len(s) <= 1:
        return s
    else:
      
        return reverse_string(s[1:]) + s[0]

print(reverse_string("Hi!"))  
print(reverse_string("Tenzin")) 
print(reverse_string(""))       
print(reverse_string("zm"))