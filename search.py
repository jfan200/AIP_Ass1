# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

from cmath import inf
from itertools import accumulate
from queue import PriorityQueue
import util


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()

def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"

    result = []
    s = problem.getStartState()
    stack = util.Stack()
    visited = []
    while not problem.isGoalState(s):
        if s not in visited:
            visited.append(s)
            successors = problem.getSuccessors(s)
            for successor in successors:
                state, action, cost = successor
                if state not in visited:
                    stack.push((state, result.append(action)))
        if state.isEmpty():
            result = []
            break
        state, result = stack.pop()
    return result


    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

# Please DO NOT change the following code, we will use it later
def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    myPQ = util.PriorityQueue()
    startState = problem.getStartState()
    startNode = (startState, '', 0, [])
    myPQ.push(startNode,heuristic(startState,problem))
    visited = set()
    best_g = dict()
    while not myPQ.isEmpty():
        node = myPQ.pop()
        state, action, cost, path = node
        if (not state in visited) or cost < best_g.get(state):
            visited.add(state)
            best_g[state]=cost
            if problem.isGoalState(state):
                path = path + [(state, action)]
                actions = [action[1] for action in path]
                del actions[0]
                return actions
            for succ in problem.getSuccessors(state):
                succState, succAction, succCost = succ
                newNode = (succState, succAction, cost + succCost, path + [(state, action)])
                myPQ.push(newNode,heuristic(succState,problem)+cost+succCost)
    util.raiseNotDefined()


def enforcedHillClimbing(problem, heuristic=nullHeuristic):
    """
    Local search with heuristic function.
    You DO NOT need to implement any heuristic, but you DO have to call it.
    The heuristic function is "manhattanHeuristic" from searchAgent.py.
    It will be pass to this function as second argument (heuristic).
    """
    "*** YOUR CODE HERE FOR TASK 1 ***"
    def improve(node):
        open = util.Queue()
        open.push(node)
        initial_state = node[0]
        h0 = heuristic(initial_state, problem)
        closed = set()

        while not open.isEmpty():
            n = open.pop()
            state, action = n
            if state not in closed:
                #print(f"Current node: {n}")
                closed.add(state)
                #print(f"h0: {h0}\ncurrent: {heuristic(state, problem)}\n")
                if heuristic(state, problem) < h0:
                    return n
                for succ in problem.getSuccessors(state):
                    succState, succAction, succCost = succ
                    open.push((succState, action + [succAction]))
        return None

    state = problem.getStartState()
    solution = []
    node = (state, solution)
    while not problem.isGoalState(state):
        node = improve(node)
        state, solution = node
        # print(f"Improved node: {node}")
        # print(f"state: {state}")
    return solution
    # put the below line at the end of your code or remove it
    util.raiseNotDefined()



from math import inf as INF
def bidirectionalAStarEnhanced(problem, heuristic=nullHeuristic, backwardsHeuristic=nullHeuristic):

    """
    Bidirectional global search with heuristic function.
    You DO NOT need to implement any heuristic, but you DO have to call them.
    The heuristic functions are "manhattanHeuristic" and "backwardsManhattanHeuristic" from searchAgent.py.
    It will be pass to this function as second and third arguments.
    You can call it by using: heuristic(state,problem) or backwardsHeuristic(state,problem)
    """
    "*** YOUR CODE HERE FOR TASK 2 ***"
    # The problem passed in going to be BidirectionalPositionSearchProblem
    #open_f
    close_f = set()
    open_f = util.PriorityQueue()
    start_state_f = problem.getStartState()
    start_node_f = (start_state_f, '', 0, [])
    open_f.push(start_node_f, heuristic(start_state_f, problem))
    best_gf = {}

    #Open_b
    close_b = set()
    open_b = util.PriorityQueue()
    goal_states = problem.getGoalStates()  #only one goal state in this situation
    for goal in goal_states:
        start_node_b = (goal, '', 0, [])
        open_b.push(start_node_b, backwardsHeuristic(goal, problem))
    best_gb = {}

    L = 0
    U = INF
    is_forward = True
    solution = []

    while not open_f.isEmpty() and not open_b.isEmpty():
        bMin_f = open_f.getMinimumPriority()
        bMin_b = open_b.getMinimumPriority()
        L = (bMin_f + bMin_b) / 2

        # Determine which direction
        if is_forward:
            n = open_f.pop()
            state, action, cost, path = n

            if str(state) not in close_f:
                close_f.add(str(state))
                best_gf[str(state)] = (cost, path)

            if str(state) in close_b and best_gf[str(state)][0] + best_gb[str(state)][0] < U:
                U = best_gf[str(state)][0] + best_gb[str(state)][0]
                solution = best_gf[str(state)][1] + list(reversed(best_gb[str(state)][1]))

            if L >= U:
                return solution

            for succ in problem.getSuccessors(state):
                succState, succAction, succCost = succ
                if str(succState) not in close_f:
                    newNode = (succState, succAction, cost + succCost, path + [succAction])
                    dx = heuristic(succState, problem) + cost + succCost \
                         + best_gf[str(state)][0] - backwardsHeuristic(state, problem)
                    open_f.push(newNode, dx)
        else:
            n = open_b.pop()
            state, action, cost, path = n

            if str(state) not in close_b:
                close_b.add(str(state))
                best_gb[str(state)] = (cost, path)

            if str(state) in close_f and (best_gf[str(state)][0] + best_gb[str(state)][0]) < U:
                U = best_gf[str(state)][0] + best_gb[str(state)][0]
                solution = best_gf[str(state)][1] + list(reversed(best_gb[str(state)][1]))

            if L >= U:
                return solution

            for succ in problem.getBackwardsSuccessors(state):
                succState, succAction, succCost = succ
                if str(succState) not in close_b:
                    newNode = (succState, succAction, cost + succCost, path + [succAction])
                    dx = backwardsHeuristic(succState, problem) + cost + succCost \
                         + best_gb[str(state)][0] - heuristic(state, problem)
                    open_b.push(newNode, dx)

        if open_f.getMinimumPriority() < open_b.getMinimumPriority():
            is_forward = True
        else:
            is_forward = False
    return solution


    # put the below line at the end of your code or remove it
    util.raiseNotDefined()



# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch


ehc = enforcedHillClimbing
bae = bidirectionalAStarEnhanced


