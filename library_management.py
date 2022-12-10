class Login:
    def __init__(self) -> None:
        self.name=''
        self.passowrd=''
        self.data={}

    def login(self):
        name=input("Enter your name ")
        if(name in self.data):
            pword=input("Enter your password ")
            if(pword == self.data[name]):
                self.name=name
                print("Login successfull !!!")
                lib=Library()
                while(True):
                    inpz=input("""
                        1. Enter 1 for lending a book
                        2. Enter 2 for returning a book
                        3. Enter 3 for viewing the books available
                        4. Enter 4 for viewing the lending info
                        5. anything else to log out
                    """)
                    if(inpz=='1'):
                        lib.lend_book(self.name)
                    elif(inpz=='2'):
                        lib.return_book()
                    elif(inpz=='3'):
                        lib.printbooks()
                    elif(inpz=='4'):
                        lib.lending_info()
                    else:
                        break
                    
                

            else:
                print("incorrect password ")
        else:
            print("Not a member, please signup ")
    def signup(self):
        name=input("Enter your name ")
        if(name in self.data):
            print("You are already a member please login")
        else :
            passw=input("Enter password you want to set ")
            self.data[name]=passw
            print("Account created successfully")
    def printdata(self):
        for it in self.data:
            print(it)

class Library(Login):
    book=['harry potter','c++','python','java','go lang','maths','physics']
    lend={}
    def __init__(self) -> None:
        print("Welcome to the library !!!")
        
    def lend_book(self,name):
        inp=input("Enter the name of the book you want ")
        if(inp in self.book):
            Library.lend[inp]=name;
            Library.book.remove(inp);
            print("You can take your book")
        else:
            print("Sorry book not available")
    
    def lending_info(self):
        for it in Library.lend:
            print(f"{it} -> {Library.lend[it]}")

    def return_book(self):
        inp=input("Enter the name of the book you want to return ")
        Library.lend.pop(inp)
        Library.book.append(inp)
        print("Book returned successfully")
    def printbooks(self):
        for it in Library.book:
            print(it)

if __name__ == '__main__':
    mav=Login();
    print("Welcome")
    while(True):
        inp=input("""
        1. Enter 1 for signup
        2. Enter 2 for login
        3. Enter 3 for viewing the people who have an account
        4. anything else to exit
        """)  
        if(inp=='2'):
            mav.login();
        elif (inp=='1'):
            mav.signup()
        elif (inp =='3'):
            mav.printdata()
        else :
            break
    