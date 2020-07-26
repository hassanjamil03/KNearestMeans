# implementing k means\

from scipy.spatial import distance as dist
from statistics import mean

"""
def kmeans(list dataset, list k_locations):
    for every point:
        calculate distance between point and all centroids and assign point to centroid with closest distance
    for every centroid:
        find midpoint between all points assigned to centroid and movecentroid to midpoint location
    if midpoint is equal to current centroid location for both centroids:
        return k_locations
    else:
        return kmeans(dataset, k_locations)

def gen_k(int k):
    for every num in k:
        generate random location and add to k_loc
    return k_loc
"""
class Centroid():
    def __init__(self, centroid=(0,0), points=[], midpoint=(0,0)):
        # tuple of the centroid location
        self.centroid = centroid

        # list of tuples of the dataset points locations nearest to it
        self.points = points

        # midpoint of all points in object
        self.midpoint = midpoint


def get_nearest_k(point, k_locations):
    distance = []
    for k in k_locations:
        if distance == [] or dist.euclidean(point, k) < distance[0]:
            distance = [dist.euclidean(point, k), k_locations.index(k)]
    return distance[1]


def get_mean(item):
    x = []
    y = []
    for i in item:
        x.append(i[0])
        y.append(i[1])
    return (mean(x), mean(y))


def kmeans(dataset, k_locations):
    # list containing all centroids
    centroids = []
    for k in k_locations:
        centroid = Centroid(k)
        centroids.append(centroid)

    # for every point:
    for point in dataset:
        # calculate distance between point and all centroids and assign point to centroid with closest distance
        k = get_nearest_k(point, k_locations)
        centroids[k].points.append(point)

    is_c_in_mid = []
    # for every centroid:
    for centroid in centroids:
        # find midpoint between all points assigned to centroid and move centroid to midpoint location
        centroid.midpoint = get_mean(centroid.points)

        # if midpoint is equal to current centroid location
        if centroid.midpoint == centroid.centroid:
            is_c_in_mid.append(True)
        else:
            is_c_in_mid.append(False)

    if is_c_in_mid.__contains__(False): # means we need to do another iteration of kmeans

        # return k_locations
    # else if :
        # return kmeans(dataset, k_locations)

def gen_k(k):
    pass
    # for every num in k:
        # generate random location and add to k_loc
    # return k_loc
