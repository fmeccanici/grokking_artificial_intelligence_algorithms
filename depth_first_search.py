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

def search(maze, root_point, visited_points):
    
    search_stack = deque()
    search_stack.append(root_point)

    parents = {}
    path = []

    while search_stack:
        current_point = search_stack.pop()

        if current_point not in visited_points:
            visited_points.append(current_point)
            if "goal" in maze[current_point]:
                path.append("goal")
                while current_point != "start":
                    current_point = parents[current_point]
                    path.append(current_point)
                return path
            else:
                neighbors = maze[current_point]
                for neighbor in neighbors:

                    # otherwise there will be an infinite loop
                    # parent of 2 is 3 and parent of 3 is 2
                    if neighbor not in visited_points:
                        parents[neighbor] = current_point
                        search_stack.append(neighbor)

    return "No path to goal"

if __name__ == "__main__":
    print(search(maze, current_point, visited_points))
