


function longestRepeat(s, k) {

    // Runtime 103ms Beats 48.27% Memory 42.7MB Beats 54.29%

    let left = 0;
    let longestRepeat = 0;
    const counts = new Array(26).fill(0);

    for (let right = 0; right < s.length; right++) {

        const rightIdx = s[right].charCodeAt(0) - 'A'.charCodeAt(0);
        counts[rightIdx]++;
        
        if ( (right - left + 1) - Math.max.apply(null, counts) > k) {
            const leftidx = s[left].charCodeAt(0) - 'A'.charCodeAt(0);
            counts[leftidx]--;
            left++;
        }

        longestRepeat = Math.max(longestRepeat, right - left + 1);
    }

    return longestRepeat;
}


function longestRepeatOptimized(s, k) {

    // Runtime 76ms Beats 92.85% Memory 42.5MB Beats 73.72%


    let left = 0;
    let longestRepeat = 0;
    const counts = new Array(26).fill(0);
    let maxFreq = 0;

    for (let right = 0; right < s.length; right++) {

        const rightIdx = s[right].charCodeAt(0) - 'A'.charCodeAt(0);
        counts[rightIdx]++;

        maxFreq = Math.max(maxFreq, counts[rightIdx]);
        
        if ( (right - left + 1) - maxFreq > k) {
            const leftidx = s[left].charCodeAt(0) - 'A'.charCodeAt(0);
            counts[leftidx]--;
            left++;
        }

        longestRepeat = Math.max(longestRepeat, right - left + 1);
    }

    return longestRepeat;
}


const s1 = "ABAB"
const k1 = 2  // 4

const s2 = "AABABBA"
const k2 = 1  // 4

const s3 = "ABABBA"
const k3 = 2  // 5

console.log(longestRepeat(s1, k1))  // 4
console.log(longestRepeat(s2, k2))  // 4
console.log(longestRepeat(s3, k3))  // 5

console.log(longestRepeatOptimized(s1, k1))  // 4
console.log(longestRepeatOptimized(s2, k2))  // 4
console.log(longestRepeatOptimized(s3, k3))  // 5