def dfa(bro,input_string):
    current_state = bro["Start State"]
    for symbol in input_string:
        if symbol not in bro["Alphabets"]:
            return "Invalid String"

        current_state = bro["Transition State"][current_state][symbol]

    if current_state == bro["Acceptance State"]:
        return "Accepted"
    return "rejected"