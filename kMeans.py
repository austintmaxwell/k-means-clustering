# Assignment header
"""
Austin Maxwell
January 28, 2024
Spring 2024 - Data 51100 - Section 002
Programming Assignment #2
"""

# K-Means Algorithm
"""
Step 1: Pick K
Step 2: Initialize with K centroids
Step 3: Assign points to clusters
Step 4: Adjust the centroid based on the mean of the centroids
Step 5: Repeat steps 3 & 4 until convergence
"""

# Initializing dataset needed for algorithm
with open(r'/Users/austinmaxwell/prog2-input-data.txt', 'r') as f:
    data = [float(line.strip()) for line in f]
    
# Initialize variables needed for algorithm
k = int(input("Enter the number of clusters: ")) # Step 1
centroids = data[:k] # Step 2
iteration = 0

# Creating helper functions
# Function to calculate average of data points in cluster
def get_average(cluster_points):
    return sum(cluster_points) / len(cluster_points)

# Function to find key based on value
def get_key(val):
    for key, value in clusters.items():
        if val in value:
            return key
 
    return "DNE"

# Steps 3 -> 5
while True:
    iteration += 1
    clusters = {i: [] for i in range(k)}
    
    # Loop to shift points between clusters based on distance from centroid
    for point in data:
        distances = [abs(point - centroid) for centroid in centroids]
        cluster = distances.index(min(distances))
        clusters[cluster].append(point)
        
    print("\n")
    print(f"Iteration {iteration}")
    for cluster, points in clusters.items():
        print(cluster, points)

    # Computes new centroids (averages of clusters)
    new_centroids = [get_average(points) for points in clusters.values()]
   
    # Breaks the loop once convergence has been reached
    if new_centroids == centroids:
        print("\n")
        break
    
    # Sets the new centroid list for next loop
    centroids = new_centroids
    
# Creates and populates output file while printing to the terminal
with open(r'/Users/austinmaxwell/prog2-output-data.txt', 'w') as f:
    for point in data:
        f.write(f"Point {point} in cluster {get_key(point)}\n")
        print(f"Point {point} in cluster {get_key(point)}")
