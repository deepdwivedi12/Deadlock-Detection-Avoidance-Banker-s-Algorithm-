# Deep Dwivedi - Deadlock Detection and Avoidance

## Operating Systems Practical Project

This project demonstrates **deadlock avoidance using Banker's Algorithm** and a small example of **deadlock detection** using Python.

## Project Information

- **Student Name:** Deep Dwivedi
- **Subject:** Operating Systems
- **Project Title:** Deadlock Detection and Avoidance
- **Programming Language:** Python 3
- **External Libraries:** Not required

## Objectives

- Understand deadlock in an operating system.
- Calculate the Need Matrix.
- Check whether the system is in a safe state.
- Generate a safe sequence using Banker's Algorithm.
- Demonstrate a simple deadlock detection example.

## Concepts Used

- Lists (matrices)
- `for` loops and `while` loops
- `if-else` conditions
- Variables and basic arithmetic
- Banker's Algorithm
- Deadlock Detection

## Files

```text
Project/
│
├── Deep_Dwivedi_Deadlock_Detection_Avoidance.py
├── Deep_Dwivedi_Deadlock_Detection_and_Avoidance_Report.pdf
└── README.md
```

## How to Run

1. Install Python 3 if it is not already installed.
2. Open the project folder in VS Code or Terminal.
3. Run the following command:

```bash
python3 Deep_Dwivedi_Deadlock_Detection_Avoidance.py
```

On Windows, you can also use:

```bash
python Deep_Dwivedi_Deadlock_Detection_Avoidance.py
```

## How the Project Works

### 1. Allocation Matrix

Stores the resources currently allocated to each process.

### 2. Maximum Matrix

Stores the maximum resources that each process may require.

### 3. Available Resources

Stores the number of currently available instances of each resource type.

### 4. Need Matrix

The program calculates the remaining resources required by each process using:

```text
Need = Maximum - Allocation
```

### 5. Banker's Algorithm

The program checks whether a process can complete with the currently available resources. When a process completes, its allocated resources are released. If all processes can complete, the system is in a **safe state**, and the program displays a safe sequence.

For the included sample input, the safe sequence is:

```text
P1 -> P3 -> P4 -> P0 -> P2
```

### 6. Deadlock Detection

The program also runs a separate small example with two processes and two resource types. Each process holds one resource and waits for the resource held by the other process. Since neither process can proceed, the example reports a deadlock.

## Sample Output

```text
Banker's Algorithm Result:
System is in SAFE STATE
Safe Sequence: P1 P3 P4 P0 P2

Deadlock Detection Result:
Deadlock Detected
Deadlocked Processes:
P0
P1
```

*The output above shows the main results. The program also prints the sample matrices.*

## Difference Between Avoidance and Detection

| Deadlock Avoidance | Deadlock Detection |
|---|---|
| Tries to prevent the system from entering an unsafe state. | Checks whether deadlock exists in the current state. |
| Banker's Algorithm is an avoidance algorithm. | Uses Allocation, Request and Available information. |

**Note:** An unsafe state does not always mean that deadlock has already occurred.

## Limitations

- The program uses fixed sample input values.
- The detection example is limited to two processes and two resource types.
- It is an educational simulation and does not manage actual operating-system processes.

## Conclusion

This project explains how an operating system can manage limited resources. Banker's Algorithm checks whether the system can safely execute all processes, while the separate detection example shows how processes can become blocked while waiting for resources.

## References

1. *Operating System Concepts* - Abraham Silberschatz, Peter B. Galvin and Greg Gagne.
2. Operating Systems classroom notes.
3. [Python 3 Documentation](https://docs.python.org/3/)
