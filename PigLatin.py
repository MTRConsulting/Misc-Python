print 'Welcome to the Pig Latin Translator!'

# Start coding here!
print "Pig Latin"
original = raw_input("Enter a word:")
if len(original) > 0:
    print ("The word entered is : " + original)
    prefix = original[0:1]
    print ( "First character is : " + prefix)
    baselength = len(original)
    print "Original length is : ", baselength
    base = original[1:baselength]
    print ("base is " + base)
    print "Answer is : " + base + prefix + "ay"
else:
    print "empty"
