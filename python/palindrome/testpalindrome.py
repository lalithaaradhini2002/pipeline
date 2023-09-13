import unittest
from palindrome import is_palindrome

class TestIsPalindrome(unittest.TestCase):

    def test_palindrome(self):
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome("A man, a plan, a canal, Panama"))
        self.assertTrue(is_palindrome("Was it a car or a cat I saw?"))
        self.assertTrue(is_palindrome("No lemon, no melon"))
        self.assertTrue(is_palindrome("Mr. Owl ate my metal worm"))

    def test_not_palindrome(self):
        self.assertFalse(is_palindrome("hello"))
        self.assertFalse(is_palindrome("python"))
        self.assertFalse(is_palindrome("OpenAI GPT"))
        self.assertFalse(is_palindrome("Palindrome? Nope, not this!"))
        self.assertFalse(is_palindrome("1234567890"))

if __name__ == "__main__":
    unittest.main()
