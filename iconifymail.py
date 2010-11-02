#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Copyright (C) 2010 Lucas De Marchi <lucas.de.marchi@gmail.com>
Copyright (C) 2010 ProFUSION embedded systems
"""
import sys, os

usage = "iconifymail domain_image name_address"
if len(sys.argv) != 3:
    print(usage)
    sys.exit(1)

imgstr = sys.argv[1]
addrstr = sys.argv[2]

FONT = 'EurostileLTStd-Demi.otf'
FONT_DIRS = ['~/.fonts/', '/usr/share/fonts/']
FONTPXSIZE = 14
COLOR_BACKGROUND= '#ffffff'
COLOR_TEXT = '#3C465F'
COLOR_BORDER = '#bebec7'
IMG_OUTPUT = 'mail_' + addrstr + '.png'

import Image, ImageFont, ImageDraw, ImageOps

def load_font(FONT, FONT_DIRS, FONTPXSIZE):
    font = None
    for d in FONT_DIRS:
        d = os.path.expanduser(d)
        for dirpath, dirnames, filenames in os.walk(d):
            for f in filenames:
                if f == FONT:
                    font = '/'.join([dirpath, f])
                    break
    if font:
        return ImageFont.truetype(font, FONTPXSIZE)

    return None

f = load_font(FONT, FONT_DIRS, FONTPXSIZE)
if not f:
    raise Exception('Unable to find font %s' % (FONT))

img_domain = Image.open(imgstr)
w, h = img_domain.size

wtxt, htxt = f.getsize(addrstr)

# + 2 for the border line
wtxt += 2

# ideally domain's height should be the biggest, but if it's not
# at least we don't fail
if htxt > h:
    h = htxt
w = w + wtxt

img = Image.new('RGBA', (w, h), COLOR_BACKGROUND)
img.paste(img_domain, (wtxt, 0))

draw = ImageDraw.Draw(img)
draw.text((2, h - htxt + 1 ), addrstr, COLOR_TEXT,f)
draw.rectangle([(0 ,0), (w - 1, h - 1)], outline=COLOR_BORDER)


img.save(IMG_OUTPUT)
