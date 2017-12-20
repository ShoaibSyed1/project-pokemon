import toml

lang = None
with open("assets/lang/en_us.toml") as file:
    lang = toml.load(file)

def get(name):
    items = name.split('.')
    
    item = lang

    for i in items:
        temp = item.get(i, None)
        if temp == None:
            return "#lang:" + name
        item = temp
    
    return item