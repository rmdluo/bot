class List:
    def __init__(self, name, author, items=[], ordered=True):
        self.name = name
        self.author = author
        self.items = items
        self.ordered = ordered

    def name(self):
        return self.name
    
    def add_item(self, item):
        self.items.append(item)

    def change_name(self, name):
        self.name = name

    def change_item(self, item, item_index):
        self.items[item_index] = item

    def turn_ordered(self):
        self.ordered = True

    def turn_unordered(self):
        self.ordered = False

    def remove_item(self, item_index):
        return self.items.pop(item_index)

    def to_output(self):
        str = ""
        str += self.name + " by " + self.author + ":\n"
        
        for i in range(len(self.items)):
            if(self.ordered):
                str += "\t" + str(i + 1) + ". " + self.items[i] + "\n"
            else:
                str += "\t- " + self.items[i] + "\n"

    def to_string(self):
        str = ""
        str += self.name + ", " + self.author + ", "+ str(self.ordered)
        
        for i in range(len(self.items)):
            str += ", " + self.items[i]

def from_string(str):
    info = str.split(", ")

    if(info[2] == "True"):
        ordered = True
    else:
        ordered = False

    return List(info[0], info[1], info[3:], ordered)