# TRANSFORM
# The Transform step on Extract-Transform-Load (ETL)

one_point = ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T']
two_points = ['D', 'G']
three_points = ['B', 'C', 'M','P']
four_points = ['F', 'H', 'V', 'W', 'Y']
five_points = ['K']
eigth_points = ['J', 'X']
ten_points = ['Q', 'Z']

points = {1: one_point, 2: two_points, 3: three_points, 4: four_points, 5: five_points, 8: eigth_points, 10: ten_points}

def transform_data(d):
    new_d = {}

    for k in d.keys():        
        for l in d[k]:
            for i in range(len(l)):
                new_d[l[i].lower()] = k
    
    return new_d
    
print('Old Dictionary: ', points)
print('New Dictionary: ', transform_data(points))
