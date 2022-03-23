import Solved_problems.Problem_15
import timeit

problem = Solved_problems.Problem_15



start_time = timeit.default_timer()

if __name__ == '__main__':
    problem.solution()

    print(f'execution time = {timeit.default_timer() - start_time} seconds')
