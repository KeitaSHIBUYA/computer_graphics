import math
import numpy as np

'''
intersect_sphere
PE: viewpoint
E: ray vector
P1, P2, P3: vertices of triangle
'''
def intersect_triangle(PE, E, P1, P2, P3):
    '''
    The value to return finally. 
    Set the initial value to infinity. 
    If an intersection is found, substitute the intersection point to this value.
    '''
    intersect_point = np.array([np.inf, np.inf, np.inf])

    ## Calculate the norm of E ##
    E_norm = np.linalg.norm(E)
    # print(E_norm)

    if E_norm != 0:
        E = E / E_norm
        N = np.cross(P1-P2, P2-P3)
        ## Calculate t to find the intersection point between the ray and the plane ##
        t = (np.dot((PE - P1), N) / np.dot(E, N)) * -1
        # print(t)

        if t > 0:
            ## Calculate the intersect point P between the ray and the plane using t ##
            P = np.dot(E, t) + PE
            N1 = np.cross(P2-P, P3-P)
            N2 = np.cross(P3-P, P1-P)
            N3 = np.cross(P1-P, P2-P)

            ## Judge whether the direction of the cross product N1, N2 and N3 is same ##
            if (np.dot(N1, N2) > 0).all() and (np.dot(N1, N3) > 0).all():
                intersect_point = P

    return intersect_point


if __name__ == "__main__":
    viewpoint = np.array([0, 0, 0])
    # ray       = np.array([1, 0, 0])        # for debug
    # ray       = np.array([1, 1/2, 1/4])    # for debug
    ray       = np.array([2, -1, 1])
    triangle  = np.array([[1, 1, 0], [1, -1, 1], [1, -1, -1]])

    PE = np.array([0, 4, 2])
    E = np.array([0, -1, -1])
    # print(intersect_triangle(viewpoint, ray, triangle[0], triangle[1], triangle[2]))
    print(intersect_triangle(PE, E, triangle[0], triangle[1], triangle[2]))