
#include <iostream>
#include <vector>

int trapWater(std::vector<int> &height)
{
    int left = 0;
    int right = height.size() - 1;
    int total = 0;
    int leftMax = height[left];
    int rightMax = height[right];

    while (left < right)
    {
        if (leftMax <= rightMax)
        {
            left++;
            leftMax = std::max(leftMax, height[left]);
            total += leftMax - height[left];
        }

        else
        {
            right--;
            rightMax = std::max(rightMax, height[right]);
            total += rightMax - height[right];
        }
    }

    return total;
}

int main(int argc, char const *argv[])
{
    std::vector<int> h1 = {0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1}; // 6
    std::vector<int> h2 = {4, 2, 0, 3, 2, 5};                   // 9

    std::cout << trapWater(h1) << std::endl;
    std::cout << trapWater(h2) << std::endl;

    return 0;
}
