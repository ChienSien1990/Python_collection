 # Counting Bobs
c=0
d=0
for x in s:
    if 'bob' in s[d:d+3]:
        c+=1
    d+=1
print "Number of vowels: %d" % c 