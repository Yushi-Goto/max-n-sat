import argparse
import problems
import benchmarks

def parse_args():
    """Command-line argument parser"""
    parser = argparse.ArgumentParser(description='MAX-N_SAT')
    parser.add_argument('--data-path', default='./data/10_10.txt', help='data root path (default: ./data/10_10.txt)')

    return parser.parse_args()

def main():
    args = parse_args()

    # Read benchmark data
    N, xc_num, ltrl_ind = benchmarks.dataloader(args.data_path)

    # Solve Max N Sat
    m3s = problems.MaxNSat(N, xc_num, ltrl_ind)
    solution = m3s.solve_max_sat()
    print(solution)

if __name__ == '__main__':
    main()
