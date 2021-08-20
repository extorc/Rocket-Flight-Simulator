from sim import *

sim = Sim((120,150,255),(600,600),"Rocket Simulator",30,(255,255,255),0,0,.1)
sim.rocket.set_angle(-45)
sim.simulate()
