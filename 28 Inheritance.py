

# It's about having one class having the functionalities of another class, without having to copy everything

class Chef:
    def make_chicken(self):
        print("The chef makes a chicken")

    def make_salad(self):
        print("The chef makes a salad")

    def make_special_dish(self):
        print("The chef makes bbq ribs")
        

Chef1 = Chef()
Chef1.make_special_dish()

class ChineseChef(Chef):
    def make_fried_rice(self): #extra
        print("The chef makes fried rice")
    
    def make_special_dish(self):
        return super().make_special_dish() #override
        print("The chef makes orange chicken")

Chef2 = ChineseChef()
Chef2.make_special_dish()