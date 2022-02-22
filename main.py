import Working_on.Problem_67
import timeit

problem = Working_on.Problem_67

start_time = timeit.default_timer()

if __name__ == '__main__':
    problem.solution()

    print(f'execution time = {timeit.default_timer() - start_time} seconds')
