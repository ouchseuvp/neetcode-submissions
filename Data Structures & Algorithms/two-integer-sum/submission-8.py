class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i=0
        result=[]
        for x in nums:
            qwe = target - x
            print(qwe)
            if qwe in nums[i+1:]:
                print("в списке")
                result.append(i)
                result.append(nums.index(qwe, i+1))
                

            if len(result) >=2:
                if nums[result[0]]+nums[result[1]] == target:
                    return result
            i+=1