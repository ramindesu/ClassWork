// let number_1 = +prompt("Please enter your first number");
// let operator = prompt("Also select an operator (-, +, *, /)");
// let number_2 = +prompt("Enter the second number");

// function calculate(number_1, operator, number_2) {
//   if (operator == "+") {
//     add(number_1, number_2);
//   } else if (operator == "-") {
//     sub(number_1, number_2);
//   } else if (operator == "*") {
//     multiply(number_1, number_2);
//   } else if (operator == "/") {
//     division(number_1, number_2);
//   } else {
//     console.log("Invalid operator!");
//   }
// }

// function add(number_1, number_2) {
//   console.log(number_1 + number_2);
// }
// function sub(number_1, number_2) {
//   console.log(number_1 - number_2);
// }
// function multiply(number_1, number_2) {
//   console.log(number_1 * number_2);
// }
// function division(number_1, number_2) {
//   if (number_2 == 0) {
//     console.log("Can't divide by zero");
//   } else {
//     console.log(number_1 / number_2);
//   }
// }

// calculate(number_1, operator,number_2);

// question number 2
let numbers = +prompt("please enter a number");
let sum = 0;
if (numbers < 1) {
  console.log("u need a postive number");
} else {
  for (let i = 0; i < numbers; i++) {
    sum += i
  }
  console.log(sum)
}
