

# DFA - Theory of Computation Project

This project implements a **Deterministic Finite Automaton (DFA)** to accept or reject input strings based on defined transition states, start state, and acceptance states. The DFA is designed to simulate the theory of computation for language recognition, where strings are processed and checked for acceptance.

## Table of Contents
- [Project Description](#project-description)
- [How to Use](#how-to-use)
- [Requirements](#requirements)
- [License](#license)

## Project Description

This project demonstrates the creation and use of a **Deterministic Finite Automaton (DFA)** that simulates a simple state machine. It accepts input strings and determines whether they are accepted or rejected based on the predefined states, alphabets, transitions, and acceptance conditions.

The DFA is implemented using Python, and it accepts input strings based on user-defined parameters for:
- **States**: The different states in the DFA.
- **Alphabet**: The set of symbols that the DFA processes.
- **Start State**: The state where the DFA starts.
- **Acceptance States**: States that define the successful termination of the DFA.
- **Transition Function**: The rules that govern state transitions based on the input symbol.

## How to Use

1. Clone or download the repository to your local machine.
   
2. **Install Python**: Ensure Python 3.x is installed. You can check by running:
   ```bash
   python --version
   ```
   If you don't have Python, download and install it from [python.org](https://www.python.org/downloads/).

3. **Run the script**:
   Navigate to the project directory and run the main Python file:
   ```bash
   python main.py
   ```

4. **Input DFA Parameters**:
   - Enter the number of states.
   - Define the alphabet of the DFA.
   - Set the start state and acceptance state(s).
   - Define the transition function for each state and symbol.

5. **Test DFA**:
   After setting up the DFA, the program will prompt you to input a string to check if it is accepted or rejected by the automaton.

### Example Usage:

```plaintext
Enter number of states: 3
Enter the number of alphabets: 2
Enter the value for alphabet: 0
Enter the value for alphabet: 1
Enter the Transition states for DFA
Enter the Transition state for q0:
  On input 0 go to (['q0', 'q1', 'q2']): q0
  On input 1 go to (['q0', 'q1', 'q2']): q1
Enter the Transition state for q1:
  On input 0 go to (['q0', 'q1', 'q2']): q0
  On input 1 go to (['q0', 'q1', 'q2']): q2
Enter the Transition state for q2:
  On input 0 go to (['q0', 'q1', 'q2']): q0
  On input 1 go to (['q0', 'q1', 'q2']): q2
```

Then, you can test it with an input string like:
```plaintext
Type the string you want to try: 101
```

The DFA will process the string and print whether it is accepted or rejected based on the transition rules you defined.

## Requirements

- **Python 3.x**: The program is written in Python, so you’ll need Python installed on your system.
  
  You can download Python from [here](https://www.python.org/downloads/).
  
- No additional libraries are required for this basic DFA implementation.

## License

This project is open-source and available under the [MIT License](LICENSE).
