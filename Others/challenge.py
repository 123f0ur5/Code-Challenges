nums = [-1,-100,3,99]
k = 2

def rotate(nums, k):
    for _ in range(k):
        nums.insert(0, nums[len(nums)-1])
        nums.pop()
    
    return nums


print(rotate(nums, k))

k = ["test", "test", "test"]

def solution(k):
    dct = dict()
    ans = []


    for i in range(len(k)):
        letters = k[i]
        for letter in letters:
            if letter not in dct.keys():
                dct[letter] = 1
            else:
                dct[letter] += 1
            
            if dct[letter] == len(k):
                ans.append(letter)
                dct[letter] = 0
    
    return(sorted(ans))


print(solution(k))