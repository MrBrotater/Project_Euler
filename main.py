import Problem_2
import timeit

problem = Problem_2

start_time = timeit.default_timer()

if __name__ == '__main__':
    problem.solution()
    print(f'execution time = {timeit.default_timer() - start_time} seconds')
