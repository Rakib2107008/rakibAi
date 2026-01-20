import math
def initial_state():
    return (
        " ", " ", " ",
        " ", " ", " ",
        " ", " ", " "
    )
def action(state):
    return  [a for a in range(9) if state[a] ==" " ]
def result(state,action,player):
    new_state=list(state)
    new_state[action]=player
    return tuple(new_state)
def terminal(state):
    return utility(state) is not None
def utility(state):
    terminal_state=[
        (0,1,2),(0,3,6),(0,4,8),
        (6,7,8),(2,5,8),(2,4,6),
        (3,4,5),(1,4,7)
    ]

    for (a,b,c) in terminal_state:
        if state[a]==state[b]==state[c]=="X":
            return 1
        if state[a]==state[b]==state[c]=="O":
            return -1
        
    if " " not in state:
        return 0
    return None
def min_val(state):
    if terminal(state):
        return utility(state)
    best_val=math.inf
    for a in action(state):
        best_val=min(best_val,max_val(result(state,a,"O")))
    return best_val
def max_val(state):
    if terminal(state):
        return utility(state)
    best_val=-math.inf
    for a in action(state):
        best_val=max(best_val,min_val(result(state,a,"X")))
    return best_val
    
def minimax(state):
    bestVal=-math.inf
    best_action=None
    
    for a in action(state):
        value=min_val(result(state,a,"X"))
        if value>bestVal:
            bestVal=value
            best_action=a

    return best_action
def print_board(state):
    for i in range(0, 9, 3):
        print(state[i], "|", state[i+1], "|", state[i+2])
    print()
            









if __name__ == "__main__":
    state=initial_state()
    while True:
        ai_move=minimax(state)
        state = result(state, ai_move, "X")
        print_board(state)
        if terminal(state):
            break
        
        human_move=int(input("enter your choice from 0-8"))
        state=result(state,human_move,"O")
        print_board(state)
        if terminal(state):
            break

    win_val=utility(state)
    if win_val==1:
        print("ai won")   

    if win_val==-1:
        print("player won")     

    if win_val==0:
        print("Draw")     


