import sys, os
from time import time

so = ['rdul', 'rdlu', 'drul', 'drlu', 'ludr', 'lurd', 'uldr', 'ulrd']


def runner():
    files = os.listdir('./puzzles')
    files.sort()
    leng = len(files)
    for idx, file in enumerate(files):
        for order in so:
            file_name = file.strip('.txt')
            file_name = f'{file_name}_bfs_{order}'

            sol_file = f'solutions/{file_name}_sol.txt'
            stat_file = f'stats/{file_name}_stats.txt'

            command = f'./program.py bfs {order} puzzles/{file} {sol_file} {stat_file}'
            os.system(command)

        yield f'{idx+1} / {leng}'


t1 = time()
for st in runner():
    sys.stdout.write("\r%s" % st)
    sys.stdout.flush()
print('\nDone')
print('Total time %f' % (time()-t1))