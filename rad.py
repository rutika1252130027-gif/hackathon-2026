from collections import Counter

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    freq = Counter(a)
    
    # Check 0 operations
    if len(freq) == 1:
        print(0)
        return
    
    # Check 1 operation
    candidates = set()
    for x, f in freq.items():
        candidates.add(x)
        candidates.add(f)
    
    for T in candidates:
        valid = True
        for x in freq:
            if x != T and freq[x] != T:
                valid = False
                break
        if valid:
            print(1)
            return
    
    print(2)

solve()