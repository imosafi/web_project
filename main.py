INVALID_OP_STRING = 'Invalid operation, reset.'

operators_dict = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b if b != 0 else exec('raise(Exception(\'can not divide by zero\'))')
}


class Calculator(object):
    def __init__(self, stack=[], is_operator_in_stack=False, is_stack_head_a_result=False, is_invalid_input=False):
        self.stack = stack
        self.display = ''
        self.is_operator_in_stack = is_operator_in_stack
        self.is_stack_head_a_result = is_stack_head_a_result
        self.is_invalid_input = is_invalid_input

    def update_display(self):
        if self.is_invalid_input:
            self.display = INVALID_OP_STRING
            self.__reset_json()
        else:
            display_string = ''
            for index, item in enumerate(self.stack):
                if item in operators_dict.keys() and not index == len(self.stack) - 1:
                    display_string = ''
                elif item not in operators_dict.keys():
                    display_string += item
            self.display = display_string

    def evaluate(self):
        a, b, operator = self.__extract_arguments()
        self.stack.clear()
        try:
            self.stack.append(str(operators_dict[operator](a, b)))
        except Exception:
            self.is_invalid_input = True

    def __reset_json(self):
        self.stack = []
        self.is_stack_head_a_result = False
        self.is_operator_in_stack = False
        self.is_invalid_input = False

    def __extract_arguments(self):
        a, b = '', ''
        operator = None
        for item in self.stack:
            if item in operators_dict.keys():
                operator = item
                break
            else:
                a = a + item
        for item in reversed(self.stack):
            if item in operators_dict.keys():
                break
            else:
                b = item + b
        return int(a), int(b), operator


def is_digit_or_fraction(input):
    if str.isdigit(input):
        return True
    else:
        values = input.split('/')
        return len(values) == 2 and all(i.isdigit() for i in values)


def calculate_next_state(json_state, input):
    if json_state is None and is_digit_or_fraction(input):
        stack = []
        stack.append(input)
        json_state = Calculator(stack)

    elif json_state is None and not is_digit_or_fraction(input):
        json_state = Calculator()
        json_state.is_invalid_input = True

    elif (not json_state.stack and not is_digit_or_fraction(input)) or\
            (len(json_state.stack) > 0 and not is_digit_or_fraction(json_state.stack[-1]) and not is_digit_or_fraction(input)):
        json_state.is_invalid_input = True

    elif (not is_digit_or_fraction(input) and not input in operators_dict and not input == '='):
        json_state.is_invalid_input = True

    elif is_digit_or_fraction(input) and not json_state.is_stack_head_a_result:
        json_state.stack.append(input)

    elif is_digit_or_fraction(input) and json_state.is_stack_head_a_result:
        json_state.stack.clear()
        json_state.stack.append(input)
        json_state.is_stack_head_a_result = False

    elif input in operators_dict.keys() and not json_state.is_operator_in_stack:
        json_state.stack.append(input)
        json_state.is_stack_head_a_result = False
        json_state.is_operator_in_stack = True

    elif input in operators_dict.keys() and json_state.is_operator_in_stack:
        json_state.evaluate()
        json_state.stack.append(input)

    elif input == '=' and not json_state.is_operator_in_stack:
        json_state.is_invalid_input = True

    elif input == '=':
        json_state.evaluate()
        json_state.is_stack_head_a_result = True
        json_state.is_operator_in_stack = False

    json_state.update_display()
    return json_state


def main():
    s = None

    # s = calculate_next_state(s, '+')
    # print(s.display)
    # s = calculate_next_state(s, '2')
    # print(s.display)
    # s = calculate_next_state(s, '+')
    # print(s.display)
    # s = calculate_next_state(s, '4')
    # print(s.display)
    # s = calculate_next_state(s, '3')
    # print(s.display)
    # s = calculate_next_state(s, '=')
    # print(s.display)
    # s = calculate_next_state(s, '+')
    # print(s.display)
    # s = calculate_next_state(s, '1')
    # print(s.display)
    # s = calculate_next_state(s, '=')
    # print(s.display)
    # s = calculate_next_state(s, '5')
    # print(s.display)
    # s = calculate_next_state(s, '/')
    # print(s.display)
    # s = calculate_next_state(s, '0')
    # print(s.display)
    # s = calculate_next_state(s, '=')
    # print(s.display)
    # s = calculate_next_state(s, '2')
    # print(s.display)
    # s = calculate_next_state(s, '+')
    # print(s.display)
    # s = calculate_next_state(s, '4')
    # print(s.display)
    # s = calculate_next_state(s, '3')
    # print(s.display)
    # s = calculate_next_state(s, '=')
    # print(s.display)

if __name__ == '__main__':
    main()