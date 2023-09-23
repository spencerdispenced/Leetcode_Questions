

const sumOfDigits = (number) => {
    let currentSum = 0;
    let temp = 0;

    while (number > 0) {
        temp = number % 10;
        currentSum += temp;
        number = Math.floor(number / 10);
    }

    return currentSum;
}

console.log(sumOfDigits(7865));