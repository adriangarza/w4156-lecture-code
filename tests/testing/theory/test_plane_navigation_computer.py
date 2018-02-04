import unittest
from lectures.testing.theory.plane_navigation_computer import FriendFoe, NearestEnemyFinder, RadarSignature
import tests.helper as helper


class MyTestCase(unittest.TestCase):
    """
    so the state space for this is pretty big
    we want to make sure that:
        - the nav computer only returns enemies
        - the nav computer never returns more than asked for
        - the nav computer only gets the nearest enemies
        - the nav computer doesn't accept invalid numbers (i.e. more than 0)
    """

    def setUp(self):
        self.nav_computer = NearestEnemyFinder()

    def test_valid_num_targets(self):
        # the nav computer won't accept 0 or fewer enemies
        # therefore, we want this to raise a valueError
        with self.assertRaises(ValueError):
            self.nav_computer.detect_nearest_enemy(0, [])

    def test_no_enemies(self):
        # with no enemies, the nav computer should return an empty list
        num_enemies = self.nav_computer.detect_nearest_enemy(1, [])

    # def test_actual_enemies(self):
        # make sure the nav computer doesn't ever return friends


if __name__ == '__main__':
    unittest.main()
