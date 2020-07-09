# гусь1 "Серый", вес - 10 кг, кормить, собирать яйца
# гусь2 "Белый", вес - 12 кг, кормить, собирать яйца
# корова "Маньку", вес 250 кг, кормить, доить
# овца1 "Барашек", вес 35 кг, кормить, стричь
# овца2 "Кудрявый", вес 40 кг, кормить, стричь
# курица1 "Ко-Ко", вес 2 кг, кормить, собирать яйца
# курица2 "Кукареку", вес 4 кг, кормить, собирать яйца
# коза1 "Рога", вес 30 кг, кормить, доить
# коза2 "Копыта", вес 25 кг, кормить, доить
# утку "Кряква", вес 5 кг, кормить, собирать яйца

all_weight = []
max_weight = {}

class Animal:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
    def eat(self):
        return 'покормили'

class Bird(Animal):  # собирать яйца у кур, утки и гусей
    goose_1_sound = 'га-га-га'
    goose_2_sound = 'га-га-га-га-га'
    chicken_1_sound = 'кудах-кудах'
    chicken_2_sound = 'кукареку'
    duck_sound = 'кря-кря'
    def eggs(self):
        return 'и собрали яйца.'

goose_1 = Bird('Серый', 10)
goose_2 = Bird('Белый', 12)
chicken_1 = Bird('Ко-ко', 2)
chicken_2 = Bird('Кукареку', 4)
duck = Bird('Кряква', 5)

print(f'1. Гусь {goose_1.name}  весит {goose_1.weight} кг. Кричит - {Bird.goose_1_sound}, чтобы его {goose_1.eat()} {goose_1.eggs()}')
print(f'2. Гусь {goose_2.name} весит {goose_2.weight} кг. Кричит - {Bird.goose_2_sound}, чтобы его {goose_2.eat()} {goose_2.eggs()}')
print(f'3. Курица {chicken_1.name} весит {chicken_1.weight} кг. Кричит - {Bird.chicken_1_sound}, чтобы ее {chicken_1.eat()} {chicken_1.eggs()}')
print(f'4. Курица {chicken_2.name} весит {chicken_2.weight} кг. Кричит - {Bird.chicken_2_sound}, чтобы ее {chicken_2.eat()} {chicken_2.eggs()}' )
print(f'5. Утка {duck.name} весит {duck.weight} кг. Кричит - {Bird.duck_sound}, чтобы ее {duck.eat()} {duck.eggs()}')
all_weight.append(goose_1.weight)
max_weight[goose_1.name] = goose_1.weight
all_weight.append(goose_2.weight)
max_weight[goose_2.name] = goose_2.weight
all_weight.append(chicken_1.weight)
max_weight[chicken_1.name] = chicken_1.weight
all_weight.append(chicken_2.weight)
max_weight[chicken_2.name] = chicken_2.weight
all_weight.append(duck.weight)
max_weight[duck.name] = duck.weight

class Sheep(Animal): #овец стричь
    sheep_1_sound = 'беееее'
    sheep_2_sound = 'бе-бе-бе'
    def cut(self):
        return 'постригли.'

sheep_1 = Sheep('Барашек', 35)
sheep_2 = Sheep('Кудрявый', 40)

print(f'6. Овца {sheep_1.name}  весит {sheep_1.weight} кг. Кричит - {Sheep.sheep_1_sound}, чтобы его {sheep_1.eat()} и {sheep_1.cut()}')
print(f'7. Овца {sheep_2.name} весит {sheep_2.weight} кг. Кричит - {Sheep.sheep_2_sound}, чтобы его {sheep_1.eat()} и {sheep_2.cut()}')
all_weight.append(sheep_1.weight)
max_weight[sheep_1.name] = sheep_1.weight
all_weight.append(sheep_2.weight)
max_weight[sheep_2.name] = sheep_2.weight

class MilkAnimal(Animal): #корову и коз доить
    cow_sound = 'муууу'
    goat_1_sound = 'мээээ'
    goat_2_sound = 'мэ-мэ-мэ'
    def get_milk(self):
        return 'подоили.'

cow = MilkAnimal('Манька', 250)
goat_1 = MilkAnimal('Рога', 30)
goat_2 = MilkAnimal('Копыта', 25)

print(f'8. Корова {cow.name}  весит {cow.weight} кг. Кричит - {MilkAnimal.cow_sound}, чтобы ее {cow.eat()} и {cow.get_milk()}')
print(f'9. Коза {goat_1.name} весит {goat_1.weight} кг. Кричит - {MilkAnimal.goat_1_sound}, чтобы ее {goat_1.eat()} и {goat_1.get_milk()}')
print(f'10. Коза {goat_2.name} весит {goat_2.weight} кг. Кричит - {MilkAnimal.goat_2_sound}, чтобы ее {goat_2.eat()} и {goat_2.get_milk()}')
all_weight.append(cow.weight)
max_weight[cow.name] = cow.weight
all_weight.append(goat_1.weight)
max_weight[goat_1.name] = goat_1.weight
all_weight.append(goat_2.weight)
max_weight[goat_2.name] = goat_2.weight

inv_max_weight = [(value, key) for key, value in max_weight.items()]

print(f' Общий вес животных - {sum(all_weight)} кг.')
print(f' Больше всех весит {max(inv_max_weight)[1]}, {max(inv_max_weight)[0]} кг.')



