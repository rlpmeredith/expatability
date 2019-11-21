from numpy import genfromtxt
file_name = "../../data/world_happiness.csv"
data = genfromtxt(file_name, delimiter=',', skip_header=1, converters={0: lambda s: str(s)})
print(type(data))