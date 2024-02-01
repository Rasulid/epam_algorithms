
# Паттерны проектирования в Python

## 1. Singleton

```python
class Singleton:
    _instance = None

    @staticmethod
    def getInstance():
        if Singleton._instance == None:
            Singleton()
        return Singleton._instance

    def __init__(self):
        if Singleton._instance != None:
            raise Exception("This class is a singleton!")
        else:
            Singleton._instance = self
```

## 2. Factory Method

```python
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

def get_pet(pet="dog"):
    pets = dict(dog=Dog(), cat=Cat())
    return pets[pet]

pet = get_pet("dog")
print(pet.speak())
```

## 3. Abstract Factory

```python
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

class PetFactory:
    def get_pet(self):
        return Dog()

    def get_food(self):
        return "Dog Food"

class CatFactory:
    def get_pet(self):
        return Cat()

    def get_food(self):
        return "Cat Food"
```

## 4. Builder

```python
class Car:
    def __init__(self):
        self.wheels = 4
        self.doors = 4
        self.engine = None

class CarBuilder:
    def __init__(self):
        self.car = Car()

    def add_engine(self, engine_type):
        self.car.engine = engine_type
        return self

    def add_wheels(self, number):
        self.car.wheels = number
        return self

    def get_result(self):
        return self.car
```

## 5. Prototype

```python
import copy

class Prototype:
    def __init__(self):
        self._objects = {}

    def register_object(self, name, obj):
        self._objects[name] = obj

    def unregister_object(self, name):
        del self._objects[name]

    def clone(self, name, **attrs):
        obj = copy.deepcopy(self._objects.get(name))
        obj.__dict__.update(attrs)
        return obj
```

## 6. Adapter

```python
class Korean:
    def speak_korean(self):
        return "An-nyeong"

class British:
    def speak_english(self):
        return "Hello"

class Adapter:
    def __init__(self, object, **adapted_method):
        self._object = object
        self.__dict__.update(adapted_method)

    def __getattr__(self, attr):
        return getattr(self._object, attr)
```

## 7. Decorator

```python
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")
```

## 8. Observer

```python
class Observer:
    def __init__(self):
        self.observers = []

    def notify(self, *args, **kwargs):
        for observer in self.observers:
            observer.update(*args, **kwargs)

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)
```

## 9. Strategy

```python
class StrategyExample:
    def __init__(self, func=None):
        if func:
            self.execute = func

    def execute(self):
        print("Default execution")

def strategy_one():
    print("Strategy one execution")

def strategy_two():
    print("Strategy two execution")
```
