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
        - the nav computer returns an empty list if no enemies
        - to add to that, the computer returns as many enemies possible that fit the number asked for
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
        enemies = self.nav_computer.detect_nearest_enemy(1, [])
        self.assertEqual(len(enemies), 0)

        # and then test again but with friends thrown in for good measure
        other_planes = [RadarSignature(x[0], x[1], x[2]) for x in [
            (1, 1, FriendFoe.Friend),
            (1, 4, FriendFoe.Friend)
        ]]
        enemies = self.nav_computer.detect_nearest_enemy(1, other_planes)
        self.assertEqual(len(enemies), 0)

    def test_actual_enemies(self):
        other_planes = [RadarSignature(x[0], x[1], x[2]) for x in [
            (1, 4, FriendFoe.Foe),
            (2, 8, FriendFoe.Foe),
            (3, 0, FriendFoe.Foe),
            (1, 10, FriendFoe.Foe),
            (1, 1, FriendFoe.Friend),
            (1, 4, FriendFoe.Friend)
        ]]

        enemies = self.nav_computer.detect_nearest_enemy(2, other_planes)
        self.assertEqual(len(enemies), 2)

        # we also want the right enemies
        # for some reason, getNearestEnemies is specified to return a list of radarSignature tuples instead of a list of
        # radar signatures. it looks like [(radarSignature), (radarSignature)].
        # therefore actually accessing the values makes PyCharm complain
        first_points = (enemies[0].x, enemies[0].y) == (3, 0)
        second_points = (enemies[1].x, enemies[1].y) == (1, 4)

        self.assertEqual(first_points, True)
        self.assertEqual(second_points, True)


if __name__ == '__main__':
    unittest.main()
