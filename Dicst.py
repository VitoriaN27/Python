#Dicionarios, Setas e Tuplas 

notas = {'joão': 6.0, 'Maria': 8.0, 'Pedro': 6.5}
print(notas)

print(notas['joão'])

notas.keys()
notas.values()

print('joão' in notas)
print('fernando' in notas)

del notas ['joão']
print(notas)

notas ['ana'] = 9
print(notas)

notas.get('Luiza', "Não encontrado!!!!")

bigdata = {'Spark', 'Hive', "Sqoop"}
print(bigdata)

print('Spark' in bigdata)

bigdata.add('Hadoop')
bigdata

print(len(bigdata))

bigdata.add("Spark")
bigdata

tupla = (1,2,3,4,5,6,7)
print(tupla)

tupla[4]

dic2 = {(0, 1): 0 , (1, 2): 1, (2, 3): 2, (3, 4): 3, (4, 5): 4, (5, 6): 5 , (6, 7): 6,  (7, 8 ): 7, (8, 9 ): 8,  (9, 10 ): 9}
print(dic2)

print(type(notas))
print(type(bigdata))
print(type(tupla))