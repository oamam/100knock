import numpy as np


def cos_sim(vec_a, vec_b):
    vec_ab = np.linalg.norm(vec_a) * np.linalg.norm(vec_b)
    if vec_ab != 0:
        return np.dot(vec_a, vec_b) / vec_ab
    else:
        return -1


def main():
    human_score = []
    sim_score = []
    D2 = []
    with open('combined_sim.txt', 'rt') as f:
        for line in f:
            cols = line.split(' ')
            human_score.append(cols[2])
            sim_score.append(cols[3])
        human_rank_index = np.argsort(human_score)
        sim_rank_index = np.argsort(sim_score)
        N = len(human_rank_index)

        for hr, hi in enumerate(human_rank_index):
            sr = np.where(sim_rank_index == hi)[0][0]
            D2.append((hr - sr)**2)
        print(1 - (6 * sum(D2) / (N**3 - N)))


if __name__ == '__main__':
    main()
