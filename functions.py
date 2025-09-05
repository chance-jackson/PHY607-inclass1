import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import g as grav_const


def initial_conditions():
    pos_x, pos_y = input("Enter comma-separated initial position: ").split(",")
    vel_x, vel_y = input("Enter comma-separated initial velocity: ").split(",")

    C_d = float(input("Enter Drag Coefficient: "))
    m = float(input("Enter mass: "))
    dt = float(input("Enter time-step (s): "))

    pos_vec = {"pos_x":float(pos_x), "pos_y": float(pos_y)}
    vel_vec = {"vel_x":float(vel_x), "vel_y": float(vel_y)}
    force_vec = {"force_x": 0, "force_y": 0}
    
    return force_vec, vel_vec, pos_vec, C_d, m, dt

def update_force(force_vec,vel_vec,C_d,m):
    drag_mag = C_d*(vel_vec["vel_x"]**2 + vel_vec["vel_y"]**2)
    grav_mag = m * grav_const

    drag_angle = np.arctan2(vel_vec["vel_y"],vel_vec["vel_x"])
    
    Fd_x = -drag_mag * np.cos(drag_angle)
    Fd_y = -drag_mag * np.sin(drag_angle)
    Fg_y = -grav_mag

    force_vec["force_x"], force_vec["force_y"] = Fd_x, Fg_y + Fd_y
    
    return force_vec

def update_vel(force_vec,vel_vec,m,dt):
    accel_x,accel_y = force_vec["force_x"]/m, force_vec["force_y"]/m

    vel_vec["vel_x"], vel_vec["vel_y"] = vel_vec["vel_x"] + accel_x * dt, vel_vec["vel_y"] + accel_y * dt

    return vel_vec

def update_pos(pos_vec,vel_vec,dt):
    pos_vec["pos_x"], pos_vec["pos_y"] = pos_vec["pos_x"] + vel_vec["vel_x"] * dt, pos_vec["pos_y"] + vel_vec["vel_y"] * dt

    return pos_vec

def calculate_KE(vel_vec,m):
    v_square = (vel_vec["vel_x"]**2 + vel_vec["vel_y"]**2)
    return (1/2)*m*v_square

def calculate_PE(pos_vec,m):
    return m*grav_const*pos_vec["pos_y"]
