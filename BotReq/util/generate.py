
f=lambda s:s[11:]and[s[0]+w+x for x in f(s[1:])for w in('.','')]or[s]
def permuation(str):
    return f(str)