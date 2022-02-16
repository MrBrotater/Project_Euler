import Problem_13
import timeit

problem = Problem_13

start_time = timeit.default_timer()

if __name__ == '__main__':
    problem.solution()

    print(f'execution time = {timeit.default_timer() - start_time} seconds')
