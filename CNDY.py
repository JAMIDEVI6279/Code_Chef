# cook your dish here
for _ in range(int(input())):
    n = int(input())
    A = list(map(int, input().split()))
    
    # Create a dictionary to store the frequency of each number in A
    freq = {}
    for num in A:
        freq[num] = freq.get(num, 0) + 1
    
    # Check if the frequency of each number is at most 2
    valid = all(count <= 2 for count in freq.values())
    
    if valid:
        print("Yes")
    else:
        print("No")
