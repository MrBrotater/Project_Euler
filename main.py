# import Solved_problems.Problem_1
import Solved_problems.Problem_20
import timeit

# problem = Solved_problems.Problem_1
problem = Solved_problems.Problem_20

start_time = timeit.default_timer()

if __name__ == '__main__':
    problem.solution()

    print(f'execution time = {timeit.default_timer() - start_time} seconds')
