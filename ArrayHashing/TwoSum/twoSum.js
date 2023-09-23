
const twoSum = (nums, target) => {
    const map = new Map();

    for (let i = 0; i < nums.length; i++) {
        const num = nums[i];
        const diff = target - num;

        if (map.has(diff)) {
            return [map.get(diff), i]
        }

        else {
            map.set(num, i);
        }
    }

    return [-1, -1];
}




const arr1 = [10, 7, 2, 15, 1]
const arr2 = [2, 5, 5, 1]


console.log(twoSum(arr1, 17)) // [0, 1]
console.log(twoSum(arr1, 9))  // [1, 2]
console.log(twoSum(arr1, 25))  // [0, 3]
console.log(twoSum(arr1, 16))  // [3, 4]
console.log(twoSum(arr1, 100))  // [-1, -1]
console.log(twoSum(arr2, 10))  // [ 1, 2]