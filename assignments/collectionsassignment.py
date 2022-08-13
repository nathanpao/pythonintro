lst = ['Norway', 'Belgium', 'Poland']
lst.append('Mexico')
print(lst)
del(lst[2])
print(lst)
lst.insert(1,'Canada')
print(lst)

s = {'Norway', 'Belgium', 'Poland'}
s.update(['Mexico'])
print(s)
s.remove('Belgium')
print(s)
s.update(['Canada'])
print(s)