#multiple inheritance

class using_photoshop:
    def edit_photo(self):
        print("Editing Photo")

class coding:
    def make_program(self):
        print("Writing Code")

class PC(using_photoshop, coding):
    def PC(self):
        print("Using PC for multiple tasks")

s = PC()

s.edit_photo()
s.make_program()
s.PC()