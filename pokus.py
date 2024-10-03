# funkce, ktera do konzole vypise pozadovany pocet hvezdicek 
def five_stars(cislo):
    
    i = cislo
    
    while i <= 5:
        print("*")
        i += 1

# funkce, ktera overi zda je cislo v danem intervalu a vypise textovy vystup

def in_range(number, minimum, maximum):
    if minimum <= maximum:
        if (number > minimum and number < maximum):
         print("Number", number ,"in range")
        else:
         print("Number", number, "out of range")
    else:
     print("Value of min number exceeds the value of max number")

#funkce

def max2(a,b,c):
    if (a > b and a > c and):
        return a
    if (b > a and b > c):
        return b
    if (c > a and c > b):
        return c    
   
   
print(max2(1, 2, 3))

