import Problem_7
import compute_primes
import timeit

problem = Problem_7

start_time = timeit.default_timer()

if __name__ == '__main__':
    problem.solution()

    # compute_primes.compute_primes()

    print(f'execution time = {timeit.default_timer() - start_time} seconds')
