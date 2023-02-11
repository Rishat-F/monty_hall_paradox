"""Doors displaying."""

import random
from typing import List, Tuple


class Scene:
    door_hand = "०"
    prize = "💰"

    doors = {
        "first": 1,
        "second": 2,
        "third": 3,
    }
    first_door = doors["first"]
    second_door = doors["second"]
    third_door = doors["third"]

    doors_pattern = \
    """   _____    _____    _____\n""" \
    """  |     |  |     |  |     |\n""" \
    """  |{r11}|  |{r21}|  |{r31}|\n""" \
    """  |{r12}|  |{r22}|  |{r32}|\n""" \
    """  |{r13}|  |{r23}|  |{r33}|\n""" \
    """  |{r14}|  |{r24}|  |{r34}|\n"""

    def __init__(self):
        self.opened_doors = []
        self.answer = random.randint(1, len(self.doors))

    def _get_door_params(self, opened: List[int], answer: int, door_number: int) -> Tuple[str]:
        if door_number in opened:
            r1 = r2 =  "     "
            if answer == door_number:
                r3 = "   " + self.prize
                r4 = " " + self.prize * 2
            else:
                r3 = r4 = "     "
        else:
            r1 = "  " + str(door_number) + "  "
            r2 = "    " + self.door_hand
            r3 = "     "
            r4 = "_" * 5
        return r1, r2, r3, r4


    def draw_doors(self, opened: List[int], answer: int) -> None:
        r11, r12, r13, r14 = self._get_door_params(opened, answer, self.first_door)
        r21, r22, r23, r24 = self._get_door_params(opened, answer, self.second_door)
        r31, r32, r33, r34 = self._get_door_params(opened, answer, self.third_door)
        print(
            self.doors_pattern.format(
                r11=r11,
                r12=r12,
                r13=r13,
                r14=r14,
                r21=r21,
                r22=r22,
                r23=r23,
                r24=r24,
                r31=r31,
                r32=r32,
                r33=r33,
                r34=r34,
            )
        )
