import numpy as np
import matplotlib.pyplot as plt

def initial_conditions():
    pos_x, pos_y = input("Enter comma-separated initial position: ")
    vel_x, vel_y = input("Enter comma-separated initial velocity: ")

    C_d = input("Enter Drag Coefficient: ")
    m = input("Enter mass: ")

    pos_vec = {"pos_x":pos_x, "pos_y": pos_y}
    vel_vec = {"vel_x":vel_x, "vel_y": vel_y}

    return pos_vec, vel_vec, C_d, m

pos_vec, vel_vec, C_d, m = initial_conditions()

