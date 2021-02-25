from collections import deque

maze = {}
maze["goal"] = ["1", "2", "5"]
maze["1"] = ["2", "goal"]
maze["2"] = ["3", "1"]
maze["3"] = ["4", "2"]
maze["4"] = ["9", "3"]
maze["9"] = ["13", "4"]
maze["13"] = ["18", "9"]

maze["18"] = ["17", "23", "13"]
maze["23"] = ["18", "22"]
maze["17"] = ["16", "22", "18"]
maze["16"] = ["start", "21", "17"]
maze["start"] = ["16"]

maze["22"] = ["17", "21", "23"]
maze["21"] = ["22", "20", "16"]
maze["20"] = ["19", "21"]
maze["19"] = ["14", "20"]
maze["14"] = ["19", "10"]
maze["10"] = ["14", "5"]
maze["5"] = ["10", "goal"]


visited_points = []
current_point = "start"

def search(maze, current_point, visited_points):
    
    search_queue = deque()
    search_queue += [current_point]

    visited_points.append(current_point)
    search_queue += maze[current_point]

    parents = {}
    path = []

    while search_queue:
        current_point = search_queue.popleft()
        neighbors = maze[current_point]

        for neighbor in neighbors:
            if neighbor not in visited_points:
                parents[neighbor] = current_point
                visited_points.append(neighbor)
                search_queue += maze[neighbor]
                if "goal" in maze[neighbor]:
                    path.append("goal")
                    current_point = neighbor
                    path.append(current_point)
                    
                    while current_point != "start":
                        current_point = parents[current_point]
                        path.append(current_point)

                    return path 

    return "No path to goal"
    
if __name__ == "__main__":
    print(search(maze, current_point, visited_points))
