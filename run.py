#! /usr/bin/python3
import sys, os
from time import time

# so = ['rdul', 'rdlu', 'drul', 'drlu', 'ludr', 'lurd', 'uldr', 'ulrd']
# so = ['hamm', 'manh']
metody = ['bfs', 'dfs', 'astr']

so = {
'bfs': ['rdul', 'rdlu', 'drul', 'drlu', 'ludr', 'lurd', 'uldr', 'ulrd'],
'dfs': ['rdul', 'rdlu', 'drul', 'drlu', 'ludr', 'lurd', 'uldr', 'ulrd'],
'astr': ['hamm', 'manh']
}


def runner(methods):
    files = os.listdir('./puzzles')
    files.sort()
    leng = len(files)

    for method in methods:
        print('='*5 + method + '='*5)

        for idx, file in enumerate(files):

            for order in so[method]:
                file_name = file.strip('.txt')

                file_name = f'{file_name}_{method}_{order}'

                sol_file = f'solutions/{file_name}_sol.txt'
                stat_file = f'stats/{file_name}_stats.txt'

                command = f'./program.py {method} {order} puzzles/{file} {sol_file} {stat_file}'
                os.system(command)

                # print(command)

            yield f'{idx+1} / {leng}'


met = sys.argv[1:]
print(met)
t1 = time()
for st in runner(met):
    sys.stdout.write("\r%s" % st)
    sys.stdout.flush()
print('\nDone')
print('Total time %f' % (time()-t1))