def main():
    n,k = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    
    charged = int(input())
    
    actual = sum(a[:k]+a[k+1:])//2
    
    if actual == charged:
        print("Bon Appetit")
    else:
        print(charged-actual)

main()
