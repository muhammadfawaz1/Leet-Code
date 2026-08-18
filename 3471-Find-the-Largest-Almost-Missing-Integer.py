class Solution(object):
    def largestInteger(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if (k==len(nums)):
            max=nums[0]
            for i in nums[1:]:
                if (max<i):
                    max=i
            return max

        
        
        if (k > 1):
            num1 = nums[0]
            num2 = nums[-1]

            # Check if num1 or num2 appear anywhere else in the list
            num1_valid = (num1 not in nums[1:])
            num2_valid = (num2 not in nums[:-1])

            if num1_valid and num2_valid:
                if num1 > num2:
                    return num1
                else:
                    return num2
            elif num1_valid:
                return num1
            elif num2_valid:
                return num2
            else:
                return -1

        


        else:
            max = -1
            for i in nums:
                if (max==i):
                    max=-1
                else:
                    if (nums.count(i) == 1):
                        if (max < i):
                            max = i
            
            return max

        
    
        