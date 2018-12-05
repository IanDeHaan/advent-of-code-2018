import sys
from collections import Counter
lines = []

for line in sys.stdin:
    # find time
    time = line.split()[1][:-1]
    hour, minute = map(int, time.split(":"))
    if hour == 23:
        minute -= 60
    
    # find event type
    # types: begin, asleep, up
    event = ""
    guard = 0
    if len(line.split()) == 6:
        event = "begin"
        guard = line.split()[3][1:]
    else:
        event = line.split()[3]

    lines.append(line)

lines = sorted(lines)
events = []
for line in lines:
    # find time
    time = line.split()[1][:-1]
    hour, minute = map(int, time.split(":"))
    if hour == 23:
        minute -= 60
    
    # find event type
    # types: begin, asleep, up
    event = ""
    guard = 0
    if len(line.split()) == 6:
        event = "begin"
        guard = line.split()[3][1:]
    else:
        event = line.split()[3]
    events.append((minute, guard, event))

currentGuard = 0
asleepAt = 0
sleepTimes = dict()
for event in events:
    if event[2] == "begin":
        guard = event[1]
    if event[2] == "up":
        if not guard in sleepTimes:
            sleepTimes[guard] = []
        for i in range(asleepAt, event[0]):
            sleepTimes[guard].append(i)
    if event[2] == "asleep":
        asleepAt = event[0]

most = 0
mostGuard = 0
for guard in sleepTimes:
    if len(sleepTimes[guard]) > most:
        most = len(sleepTimes[guard])
        mostGuard = guard
cnt = Counter(sleepTimes[mostGuard])
time = cnt.most_common(1)[0][0]
print("--- Part 1 ---")
print("Guard:", mostGuard, "Time:", time)
print("Answer:", int(mostGuard)*int(time))


# Part 2
most = 0
mostGuard = 0
mostTime = 0
for guard in sleepTimes:
    cnt = Counter(sleepTimes[guard])
    time, freq = cnt.most_common(1)[0]
    if freq > most:
        mostTime = time
        mostGuard = guard
        most = freq
print("--- Part 2 ---")
print("Guard:", mostGuard, "Time:", mostTime)
print("Answer:", int(mostGuard)*int(mostTime))
