def find_two_sum(List, target):
    size = len(List)
    for i in range(size):
        for j in range(i + 1, size): # all the + 1 means is that it does not start at the same index
            if List[i] + List[j] == target:
                return (i, j)
    return None

# Example usage
List = [2, 7, 11, 15]
target = 17
result = find_two_sum(List, target)
if result:
    print(f"Indices: {result[0]}, {result[1]}")
    print(f"Numbers: {List[result[0]]}, {List[result[1]]}")
else:
    print("No two sum solution found")
