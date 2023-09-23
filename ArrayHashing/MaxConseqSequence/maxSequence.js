


const findMaxSequence = (nums)=> {
    const numSet = new Set(nums);
    
    let maxSeq = 0;
    for (let num of nums) {
        if (!numSet.has(num -1)) {
            let sequence = 1;
            while (numSet.has(sequence + num)) {
                sequence++;
            }
           maxSeq = Math.max(maxSeq, sequence);
        }
    }
    return maxSeq;
}

const nums = [100, 4, 200, 1, 3, 2];
const nums2 = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1];

console.log(findMaxSequence(nums))  // 4
console.log(findMaxSequence(nums2))  // 9