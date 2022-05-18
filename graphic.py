import os
import time

FRAMES = []
FRAME0 = ["    ╔════════════╗                 \r",
          "    ║            │                 \r",
          "    ║                              \r",
          "    ║                              \r",
          "    ║                              \r",
          "    ║                              \r",
          "    ║                              \r",
          "    ║                              \r",
          "    ║                              \r",
          " ═══╩═══                           \r"]

FRAME1 = ["    ╔════════════╗                 \r",
          "    ║            │                 \r",
          "    ║            Ό                 \r",
          "    ║                              \r",
          "    ║                              \r",
          "    ║                              \r",
          "    ║                              \r",
          "    ║                              \r",
          "    ║                              \r",
          " ═══╩═══                           \r"]

FRAME2 = ["    ╔════════════╗                 \r",
          "    ║            │                 \r",
          "    ║            Ό                 \r",
          "    ║           ═╬═                \r",
          "    ║                              \r",
          "    ║                              \r",
          "    ║                              \r",
          "    ║                              \r",
          "    ║                              \r",
          " ═══╩═══                           \r"]

FRAME3 = ["    ╔════════════╗                 \r",
          "    ║            │                 \r",
          "    ║            Ό                 \r",
          "    ║           ═╬═╛               \r",
          "    ║                              \r",
          "    ║                              \r",
          "    ║                              \r",
          "    ║                              \r",
          "    ║                              \r",
          " ═══╩═══                           \r"]

FRAME4 = ["    ╔════════════╗                 \r",
          "    ║            │                 \r",
          "    ║            Ό                 \r",
          "    ║          ╒═╬═╛               \r",
          "    ║                              \r",
          "    ║                              \r",
          "    ║                              \r",
          "    ║                              \r",
          "    ║                              \r",
          " ═══╩═══                           \r"]

FRAME5 = ["    ╔════════════╗                 \r",
          "    ║            │                 \r",
          "    ║            Ό                 \r",
          "    ║          ╒═╬═╛               \r",
          "    ║            ║                 \r",
          "    ║                              \r",
          "    ║                              \r",
          "    ║                              \r",
          "    ║                              \r",
          " ═══╩═══                           \r"]

FRAME6 = ["    ╔════════════╗                 \r",
          "    ║            │                 \r",
          "    ║            Ό                 \r",
          "    ║          ╒═╬═╛               \r",
          "    ║            ║                 \r",
          "    ║           ╔╩                 \r",
          "    ║                              \r",
          "    ║                              \r",
          "    ║                              \r",
          " ═══╩═══                           \r"]

FRAME7 = ["    ╔════════════╗                 \r",
          "    ║            │                 \r",
          "    ║            Ό                 \r",
          "    ║          ╒═╬═╛               \r",
          "    ║            ║                 \r",
          "    ║           ╔╩╗                \r",
          "    ║                              \r",
          "    ║                              \r",
          "    ║                              \r",
          " ═══╩═══                           \r"]

FRAME8 = ["    ╔════════════╗                 \r",
          "    ║            │                 \r",
          "    ║            Ό                 \r",
          "    ║          ╒═╬═╛               \r",
          "    ║            ║                 \r",
          "    ║           ╔╩╗                \r",
          "    ║           ╜                  \r",
          "    ║                              \r",
          "    ║                              \r",
          " ═══╩═══                           \r"]

FRAME9 = ["    ╔════════════╗                 \r",
          "    ║            │                 \r",
          "    ║            Ό                 \r",
          "    ║          ╒═╬═╛               \r",
          "    ║            ║                 \r",
          "    ║           ╔╩╗                \r",
          "    ║           ╜ ╙                \r",
          "    ║                              \r",
          "    ║                              \r",
          " ═══╩═══                           \r"]

FRAME9 = ["    ╔════════════╗                 \r",
          "    ║            │                 \r",
          "    ║            Ό                 \r",
          "    ║          ╒═╬═╛               \r",
          "    ║            ║                 \r",
          "    ║           ╔╩╗                \r",
          "    ║           ╜ ╙                \r",
          "    ║                              \r",
          "    ║                              \r",
          " ═══╩═══                           \r"]

FRAME10 = ["    ╔════════════╗                \r",
           "    ║            │                \r",
           "    ║            Ό                \r",
           "    ║          ╒═╬═╛               \r",
           "    ║            ║                 \r",
           "    ║           ╔╩╗                \r",
           "    ║           ╜ ╙                \r",
           "    ║                              \r",
           "    ║                              \r",
           " ═══╩═══                           \r"]

FRAME11 = ["    ╔════════════╗                 \r",
           "    ║            │                 \r",
           "    ║            Ό                \r",
           "    ║          ╒═╬═╛               \r",
           "    ║            ║                 \r",
           "    ║           ╔╩╗                \r",
           "    ║           ╜ ╙                \r",
           "    ║                              \r",
           "    ║                              \r",
           " ═══╩═══                           \r"]

FRAME12 = ["    ╔════════════╗                 \r",
           "    ║            │                 \r",
           "    ║            Ό                 \r",
           "    ║          ╒═╬═╛               \r",
           "    ║            ║                 \r",
           "    ║           ╔╩╗                \r",
           "    ║           ╜ ╙                \r",
           "    ║                              \r",
           "    ║                              \r",
           " ═══╩═══                           \r"]

FRAME13 = ["    ╔════════════╗                 \r",
           "    ║            │                 \r",
           "    ║            Ό                 \r",
           "    ║          ╒═╬═╛               \r",
           "    ║            ║                 \r",
           "    ║           ╔╩╗                \r",
           "    ║           ╜ ╙                \r",
           "    ║                              \r",
           "    ║                              \r",
           " ═══╩═══                           \r"]

FRAME14 = ["    ╔════════════╗                 \r",
           "    ║            │                 \r",
           "    ║            Ό                 \r",
           "    ║          ╒═╬═╛               \r",
           "    ║            ║                 \r",
           "    ║           ╔╩╗                \r",
           "    ║           ╜ ╙                \r",
           "    ║                              \r",
           "    ║                              \r",
           " ═══╩═══                           \r"]

FRAME15 = ["    ╔════════════╗                 \r",
           "    ║            │                 \r",
           "    ║            Ό                 \r",
           "    ║          ╒═╬═╛               \r",
           "    ║            ║                 \r",
           "    ║           ╔╩╗                \r",
           "    ║           ╜ ╙                \r",
           "    ║                              \r",
           "    ║                              \r",
           " ═══╩═══                           \r"]

FRAME16 = ["    ╔════════════╗                 \r",
           "    ║            │                 \r",
           "    ║            Ό                 \r",
           "    ║          ╒═╬═╛               \r",
           "    ║            ║                 \r",
           "    ║           ╔╩╗                \r",
           "    ║           ╜ ╙                \r",
           "    ║                              \r",
           "    ║                              \r",
           " ═══╩═══                           \r"]

LABELS = ["             _A____                \r",
          "             _AN____               \r",
          "             _ANG___               \r",
          "             _ANGT__               \r",
          "             _ANG_E_               \r",
          "             _ANG_A_               \r",
          "             _ANGLA_               \r",
          "             _ANG_A_               \r",
          "             _ANGRA_               \r",
          "             _ANG_A_               \r",
          "             _ANGMA_               \r",
          "             SANGMAN               \r",
          "             _ANGMAN               \r",
          "             DANGMAN               \r",
          "             xANGMAM               \r",
          "\"HANGMAN\" GAME by Gallow's pole software inc. \r"]

FRAMES.append(FRAME0)
FRAMES.append(FRAME1)
FRAMES.append(FRAME2)
FRAMES.append(FRAME3)
FRAMES.append(FRAME4)
FRAMES.append(FRAME5)
FRAMES.append(FRAME6)
FRAMES.append(FRAME7)
FRAMES.append(FRAME8)
FRAMES.append(FRAME9)
FRAMES.append(FRAME10)
FRAMES.append(FRAME11)
FRAMES.append(FRAME12)
FRAMES.append(FRAME13)
FRAMES.append(FRAME14)
FRAMES.append(FRAME15)
FRAMES.append(FRAME16)

# draws a short animation to present the game
def splash():
    for idx in range(len(FRAMES)):
        os.system('cls')
        for line in FRAMES[idx-1]:
            print(line)
        print(LABELS[idx-1])
        time.sleep(0.01)
    time.sleep(1)
