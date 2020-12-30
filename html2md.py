#!/usr/bin/python3
# -*- coding: utf-8 -*-

import fileinput
import re
import sys

prepattern = re.compile('</?pre>')
codepattern = re.compile('</?code>')
apattern = re.compile('<a href="([^"]+)">(.+?)</a>')
h2pattern = re.compile('<h2[^>]+>(.+?)</h2>')
h3pattern = re.compile('<h3[^>]+>(.+?)</h3>')
h4pattern = re.compile('<h4[^>]+>(.+?)</h4>')
dlpattern = re.compile('<dl[^>]+><dt>(.+?)</dt>')

for line in fileinput.input():
    line = h2pattern.sub(r'# \1', line)
    line = h3pattern.sub(r'## \1', line)
    line = h4pattern.sub(r'### \1', line)
    line = dlpattern.sub(r'### \1', line)
    line = prepattern.sub(r'```', line)
    line = codepattern.sub(r'`', line)
    line = apattern.sub(r'[\2](\1)', line)
    line = line.replace('](/', '](https://tip.golang.org/')
    sys.stdout.write(line)
