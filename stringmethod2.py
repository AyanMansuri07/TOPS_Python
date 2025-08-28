s1="PyThoN"
s2=""
s3=""
for c in s1:
    if c.islower():
        s2+=s2.join(c.upper())
        s3+=c.upper()
    else:
        s2+=s2.join(c.lower())
        s3+=c.lower()
print(s1)
print(s2)
print(s3)