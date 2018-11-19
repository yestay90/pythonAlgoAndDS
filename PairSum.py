
def pair_sum(arr, k):

    if len(arr) < 2:
        return

    #sets for traking
    seen = set()
    output = set()

    #1,3,2,2
    for num in arr:

        target = k - num

        if target not in seen:
            seen.add(num)
        else:
            output.add((min(num, target), max(num, target)))

        # print('\n'.join(map(str, list(output))))
    return output