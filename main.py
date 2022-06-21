import csv
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=str, default='annotations/output/UniteD-SRL')
    parser.add_argument('--output', type=str, default='annotations/output/UniteD-SRL')
    parser.add_argument('--splits', type=list, default=['Train', 'Dev', 'Test'])
    parser.add_argument('--srl_types', type=list, default=['dependency', 'span'])
    parser.add_argument('--langs', type=list, default=['EN', 'ES', 'FR', 'ZH'])

    args = parser.parse_args()
    create(args.input, args.output, args.splits, args.langs, args.srl_types)