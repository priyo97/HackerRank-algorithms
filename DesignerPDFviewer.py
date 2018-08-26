def main():
    alphabet = [int(x) for x in input().split()]
    word = input()
    
    max = 0
    
    for s in word:
        h = alphabet[ord(s) - 97]
        if h > max:
            max = h
    
    print(max*len(word))
    
main()
