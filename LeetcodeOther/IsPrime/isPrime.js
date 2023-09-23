
const isPrime = (n) => {
    // Time: O(sqrt(n))
    // Prime number must be greater than 1
    if (n <= 1)
        return false;

    // One factor of a prime number is at least less
    // than the square root of target
    for (let i = 2; i < Math.sqrt(n); i++) {
        // If a number can divide target, its not prime
        if (n % i === 0)
            return false;
    }
    return true;
}


const isPrime_2 = (n) => {
    // 1 or 0 aren't prime
    if (n <= 1)
        return false;

    // 2 and 3 are prime
    if (n === 2 || n === 3)
        return true;

    // If divisible by 2 or 3, not prime
    // Allows skipping of middle five numbers in loop
    if (n % 2 === 0 || n % 3 === 0)
        return false;

    // All primes except 2 and 3 can be represented by 6n+1 or 6n-1
    // Every increment is 6
    // Starting at 5 accounts for 6n-1, n % 1 checks 6n-1
    // n % (i+2) accounts for 6n+1
    for (let i = 5; i <= Math.sqrt(n); i += 6) {
        if (n % i === 0 || n % (i + 2) === 0)
            return false;
    }

    return true;
}

isPrime(11) ? console.log("true") : console.log("false");
isPrime(20) ? console.log("true") : console.log("false");
isPrime_2(11) ? console.log("true") : console.log("false");
