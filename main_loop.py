import functions as func
import matplotlib.pyplot as plt

force_vec, vel_vec, pos_vec, C_d, m, dt = func.initial_conditions() #pull initial conditions

pos_y = pos_vec["pos_y"]
pos_hist_x, pos_hist_y = [],[] #define lists to store position history
while pos_y > 0:
    updated_force = func.update_force(force_vec, vel_vec, C_d, m) #update force vector
    updated_vel = func.update_vel(force_vec, vel_vec, m, dt)      #update velocity vector
    updated_pos = func.update_pos(pos_vec, vel_vec, dt)           #update position vector

    pos_vec = updated_pos
    vel_vec = updated_vel
    force_vec = updated_force
    
    pos_hist_x.append(pos_vec["pos_x"])
    pos_hist_y.append(pos_vec["pos_y"])

    pos_y = pos_vec["pos_y"]

plt.plot(pos_hist_x,pos_hist_y)
plt.savefig("position.png",dpi=300)
