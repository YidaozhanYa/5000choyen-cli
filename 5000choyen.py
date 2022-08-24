#!/usr/bin/env python3

from PIL import Image
import sys
from generator import genImage

if '-h' in sys.argv or '--help' in sys.argv:
    print('Usage: 5000choyen [上半句] [下半句] [输出文件]')
    exit()
img=genImage(word_a=sys.argv[1], word_b=sys.argv[2])
img.save(sys.argv[3])