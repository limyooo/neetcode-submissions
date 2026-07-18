class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product = nums[0]
        min_product = nums[0]
        global_product = nums[0]
        for num in nums[1:]:
            curr_product = max_product
            max_product = max(num, curr_product * num, min_product * num )
            min_product = min(num, curr_product * num ,min_product * num)
            global_product = max(max_product,global_product)
        return global_product