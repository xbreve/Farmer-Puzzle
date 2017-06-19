
# state representation order = [Farmer, Fox, Chicken, Grain]

# globals
initial_state = [0, 0, 0, 0]  # all on left bank
final_state = [1, 1, 1, 1]  # all on right bank
illegal_states = [
    [0, 1, 1, 0],  # fox eats chicken
    [1, 0, 0, 1],  # fox eats chicken
    [0, 0, 1, 1],  # chicken eats grain
    [1, 1, 0, 0],  # chicken eats grain
    [0, 1, 1, 1],  # fox eats chicken eats grain
    [1, 0, 0, 0]   # fox eats chicken eats grain
]

# recursive function to find first solution
def search_tree(thisState, pathToGetHere):

    # check whether we have reached an illegal state
    if thisState in illegal_states:
        return -1

    # check whether we have reached a loop
    if thisState in pathToGetHere:
        return -1

    # add this state to path
    pathToGetHere.append(thisState)

    # check whether we have found a solution
    if thisState == final_state:
        return pathToGetHere

    # search next layer of nodes

    # try moving farmer to other bank
    newState = newTargetState(thisState,[0])
    result = search_tree(newState,pathToGetHere)
    if result != -1:
        # Success!
        return result

    # try moving farmer and fox to other bank
    newState = newTargetState(thisState,[0,1])
    result = search_tree(newState,pathToGetHere)
    if result != -1:
        # Success!
        return result

    # try moving farmer and chicken to other bank
    newState = newTargetState(thisState, [0, 2])
    result = search_tree(newState, pathToGetHere)
    if result != -1:
        # Success!
        return result

    # try moving farmer and grain to other bank
    newState = newTargetState(thisState, [0, 3])
    result = search_tree(newState, pathToGetHere)
    if result != -1:
        # Success!
        return result


# function to apply move to create new state
def newTargetState(currentState,itemsToFlip):
    newState = []
    for i in range(0, 4):
        if i in itemsToFlip:
            if currentState[i] == 0:
                newState.append(1)
            else:
                newState.append(0)
        else:
            newState.append(currentState[i])
    return newState


# now do it
solutionPath = []
result = search_tree(initial_state, solutionPath)
print(result)
count = len(result)
print(count)
