
def lexi_order(nums):

    permutations = [nums]
    length = len(nums)

    while True:

        nums = list(nums)

        # find largest index i such that nums[i] < nums[i + 1]
        exists = False
        for j, elem in enumerate(nums):
            # check if last element
            if j == length - 1:
                break

            if elem < nums[j + 1]:
                i = j
                exists = True

        if not exists:
            break

        # find largest index k, such that i < k AND nums[i] < nums[k]
        for j in range(i + 1, length):
            if nums[j] > nums[i]:
                k = j

        # swap order of nums[i] and nums[k]
        nums[i], nums[k] = nums[k], nums[i]

        # reverse order of elements starting at position i+1
        to_reverse = nums[i+1:][::-1]
        nums[i+1::] = to_reverse

        permutations.append(nums)

    return permutations


if __name__ == '__main__':
    perms = lexi_order([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    print(perms[999999])
