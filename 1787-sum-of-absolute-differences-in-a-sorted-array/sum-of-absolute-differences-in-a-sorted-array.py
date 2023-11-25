class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        ## solution = | nums[i] * previous_n - sum_previous_n | +
        ##            | nums[i] * after_n - sum_after_n |

        # prefix sum
        prefix = [0]
        for i in range(1, len(nums)):
            prefix.append(prefix[i-1] + nums[i-1])
        
        res = []
        n = len(nums)
        total_sum = sum(nums)
        for i, x in enumerate(nums):
            b = abs(nums[i] * (i) - prefix[i])
            a = abs(nums[i] * (n-i-1) - (total_sum - prefix[i]- nums[i] ) )
            # print(x, b, a)
            res.append(b + a)
        # print(prefix)
        return res