import random

locations = ['A','B']
loc_type = ['Clean','Dirty']

def create_envi(n):
    percept_sequence = []
    while n:
        tile = []
        l = random.choice(locations)
        t = random.choice(loc_type)
        tile = [l,t]
        percept_sequence.append(tile)
        n -= 1
    return percept_sequence
    # loc_dup = locations.copy()
    # l = random.choice(locations)
    # loc_dup.remove(l)
    # t = random.choice(loc_type)
    # tile.append([l,t])
    # l1 = loc_dup[0]
    # t1 = random.choice(loc_type)
    # tile.append([l1,t1])

def clean(tile):
    # prev = None
    # for i in tile:
    #     if i[0] == 'A' and i[1] == 'Clean':
    #         if prev == 'Left':
    #             print("NoAction", end = '\t')
    #         else:
    #             prev = "Right"
    #             print("Right", end = '\t')
    #     elif i[0] == 'B' and i[1] == 'Clean':
    #         if prev == "Left":
    #             print("NoAction", end = '\t')
    #         else: 
    #             prev = "Left"
    #             print("Left", end = '\t')
    #     elif i[1] == "Dirty":
    #         print("Suck", end = "\t")
    curr = tile[0][0]
    # count = 0
    for i in tile:
        # if count == 0:
            
        if i[0] == 'A' and i[1] == 'Clean':
            if curr == 'Left':
                print("NoAction", end = '\t')
        elif i[0] == 'B' and i[1] == 'Clean':
            if curr == 'Right':
                print("NoAction", end = '\t')
        elif i[1] == "Dirty":
            if i[0] == "A" and curr == 'Right':
                curr = 'Left'
                print("Left","Suck", sep='\t', end='\t')
            if i[0] == "B" and curr == 'Left':
                curr = 'Right'
                print("Right","Suck", sep='\t', end='\t')
            else: 
                print("Suck", end = "\t")
        # count += 1

# tile1 = create_envi()
# tile2 = create_envi()
# print(tile1,tile2,sep="\n")

n= int(input("Ënter number of sequences: "))
tile = create_envi(n)
for i in tile:
    print(i,end = "\t")
print()
clean(tile)
