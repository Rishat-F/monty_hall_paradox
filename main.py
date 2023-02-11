"""Doors displaying."""

import os
import platform
import random
import sys
from typing import Optional, Tuple


class Scene:
    GREETING = "Welcome to our TV Show! You have a chance to win a prize!"
    ASK_TO_PLAY = "Do you want to play? (yes/no)\n- "
    CHOOSE = "Behind one of these 3 doors is a prize. Try to guess which one!\nChoose the door: "
    rounds = 0
    changed_prediction_rounds = 0
    changed_prediction_wins = 0
    no_changed_prediction_rounds = 0
    no_changed_prediction_wins = 0

    stats_pattern = \
        "Changing prediction winrate:\t{ch_pred_wr}  ({ch_pred_wins}/{ch_pred_rounds})\n" \
        "No changing prediction winrate:\t{no_ch_pred_wr}  ({no_ch_pred_wins}/{no_ch_pred_rounds})\n"

    door_hand = "०"
    prize = "💰"
    pointer = "▼"

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
    """  |{pt1}|  |{pt2}|  |{pt3}|\n""" \
    """  |{r11}|  |{r21}|  |{r31}|\n""" \
    """  |{r12}|  |{r22}|  |{r32}|\n""" \
    """  |{r13}|  |{r23}|  |{r33}|\n""" \
    """  |{r14}|  |{r24}|  |{r34}|\n"""

    def greeting(self):
        self.clear_terminal()
        print(self.GREETING)

    def want_to_play(self):
        answer = ""
        while answer not in ["yes", "y", "no", "n"]:
            answer = input(self.ASK_TO_PLAY).lower()
        if answer not in ["yes", "y"]:
            sys.exit(0)
        else:
            return True

    def new_round(self):
        self.opened_doors = []
        self.answer = random.randint(1, len(self.doors))

    def _get_door_params(self, door_number: int, prediction: Optional[int]) -> Tuple[str]:
        if door_number in self.opened_doors:
            r1 = r2 = pt = "     "
            if self.answer == door_number:
                r3 = "   " + self.prize
                r4 = " " + self.prize * 2
            else:
                r3 = r4 = "     "
        else:
            r1 = "  " + str(door_number) + "  "
            if door_number == prediction:
                pt = "  " + self.pointer + "  "
            else:
                pt = "     "
            r2 = "    " + self.door_hand
            r3 = "     "
            r4 = "_" * 5
        return pt, r1, r2, r3, r4

    def _draw_doors(self, prediction: Optional[int] = None) -> None:
        pt1, r11, r12, r13, r14 = self._get_door_params(self.first_door, prediction)
        pt2, r21, r22, r23, r24 = self._get_door_params(self.second_door, prediction)
        pt3, r31, r32, r33, r34 = self._get_door_params(self.third_door, prediction)
        print(
            self.doors_pattern.format(
                pt1=pt1,
                r11=r11,
                r12=r12,
                r13=r13,
                r14=r14,
                pt2=pt2,
                r21=r21,
                r22=r22,
                r23=r23,
                r24=r24,
                pt3=pt3,
                r31=r31,
                r32=r32,
                r33=r33,
                r34=r34,
            )
        )

    def draw_doors(self, prediction: Optional[int] = None) -> None:
        self.display_stats()
        self._draw_doors(prediction)

    def choose_door(self) -> int:
        self.draw_doors()
        prediction = int(input(self.CHOOSE))
        return prediction

    def open_empty_door(self, prediction: int) -> None:
        doors_ = list(self.doors.values())
        doors_.remove(prediction)
        try:
            doors_.remove(self.answer)
        except:
            pass
        self.opened_doors.append(random.choice(doors_))
        self.draw_doors(prediction)

    def open_all_doors(self):
        self.opened_doors = list(self.doors.values())
        self.draw_doors()

    @staticmethod
    def want_change():
        answer = ""
        while answer not in ["yes", "no", "y", "n"]:
            answer = input("Want to change your prediction? (yes/no)\n- ").lower()
        return answer in ["yes", "y"]

    def change_prediction(self, old_prediction: int) -> int:
        doors_ = list(self.doors.values())
        doors_.remove(self.opened_doors[-1])
        doors_.remove(old_prediction)
        return doors_.pop()

    @staticmethod
    def clear_terminal():
        if platform.system() == "Windows":
            os.system("cls")
        else:
            os.system("clear")

    def display_stats(self):
        self.clear_terminal()
        if self.changed_prediction_rounds == 0:
            changed_prediction_winrate = "-"
        else:
            changed_prediction_winrate = str(round(
                self.changed_prediction_wins / self.changed_prediction_rounds * 100
            )) + "%"
        if self.no_changed_prediction_rounds == 0:
            no_changed_prediction_winrate = "-"
        else:
            no_changed_prediction_winrate = str(round(
                self.no_changed_prediction_wins / self.no_changed_prediction_rounds * 100
            )) + "%"
        print(
            self.stats_pattern.format(
                ch_pred_wr=changed_prediction_winrate,
                ch_pred_wins=self.changed_prediction_wins,
                ch_pred_rounds=self.changed_prediction_rounds,
                no_ch_pred_wr=no_changed_prediction_winrate,
                no_ch_pred_wins=self.no_changed_prediction_wins,
                no_ch_pred_rounds=self.no_changed_prediction_rounds,
            )
        )

    def try_again(self):
        answer = ""
        while answer not in ["yes", "y", "no", "n"]:
            answer = input("Want to try again? (yes/no)\n- ").lower()
        return answer in ["yes", "y"]


def main():
    scene = Scene()
    scene.clear_terminal()
    scene.greeting()
    answer = scene.want_to_play()
    while answer:
        scene.new_round()
        prediction = scene.choose_door()
        scene.open_empty_door(prediction)
        changed = False
        if scene.want_change():
            changed = True
            prediction = scene.change_prediction(prediction)
        win = (prediction == scene.answer)
        scene.rounds += 1
        if win:
            if changed:
                scene.changed_prediction_rounds += 1
                scene.changed_prediction_wins += 1
            else:
                scene.no_changed_prediction_rounds += 1
                scene.no_changed_prediction_wins += 1
        else:
            if changed:
                scene.changed_prediction_rounds += 1
            else:
                scene.no_changed_prediction_rounds += 1
        scene.open_all_doors()
        if win:
            print("YOU WIN!!!\n")
        else:
            print("YOU LOSE...\n")
        answer = scene.try_again()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)
