a={
'W' : ('w         w','w    w    w',' w   w   w ','  w w w w  ','   w   w   '),
'L' : ('wwww       ',' ww        ',' ww        ',' ww       w','wwwwwwwwwww'),
'T' : ('wwwwwwwwwww','w    w    w','     w     ','     w     ','    www    ')
}
name = raw_input('please enter wlt: ').upper()
for i in range(0,5):
    for o in name:
	    print a[o][i],
    print ''
