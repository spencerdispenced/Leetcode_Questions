
const findPalindrome = (number) => {
    let remainder = 0;
    let reversed = 0;
    let temp = 0;

    temp = number;

    while (temp > 0) {
        remainder = temp % 10;
        reversed = (reversed * 10) + remainder;
        temp = Math.floor(temp / 10);
    }

    if (number === reversed) {
        console.log(`${number} is a Palindrome`);
    }

    else {
        console.log(`${number} is not a Palindrom`);
    }
}


findPalindrome(1331);
findPalindrome(4774);
findPalindrome(1234);
findPalindrome(47744774);