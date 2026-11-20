# Deadlock Detection and Avoidance
# Operating Systems Practical Project
# Simple Python Source Code

# --------------------------------------------------
# 1. Sample Input
# --------------------------------------------------

# Allocation Matrix: resources currently allocated
allocation = [
    [0, 1, 0],
    [2, 0, 0],
    [3, 0, 2],
    [2, 1, 1],
    [0, 0, 2]
]

# Maximum Matrix: maximum resources required
maximum = [
    [7, 5, 3],
    [3, 2, 2],
    [9, 0, 2],
    [2, 2, 2],
    [4, 3, 3]
]

# Available resources
available = [3, 3, 2]

print("DEADLOCK DETECTION AND AVOIDANCE")
print("--------------------------------")

print("\nAllocation Matrix:")
for row in allocation:
    print(row)

print("\nMaximum Matrix:")
for row in maximum:
    print(row)

print("\nAvailable Resources:", available)


# --------------------------------------------------
# 2. Calculate Need Matrix
# Need = Maximum - Allocation
# --------------------------------------------------

need = []

for i in range(5):
    row = []
    for j in range(3):
        row.append(maximum[i][j] - allocation[i][j])
    need.append(row)

print("\nNeed Matrix:")
for row in need:
    print(row)


# --------------------------------------------------
# 3. Banker's Algorithm - Safe State Detection
# --------------------------------------------------

work = available.copy()
finish = [False, False, False, False, False]
safe_sequence = []

while len(safe_sequence) < 5:
    found = False

    for i in range(5):
        if finish[i] == False:
            if (need[i][0] <= work[0] and
                need[i][1] <= work[1] and
                need[i][2] <= work[2]):

                # Process finishes and releases its resources
                work[0] += allocation[i][0]
                work[1] += allocation[i][1]
                work[2] += allocation[i][2]

                finish[i] = True
                safe_sequence.append(i)
                found = True

    # If no process can finish, stop the loop
    if found == False:
        break

print("\nBanker's Algorithm Result:")

if len(safe_sequence) == 5:
    print("System is in SAFE STATE")
    print("Safe Sequence:", end=" ")

    for p in safe_sequence:
        print("P" + str(p), end=" ")

    print()
else:
    print("System is in UNSAFE STATE")
    print("Safe sequence does not exist.")


# --------------------------------------------------
# 4. Deadlock Detection Algorithm
# --------------------------------------------------

# Example with 2 processes and 2 resource types
# P0 holds resource A and waits for B.
# P1 holds resource B and waits for A.

allocation2 = [
    [1, 0],
    [0, 1]
]

request = [
    [0, 1],
    [1, 0]
]

available2 = [0, 0]

finish2 = [False, False]
work2 = available2.copy()

# A process holding no resources can finish immediately
for i in range(2):
    if allocation2[i] == [0, 0]:
        finish2[i] = True

# Check whether waiting processes can finish
found = True

while found:
    found = False

    for i in range(2):
        if finish2[i] == False:
            if (request[i][0] <= work2[0] and
                request[i][1] <= work2[1]):

                # Process finishes and releases its resources
                work2[0] += allocation2[i][0]
                work2[1] += allocation2[i][1]

                finish2[i] = True
                found = True

print("\nDeadlock Detection Result:")

if finish2[0] == False or finish2[1] == False:
    print("Deadlock Detected")
    print("Deadlocked Processes:")

    for i in range(2):
        if finish2[i] == False:
            print("P" + str(i))
else:
    print("No Deadlock Detected")


# --------------------------------------------------
# 5. Conclusion
# --------------------------------------------------

print("\nConclusion:")
print("Banker's Algorithm checks whether the system is safe.")
print("Deadlock Detection checks whether processes are stuck")
print("waiting for resources.")
