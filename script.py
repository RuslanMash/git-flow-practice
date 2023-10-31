class Diary:
    def __init__(self, pages, marks, id, student):
        self.id = id
        self.student_id = student.id
        self.pages = pages
        self.marks = marks
        
    def plohoi(self):
        return f"У вашего ребенка не хватает {self.pages} страниц и у него плохие оценки {self.marks}" 
        
class Subject:
    def __init__(self, name, id):
        self.id = id
        self.name = name
        
    def info(self):
        return f"{self.name}"
        
class Student:
    def __init__(self, name, surname, age, id):
        self.id = id
        self.name = name
        self.surname = surname
        self.age = age
        
    def description(self):
        return f"Students name {self.name}, surname {self.surname} and his age is {self.age}"
        
st = Student('Ruslan', 'Mashukhei', 18, 2)
st.description()        
d1 = Diary(12,5,2, st)
d1.plohoi()
s1 = Subject('math', 1)
s1.info()



