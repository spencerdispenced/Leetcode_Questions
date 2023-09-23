#include <iostream>
#include <vector>
#include <unordered_set>
using namespace std;

bool containsDuplicate(vector<int> &nums)
{
    unordered_set<int> s;

    for (int i = 0; i < nums.size(); i++)
    {
        if (s.find(nums[i]) != s.end())
        {
            return true;
        }
        s.insert(nums[i]);
    }

    return false;
}

int main()
{
    vector<int> test1{1, 2, 3, 1};
    vector<int> test2{1, 2, 3, 4};
    cout << containsDuplicate(test1) << endl;
    cout << containsDuplicate(test2) << endl;
}