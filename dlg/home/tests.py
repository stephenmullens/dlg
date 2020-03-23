from django.test import TestCase, Client
from .utils import clean_number_list

import json


class IntegrationTestCase(TestCase):
    """
    A series of Integration test cases which utilize POST
    to access the API and verify the end result
    """
    def setUp(self):
        """
        Initialize Client
        """
        self.client = Client()

    def function_pass(self, numbers_list, http_response_code, total_expected):
        """
        Function to be used for tests which are expected to pass
        """
        c = self.client
        test_dict = {"numbers_to_add": numbers_list}
        # print(test_dict)
        response = c.post('/total',
                            test_dict,
                            format='json',
                            content_type='application/json')
        try:
            print(json.loads(response.content)["msg"])
        except:
            pass
        self.assertEqual(response.status_code,
                        http_response_code,
                        "Incorrect error code returned")
        self.assertEqual(response.json()['total'], total_expected)

    def function_exception(self, numbers_list, http_response_code):
        """
        Function to be used for tests which are expected to fail
        due to invalid lists
        """
        c = self.client
        test_dict = {'numbers_to_add': numbers_list}
        response = c.post('/total', test_dict, format='json')
        self.assertEqual(response.status_code, http_response_code)
        # print(test_dict)
        # print(json.loads(response.content)["msg"])

    def test_empty_list(self):
        """
        Empty list returns a 0 total
        """
        numbers_list = []
        http_response_code = 200
        total_expected = '0'
        self.function_pass(numbers_list, http_response_code, total_expected)

    def test_successful_lists(self):
        """
        Runs a number of basic tests and confirm success
        """
        numbers_list = list(range(10000001))
        http_response_code = 200
        total_expected = '50000005000000'
        self.function_pass(numbers_list, http_response_code, total_expected)

        numbers_list = [4]
        http_response_code = 200
        total_expected = '4'
        self.function_pass(numbers_list, http_response_code, total_expected)

        numbers_list = [0, 1, 2, 3, 4]
        http_response_code = 200
        total_expected = '10'
        self.function_pass(numbers_list, http_response_code, total_expected)

        numbers_list = ["0", "1", "2", "3", "4"]
        http_response_code = 200
        total_expected = '10'
        self.function_pass(numbers_list, http_response_code, total_expected)

        numbers_list = [0.25, 1.25, 2.25, 3.25, 4.25]
        http_response_code = 200
        total_expected = '11.25'
        self.function_pass(numbers_list, http_response_code, total_expected)

        numbers_list = [-0, 1, -2, 3, -4, -8]
        http_response_code = 200
        total_expected = '-10'
        self.function_pass(numbers_list, http_response_code, total_expected)

    def test_unsuccessful_lists(self):
        """
        Runs a number of basic tests to confirm error response
        """
        numbers_list = ["0a", 1, 2, 3, 4, 8]
        http_response_code = 400
        self.function_exception(numbers_list, http_response_code)

        numbers_list = ["0", 1, "2._", 3, 4, 8]
        http_response_code = 400
        self.function_exception(numbers_list, http_response_code)

        numbers_list = ['']
        http_response_code = 400
        self.function_exception(numbers_list, http_response_code)

    def test_incorrect_method(self):
        """
        API requires POST, send by GET instead
        Verify 405 error
        """
        c = self.client
        numbers_list = [0, 1, 2, 3, 4]
        test_dict = {'numbers_to_add': numbers_list}
        response = c.get('/total', test_dict, format='json')
        self.assertEqual(response.status_code, 405)

    def test_missing_post_field(self):
        """
        Do not send the numbers_to_add field and confirm error
        """
        c = self.client
        numbers_list = [0, 1, 2, 3, 4]
        test_dict = {'incorrect_field_name': numbers_list}
        response = c.post('/total', test_dict, format='json')
        self.assertEqual(response.status_code, 400)

    def test_non_list(self):
        """
        Send a single integer instead of a list
        """
        c = self.client
        numbers_list = 4
        test_dict = {'incorrect_field_name': numbers_list}
        response = c.post('/total', test_dict, format='json')
        self.assertEqual(response.status_code, 400)


class UnitTestCase(TestCase):
    """
    A series of Unit test cases which verify "clean_number_list"
    """
    def function_verify_cleaning(self, input_numbers_list, valid_numbers_list):
        """
        Function to be used for tests which are expected to pass
        """
        cleaned_list = clean_number_list(input_numbers_list)
        self.assertEqual(cleaned_list, valid_numbers_list, "List is incorrect")

    def function_verify_bad_input(self, input_numbers_list):
        """
        Function to be used for tests which are expected to return False
        """
        cleaned_list = clean_number_list(input_numbers_list)
        self.assertFalse(cleaned_list)

    def test_good_lists(self):
        """
        Verifies that good lists are simply cleaned
        """
        input_numbers_list = []
        valid_numbers_list = []
        self.function_verify_cleaning(input_numbers_list, valid_numbers_list)

        input_numbers_list = [1, 2, 3]
        valid_numbers_list = [1, 2, 3]
        self.function_verify_cleaning(input_numbers_list, valid_numbers_list)

        input_numbers_list = ["1", 2, 3]
        valid_numbers_list = [1, 2, 3]
        self.function_verify_cleaning(input_numbers_list, valid_numbers_list)

        input_numbers_list = ["1", 2.1, 3]
        valid_numbers_list = [1, 2.1, 3]
        self.function_verify_cleaning(input_numbers_list, valid_numbers_list)

    def test_bad_lists(self):
        """
        Verifies that bad lists return False
        """
        input_numbers_list = ["0a", 1, 2, 3, 4, 8]
        self.function_verify_bad_input(input_numbers_list)

        input_numbers_list = ["0", 1, "2._", 3, 4, 8]
        self.function_verify_bad_input(input_numbers_list)

        input_numbers_list = 4
        self.function_verify_bad_input(input_numbers_list)

        input_numbers_list = "5.6"
        self.function_verify_bad_input(input_numbers_list)


# TODO - Other things to consider
# Decimals, limits of ieee precision, edge cases
