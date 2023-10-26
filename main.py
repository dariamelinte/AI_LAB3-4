import copy
import logging
import time

from models.directions import Directions
from models.state import State

MAXDEPTH = 2000
DIRECTIONS_VARIANTS = [Directions.UP, Directions.DOWN, Directions.LEFT, Directions.RIGHT]

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s | %(levelname)s | %(message)s',
    filename='loguri.log',
    filemode='a'
)

def find_state(visited: set, state):
   for other_state in visited:
      if state.matrix == other_state.matrix:
         return True
   return False

def depth_limited_dfs(state: State, depth, visited:set, stack):
   if state.is_final():
      stack.append(copy.deepcopy(state))
      return True

   if depth == 0:
      return False

   visited.add(copy.deepcopy(state))

   for direction in DIRECTIONS_VARIANTS:
      logging.info(f"MOVE: {direction}")
      transition = state.get_move(direction)
      if transition is not None and not find_state(visited, transition):
         res = depth_limited_dfs(transition, depth - 1, visited, stack)
         if res:
            stack.append(copy.deepcopy(state))
            return True
   return False

def iddfs(state, depth, stack):
    for d in range(depth + 1):
        visited = set()
        res = depth_limited_dfs(state, d, visited, stack)
        if res:
            return True
        else:
            stack.clear()
    return False

def main():
   first = State()
   first.matrix = [[8, 6, 7], [2, 5, 4], [0, 3, 1]]
   second = State()
   second.matrix = [[2, 5, 3], [1, 0, 6], [4, 7, 8]]
   third = State()
   third.matrix = [[2, 7, 5], [0, 8, 4], [3, 1, 6]]
   
   states = [first, second, third]

   for i, actual_state in enumerate(states):
      stack = []
      start_time = time.time()

      result = iddfs(actual_state, MAXDEPTH, stack)

      if not result:
         print("Solution not found :(")
         continue

      with open(f"out/solution_{i}.txt", "w") as file:
         file.write(f"Number of moves: {len(stack) - 1}\n\n")
         end_time = time.time()
         execution_time = end_time - start_time
         file.write(f"Execution Time: {execution_time} seconds\n\n")

         for state in reversed(stack):
            state_str = "\n".join(" ".join(map(str, row)) for row in state.matrix)

            file.write(state_str + "\n\n")
         
         logging.info("------------------------------------")

if __name__ == "__main__":
    main()
