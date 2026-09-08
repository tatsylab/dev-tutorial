import unittest

from hello import repeat_message


class RepeatMessageTest(unittest.TestCase):
    def test_repeats_message(self) -> None:
        self.assertEqual(repeat_message("hello", 2), "hello\nhello")

    def test_rejects_non_positive_count(self) -> None:
        with self.assertRaises(ValueError):
            repeat_message("hello", 0)


if __name__ == "__main__":
    unittest.main()
