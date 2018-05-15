import unittest
from main import calculate_next_state, INVALID_OP_STRING


class TestCalculateNextState(unittest.TestCase):

    def setUp(self):
        self.s = None

    def test_send_when_state_is_null_should_be_created(self):
        self.s = calculate_next_state(self.s, '1')
        self.assertNotEqual(self.s, None)

    def test_display_pressed_number_when_state_is_null(self):
        self.s = calculate_next_state(self.s, '1')
        self.assertEqual('1', self.s.display)

    def test_display_when_operator_is_pressed_after_a_number(self):
        self.s = calculate_next_state(self.s, '1')
        self.s = calculate_next_state(self.s, '+')
        self.assertEqual('1', self.s.display)

    def test_display_when_numer_operator_number_are_pressed(self):
        self.s = calculate_next_state(self.s, '1')
        self.s = calculate_next_state(self.s, '+')
        self.s = calculate_next_state(self.s, '3')
        self.assertEqual('3', self.s.display)

    def test_display_when_valid_calculation_is_performed(self):
        self.s = calculate_next_state(self.s, '1')
        self.s = calculate_next_state(self.s, '+')
        self.s = calculate_next_state(self.s, '3')
        self.s = calculate_next_state(self.s, '=')
        self.assertEqual('4', self.s.display)

    def test_display_when_2_valid_calculation_are_preformed(self):
        self.s = calculate_next_state(self.s, '1')
        self.s = calculate_next_state(self.s, '+')
        self.s = calculate_next_state(self.s, '3')
        self.s = calculate_next_state(self.s, '=')
        self.s = calculate_next_state(self.s, '-')
        self.s = calculate_next_state(self.s, '7')
        self.s = calculate_next_state(self.s, '=')
        self.assertEqual('-3', self.s.display)

    def test_display_when_number_operation_numer_operation_are_pressed_should_evaluate(self):
        self.s = calculate_next_state(self.s, '1')
        self.s = calculate_next_state(self.s, '+')
        self.s = calculate_next_state(self.s, '3')
        self.s = calculate_next_state(self.s, '-')
        self.s = calculate_next_state(self.s, '2')
        self.s = calculate_next_state(self.s, '=')
        self.assertEqual('2', self.s.display)

    def test_divide_by_zero_should_display_invalid_operation(self):
        self.s = calculate_next_state(self.s, '1')
        self.s = calculate_next_state(self.s, '/')
        self.s = calculate_next_state(self.s, '0')
        self.s = calculate_next_state(self.s, '=')
        self.assertEqual(INVALID_OP_STRING, self.s.display)

    def test_enter_operator_as_first_input_should_display_invalid_operation(self):
        self.s = calculate_next_state(self.s, '+')
        self.assertEqual(INVALID_OP_STRING, self.s.display)

    def test_enter_equal_as_first_input_should_display_invalid_operation(self):
        self.s = calculate_next_state(self.s, '=')
        self.assertEqual(INVALID_OP_STRING, self.s.display)

    def test_enter_2_operators_in_a_row_should_display_invalid_operation(self):
        self.s = calculate_next_state(self.s, '7')
        self.s = calculate_next_state(self.s, '+')
        self.s = calculate_next_state(self.s, '+')
        self.assertEqual(INVALID_OP_STRING, self.s.display)

    def test_enter_few_numbers_in_a_row_should_display_as_one(self):
        self.s = calculate_next_state(self.s, '1')
        self.s = calculate_next_state(self.s, '2')
        self.s = calculate_next_state(self.s, '3')
        self.assertEqual('123', self.s.display)

    def test_enter_number_then_equal_should_display_invalid_operation(self):
        self.s = calculate_next_state(self.s, '3')
        self.s = calculate_next_state(self.s, '=')
        self.assertEqual(INVALID_OP_STRING, self.s.display)

    def test_pressing_number_after_result_calculated_should_display_number(self):
        self.s = calculate_next_state(self.s, '1')
        self.s = calculate_next_state(self.s, '+')
        self.s = calculate_next_state(self.s, '3')
        self.s = calculate_next_state(self.s, '=')
        self.s = calculate_next_state(self.s, '8')
        self.assertEqual('8', self.s.display)

    def test_divide_2_numbers_should_return_float(self):
        self.s = calculate_next_state(self.s, '1')
        self.s = calculate_next_state(self.s, '+')
        self.s = calculate_next_state(self.s, '3')
        self.s = calculate_next_state(self.s, '=')
        self.s = calculate_next_state(self.s, '8')
        self.assertEqual('8', self.s.display)

    def test_send_invalid_character_should_display_invalid_operation(self):
        self.s = calculate_next_state(self.s, 'A')
        self.assertEqual(INVALID_OP_STRING, self.s.display)

    def test_send_nothing_should_display_invalid_operation(self):
        self.s = calculate_next_state(self.s, '')
        self.assertEqual(INVALID_OP_STRING, self.s.display)

    def test_send_braces_should_display_invalid_operation(self):
        self.s = calculate_next_state(self.s, '2')
        self.s = calculate_next_state(self.s, '(')
        self.assertEqual(INVALID_OP_STRING, self.s.display)

    def test_divide_should_return_fraction(self):
        self.s = calculate_next_state(self.s, '3')
        self.s = calculate_next_state(self.s, '/')
        self.s = calculate_next_state(self.s, '2')
        self.s = calculate_next_state(self.s, '=')
        self.assertEqual('1.5', self.s.display)

    def test_when_number_has_0_prefix(self):
        self.s = calculate_next_state(self.s, '00003')
        self.s = calculate_next_state(self.s, '-')
        self.s = calculate_next_state(self.s, '1')
        self.s = calculate_next_state(self.s, '=')
        self.assertEqual('2', self.s.display)
