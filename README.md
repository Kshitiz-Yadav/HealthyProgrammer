# HealthyProgrammer
Noobish Python project

"""
Aim - 
    This program is supposed to work as a reminder setter. Music is played everytime the programmer needs to do a task.
    The programmer is supposed to do the task and reply to the programmer. A log file, keeping track of the entire process is also maintained.

Requirements-
    inputtimeout module
    time module
    datetime module
    pygame module

Working -
    1)  The starting time, sleeping time and frequency of each task is taken as input.
    2)  The program sleeps till start time.
    3)  After start time, the program asks to perform the tasks after regular intervals of time.
        The tasks are chosen as per the written algorithm so that they are as natural as possible.
    4)  For each task, music will be played for a duration equal to half the time gap between two tasks.
    5)  The programmer responds by replying to the program if he has done the task or will be skipping it.
        In case of no response within the time that music plays, the task is considered to be missed.
    
Flow of control-
    main -> play music(stops after logging procedure) -> log(completed/canceled/missed)

Precautions - 
    Make sure that the number of tasks do not make the time intervals so small that the process becomes unpractically faster.

Sample Input
    1)  4 Minutes Program ->
        Staring Time - hh:mm:ss
        Ending Time - HH:MM:SS
        such that, (Ending Time - Staring Time = 00:04:00)
        For e.g. - 13:01:00 and 13:05:00
        Number of tasks - 1 1 1

        Output ->
          Start  -> Wait time -> Task 1 -> Wait time -> Task 2 -> Wait time -> Task 3 ->  Wait time  ->  End
        13:01:00                13:02:00               13:03:00               13:04:00                 13:05:00
"""
