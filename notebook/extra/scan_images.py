import os

from PIL import Image
from argparse import ArgumentParser  # from Python 3.2 on


attrbs = ['format', 'size', 'mode']
format_string = '{:>10s} : {}'


parser = ArgumentParser()
parser.add_argument('-p', '--path',
                    help='specify the path to the directory that will be explored',
                    default='.')
parser.add_argument('-d', '--depth',
                    help='depth 0 is the specified directory, depth 1 is the specified directory and' +\
                    ' its children, etc.\n-1 specifies recursively going through all children nodes',
                    default=0,
                    type=int)

args = parser.parse_args()

path = os.path.abspath(args.path)
startdepth = len(path.split(os.sep))

cntr = 0

for curpath, dnames, fnames in os.walk(path):
    curdepth = len(curpath.split(os.sep))
    if args.depth > -1 and curdepth - startdepth > args.depth:
        continue 
    for f in fnames:
        file = os.path.join(curpath, f)
        try:
            with Image.open(file) as img:
                print('Attributes of {}'.format(img.filename))
                for attr in attrbs:
                    print(format_string.format(attr, getattr(img, attr)))
            print('\n')
            cntr += 1
        except IOError:  # this is not an image, just continue... any other error should be fetched 
            # print('{} is not an image'.format(file))
            pass

print('found a total of {} images'.format(cntr))