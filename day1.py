import sys

current = 0
freqs = []
lines = []

for line in sys.stdin:
    lines.append(line) 

while True:
    for line in lines:
        freqs.append(current)
        if (line[0] == "+"):
            current += int(line[1:])
        else:
            current -= int(line[1:])
        if current in freqs:
            print(current)
            sys.exit(0)

