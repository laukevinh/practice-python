import unittest

from decorator.decorator import (do_twice, generic_greeting,
                                 do_twice_with_args, personal_greeting,
                                 greet_twice, greet_twice_by_name,
                                 greet_by_name_with_header)

class TestDecorator(unittest.TestCase):

    def test_do_twice(self):
        function = do_twice(generic_greeting)
        output = function()
        expected = ('Hello world!', 'Hello world!')
        self.assertEqual(output, expected)

    def test_do_twice_with_args(self):
        function = do_twice_with_args(personal_greeting)
        output = function("Kevin")
        expected = ('Hello Kevin!', 'Hello Kevin!')
        self.assertEqual(output, expected)

    def test_greet_twice(self):
        expected = ("This uses the `do_twice` decorator.",
                    "This uses the `do_twice` decorator.")
        self.assertEqual(greet_twice(), expected)

    def test_greet_twice_by_name(self):
        expected = ("Kevin, this uses the `do_twice_with_args` decorator",
                    "Kevin, this uses the `do_twice_with_args` decorator")
        self.assertEqual(greet_twice_by_name("Kevin"), expected)

    def test_greet_by_name_with_header(self):
        expected = ("This is a header",
                    "Kevin, this uses the `header` decorator")
        self.assertEqual(greet_by_name_with_header("Kevin"), expected)
