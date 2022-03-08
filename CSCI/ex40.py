class one:
    def __init__(self):
        self.x = 3
    def get_x(self):
        print(self.x)
x = 4
print(x)
if __name__ == "__main__":
    one = one()
    one.get_x()
    print(one.x)
    import one
    one.get_x()
    print(one.x)


'''
First the program prints four because it sees the x=4 and then print(x). Next it prints 3 when one.get(x) is run and it goes into the one function running get_x and printing 3 then printing 3 again when it prints one.x. After this it imports one which is the seperate file and goes there which prints 6. Now that one has been imported when it calls one.get(x) it goes to the program one and it uses that get_x() function which prints 2. Finally x has been set to five in the one program so when it calls print(one.x) it prints 5.
'''
