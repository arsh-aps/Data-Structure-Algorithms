#Reversing recursively
def revString(s):
    if len(s) == 0:
        return ""
    return s[-1] + revString(s[:-1])
s = revString('teri')
print(s)