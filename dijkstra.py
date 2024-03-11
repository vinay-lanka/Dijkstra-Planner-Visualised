'''
Dikjstra Algorithm
dijkstra.py
Author - Vinay Lanka
vlanka@umd.edu
120417665
'''

#Github link to repository - https://github.com/vinay-lanka/Dijkstra-Planner-Visualised

#Imports
import numpy as np
import cv2
from heapq import *
import copy
import time

#Initialising variables for map and frame
start_pos = [0,0]
goal_pos = [0,0]
map_size = [1200,500]
frame = np.full([map_size[1],map_size[0],3], (0,255,0)).astype(np.uint8)

#Goal found flag to stop exploring nodes
goal_found = False

#Priority queue used for dijkstra
nodes = []
heapify(nodes)

#Size for output video frames
size = (1200, 500)
result = cv2.VideoWriter('dijkstra.mp4',
                         cv2.VideoWriter_fourcc(*'MP4V'),
                         20, size)

# Function to generate the map and add obstacles
def generate_map():
    #Walls
    walls_inflated = np.array([[[5,5],
            [map_size[0]-5,5], 
            [map_size[0]-5,map_size[1]-5],
            [0+5, map_size[1]-5]]
    ])
    #Obstacles
    rectangles_inflated = np.array([
        [(95,5),(180,5),(180,405),(95,405)],
        [(270,95),(355,95),(355,495),(270,495)]
    ]) 
    rectangles = np.array([
        [(100,0),(175,0),(175,400),(100,400)],
        [(275,100),(350,100),(350,500),(275,500)]
    ])
    hexagon_inflated = np.array([
        [(650,95),(785,172),(785,328),(650,405),(515,328),(515,172)]
    ]) 
    hexagon = np.array([
        [(650,100),(780,175),(780,325),(650,400),(520,325),(520,175)]
    ])
    random_shape_inflated = np.array([
        [(895,45),(1105,45),(1105,455),(895,455),(895,370),(1015,370),(1015,130),(895,130)]
    ]) 
    random_shape = np.array([
        [(900,50),(1100,50),(1100,450),(900,450),(900,375),(1020,375),(1020,125),(900,125)]
    ]) 
    cv2.fillPoly(frame, pts=walls_inflated, color=(255, 255, 255))
    cv2.fillPoly(frame, pts=rectangles_inflated, color=(0, 255, 0))
    cv2.fillPoly(frame, pts=rectangles, color=(0, 0, 0))
    cv2.fillPoly(frame, pts=hexagon_inflated, color=(0, 255, 0))
    cv2.fillPoly(frame, pts=hexagon, color=(0, 0, 0))
    cv2.fillPoly(frame, pts=random_shape_inflated, color=(0, 255, 0))
    cv2.fillPoly(frame, pts=random_shape, color=(0, 0, 0))
    # cv2.imshow("Starting Map", frame)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

# FUnction to validate input coordinates
def input_validation(position):
    #Check if input in map
    if 5 < position[0] < 1195:
        pass
    else:
        return False
    if 5 < map_size[1] - position[1] < 495:
        pass
    else:
        return False
    #Check if in obstacle
    if np.all(frame[position[1],position[0]]):
        return True
    else:
        return False

# Function to take input coordinates and pass to validation function
def set_start_goal_pos():
    global start_pos, goal_pos
    positions_valid = False
    print("Enter Start and Goal Coordinates")
    print("Map size is 1200x500 with a clearance of 5")
    print("Enter Coordinate as x,y (x and y seperated with a comma)")
    while not positions_valid:
        start_ip = input("Enter start x,y coordinate: ") or "6,6"
        start_pos = list(int(x) for x in start_ip.split(","))
        start_pos[1] = map_size[1] - start_pos[1]
        positions_valid = input_validation(start_pos)
        if not positions_valid:
            print("Enter valid coordinates")
            continue
        goal_ip = input("Enter goal x,y coordinate: ") or "1194,494"
        goal_pos = list(int(x) for x in goal_ip.split(","))
        goal_pos[1] = map_size[1] - goal_pos[1]
        positions_valid = input_validation(goal_pos)
        if not positions_valid:
            print("Enter valid coordinates")
            continue
    
    start_goal_frame = copy.deepcopy(frame)
    start_goal_frame = cv2.circle(start_goal_frame, start_pos, 5, (0,0,255), -1) 
    start_goal_frame = cv2.circle(start_goal_frame, goal_pos, 5, (255,0,0), -1) 
    # cv2.imshow("Starting positons", start_goal_frame)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

#Backtrack dictionary for path backtracking
backtrack_dict = {}

# Function for validating a neighbour 
def position_validation(position):
    global goal_found
    #Check if goal is found
    if [int(position[2]),int(position[3])] == goal_pos:
        backtrack_dict[(int(position[2]),int(position[3]))] = (int(position[4]),int(position[5]))
        print("Goal reached")
        goal_found = True
    #Check if neighbour in map
    if 5 < position[2] < 1195:
        pass
    else:
        return
    if 5 < position[3] < 495:
        pass
    else:
        return
    #Check if the neighbour is in an obstacle or is already visited
    if np.all(frame[int(position[3]),int(position[2])]):
        frame[int(position[3]),int(position[2])] = [255,0,0]
        #child -> parent
        backtrack_dict[(int(position[2]),int(position[3]))] = (int(position[4]),int(position[5]))
        position[0] = position[0]+position[1]
        heappush(nodes,[position[0],position[2],position[3]])
        return
    else:
        return
    
# Function to add the neighbours of a possible node
def add_neighbours(position):
    c,x,y = position[0], position[1], position[2]
    # print(x,500-y)
    position_validation([c,1,x+1,y,x,y])
    position_validation([c,1,x-1,y,x,y])
    position_validation([c,1,x,y+1,x,y])
    position_validation([c,1,x,y-1,x,y])
    position_validation([c,1.4,x+1,y+1,x,y])
    position_validation([c,1.4,x-1,y+1,x,y])
    position_validation([c,1.4,x+1,y-1,x,y])
    position_validation([c,1.4,x-1,y-1,x,y])

# Function to find the path to a goal node using backtracking dict
def backtrack():
    parent_pixel = backtrack_dict[(goal_pos[0],goal_pos[1])]
    start_to_goal = [parent_pixel]
    while not parent_pixel == (start_pos[0],start_pos[1]):
        start_to_goal.append(parent_pixel)
        parent_pixel = backtrack_dict[parent_pixel]
        # print(backtrack_dict[(goal_pos[0],goal_pos[1])])
        # frame[parent_pixel[1],parent_pixel[0]] = [255,0,255]
    start_to_goal.reverse()
    count=0
    for pixel in start_to_goal: 
        cv2.circle(frame, [pixel[0],pixel[1]], 2, (0,255,255), -1) 
        if count%10 == 0:
            # cv2.imshow("Starting Map", frame)
            result.write(frame)
            # if cv2.waitKey(1) == ord('q'):
            #     break
        count = count+1
    
# The code dijkstra algorithm, using priority queues to pop nodes and add neighbours back to a heap
def djikstra():
    current_pos = [0,start_pos[0],start_pos[1]]
    frame[int(current_pos[1]),int(current_pos[0])] = [255,0,0]
    add_neighbours(current_pos)
    count = 0
    while not goal_found:
        current_pos = heappop(nodes)
        add_neighbours(current_pos)
        if count%500 == 0:
            result.write(frame)
            # cv2.imshow("Starting Map", frame)
            # if cv2.waitKey(1) == ord('q'):
            #     break
        count = count+1
    backtrack()
    result.release()
    cv2.destroyAllWindows()
    return

# Visualise the output video generated
def visualise():
    cap = cv2.VideoCapture('dijkstra.mp4')
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Exiting, end of video?")
            break
        cv2.imshow('Dijkstra Visualisation', frame)
        time.sleep(0.05)
        if cv2.waitKey(1) == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

#Run all functions in order
def main():
    generate_map()
    set_start_goal_pos()
    start_time = time.time()
    print("Starting position of the robot", start_pos[0], ",", map_size[1] - start_pos[1])
    print("Goal position of the robot", goal_pos[0], ",", map_size[1] - goal_pos[1])
    djikstra()
    end_time = time.time()
    print("Time taken for solution: ", end_time - start_time)
    visualise()

if __name__ == "__main__":
    main()