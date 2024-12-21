# THOSE ARE NAMED PROCESSED. FOR THE PLOT OF THE CYCLE, WE NEED TO DEFINE THE PROCESSES AND THE STEPS

# TODO: Need: Diagram (p-v) (t-s) for the cycle
# TODO: Pressure and hentalpy at each state
# TODO: Mass flow
# TODO: Efficiency

from src.processes import Isochoric, Isobaric, Isentropic
from src.cycle import Cycle
from src.point import Point

######################################
# Diesel cycle - Exercise 3
######################################
# # Define the points
# p1 = Point("P1", T=298, p=1)
# p2 = Point("P2", p=50)
# p3 = Point("P3", T=1600)
# p4 = Point("P4")
# 
# # Define the cycles
# cycle = Cycle(R=287, gamma=1.4)
# cycle.add_step(Isentropic(p1, p2))
# cycle.add_step(Isobaric(p2, p3))
# cycle.add_step(Isentropic(p3, p4))
# cycle.add_step(Isochoric(p4, p1))
# 
# # Solve the cycle
# cycle.solve()
# 
# print(p1)
# print(p2)
# print(p3)
# print(p4)


######################################
# Otto cycle - Tutorial 3
######################################
# Define the points
p1 = Point("P1", T=300, p=1)
p2 = Point("P2", v=0.0703 * 100000)
p3 = Point("P3", T=1600)
p4 = Point("P4")

step1 = Isentropic(p1, p2)
step2 = Isochoric(p2, p3)
step3 = Isentropic(p3, p4)
step4 = Isochoric(p4, p1)

# Define the cycles
cycle = Cycle(R=287, gamma=1.4)
cycle.add_step(step1)
cycle.add_step(step2)
cycle.add_step(step3)
cycle.add_step(step4)

# Solve the cycle
cycle.solve()
cycle.solve()

print(p1)
print(p2)
print(p3)
print(p4)

print(step1.work())
print(step2.work())
print(step3.work())
print(step4.work())

print((step3.work() + step1.work()) * 8) 
