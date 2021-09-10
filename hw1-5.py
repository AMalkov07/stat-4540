import math

# part (d)
with open('C:\\Users\\Andrey\\Downloads\\ml-100k\\ml-100k\\u.data', 'r') as f:
    ratings_data = []
    for line in f:
        ratings_data.append(line.split('\t'))
arr = []
for i in range(1682):
    arr.append([0, 0])
for i in range(0, len(ratings_data)):
    index = int(ratings_data[i][1])-1
    arr[index][1]+=1
    if(int(ratings_data[i][2])>3):
        arr[index][0]+=1
pop = []
for i in range(len(arr)):
    p = int(arr[i][0])/int(arr[i][1])
    pop.append(math.log((p+.5)/((1-p)+1), 10))
print("question (d) output:")
for i in range(5):
    print(pop[i])

# part (e)
matrixG = []
ratings = []
output = []
with open('C:\\Users\\Andrey\\Desktop\\G.csv', 'r') as f:   # r output file
    for line in f:
        matrixG.append(line.rstrip().split(','))
for i in range (100000):
    output.append([0,0,0,0,0])
    index = int(ratings_data[i][1])-1
    output[i][0]=pop[index]
    for j in range(4):
        output[i][j+1]=matrixG[index][j]
print("\nquestion (e) output:")
for i in range(5):
    print(output[i])
with open('C:\\Users\\Andrey\\Desktop\\ratings.csv', 'r') as f:   # r output file
    counter = 0
    for line in f:
        if counter == 5:
            break
        counter+=1
        print(line.rstrip())