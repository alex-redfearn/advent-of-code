# Day 7: Bridge Repair

Given a target number, a list of numbers and operators.
Check if the target number can be calculated by rearranging the operators.
e.g. all possible combinations of the numbers 1,2,3 and operators + and *.

The evaluation doesn't follow standard operator precedence. Equations are always evaluated left to right. Numbers can't be reordered only operators.

1 + 2
1 + 2 + 3
1 + 2 * 3
1 * 2
1 * 2 + 3
1 * 2 * 3

## Part 1

Input is a list of test cases. Each line has a target value and a list of numbers. Determine whether the target value can be acheived from any order of operators. For all matches, sum up the target values and return that result.

## Part 2

A new operator is introduced! The concatenation operator (||). This operator simply concatenates the numbers either side of it.
e.g. 6 * 8 || 6 * 15 evaluates as:
6 * 8 = 48
48 || 6 = 486
486 * 15 = 7290
Again, calculate if the target value can be achieved from the numbers and different operator orders. For all matches, sum up the target values and return that result.
