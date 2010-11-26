#!/usr/bin/python
# -*- coding: utf-8 -*-
# recode a file from arabic windows(windows-1256) to utf8
import sys, os
def winArabicToUtf8(s, arabic2farsi=True):
 u = s.decode('windows-1256')
 if arabic2farsi:
  for item in [(u'ي',u'ی'),(u'ك',u'ک')]:
   u = u.replace(item[0], item[1])
 return u.encode('utf8')

s = file(sys.argv[1]).read()
ws = winArabicToUtf8(s)
newName = sys.argv[1]
if newName[-4:]=='.srt':
  newName = newName[:-4]
newName += '.utf8.txt'
file(newName, 'w').write(ws)

