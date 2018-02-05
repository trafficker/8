people={'Alice':{'phone':'12345','addr':'bark'}}
nam=input('Name：')
person=people.get(nam,{})
k=input()
res=person.get(k, k)
print(res)
print(person)
print(people.values())
