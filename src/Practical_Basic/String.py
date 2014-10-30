string="this is a string"
#=============================================================
string = string.capitalize()
print(string)
#=============================================================
# string = string.casefold()
# print(string)
#=============================================================
index = string.find('This is ')
print(index)
#=============================================================
index = string.index('is')
print(index)
#=============================================================
isnum = string.isalnum()
print(isnum)
#=============================================================
isalpha = string.isalpha()
print(isalpha)
#=============================================================
count = string.count("i")
print(count)
#=============================================================
split = string.split()
print(split)
#=============================================================
joinStr = ",".join(split)
print(joinStr)
#=============================================================
stringwithspace="   this is a string   "
stringwithoutspace = stringwithspace.strip()
stringwithoutleftspace = stringwithspace.lstrip()
stringwithoutrightspace = stringwithspace.rstrip()
print(stringwithoutspace)
print(stringwithoutleftspace)
print(stringwithoutrightspace)
#=============================================================
upcase = string.upper()
print(upcase)
#=============================================================
lower = string.lower()
print(lower)
#=============================================================
cap = string.title()
print(cap)
#=============================================================
capFirst = string.capitalize()
print(capFirst)
#=============================================================
uStr = u"This is a String with\nnew line"
print(uStr)
rawStr = r"This is a String with\nnew line"
print(rawStr)
#=============================================================