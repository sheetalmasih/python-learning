mydict={"pankha":"fan","dabba":"box",
    "aakarshak":"Attractive",
    "ganja":"Bald",
    "sundar":"Beautiful",
    "bada":"Big",
    "boring":"Boring",
    "bhadur":"Brave",
    "chalak":"Clever",
    "thanda":"Cold",
    "kayar":"Coward",
    "andhera":"Dark",
    "sust":"Dull",
    "mota":"Fat"}
print("option are",mydict.keys())
a=input("enter the hindi word\n")
# print("the meaning of your word is:",mydict[a])
print("the meaning of your word is:",mydict.get(a))
