from .objects import Ray, Sphere, Triangle
from .objects import point,Ray, Sphere, Triangle
import numpy as np


def intersect(first_object, second_object):
    if isinstance(first_object,Ray) and isinstance(second_object,Sphere):
        return _intersect_ray_with_sphere(first_object,second_object)

    if isinstance(first_object,Ray) and isinstance(second_object,Triangle):
        return _intersect_ray_with_triangle(first_object,second_object)

    ...


def _intersect_ray_with_sphere(ray, sphere):
    diff_sphereCenter_rayOrigin = np.subtract(Ray._origin,Sphere._center)
    nabla = (np.dot(Ray._direction,diff_sphereCenter_rayOrigin))**2 - ((np.dot(diff_sphereCenter_rayOrigin,diff_sphereCenter_rayOrigin)) - Sphere._radius**2)
    if nabla < 0:
        points.append(Point((Ray._origin) + (d*Ray._direction))) # two intersection points, if a ray passes through the sphere
    return np.array(points)    


    ...


def _intersect_ray_with_triangle(ray, triangle):
    ...
