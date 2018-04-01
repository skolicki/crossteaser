import random
# encoding order: UFRBLD (up front right back left down)
# Y - yellow, O - orange, B - blue, G - green, V - violet, R - red

# Encode the exact initial and desired state (hint: that won't probably work due to number of combinations ;))
# initial_state = ["RYOVGB", "OYBVOG", "GYRVBO", "OYBVRG", "", "OYBVRG", "GYOVBO", "RYOVGB", "OYBVRG"]
# final_state = ["RYOVGB", "RYOVGB", "RYOVGB", "RYOVGB", "", "RYOVGB", "RYOVGB", "RYOVGB", "RYOVGB"]

# Or better encode just the position of one color, e.g. yellow, and the desired final state:
initial_state = ["**Y***", "***Y**", "*Y****", "Y*****", "", "***Y**", "****Y*", "*****Y", "***Y**"]
final_state = ["*Y****", "*Y****", "*Y****", "*Y****", "", "*Y****", "*Y****", "*Y****", "*Y****"]

def up(element):
    # FDRULB
    return element[1] + element[5] + element[2] + element[0] + element[4] + element[3]

def down(element):
    # BURDLF
    return element[3] + element[0] + element[2] + element[5] + element[4] + element[1]

def right(element):
    # URBLFD
    return element[0] + element[2] + element[3] + element[4] + element[1] + element[5]

def left(element):
    # ULFRBD
    return element[0] + element[4] + element[1] + element[2] + element[3] + element[5]

def move(state, direction):
    position = state.index('')
    if direction == 'L' and position not in [2, 5, 8]:
            state[position] = left(state[position + 1])
            state[position + 1] = ''
    elif direction == 'R' and position not in [0, 3, 6]:
            state[position] = right(state[position - 1])
            state[position - 1] = ''
    elif direction == 'U' and position not in [6, 7, 8]:
            state[position] = up(state[position + 3])
            state[position + 3] = ''
    elif direction == 'D' and position not in [0, 1, 2]:
            state[position] = down(state[position - 3])
            state[position - 3] = ''
    return state

best_solution = ""
checked = 0
visited = {str(initial_state) : ""}  # from initial
visited2 = {str(final_state) : ""}  # to final
while True:
    if checked % 1000 == 0:
        print "checked: ", checked, "best solution: ", len(best_solution), " : ", best_solution
    state = [el for el in initial_state]  # copy
    solution = ""
    for i in range(1000):  # forward
        m = random.choice(['L', 'R', 'U', 'D'])
        solution += m
        state = move(state, m)
        key = str(state)
        if key not in visited or len(visited[key]) > len(solution):
            visited[key] = solution
        else:
            solution = visited[key]  # shorten, also if equal
        if key in visited2:
            candidate = solution + visited2[key]
            if best_solution == "" or len(candidate) < len(best_solution):
                best_solution = candidate
            break
    state = [el for el in final_state]  # copy
    solution = ""
    for i in range(1000):  # backward
        m_back = random.choice(['L', 'R', 'U', 'D'])
        m = {'R' : 'L', 'L' : 'R', 'U' : 'D', 'D' : 'U'}.get(m_back)
        solution = m + solution
        state = move(state, m_back)
        key = str(state)
        if key not in visited2 or len(visited2[key]) > len(solution):
            visited2[key] = solution
        else:
            solution = visited2[key]
        if key in visited:
            candidate = visited[key] + solution
            if best_solution == "" or len(candidate) < len(best_solution):
                best_solution = candidate
            break
    checked += 1