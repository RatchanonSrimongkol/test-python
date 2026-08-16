def find_pair_with_product(nums: list, target: int) -> list:
    for i in range(len(nums)):          # ตัวเลขตัวที่ 1
        for j in range(i + 1, len(nums)):   # ตัวเลขตัวที่ 2 (เริ่มถัดจาก i เสมอ)
            if nums[i] * nums[j] == target:
                return [nums[i], nums[j]]
    return []

print(find_pair_with_product([1, 2, 3, 4, 6], 6))    # [1, 6]
print(find_pair_with_product([2, 4, 5, 7], 14))      # [2, 7]
print(find_pair_with_product([3, 5, 9, 10], 25))     # []
print(find_pair_with_product([1, 2, 3, 4, 5], 20))   # [4, 5]