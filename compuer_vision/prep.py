# Problem 1 two sum modified
def twosum(nums: list[int], target: int) -> list[int]:
    d = {}
    for i, elei in enumerate(nums):
        r = target - elei
        if r in d:
            return [d[r], i], d
        d[elei] = i 

print(twosum([2,11,15,7], 9))