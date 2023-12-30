import random

# Making list to loop down and using alphabets at random, making it harder to trace
art = ['1','2','3','4','5','6','7','8','9','10','q','w','e','r','t','y','u','i','o','p','z','x','c','v','b','n','m','a','s','d','f','g','h','j','k','l','1','2','3','4','5','6','7','8','9','0','-','=','!','#','$','%','^','&','*','(',')','_','+','[',']','{','}', ';', ':', '?', '.', 'Z', 'A', 'Q', 'W', 'S', 'X', 'E', 'D', 'C', 'V', 'F', 'R', 'B', 'G', 'T', 'N', 'H', 'Y', 'M', 'J', 'U', 'I', 'K', 'L', 'O', 'P']

var = 0
# Let's jumble the list every time when it's run. This will make it harder to trace.
leng = int(len(art))
tar = []
while True:
    if var == 83:
        break
    else:
        mat = random.randint(0,leng-1)
        num = art[mat]
        tar.append(num)
        var = var + 1

# Done, now using 10 random letters
passwords = ""
d = 0 
while True :
    if d == 20:
        break
    else:
        rint = random.randint(0,10)
        char = tar[rint]
        passwords = passwords + char
        d = d + 1

print(passwords)
