s = "When life gives you lemons, and more lemons, and even more lemons, eat a lemon."
subs = "lemons"
found = False
pos = -1
length = len(s)
while True:
    pos = s.find(subs,pos+1,length)
    if pos == -1:
        break
    print("Found the substring at position ", pos)
    found = True
if found == False:
    print("Substring was not found.")