#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Copyright (C) 2010 Lucas De Marchi <lucas.de.marchi@gmail.com>
"""
import sys

usage = "iconifymail domain_image name_address"
if len(sys.argv) != 3:
    print usage
    sys.exit(1)

import Image, ImageFont, ImageDraw, ImageOps

imgstr = sys.argv[1]
addrstr = sys.argv[2]

img_domain = Image.open(imgstr)
w, h = img_domain.size
print "Domain size: %dx%d" % (w, h)

f = ImageFont.truetype('/home/lucas/.fonts/EurostileLTStd-Demi.otf', 14)

wtxt, htxt = f.getsize(addrstr)

print "height: txt: %d, img: %d pos: %d" % (htxt, h, (h - htxt) / 2)

if htxt > h:
    h = htxt
w = w + wtxt + 2

img = Image.new('RGBA', (w, h), '#ffffff')

img.paste(img_domain, (wtxt + 2, 0))

draw = ImageDraw.Draw(img)
draw.text((2, h - htxt + 1 ), addrstr, "#3C465F", f)
draw.rectangle([(0 ,0), (w - 1, h - 1)], outline="#bebec7")


img.save('mail_' + addrstr + '.png')
