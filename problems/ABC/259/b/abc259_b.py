import numpy as np

a, b, d = map(int, input().split())

def R(theta):
    theta = np.deg2rad(theta)
    return np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])

R = R(d)
ab = np.array([a, b])
ab_ = R.dot(ab)
print(ab_[0], ab_[1])