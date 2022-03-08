class Item:
    '''
    Purpose: This class represents a specific clothing item.
    Instance Variables:
        name: this is a string representing the name of the item
        price: this is a float representing the price of the item
        category: this is a string representing the type of clothing item this is/what its for
        store: this is a string representing the name of the store that the item is held at
    Methods:
        __init__: this is a constructor method which instantiates all of the instance Variables
        __str__: this is a string method which returns a specifically formatted string including each instance variable
        __lt__: this is a method that evaluates if an item has a lower price than another item
    '''
    def __init__(self, name, price, category, store):
        self.name = name
        self.price = price
        self.category = category
        self.store = store
    def __str__(self):
        return self.name+", "+self.category+", "+self.store+": $"+str(self.price)
    def __lt__(self,other):
        return self.price<other.price

class Store:
    '''
    Purpose: This class represents a store containing many clothing items
    Instance Variables:
        name: this is a string representing the name of the store
        items: this is a list of items representing the items held in the inventory of the store
    Methods:
        __init__: this is a constructor method which instantiates all of the instance Variables
        __str__: this is a string method which returns a specifically formatted string including the name and the string representation of each item in items
    '''
    def __init__(self, name, filename):
        self.name = name
        self.items = []
        fp = open(filename,'r')
        fp.readline()
        list1 = fp.readlines()
        for i in range(len(list1)):
            list2 = list1[i].split(',')
            list2[2] = list2[2].replace('\n','')
            self.items.append(Item(list2[0],float(list2[1]),list2[2],self.name))
    def __str__(self):
        string = ''
        string +=self.name + '\n'
        for i in range(len(self.items)):
            string+= str(self.items[i])+'\n'
        return string

def cheap_outfit(store_list):
    dict1 = {}
    headlist = []
    torsolist= []
    legslist = []
    feetlist = []
    for i in range(len(store_list)):
        for j in range(len(store_list[i].items)):
            if store_list[i].items[j].category == 'Head':
                headlist.append(store_list[i].items[j])
            if store_list[i].items[j].category == 'Torso':
                torsolist.append(store_list[i].items[j])
            if store_list[i].items[j].category == 'Legs':
                legslist.append(store_list[i].items[j])
            if store_list[i].items[j].category == 'Feet':
                feetlist.append(store_list[i].items[j])
    minhead = min(headlist)
    mintorso = min(torsolist)
    minlegs = min(legslist)
    minfeet = min(feetlist)
    dict1['Head'] = minhead
    dict1['Torso'] = mintorso
    dict1['Legs'] = minlegs
    dict1['Feet'] = minfeet
    return dict1

outfit1 = cheap_outfit([Store('Professional Wear', 'professionalwear.csv')])
outfit2 = cheap_outfit([Store('Blacksmith', 'blacksmith.csv'), Store('Sparkles', 'sparkles.csv')])
for key in outfit1:
	print(key,' - ',outfit1[key])
for key in outfit2:
	print(key,' - ',outfit2[key])
