
class Coffee:
    def cost(self):
        return 5
    

class MilkDecorator:

    def __init__(self, coffee: Coffee):
        self._coffe = coffee

    def cost(self):
        return self._coffe.cost() + 2
    

class SugarDecorator:
    def __init__(self, coffee: Coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost() + 1

if __name__ == "__main__":
    my_coffee = Coffee()
    print("Cost of plain coffee:", my_coffee.cost())

    my_coffee_with_milk = MilkDecorator(my_coffee)
    print("Cost of coffee with milk:", my_coffee_with_milk.cost())

    my_coffee_with_milk_and_sugar = SugarDecorator(my_coffee_with_milk)
    print("Cost of coffee with milk and sugar:", my_coffee_with_milk_and_sugar.cost())