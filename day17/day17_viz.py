import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

def simulate(vx0, vy0):

  x, y, = 0, 0
  vx, vy = vx0, vy0
  ymax = float("-inf")
  trajec = [(0,0)]
  while True:
    
    x += vx
    y += vy
    if vx != 0:
      vx += -1 if vx > 0 else +1
    vy -= 1

    trajec.append((x,y))

    if x1 <= x <= x2 and y1 <= y <= y2:
      return True, trajec

    if x > x2 or y < y1:
      return False, trajec

# ----------------------------------------

x1, x2 = 209, 238
y1, y2 = -86, -59

# Determine range of x velocity
vx_min = 1
while True:
  max_x = vx_min*(vx_min+1)//2
  if max_x >= x1:
    break
  vx_min += 1
# print(vx_min)
vx_max = x2

# Set range of y velocity
vy_min = -100
vy_max = 100

solutions = []
for vx in range(vx_min, vx_max+1):
  for vy in range(vy_min, vy_max):
    hit_target, trajec = simulate(vx, vy)
    if hit_target:
      solutions.append(trajec)

# ----------------------------------------

# plt.figure(figsize=(6,12))
plt.figure(figsize=(6,6))

for trajec in solutions:
  xs, ys = zip(*trajec)
  plt.plot(xs, ys, "-", color="k", alpha=0.05, lw=1)

plt.scatter([0], [0], marker="+", color="red")
plt.gca().add_artist(Rectangle((x1,y1), x2-x1, y2-y1, fc="none", ec="red", zorder=50))
plt.gca().set_aspect("equal")
# plt.xlim(-150, 450)
# plt.ylim(-120, 1400)
plt.xlim(-20, 250)
plt.ylim(-90, 180)
plt.tight_layout()

plt.show()
