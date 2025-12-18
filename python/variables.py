# name="Gaurav"
# age=19
# college="united intitute of technology"
# print(name, age, college)

class student:
    def __init__(self,name,age,college):
        self.name=name
        self.age=age
        self.college=college

c2=student("amit",26,"vikash inter college")
c1=student()
print(c1.name())
print(c1.age())
print(c1.college())     
