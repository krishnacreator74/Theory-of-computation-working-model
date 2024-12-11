
import dfa
import Transis

def justdoit(my_list,size):
    for i in range (size):
        temp = input(f"enter the {i+1} value:")
        my_list.append(temp)

#dictionary
bro={}

#taking input for states
size = int(input("enter number of states:"))
states= []
for i in range(size):
    states.append("q"+ str(i) )
bro["States"] = states

#taking input for alphabets
size1 = int(input("Enter the number of alphabets:"))
alphbates=[]
print("enter the value for alphabets:")
justdoit(alphbates,size1)
bro["Alphabets"] = alphbates

#setting start state
bro["Start State"] = states[0]

#acceptance state
bro["Acceptance State"] = "q"+str(size-1)

#transition state
bro["Transition State"] = Transis.transistion_state(states,alphbates)
print(bro)

print("Dfa is created")

while True:
    choice = input("\nType 1 to try with an input string\nType 2 to exit\nYour choice: ")

    if choice == "1":
        input_string = input("Type the string you want to try:\n")
        result = dfa.dfa(bro, input_string)
        print(f"Result: {result}")

    elif choice == "2":
        print("Exiting...")
        break
    
    else:
        print("Invalid choice. Please try again.")
