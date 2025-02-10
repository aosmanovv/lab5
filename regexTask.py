import re
txt="abbbababba_test1_Dd_test2_Testing_TTesting 1,2.3 TesTing ReadTheBook"
x=re.findall("a*b",txt)
print(x)

x=re.findall("abb|abbb",txt)
print(x)

x=re.findall("[a-z^_]*_",txt)
print(x)

x=re.findall("[A-Z][a-z]*",txt)
print(x)

x=re.findall("^a.*b$",txt)
print(x)
#or
x=re.findall("a.*b",txt)
print(x)

x=re.sub("[., ]",":",txt)
print(x)

x=re.sub(r'_(\w)', lambda m:  m.group(1).upper(), txt)
print(x)
x=re.findall(r'_(\w)', txt)
print(x)

x=re.split("[A-Z]", txt)
print(x)

x=re.sub(r'(?=[A-Z])', ' ', txt)
print(x)


x=re.sub(r'[a-z]([A-Z])', lambda m:  m.group(0).lower()[0]+"_"+m.group(0).lower()[1], txt)
print(x)



