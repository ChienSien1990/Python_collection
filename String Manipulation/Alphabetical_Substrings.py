c=0
d=1
e=0
f=s[0]
for x in s:
    if s.index(x) < len(s):
        if (d!=len(s)):
            if (x <= s[d]) :
                c+=1          
            else: 
                if e<c:          
                    e=c
                    f=s[d-e-1:d]
                c=0
        elif (d==len(s)):
                if e<c:          
                    e=c
                    f=s[d-e-1:d]
        if d < len(s):
            d+=1
print "Longest substring in alphabetical order is:",f