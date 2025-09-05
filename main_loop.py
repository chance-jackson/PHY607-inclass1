import functions as func
import matplotlib.pyplot as plt

force_vec, vel_vec, pos_vec, C_d, m, dt = func.initial_conditions() #pull initial conditions

pos_hist_x, pos_hist_y = [],[] #define lists to store position history
KE,PE,TE = [],[],[]
while pos_vec["pos_y"] >= 0:
    updated_force = func.update_force(force_vec, vel_vec, C_d, m) #update force vector
    updated_vel = func.update_vel(force_vec, vel_vec, m, dt)      #update velocity vector
    updated_pos = func.update_pos(pos_vec, vel_vec, dt)           #update position vector

    pos_vec = updated_pos
    vel_vec = updated_vel
    force_vec = updated_force
    
    pos_hist_x.append(pos_vec["pos_x"])
    pos_hist_y.append(pos_vec["pos_y"])
    
    KE.append(func.calculate_KE(vel_vec,m))
    PE.append(func.calculate_PE(pos_vec,m))
    TE.append(KE[-1] + PE[-1])

fig, axs = plt.subplots(ncols = 2,layout='constrained')
axs[0].plot(pos_hist_x,pos_hist_y)
axs[0].set_xlabel('X-position [m]')
axs[0].set_ylabel("Y-position [m]")

axs[1].plot(pos_hist_x,KE,label='KE')
axs[1].plot(pos_hist_x,PE,label='PE')
axs[1].plot(pos_hist_x,TE,label='TE')
axs[1].set_xlabel('X-position [m]')
axs[1].set_ylabel('Energy [J]')
axs[1].legend(loc='upper right')

plt.show()
