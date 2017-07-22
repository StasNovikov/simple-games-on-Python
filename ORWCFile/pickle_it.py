# Консервация данных в файд
# Демонстрирует консервацию данных и доступ к ним

import pickle, shelve

print("Консервация списков")
variety = ["огурцы","помидора","капуста"]
shape = ["целые","кубиками","соломкой"]
brand = ["Главпродукт","Чумак","Бондюэль"]

# Запись двоичных данных в файл
# Для этого используется режим доступа - wb
f = open("pickles.dat","wb")

# Функция pickle.dump() - предназначена для консервации данных в файл
pickle.dump(variety, f)
pickle.dump(shape, f)
pickle.dump(brand, f)
f.close()
print("\nРасконсервация списков")
f = open("pickles.dat","rb")
variety = pickle.load(f)
shape = pickle.load(f)
brand = pickle.load(f)
print(variety)
print(shape)
print(brand)
f.close()