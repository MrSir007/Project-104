import csv
from collections import Counter

# To open and read a csv file
with open ("HeightWeight.csv", newline='') as hw :
  hwread = csv.reader(hw)
  # To convert the read files into list
  filedata = list(hwread)

# To remove the title of the data
filedata.pop(0)
newdata = []
for i in range (len(filedata)) :
  height = filedata[i][1]
  newdata.append(float(height))

# To calculate the mean
n1 = len(newdata)
total = 0
for i in newdata :
  total += i
mean = total/n1

print("The mean is", str(mean))

# To calculate the median
n2 = len(newdata)
newdata.sort()

if (n2%2 == 0) :
  m1 = float(newdata[n2//2])
  m2 = float(newdata[n2//2-1])
  median = (m1+m2)/2
else :
  median = newdata[n2//2]

print("The median is", str(median))

# To calculate the mode
data = Counter(newdata)
modelist = {
  "75-85": 0,
  "85-95": 0,
  "95-105": 0,
  "105-115": 0,
  "115-125": 0,
  "125-135": 0,
  "135-145": 0,
  "145-155": 0,
  "155-165": 0,
  "165-175": 0
}
for height, occurence in data.items() :
  if 75 < float(height) < 85 :
    modelist["75-85"] += occurence
  elif 85 < float(height) < 95 :
    modelist["85-95"] += occurence
  elif 95 < float(height) < 105 :
    modelist["95-105"] += occurence
  elif 105 < float(height) < 115 :
    modelist["105-115"] += occurence
  elif 115 < float(height) < 125 :
    modelist["115-125"] += occurence
  elif 125 < float(height) < 135 :
    modelist["125-135"] += occurence
  elif 135 < float(height) < 145 :
    modelist["135-145"] += occurence
  elif 145 < float(height) < 155 :
    modelist["145-155"] += occurence
  elif 155 < float(height) < 165 :
    modelist["155-165"] += occurence
  elif 165 < float(height) < 175 :
    modelist["165-175"] += occurence
moderange, modeoccur = 0, 0
for range, occur in modelist.items() :
  if occur > modeoccur :
    moderange, modeoccur = [int(range.split("-")[0]), int(range.split("-")[0])], occur
mode = float((moderange[0]+moderange[1])/2)
print("The mode is", str(mode))