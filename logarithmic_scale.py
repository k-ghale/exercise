import math
def log_scale(data, base):
    result = []
    for i in range(len(data)):
        result.append(math.log(data[i], base))
    return result


# implementation 1

data = [1, 10, 100, 1000]
base = 10

print(log_scale(data, base))

# implementation 2

data = [2, 4, 8, 16]
base = 2

print(log_scale(data, base))

