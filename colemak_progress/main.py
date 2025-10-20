import datetime
import os
from dataclasses import dataclass
import matplotlib.pyplot as plt

@dataclass
class Entry():
    date: datetime.date
    qwerty_wpm: int
    colemak_wpm: int

entries = (
    Entry(date=datetime.date(2025,8,13), qwerty_wpm=97, colemak_wpm=9),
    Entry(date=datetime.date(2025,8,14), qwerty_wpm=87, colemak_wpm=12),
    Entry(date=datetime.date(2025,8,15), qwerty_wpm=89, colemak_wpm=13),
    Entry(date=datetime.date(2025,8,16), qwerty_wpm=89, colemak_wpm=16),
    Entry(date=datetime.date(2025,8,17), qwerty_wpm=97, colemak_wpm=19),
    Entry(date=datetime.date(2025,8,18), qwerty_wpm=89, colemak_wpm=22),
    Entry(date=datetime.date(2025,8,19), qwerty_wpm=88, colemak_wpm=25),
    Entry(date=datetime.date(2025,8,20), qwerty_wpm=89, colemak_wpm=23),
    Entry(date=datetime.date(2025,8,21), qwerty_wpm=90, colemak_wpm=28),
    Entry(date=datetime.date(2025,8,22), qwerty_wpm=90, colemak_wpm=29),
    Entry(date=datetime.date(2025,8,23), qwerty_wpm=93, colemak_wpm=33),
    Entry(date=datetime.date(2025,8,24), qwerty_wpm=81, colemak_wpm=33),
    Entry(date=datetime.date(2025,8,25), qwerty_wpm=81, colemak_wpm=33),
    Entry(date=datetime.date(2025,8,26), qwerty_wpm=86, colemak_wpm=35),
    Entry(date=datetime.date(2025,8,27), qwerty_wpm=72, colemak_wpm=32),
    Entry(date=datetime.date(2025,8,28), qwerty_wpm=77, colemak_wpm=31),
    Entry(date=datetime.date(2025,8,30), qwerty_wpm=72, colemak_wpm=39),
    Entry(date=datetime.date(2025,9,1), qwerty_wpm=72, colemak_wpm=34),
    Entry(date=datetime.date(2025,9,3), qwerty_wpm=86, colemak_wpm=42),
    Entry(date=datetime.date(2025,9,4), qwerty_wpm=76, colemak_wpm=39),
    Entry(date=datetime.date(2025,9,4), qwerty_wpm=79, colemak_wpm=40),
    Entry(date=datetime.date(2025,9,12), qwerty_wpm=61, colemak_wpm=42),
    Entry(date=datetime.date(2025,9,15), qwerty_wpm=67, colemak_wpm=44),
    Entry(date=datetime.date(2025,9,19), qwerty_wpm=66, colemak_wpm=49),
    Entry(date=datetime.date(2025,10,11), qwerty_wpm=68, colemak_wpm=53),
    Entry(date=datetime.date(2025,10,20), qwerty_wpm=74, colemak_wpm=49),
)

def main():
    dates = [entry.date for entry in entries]
    days_elapsed = [(date - dates[0]).days for date in dates]
    qwe_speeds = [entry.qwerty_wpm for entry in entries]
    cmk_speeds = [entry.colemak_wpm for entry in entries]

    fig, ax = plt.subplots(1, 1)
    ax.plot(days_elapsed, qwe_speeds, '-xk')
    ax.plot(days_elapsed, cmk_speeds, '-xb')
    ax.legend(("QWE (wpm)", "CMK (wpm)"))
    ax.set_ylim((0,100))
    ax.set_xlim((min(days_elapsed), max(days_elapsed)))
    ax.set_xticks([i for i in range(min(days_elapsed), max(days_elapsed) + 1)])
    ax.grid(axis='y')
    ax.set_xlabel("Day")
    ax.set_ylabel("WPM")
    plt.savefig(os.path.join("..", "colemak progress.png"))

if __name__ == "__main__":
    main()
