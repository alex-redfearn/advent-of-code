class Equation:

    @staticmethod
    def is_any_match(target, numbers, operators):
        return Equation.__is_any_match(target, numbers, operators, numbers[0])

    @staticmethod
    def __is_any_match(target, numbers, operators, current_value, index=0):
        if index == len(numbers) - 1:
            return current_value == target

        for operator in operators:
            next_expression = f"{current_value} {operator} {numbers[index + 1]}"

            # This is a concatenation operator e.g. 6 * 8 || 6 * 15 evaluates as:
            # 6 * 8 = 48
            # 48 || 6 = 486
            # 486 * 15 = 7290
            if operator == "||":
                next_value = int(f"{current_value}{numbers[index + 1]}")
            else:
                # Operators are always evaluated left to right, that is why we sum here rather than at the end.
                next_value = eval(next_expression)

            if Equation.__is_any_match(
                target, numbers, operators, next_value, index + 1
            ):
                return True

        return False


# How recursion can be used to cycle through all possible combinations.

# def simple_recursive_example(numbers, operators, current_value, index=0):
#     if index == len(numbers) - 1:
#         return

#     for operator in operator:
#         next_expression = f"{current_value} {operator} {numbers[index + 1]}"

#         simple_recursive_example(numbers, operators, next_expression, index + 1)

# first call, first loop

# next_expression, 1 + 2

# second call (recursive), first loop
# next_expression, 1 + 2 + 3

# second call (recursive), second loop
# next_expression, 1 + 2 * 3

# first call, second loop
# next_expression, 1 * 2

# third call (recursive)
# next_expression, 1 * 2 + 3

# third call (recursive), second loop
# next_expression, 1 * 2 * 3

# returns to first call and exits
