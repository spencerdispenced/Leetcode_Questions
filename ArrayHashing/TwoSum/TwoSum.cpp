#include <iostream>
#include <vector>
#include <unordered_map>

std::vector<int> twoSum(std::vector<int> &nums, int target)
{
    std::unordered_map<int, int> map;
    std::vector<int> result;

    for (int i = 0; i < nums.size(); i++)
    {
        int diff = target - nums[i];

        if (map.find(diff) != map.end())
        {
            result.push_back(map[diff]);
            result.push_back(i);
            return result;
        }

        else
        {
            map.insert({nums[i], i});
        }
    }

    return {-1, -1};
}

std::ostream &operator<<(std::ostream &os, const std::vector<int> &input)
{
    os << "[ ";
    for (auto const &i : input)
    {
        os << i << " ";
    }

    os << "]";

    return os;
}

int main(int argc, char *argv[])
{
    std::vector<int> arr1 = {10, 7, 2, 15, 1};
    std::vector<int> arr2 = {2, 5, 5, 1};

    std::cout << twoSum(arr1, 17) << std::endl;
    std::cout << twoSum(arr1, 9) << std::endl;
    std::cout << twoSum(arr1, 25) << std::endl;
    std::cout << twoSum(arr1, 16) << std::endl;
    std::cout << twoSum(arr1, 100) << std::endl;
    std::cout << twoSum(arr2, 10) << std::endl;
}