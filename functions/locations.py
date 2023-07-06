from functions import *


def polygon_random_points(poly, num_points):
    min_x, min_y, max_x, max_y = poly.bounds
    points = []
    while len(points) < num_points:
        random_point = Point([random.uniform(min_x, max_x), random.uniform(min_y, max_y)])
        if random_point.within(poly):
            points.append(random_point)

    return points


# Choose the number of points desired. This example uses 20 points.


def get_geo(city):
    match city:
        case "msk":
            geo = Polygon([(55.76664217677472, 37.536612561151145), (55.78421407372232, 37.551375439569114),
                           (55.78749585758228, 37.589827588006614), (55.77398085539273, 37.600813916131614),
                           (55.75640434392775, 37.585021069451926), (55.74442459958629, 37.57300477306521),
                           (55.74597057977355, 37.510863354608176)])
        case "piter":
            geo = Polygon([(59.862221743726344, 30.23731712041689), (59.843254994647296, 30.337567364557515),
                           (59.86773731376941, 30.456357037409077), (59.91905715596102, 30.47077659307314),
                           (59.992282844026626, 30.44056419072939), (60.033465533251054, 30.401425396784077),
                           (60.02283158573057, 30.255169903620015), (59.94589097499788, 30.202298199518452)])

    return geo


def get_points(city):
    geo = get_geo(city)
    points = polygon_random_points(geo, 1)

    for p in points:
        latitude = str(p.x)
        longitude = str(p.y)

    return latitude, longitude
