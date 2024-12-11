def transistion_state(states,alphabets):
    Transition={}
    print("Enter the Transition states for dfa\n")
    for state in states:
        print(f"Enter the Transition state for {state}:")
        Transition[state] = {}
        for alphabet in alphabets:
            next_state = input(f"on input {alphabet} go to (one of {states}):")
            Transition[state][alphabet]=next_state
    return Transition