"""Doors displaying."""

from typing import List

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


def draw_doors(opened: List[int], answer: int) -> None:
    if first_door in opened:
        r11 = r12 =  "     "
        if answer == first_door:
            r13 = "   " + prize
            r14 = " " + prize * 2
        else:
            r13 = r14 = "     "
    else:
        r11 = "  " + str(first_door) + "  "
        r12 = "    " + door_hand
        r13 = "     "
        r14 = "_" * 5
    if second_door in opened:
        r21 = r22 = "     "
        if answer == second_door:
            r23 = "   " +  prize
            r24 = " " + prize * 2
        else:
            r23 = r24 = "     "
    else:
        r21 = "  " + str(second_door) + "  "
        r22 = "    " + door_hand
        r23 = "     "
        r24 = "_" * 5
    if third_door in opened:
        r31 = r32 = "     "
        if answer == third_door:
            r33 = "   " + prize
            r34 = " " + prize * 2
        else:
            r33 = r34 = "     "
    else:
        r31 = "  " + str(third_door) + "  "
        r32 = "    " + door_hand
        r33 = "     "
        r34 = "_" * 5
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
