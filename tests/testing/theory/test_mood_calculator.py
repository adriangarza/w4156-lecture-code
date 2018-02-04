import unittest
from lectures.testing.theory.mood_calculator import MoodCalculator
from lectures.testing.theory.mood_calculator import Mood


class MyTestCase(unittest.TestCase):
    """
    Note - we have two methods beginning 'test'. Both these methods will be run
    """

    def setUp(self):
        self.mood_calculator = MoodCalculator()

    def test_out_of_range(self):
        with self.assertRaises(ValueError):
            self.mood_calculator.calculate_mood(-1, 70)
            self.mood_calculator.calculate_mood(10, 200)

    def test_mood_calculator(self):

        """
        TODO - Exercise for the student to write and test the mood calculator
        :return: nothing

        according to the lecture slides, we know:
        sleep between 0 and 26:
            blood sugar between 70 and 75: irritable
            blood sugar between 75.1 and 90: joy
        sleep between 26.1 and 36:
            blood sugar between 70 and 75: moody
            blood sugar between 75.1 and 90: hulk smash

        so those are the boundaries, test different permutations of them
        """

        # first we test that it works within range
        self.test_out_of_range()

        # then test boundaries that fall within the expected range
        # (sleep_dep, blood_sugar, expected_result)
        test_cases = [
            (0,  70, Mood.Irritated),
            (0,  75, Mood.Irritated),
            (26, 76, Mood.Joyful),
            (26, 90, Mood.Joyful),
            (27, 70, Mood.Grumpy),
            (27, 75, Mood.Grumpy),
            (36, 76, Mood.Hulk),
            (36, 90, Mood.Hulk)
        ]

        for t in test_cases:
            value = self.mood_calculator.calculate_mood(t[0], t[1])
            self.assertEqual(value, t[2])


if __name__ == '__main__':
    unittest.main()
