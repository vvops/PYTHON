# cat: кошка

#dictionary = {
#    "cat": "кошка",
#    "dog": "собака"
#}

#print(dictionary)
#cat = dictionary["cat"]
#print(cat)
################Доступ к элементу по ключу##########################
countries = {
    "Африка": ["ЕГИПЕТ","КОД-ДИВУАР"],
    "Азия": ["ЯПОНИЯ","КИТАЙ"]
}

africa = countries["Африка"] 
print(africa)


africa_key = "Африка"
print(countries[africa_key])  

#############Добавление элементов в существующий список############################

countries["Европа"] = ["Россия", "Испания","Италия"]  #добавление в словарь countries
print(countries)

#countries[0] = "Франция"  #добавление
#print(countries)
#############Добавление элементов в существующий список############################

africa.append("жопия")
print(africa)
print(countries)
print(len(countries["Африка"]))