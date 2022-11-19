def get_result_div(n, wires):
    i = 0
    gp = set()
    gp.add(wires[0][0])
    changed = False
    
    while True:
        if (i >= len(wires) and changed == False) or len(wires)== 0:
            break
        if i >=len(wires):
            changed = False
            
        i = i % len(wires)
        wire = wires[i]
        if wire[0] in gp and wire[1] not in gp:
            gp.add(wire[1])
            wires.pop(i)
            changed = True
        elif wire[1] in gp and wire[0] not in gp:
            gp.add(wire[0])
            wires.pop(i)
            changed = True
        else:
            i = i+1
    return min(len(gp), n-len(gp)), max(len(gp), n-len(gp)) 

def solution(n, wires):
    min_diff = n
    for i in range(len(wires)):
        temp_wires = wires[:]
        temp_wires.pop(i)
        mi, mx = get_result_div(n, temp_wires)
        if mi == mx or mx-mi == 1: 
            min_diff = mx - mi
            break
        if min_diff > mx - mi:
            min_diff = mx - mi
    return min_diff
