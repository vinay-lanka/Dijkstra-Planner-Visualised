import numpy as np
import cv2
 
#Initialising variables
start_pos = [0,0]
goal_pos = [0,0]
map_size = [1200,500]
frame = np.full([map_size[1],map_size[0],3], (0,255,0)).astype(np.uint8)

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
    cv2.imshow("Starting Map", frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def main():
    generate_map()

if __name__ == "__main__":
    main()