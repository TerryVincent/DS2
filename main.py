#Vishnu Krishnakumar #001145833



import csv
from datetime import *


class HashMap:
    def __init__(self):
        self.size = 40
        self.map = [None] * self.size

    def _get_hash(self, key):
        hash = 0
        for char in str(key):
            hash += ord(char)
        return hash % self.size

    def add(self, key, value, value2, value3, value4, value5, value6, value7):
        key_hash = self._get_hash(key)
        key_value = [key, value, value2, value3, value4, value5, value6, value7]

        if self.map[key_hash] is None:
            self.map[key_hash] = list([key_value])
            return True
        else:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.map[key_hash].append(key_value)
            return True

    def get(self, key):
        key_hash = self._get_hash(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[7]
        return None

    def delete(self, key):
        key_hash = self._get_hash(key)

        if self.map[key_hash] is None:
            return False
        for i in range(0, len(self.map[key_hash])):
            if self.map[key_hash][i][0] == key:
                self.map[key_hash].pop(i)
                return True
        return False

    def keys(self):
        arr = []
        for i in range(0, len(self.map)):
            if self.map[i]:
                arr.append(self.map[i][0])
        return arr

    def print(self):
        for item in self.map:
            if item is not None:
                print(str(item))


class Truck:
    packages = [16]


# construct the package file hashmap by reading in the csv file, this is O(N)
with open('WGUPS Package File-1.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    h = HashMap()
    dates = []
    packages = []
    for row in readCSV:
        date = row[0]
        address = row[1]
        city = row[2]
        zip = row[4]
        time = row[5]
        weight = row[6]
        location = 'hub'
        place = row[8]
        h.add(date, address, city, zip, time, weight, location, place)
        packaging = [date, address, city, zip, time, weight, location, place]
        packages.append(packaging)
    csvfile.close()
distances_list = []

# construct the distance adjacent matrix graph by reading in the csv file, this is O(N)
with open('WGUPS Distance Table.csv') as csv_distance_file:
    readCSV = csv.reader(csv_distance_file, delimiter=',')
    for row in readCSV:
        distances_list.append(row)

    csv_distance_file.close()

# Using one truck , with packages manually loaded. One truck is taking multiple trips
trucks = [1, 7, 13, 14, 15, 16, 19, 20, 21, 29, 30, 31, 34, 37, 39, 40]
truck2 = [3, 6, 18, 25, 28, 32, 36, 38]
truck3 = [2, 4, 5, 8, 9, 10, 11, 12, 17, 22, 23, 24, 26, 27, 33, 35]

# sets the distance comparison variable to a high enough number
lowest = 10000.0
# sets where the last accepted point was put in.
index = 0
# A list that represents delivered packages in their appropriately sorted order
delivered = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
s = 0
# Used to identify that package number found.
found = 0
# Total amount of miles traveled
total = 0
# The time in minutes of packages delivered
time = 0
# The start time of the day
start = datetime(2021, 4, 5, 8, 0, 0, 0)

# Finds the starting point on the first truck trip, this is O(N)
for i in trucks:

    if float(distances_list[int(h.get(str(i))) - 1][0]) < lowest:
        lowest = float(distances_list[int(h.get(str(i))) - 1][0])
        index = int(h.get(str(i))) - 1
        found = i
delivered[s] = found
packages[found - 1][6] = "delivered" + str(start + timedelta(minutes=time))
trucks.remove(found)
total = total + lowest
lowest = 100000.0
s += 1
time += total * 3.3
print(time)

while delivered[15] == 0:

    # This algorithm looks for the nearest package to go to next, this is O(N).
    # This is accomplished by finding the index from the previous starting point code block, which is used to compare
    # and help find where to go in the adjacency graph matrix
    for i in trucks:
        if index > int(h.get(str(i))) - 1:
            test = float(distances_list[index][int(h.get(str(i))) - 1])
            if test < lowest:
                index = int(h.get(str(i))) - 1

        if index < int(h.get(str(i))) - 1:
            test = float(distances_list[int(h.get(str(i))) - 1][index])
            if test < lowest:
                index = int(h.get(str(i))) - 1

        if test < lowest:
            lowest = test
            found = i
    delivered[s] = found
    trucks.remove(found)
    total = total + lowest
    time += lowest * 3.3
    packages[found - 1][6] = "delivered " + str(start + timedelta(minutes=time))
    if datetime(2021, 4, 5, 8, 35, 0, 0) < start + timedelta(minutes=time) < datetime(2021, 4, 5, 8, 40, 0, 0):
        print('Packages between 8:35 a.m. and 8:40 a.m.')
        for x in packages:
            print(x)
    if datetime(2021, 4, 5, 9, 35, 0, 0) < start + timedelta(minutes=time) < datetime(2021, 4, 5, 9, 40, 0, 0):
        print('Packages between 9:35 a.m. and 9:40 a.m.')
        for x in packages:
            print(x)
    lowest = 100000.0
    s += 1
lowest = 10000.0
index = 0
delivered = [0, 0, 0, 0, 0, 0, 0, 0]
s = 0
found = 0
# Finds the starting point on the second truck trip, this is O(N)
for i in truck2:

    if float(distances_list[int(h.get(str(i))) - 1][0]) < lowest:
        lowest = float(distances_list[int(h.get(str(i))) - 1][0])
        index = int(h.get(str(i))) - 1
        found = i
delivered[s] = found
packages[found - 1][6] = "delivered" + str(start + timedelta(minutes=time))
truck2.remove(found)
total = total + lowest
time += lowest * 3.3
lowest = 100000.0
s += 1

while delivered[7] == 0:

    # This algorithm looks for the nearest package to go to next, this is O(N)
    # This is accomplished by finding the index from the previous starting point code block, which is used to compare
    # and help find where to go in the adjacency graph matrix
    for i in truck2:
        if index > int(h.get(str(i))) - 1:
            test = float(distances_list[index][int(h.get(str(i))) - 1])
            if test < lowest:
                index = int(h.get(str(i))) - 1

        if index < int(h.get(str(i))) - 1:
            test = float(distances_list[int(h.get(str(i))) - 1][index])
            if test < lowest:
                index = int(h.get(str(i))) - 1

        if test < lowest:
            lowest = test
            found = i
    delivered[s] = found
    time += lowest * 3.3
    packages[found - 1][6] = "delivered " + str(start + timedelta(minutes=time))
    truck2.remove(found)
    total = total + lowest
    if datetime(2021, 4, 5, 12, 3, 0, 0) < start + timedelta(minutes=time) < datetime(2021, 4, 5, 12, 10, 0, 0):
        print('Packages between 12:03 p.m. and 12:10 p.m.')
        for x in packages:
            print(x)
    lowest = 100000.0
    s += 1
lowest = 10000.0
index = 0
delivered = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
s = 0
found = 0

# Finds the starting point on the third truck trip, this is O(N)
for i in truck3:

    if float(distances_list[int(h.get(str(i))) - 1][0]) < lowest:
        lowest = float(distances_list[int(h.get(str(i))) - 1][0])
        index = int(h.get(str(i))) - 1
        found = i
delivered[s] = found
packages[found - 1][6] = "delivered" + str(start + timedelta(minutes=time))
truck3.remove(found)
total = total + lowest
s += 1
time += lowest * 3.3
lowest = 100000.0

while delivered[15] == 0:

    # This algorithm looks for the nearest package to go to next, this is O(N)
    # This is accomplished by finding the index from the previous starting point code block, which is used to compare
    # and help find where to go in the adjacency graph matrix
    for i in truck3:
        if index > int(h.get(str(i))) - 1:
            test = float(distances_list[index][int(h.get(str(i))) - 1])
            if test < lowest:
                index = int(h.get(str(i))) - 1

        if index < int(h.get(str(i))) - 1:
            test = float(distances_list[int(h.get(str(i))) - 1][index])
            if test < lowest:
                index = int(h.get(str(i))) - 1

        if test < lowest:
            lowest = test
            found = i
    delivered[s] = found
    time += lowest * 3.3
    packages[found - 1][6] = "delivered " + str(start + timedelta(minutes=time))
    truck3.remove(found)
    if datetime(2021, 4, 5, 12, 3, 0, 0) < start + timedelta(minutes=time) < datetime(2021, 4, 5, 12, 10, 0, 0):
        print('Packages between 12:03 p.m. and 12:10 p.m.')
        for x in packages:
            print(x)
    total = total + lowest
    lowest = 100000.0
    s += 1

print(" ")
print("EOD package list")
print(" ")
# prints the EOD package list, this is O(N) linear
for x in packages:
    print(x)
print(total, " miles in total for delivery")
