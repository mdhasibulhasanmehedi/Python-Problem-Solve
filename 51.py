# python inheritance
class american:
   
    def show1(self):
        print('inside american class')


class newyorker(american):  # inherite parent class american
    def show2(self):
        
        print('inside newyorker class')

print('inside obj1 has one method')
obj1 = american()
obj1.show1()
print('inside obj2 has two methods')
obj2=newyorker()
obj2.show1()
obj2.show2()

