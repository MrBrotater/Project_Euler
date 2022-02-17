# import Solved_problems.Problem_1
import Working_on.Problem_17
import timeit

problem = Working_on.Problem_17

start_time = timeit.default_timer()

if __name__ == '__main__':
    problem.solution()

    print(f'execution time = {timeit.default_timer() - start_time} seconds')
