from sim import *

sim = Sim(dim = (600,600),fps = 30,rocket_color = (255,255,255),rotation = 0,desired_rot = 0,mmoi = .2)
sim.set_bg_color((120,150,255))
sim.set_caption("Blah")
sim.rocket.set_angle(-45)
sim.simulate()
