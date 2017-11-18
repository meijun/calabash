def power_by_mtt(state, edges):
    """Calculate the total power of the state, by the matrix-tree theorem.
    """
    import numpy as np

    n = len(state)
    graph = np.zeros((n+1, n+1), dtype=np.float64)
    for u, v, w in edges:
        if (u == 0 or u in state) and v in state:
            graph[abs(u), abs(v)] = w
    mat_l = np.zeros((n+1, n+1), dtype=np.float64)
    for i in range(n+1):
        for j in range(n+1):
            if i == j:
                for k in range(n+1):
                    if k != i:
                        mat_l[i, j] += graph[k, i]
            else:
                mat_l[i, j] = -graph[i, j]
    det = np.linalg.det(mat_l[1:, 1:])
    return det


def randomized_algorithm():
    import random
    random.seed(0)

    n, edges = read_input()
    times = 10
    best_state, best_power = None, None
    for _ in range(times):
        rand_state = tuple(i * (-1)**random.randrange(1, 3) for i in range(1, n+1))
        power = power_by_mtt(rand_state, edges)
        if best_state is None or best_power < power:
            best_state = rand_state
            best_power = power
    assert best_state is not None
    print ' '.join('%+d' % i for i in best_state)


def read_input():
    def one_edge():
        line = raw_input()
        u, v, w = line.split()
        return int(u), int(v), float(w)
    n = int(raw_input())
    edges = [one_edge() for _ in range(4 * n**2 - 2*n)]
    return n, edges


if __name__ == '__main__':
    randomized_algorithm()
