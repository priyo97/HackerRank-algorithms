def main():
    
    n = int(input())
    s = input()
    k = int(input())
    
    for i in s:
        if "a" <= i <= "z":
            c = ord(i) - ord("a")
            c = ((c + k) % 26) + ord("a")
            print(chr(c),end="")
            
        elif"A" <= i <= "Z":
            c = ord(i) - ord("A")
            c = ((c + k) % 26) + ord("A")
            print(chr(c),end="")
        else:
            print(i,end="")
            
main()
            
            
