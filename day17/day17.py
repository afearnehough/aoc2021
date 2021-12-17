import math

input = [list((map(int, it.strip()[2:].split("..")))) for it in open("input.txt").read()[13:].split(",")]

sx, sy = 0, 0
dlta = sy-input[1][0]

print("Part 1: %d" % sum(list(range(dlta))))

def xvels(a, b):
    result = [(b-a)]
    for vel in reversed(range(math.ceil(result[0]/2)+1)):
        c, d = vel, result[0]
        while c > 0:
            d -= c
            c -= 1
            if d == 0:
                result.append(vel)
    return result

velocities = []
for tx in range(input[0][0], (input[0][1]+1)):
    for vx in xvels(sx, tx):
        for ty in range(input[1][0], (input[1][1]+1)):
            for vy in range(ty, dlta):
                px, py, pvx, pvy = sx, sy, vx, vy
                while py > ty:
                    px += pvx
                    pvx = max(0, (pvx-1))
                    py += pvy
                    pvy -= 1
                    if px == tx and py == ty:
                        velocities.append((vx, vy))

print(velocities)
print(len(set(velocities)))