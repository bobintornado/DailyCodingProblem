def permute(array, permutation):
    for i in range(len(array)):
        p = permutation[i]
        j = i

        # stop when (use and since both must hold for the loop)
        # 1. p is -1, means it has been settled before or
        # 2. p is original i, means the loop has closed
        while p != -1 and p != i:
            # swap
            array[j],array[p] = array[p],array[j]
            # permutation[j] is good 
            permutation[j] = -1
            # prepare for next swap
            j = p
            # next p 
            p = permutation[p]

        # end loop fix
        permutation[j] = -1

    return array

print permute(["a", "b", "c"],[2, 1, 0])
print permute(["a", "b", "c", "d"], [3, 0, 2, 1])
print permute(["a", "b", "c", "d", "e"], [4, 3, 2, 0, 1])

# ['c', 'b', 'a']
# ['d', 'a', 'c', 'b']
# ['e', 'd', 'c', 'a', 'b']
