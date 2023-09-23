
#include <iostream>
#include <vector>

// 2 pointers outside in, greedily iterate pointer w/ lower height

//     Time: O(n)
//     Space: O(1)

int maxArea(std::vector<int> &nums)
{
    int left = 0;
    int right = nums.size() - 1;
    int maxArea = 0;

    while (left < right)
    {
        int area = (right - left) * std::min(nums[left], nums[right]);

        maxArea = std::max(area, maxArea);

        if (nums[left] < nums[right])
            left++;
        else
            right--;
    }

    return maxArea;
}

int main(int argc, char const *argv[])
{
    std::vector<int> h1 = {1, 8, 6, 2, 5, 4, 8, 3, 7}; // 49
    std::vector<int> h2 = {1, 1};                      // 1

    std::cout << maxArea(h1) << std::endl;
    std::cout << maxArea(h2) << std::endl;

    return 0;
}
