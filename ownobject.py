from dataclasses import dataclass, field
@dataclass
class knife:
    color: str
    size: str
    sharpness: int
    def sharpen(self, sharpness: int):
        self.sharpness = sharpness
    def cut_pizza(self, pizza: object):
        if self.sharpness > 5:
            print("Pizza cut")
        else:
            print("Pizza not cut")
@dataclass
class pizza:
    name: str
    size: int = 10
    topping: str = "Cheese"
    slice_left: int = 6
    crust: str = "Normal Crust"  # Add this if you want to pass crust
    pizza_brand: str = field(default="Dominoes", init=False)  # Class variable, not set during __init__

    def big(self, sizes: int):
        self.size = sizes

    def items(self, new_topping: str):
        self.topping = new_topping

    def left(self, remains: int):
        self.slice_left = remains

    def status(self):
        return f"{self.name}: \n Toppings: {self.topping}, \n Size: {self.size} inches, \n Slices left: {self.slice_left}, \n Crust: {self.crust}"

    def eat_slice(self):
        if self.slice_left > 0:
            self.slice_left -= 1
        else:
            print("No slices left!")

    def extra_topping(self, extra: str):
        self.topping += ", " + extra
        return self.topping

    def crust_type(self, crust: str):
        self.crust = crust
        return self.crust
    name: str
    size: int = 10
    topping: str = "Cheese"
    pizza_brand = "Dominoes"
    slice_left: int = 6
    def big(self, sizes: int):
        self.size = sizes
    def items(self, new_topping: str):
        self.topping = new_topping
    def left(self, remains: int):
        self.slice_left = remains
    def status(self):
        return f"{self.name}: \n Toppings: {self.topping}, \n Size: {self.size} inches, \n Slices left: {self.slice_left}"
    def eat_slice(self):
        if self.slice_left > 0:
            self.slice_left -= 1
        else:
            print("No slices left!")
    def extra_topping(self, extra: str):
        self.topping += ", " + extra
        return self.topping
    def crust_type(self, crust: str):
        self.crust = crust
        return self.crust
if __name__ == "__main__":
    pineapple_pizza = pizza(name="Pineapple pizza", size=16, topping="Pineapple", slice_left=4,crust="Normal Crust")
    extra_cheese_pizza = pizza(name="Extra cheese pizza", size=12, topping="Extra cheese", slice_left=6,crust="Normal Crust")
    print(pineapple_pizza.pizza_brand)
    print(extra_cheese_pizza.pizza_brand)
    pineapple_pizza.eat_slice()
    extra_cheese_pizza.eat_slice()
    print(pineapple_pizza.status())
    print(extra_cheese_pizza.status())
    print(pineapple_pizza.extra_topping("Ham"))
    print(extra_cheese_pizza.extra_topping("Bacon"))
    print(pineapple_pizza.status())
    print(extra_cheese_pizza.status())
    print(pineapple_pizza.crust_type("Normal Crust"))
    print(extra_cheese_pizza.crust_type("Normal Crust"))
    print(pineapple_pizza.status())
    print(extra_cheese_pizza.status())
    knife = knife(color="red", size="small", sharpness=5)
    knife.sharpen(10)
    knife.cut_pizza(pineapple_pizza)
    knife.cut_pizza(extra_cheese_pizza)