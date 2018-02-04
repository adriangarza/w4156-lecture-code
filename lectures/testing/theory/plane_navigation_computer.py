from typing import Dict, Tuple, List
from enum import Enum, auto
from math import sqrt, pow


class FriendFoe(Enum):
    Friend = auto()
    Foe = auto()


class RadarSignature:

    def __init__(self, x: float, y: float, friend_foe: FriendFoe):
        """
        :param x: in coordinate system relative to our plane
        :param y: in coordinate system relative to our plane
        :param friend_foe: is the plane friendly or foe
        """
        self.x = x
        self.y = y
        self.friend_foe = friend_foe


class NearestEnemyFinder:

    def detect_nearest_enemy(self, number_targets, signatures: List[RadarSignature]) -> List[Tuple[RadarSignature]]:
        """
        Detect the nearest N enemy targets
        :param number_targets: the number of enemy targets to return
        :param signatures: a list of radar signatures of planes. Coordinate system based around our plane being (0,0)
        :return: the N nearest enemy targets. If there are less than N enemy radar then return the
        # the above line ended oddly. I assume it should just return the entire list of enemies if it's less than N.
        """

        # make sure N is valid
        if not number_targets >= 1:
            raise ValueError("Number of targets:%s not valid" % number_targets)

        # make a list of all the enemies
        enemies = [x for x in signatures if x.friend_foe == FriendFoe.Foe]

        # list of (enemy, distance) tuples
        enemies_distance = []
        for x in enemies:
            enemies_distance.append((x, self.get_distance(x)))

        # sort by the second tuple element, distance and cut to desired number
        nearest_enemies = sorted(enemies_distance, key=lambda x: x[1])[:number_targets]

        # then get the radar signature for each tuple
        return [x[0] for x in nearest_enemies]

    # helper function to get euclidean distance from (0, 0)
    def get_distance(self, enemy: RadarSignature) -> float:
        return sqrt(pow(enemy.x, 2) + pow(enemy.y, 2))
