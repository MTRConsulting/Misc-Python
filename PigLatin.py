print "Pig Latin"
s = raw_input("Enter a word:")
print ("s is " + s)
prefix = s[0:1]
print ( "prefix is " + prefix)
baselength = len(s)
print "base is ", baselength
base = s[1:baselength]
print ("base is " + base)
print "Answer is : " + base + prefix + "ay"
