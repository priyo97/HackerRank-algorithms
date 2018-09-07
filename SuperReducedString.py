def main():
    
    s = list(input())
    
    while True:

        n = len(s)    
        i = 1
        while i < n:
            if s[i] == s[i-1]:
                s.pop(i)
                s.pop(i-1)
                break
            i += 1
        else:
            if not s:
                print("Empty String")
            else:
                print("".join(s))
            break
                     
main()
