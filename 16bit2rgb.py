import sys,os
import argparse
import glob 
import numpy as np
import cv2
from matplotlib import cm


parser = argparse.ArgumentParser(description='16bit2rgb.py: script for 16 bit TIFF to 24bit RGB PNG conversion')
parser.add_argument('input_files', help='Input image Files (ex. '/img/*.tiff')')
parser.add_argument('--out', '-o', default='', help='Output directory')
parser.add_argument('--min_val', type=int, default=-1, help='Min value')
parser.add_argument('--max_val', type=int, default=-1, help='Max value')
parser.add_argument('--map', '-m', default='CMRmap', help='Colour Map')

args = parser.parse_args()

if hasattr(cm, args.map):
    cmap = getattr(cm, args.map)
else:
    raise NotImplementedError(args.map)

max_val = 0 if args.max_val < 0 else args.max_val
min_val = 255**2 if args.min_val < 0 else args.min_val

if args.max_val < 0 and args.min_val < 0:
    print('finding minmax values')
    for filepath in glob.glob(args.input_files):
        print(' target file: ' + filepath)
        img = cv2.imread(filepath, cv2.IMREAD_ANYDEPTH)
        ma = img.max()
        mi = img.min()
        if ma>max_val:
            max_val = ma
        if mi<min_val:
            min_val = mi

print('converting files')
for filepath in glob.glob(args.input_files):
    print(' target file: ' + filepath)
    img = cv2.imread(filepath, cv2.IMREAD_ANYDEPTH)
    img = (img-min_val).astype('float64') / (max_val-min_val)
    img2 = (cmap(img) * 255).astype('uint8')
    img2 = cv2.cvtColor(img2, cv2.COLOR_RGB2BGR)
    filename = os.path.basename(filepath).replace('.tiff','.png')
    output_filename = os.path.join(args.out, filename)
    print('  saving: ' + output_filename)
    cv2.imwrite(output_filename, img2)

print('done (max: %d, min: %d)' % (max_val, min_val))
