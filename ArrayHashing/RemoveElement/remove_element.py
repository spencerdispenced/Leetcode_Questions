
# https://leetcode.com/problems/remove-element/description/


# elements may be changed. Then return the number of elements in nums which are not equal to val.

# Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

#     Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
#     Return k.



def removeElement(self, nums: list[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k +=1
        return k


if __name__ == '__main__':
    nums = [3,2,2,3]
    val = 3
    print(removeElement(nums, val)) # 2, nums = [2,2,_,_]

    nums2 = [0,1,2,2,3,0,4,2]
    val2 = 2
    print(removeElement(nums2, val2))  # 5, nums = [0,1,4,0,3,_,_,_]