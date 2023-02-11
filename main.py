"""Doors displaying."""

from typing import List, Tuple

door_hand = "०"
prize = "💰"
first_door = 1
second_door = 2
third_door = 3


doors_pattern = """\
   _____    _____    _____
  |     |  |     |  |     |
  |{r11}|  |{r21}|  |{r31}|
  |{r12}|  |{r22}|  |{r32}|
  |{r13}|  |{r23}|  |{r33}|
  |{r14}|  |{r24}|  |{r34}|
"""


def _get_door_params(opened: List[int], answer: int, door_number: int) -> Tuple[str]:
    if door_number in opened:
        r1 = r2 =  "     "
        if answer == door_number:
            r3 = "   " + prize
            r4 = " " + prize * 2
        else:
            r3 = r4 = "     "
    else:
        r1 = "  " + str(door_number) + "  "
        r2 = "    " + door_hand
        r3 = "     "
        r4 = "_" * 5
    return r1, r2, r3, r4


def draw_doors(opened: List[int], answer: int) -> None:
    r11, r12, r13, r14 = _get_door_params(opened, answer, first_door)
    r21, r22, r23, r24 = _get_door_params(opened, answer, second_door)
    r31, r32, r33, r34 = _get_door_params(opened, answer, third_door)
    print(
        doors_pattern.format(
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
