#!/usr/bin/env python3

import sys
import calendar

days = ["Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday", "Sunday"]

lines = ["Monday's child is fair of face",
         "Tuesday's child is full of grace",
         "Wednesday's child is full of woe",
         "Thursday's child has far to go",
         "Friday's child is loving and giving",
         "Saturday's child works hard for a living",
         "Sunday's child is fair and wise and good in every way"
         ]
birthdays = sys.stdin.readlines()
for birth in birthdays:
  birth = birth.strip().split()
  day, month, year = birth
  day_num = calendar.weekday(int(year), int(month), int(day))
  print(f'You were born on a {days[day_num]} and {lines[day_num]}.')
