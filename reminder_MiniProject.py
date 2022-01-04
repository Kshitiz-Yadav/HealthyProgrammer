import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from pygame import mixer
from inputimeout import inputimeout, TimeoutOccurred
import time
import datetime

#Function to add logs upon task completion
def addLog(task):
    global timeOut
    global file
    reply = ""
    try:
        reply = inputimeout(prompt = 'Enter status of task. [done / skip]\n', timeout = timeOut)
    except TimeoutOccurred:
        pass
    
    logTime = datetime.datetime.now().strftime("%H:%M:%S, %d-%m-%Y")
    file.write(f"[{logTime}]:")

    if task == 1:
        file.write("\t\tRest Eyes\t\t")
    elif task == 2:
        file.write("\t\tDrink Water\t\t")
    else:
        file.write("\t\tExercise\t\t")

    if reply == "done":
        print(":)\n")
        file.write("Completed\n")
    elif reply == "skip":
        print(":(\n")
        file.write("Cancelled\n")
    else:
        print(":|\n")
        file.write("Missed\n")
        
#Function to play the reminder alarm
def playMusic(song, task):
    mixer.init()
    mixer.music.load(song)
    mixer.music.play(-1)
    addLog(task)
    mixer.music.stop()
    mixer.quit()

#Returns time taken to perform restEyes task
def restEyes():
    begin = time.time()
    print("Its time to rest your eyes!!")
    playMusic('Python\onMyWay.mp3', 1)
    return time.time() - begin

#Returns time taken to perform drinkWater task
def drinkWater():
    begin = time.time()
    print("Its time to drink some water!!")
    playMusic('Python\onMyWay.mp3', 2)
    return time.time() - begin

#Returns time taken to perform exercise task
def exercise():
    begin = time.time()
    print("Its time to exercise!!")
    playMusic('Python\onMyWay.mp3', 3)
    return time.time() - begin

#Getting starting date and time
startingPoint = datetime.datetime.now()
fileName = startingPoint.strftime("%Y%m%d_%H%M%S_")
file = open(f'{fileName}Log.txt', 'a')

timeToStartList = list(input("Enter time to begin the program (HH:MM:SS):\n").split(':'))
timeToEndList = list(input("Enter time to end the program (HH:MM:SS):\n").split(':'))

#Getting frequency of tasks to be performed
taskCount = []
print("")
taskCount.append(int(input("Enter number of eye breaks needed: ")))
taskCount.append(int(input("Enter number of water breaks needed: ")))
taskCount.append(int(input("Enter number of exercise breaks needed: ")))
print("")

currentTime = datetime.datetime.now().time()
timeToStart = datetime.time(int(timeToStartList[0]),int(timeToStartList[1]),int(timeToStartList[2]))
timeToEnd = datetime.time(int(timeToEndList[0]),int(timeToEndList[1]),int(timeToEndList[2]))
tempDate = datetime.date.today()
t1 = datetime.datetime.combine(tempDate, currentTime)
t2 = datetime.datetime.combine(tempDate, timeToStart)
t3 = datetime.datetime.combine(tempDate, timeToEnd)


initLog = t1.strftime("%H:%M:%S, %d-%m-%Y")
file.write(f"[{initLog}]: Program initiated\n")

#Waiting till start time
time.sleep((t2 - t1).seconds)

startLog = datetime.datetime.combine(datetime.date.today(), timeToStart).strftime("%H:%M:%S, %d-%m-%Y")
file.write(f"[{startLog}]: Program started\n")

timeGap = ((t3 - t2).seconds)/(sum(taskCount) + 1)
timeOut = timeGap / 2

#Algorithm to choose which task to perform (This avoids repetetion of tasks if other tasks are available and avoids patterns)
nextTask = max(taskCount)
i = 0
j = 1
prevIndex = 3
time.sleep(timeGap)
while nextTask > 0:
    index = taskCount.index(nextTask)
    if j % 2 == 0:
        for ind in range(3):
            if taskCount[ind] == nextTask:
                index = ind
    if index == prevIndex:
        temp = 3 - prevIndex - taskCount.index(min(taskCount))
        if taskCount[temp] > 0:
            index = temp
    prevIndex = index
    taskCount[index] = taskCount[index] - 1
    if index == 0:
        timeConsumed = restEyes()
    elif index == 1:
        timeConsumed = drinkWater()
    elif index == 2:
        timeConsumed = exercise()
    time.sleep(timeGap - timeConsumed)
    j = j + 1
    nextTask = max(taskCount)

finishLog = datetime.datetime.now().strftime("%H:%M:%S, %d-%m-%Y")
file.write(f"[{finishLog}]: Program ended")
file.close()

print("Ending program! Have a good day!!")