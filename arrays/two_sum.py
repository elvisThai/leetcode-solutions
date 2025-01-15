from typing import List, Optional

class Solution:
    def twoSum(self, nums: List[int], target: int) -> Optional[List[int]]:
        """
        Given an array of integers `nums` and a target integer `target`, 
        returns the indices of the two numbers such that they add up to the target.
        
        Args:
        nums: List[int] - List of integers
        target: int - Target sum
        
        Returns:
        List[int] - Indices of the two numbers that add up to target, or None if no such pair exists
        """
        #initialize dictionary to solve the problem
        dictionary = {}

        #iterate through the indexes and values of nums array with enumerate 
        for index, value in enumerate(nums):
            difference = target - value  #initialize difference as target - value
            #if we have difference in the dictionary, that means we found two numbers in the array that added equal to target
            if difference in dictionary:
                return [dictionary[difference], index] #simply return the index of the difference that was already inside the dict and our current index
      
            dictionary[value] = index #if we have not returned we have not yet found two sums for our target, so we can add our current value in the dict with its index
        
        return None #after exiting the loop that means we have not found any two sums for our target, so return None 
