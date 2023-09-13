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
    action_sequence = []
    if tile[0][0]=='A':
        curr = 'Left'
    else:
        curr = 'Right'
    curr = tile[0][0]
    count = 0
    for i in range(len(tile)):
        if count == len(tile)-1:
            if tile[i][1]== "Dirty":
                action_sequence.append("Suck") 
        else:
            if tile[i][0] == 'A' and tile[i][1] == 'Clean' and tile[i+1][0]=='B':
                if curr == 'Left':
                    action_sequence.append("Right")
                    curr = 'Right'
            elif tile[i][0] == 'B' and tile[i][1] == 'Clean' and tile[i+1][0]=='A':
                if curr == 'Right':
                    action_sequence.append("Left")
                    curr = 'Left'
            elif tile[i][1] == "Dirty":
                if tile[i][0] == "A" and tile[i+1][0] == 'B':
                    action_sequence.append("Suck")
                    action_sequence.append("Right")
                    curr = 'Right'
                elif tile[i][0] == "A" and tile[i+1][0] == 'A':
                    action_sequence.append("Suck")
                    curr = 'Left'   
                elif tile[i][0] == "B" and tile[i+1][0] == 'B':
                    action_sequence.append("Suck")
                    curr = 'Right'
                elif tile[i][0] == "B" and tile[i+1][0] == 'A':
                    action_sequence.append("Suck")
                    action_sequence.append("Left")
                    curr = 'Left'
        count += 1
    return action_sequence

# tile1 = create_envi()
# tile2 = create_envi()
# print(tile1,tile2,sep="\n")

n= int(input("Ënter number of sequences: "))
tile = create_envi(n)
for i in tile:
    print(i,end = "\t")
print()
print(clean(tile))
