text = """&#1587;&#1604;&#1575;&#1605; &#1576;&#1607; &#1607;&#1605;&#1607; &#1583;&#1608;&#1587;&#1578;&#1575;&#1606;
&#1605;&#1606; &#1583;&#1705;&#1578;&#1585; &#1587;&#1602;&#1575;&#1740;&#1740; &#1607;&#1587;&#1578;&#1605; &#1605;&#1583;&#1585;&#1587; &#1586;&#1740;&#1585;&#1711;&#1585;&#1608;&#1607; &#1662;&#1575;&#1740;&#1578;&#1608;&#1606;
&#1575;&#1740;&#1606; &#1601;&#1575;&#1740;&#1604;&#1740; &#1705;&#1607; &#1583;&#1585; &#1586;&#1740;&#1585; &#1605;&#1606; &#1608;&#1575;&#1587;&#1607; &#1583;&#1575;&#1606;&#1604;&#1608;&#1583; &#1711;&#1584;&#1575;&#1588;&#1578;&#1605; &#1585;&#1575; &#1583;&#1575;&#1606;&#1604;&#1608;&#1583; &#1705;&#1585;&#1583;&#1607; &#1608; &#1585;&#1608;&#1740; &#1587;&#1740;&#1587;&#1578;&#1605; &#1593;&#1575;&#1605;&#1604;
&#1608;&#1740;&#1606;&#1583;&#1608;&#1586; &#1578;&#1587;&#1578; &#1606;&#1605;&#1575;&#1740;&#1740;&#1583;"""
test = text.split("&#")
test.remove("")
s = ""
for i in test:
	d = chr(int(i[:4]))
	z = i[5:]
	s += d+z
else:
    print(s)
