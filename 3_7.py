class AnimalShelter:
    
    def __init__(self):
        from Queue import Queue
        self.dogs = Queue()
        self.cats = Queue()
        self.oldest = Queue()
    def enqueue(self, data, type):
        if str.lower(type) == "dogs" or str.lower(type) == "dog":
            self.dogs.put(data)
            self.oldest.put(str.lower(type))
        elif str.lower(type) == "cats" or str.lower(type) == "cat":
            self.cats.put(data)
            self.oldest.put(str.lower(type))
    def dequeueAny(self):
        if self.oldest.empty():
            return None
        type = self.oldest.get()
        if type == "dogs" or type == "dog":
            return self.dequeueDog()
        else:
            return self.dequeueCat()
    def dequeueDog(self):
        if not self.dogs.empty():
            return self.dogs.get()
        else:
            return None
    def dequeueCat(self):
        if not self.cats.empty():
            return self.cats.get()
        else:
            return None

shelter = AnimalShelter()
print shelter.dequeueAny()
print shelter.dequeueDog()
print shelter.dequeueCat()
shelter.enqueue("Golden Retriever", "dog")
shelter.enqueue("Calico", "cats")
shelter.enqueue("Pitbull", "dog")
shelter.enqueue("Parrot", "bird")
shelter.enqueue("Tabby", "CAT")
print shelter.dequeueAny()
print shelter.dequeueDog()
print shelter.dequeueCat()
print shelter.dequeueAny()