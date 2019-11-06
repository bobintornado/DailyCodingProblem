def permute(array, permutation):
    for i in range(len(array)):
        p = permutation[i]
        j = i

        while p != j:
            array[j],array[p] = array[p],array[j]
            j = p
            p = permutation[p]
            permutation[j] = i      

    return array

print permute(["a", "b", "c"],[2, 1, 0])
print permute(["a", "b", "c", "d"], [3, 0, 2, 1])

# ['c', 'b', 'a']
# ['d', 'a', 'c', 'b']
