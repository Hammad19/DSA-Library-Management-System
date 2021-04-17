import os
import linkedlist 


#Linear Search
#Binary Search
#Linked List_2
#Merge Sort
#Selection Sort
#Stack
#Array_2

stack = []  
def binary_search(arr, low, high, x):

        if high >= low:
            mid = (high + low) // 2
            if int(arr[mid]) == x:
                return arr[mid]
            elif int(arr[mid]) > x:
                return binary_search(arr, low, mid - 1, x)
            else:
                return binary_search(arr, mid + 1, high, x)
     
        else:
            return -1


def linearsearch(arr, x):
  
    for i in range(len(arr)):
  
        if int(arr[i]) == int(x):
            return arr[i]
  
    return -1

class Books:
    books = linkedlist.LinkedList()
    avail_books=0
    total_books=0
    issued_books=0
    def __init__(self,no,name,bookcout,available):
                 self.book_no=no
                 self.book_name=name
                 self.bookcout=bookcout
                 self.book_available = available
                     
                 
                
    def getallbookno(self):
            if os.path.exists("books.txt"):
                for line in open("books.txt", "r").readlines():
                    data = line.split(',')
                    self.books.push(str(data[0]))
                    
                    
    #Linear Search        
    def IsBookIdAlreadyTaken(self):
        bookids = []
        if os.path.exists("books.txt"):
            for line in open("books.txt", "r").readlines():
                data = line.split(',')
                bookids.append(data[0])
                
        if(linearsearch(bookids,self.book_no)==-1):
            return False
        else:
            return True
        
    def AddBook(self):
        f = open("books.txt","a+")
        if(self.IsBookIdAlreadyTaken()==False):
            f.write(str(self.book_no) + "," + 
                   str(self.book_name)+ "," + 
                   str(self.bookcout)+ "," +
                   str(self.book_available) + ",\n")   
            print("\tBook Added")
           
            
        else:
             print('This Book Number is Already in Use')
            
        f.close()
        str(input("Press any key To Continue"))
        stack.pop()()
    
    
    def MoveData(self):
         with open("tempbooks.txt","r") as f:
            with open("books.txt", "w+") as f1:
                for line in f:
                    f1.write(line)
                f.close()
                f1.close()
         
         if os.path.exists("tempbooks.txt"):
             os.remove("tempbooks.txt")
         else:
            print("The file does not exist")
            
    def DeleteBook(self):
    
        f = open("books.txt","r")
        fx = open("tempbooks.txt","w")
        #Linear Search
        for line in f.readlines():
            data = line.split(',')
            if(str(self.book_no)==str(data[0])):
                continue
            else:
                fx.write(
                    str(data[0]) + "," + 
                    str(data[1])+ "," + 
                    str(data[2]) +"," + 
                    str(data[3])+",\n" )
                
        f.close()
        fx.close()
        self.MoveData()
        
        str(input("\n\tBook Deleted\n\tPress Any Key To Go Back To The main menu\n\n"))
        stack.pop()()
    
    
    def VeiwBook(self):
        for line in open("books.txt", "r").readlines():
                data = line.split(',')   
                if(self.book_no==data[0]):
                    
                    print('Book ID: ' + data[0])
                    print('Student Name: ' + data[1])
                    print('Books Available: ' + data[2])
                    print('Book Status Available/Not: ' + data[3])
                    
                
        str(input("Press Any Key To Go Back To The main menu"))
        stack.pop()()
    
    def DisplayAllBookRecord(self):
        self.books= linkedlist.LinkedList()
        self.getallbookno()
        self.books.selectionSort()
    
        for i in range(self.books.getCount()):
            for line in open("books.txt", "r").readlines():
                data = line.split(',')   
                if(self.books.returnNthfromfirst(i)==data[0]):
                    self.book_no = data[0]
                    self.book_name = data[1]
                    self.bookcout=data[2]
                    print(self.book_no + "     |      " + self.book_name )
                    
        str(input("\n\nPress Any Key To Go Back To The main menu\n\n"))
        stack.pop()()
        
    
    def DisplayAvailableBooks(self):
        self.books= linkedlist.LinkedList()
        self.getallbookno()
        self.books.selectionSort()
        for i in range(self.books.getCount()):
            for line in open("books.txt", "r").readlines():
                data = line.split(',')   
                if((self.books.returnNthfromfirst(i)==data[0]) and (int(data[2])> 0)):
                    self.book_no = data[0]
                    self.book_name = data[1]
                    self.bookcout=data[2]
                    print(self.book_no + "     |      " + self.book_name )
                    
        str(input("\n\nPress Any Key To Go Back To The main menu\n\n"))
        stack.pop()()
            
        

class Student:
    total_students=0
    student = linkedlist.LinkedList()
         
    def __init__(self,no,name,grade,booksborrowed):
        self.student_no=no
        self.student_name=name
        self.student_grade=grade
        self.booksborrowed = booksborrowed
        

        
    def getAllStudentdno(self):
            for line in open("students.txt", "r+").readlines():
                data = line.split(',')
                self.student.push(data[0])
                
       
    def IsStudentIdAlreadyTaken(self):
        studentids = []
        if os.path.exists("students.txt"):
            for line in open("students.txt", "r").readlines():
                data = line.split(',')
                studentids.append(data[0])
                
        if(binary_search(studentids,0,len(studentids)-1,self.student_no)==-1):
            return False
        else:
            return True
    def AddStudent(self):
        
        f = open("students.txt","a+")
        if(self.IsStudentIdAlreadyTaken()==False):
            f.write(
                str(self.student_no) + "," + 
                str(self.student_name)+ "," + 
                str(self.student_grade) +"," +
                str(0) + ",\n")
            print('\tStudent Added')
           

        else:
            
            print('\tThis ID is Already in Use')
             
        
        f.close()
        str(input("\n\nPress Any Key To Go Back To The main menu\n\n"))
        stack.pop()()
        
     
     
    def ModifyStudentRecord(self):
        
        f = open("students.txt","r")
        fx = open("tempstudents.txt","w")
        for line in f.readlines():
            data = line.split(',')

            if(str(self.student_no)==str(data[0])):
                fx.write(str(input('Enter New Student Number: '))+ "," 
                         + str(input('Enter New Name: '))+ ","
                         + str(input('Enter New Grade: '))+ ","
                         + str(input('Enter Books Borrowed: '))
                         + "\n")        
            else:
                fx.write(str(data[0]) + "," + 
                         str(data[1])+ "," + 
                         str(data[2]) +", "+
                         str(data[3]) +",")
                        
        f.close()
        fx.close()
        self.MoveData()
        
        str(input("\n\nPress Any Key To Go Back To The main menu\n\n"))
        stack.pop()()
        
            
    def MoveData(self):
         with open("tempstudents.txt","r") as f:
            with open("students.txt", "w+") as f1:
                for line in f:
                    f1.write(line)
                
            f1.close()
            f.close()
         
         if os.path.exists("tempstudents.txt"):
             os.remove("tempstudents.txt")
         else:
            print("The file does not exist")
        
                
        
    def VeiwStudentRecord(self):
        if(os.path.exists("students.txt")):
            for line in open("students.txt", "r").readlines():
                data = line.split(',')   
                #Linear Search
                if(str(self.student_no)==data[0]):
                    print('Student ID: ' + data[0])
                    print('Student Name: ' + data[1])
                    print('Student Grade: ' + data[2])
                    print('Books Borrowed: ' + data[3])
        else:
            print("No Record Found")
        str(input("Press Any Key To Go Back To The main menu"))
        stack.pop()()
    
    
    
    def DisplayAllStudentRecord(self):
        self.student = linkedlist.LinkedList()
        self.getAllStudentdno()
        self.student.head = self.student.mergeSort(self.student.head)
        #LINEAR SEARCH
        for i in range(self.student.getCount()):
            for line in open("students.txt", "r").readlines():
                data = line.split(',')   
                if(self.student.returnNthfromfirst(i)==data[0]):
                    print("\n\t"+ data[0] + "     |      " + data[1])
        str(input("\n\nPress Any Key To Go Back To The main menu\n\n"))
        stack.pop()()
                    
        
        
        
        

print('*******************************************************')
print('       L I B R A R Y           M A N  A G E R')
print('*******************************************************')


print()
isissuing= True
def updatebookavailable(bookno,stdno):
    f = open("books.txt","r")
    fx = open("tempbooks.txt","w")
    for line in f.readlines():
            data = line.split(',')

            if(str(bookno)==str(data[0])):
                if(int(data[2])> 0):
                    data[2]= str(int(data[2]) -1)
                else:
                    data[3] = 'no'
                
                fx.write(str(data[0])+ "," 
                     + str(data[1])+ ","
                     + str(data[2])+ ","
                     + str(data[3])
                     + ",\n")    
                
                    
            else:
                fx.write(str(data[0]) + "," + 
                         str(data[1])+ "," + 
                         str(data[2]) +", "+
                         str(data[3]) +",")
                
                        
    
    bk = Books('none','none','none','none')
    bk.MoveData()   
    UpdateStudentBorrowedBooksNo(stdno)
    
    
def UpdateStudentBorrowedBooksNo(stdid):
    f = open("students.txt","r")
    fx = open("tempstudents.txt","w")
    for line in f.readlines():
            data = line.split(',')
            if(str(stdid)==str(data[0])):
                
                if(int(data[3])>= 0 and int(data[3])< int(2)):
                    data[3]= str(int(data[3])+ 1)
                    fx.write(str(data[0])+ "," 
                         + str(data[1])+ ","
                         + str(data[2])+ ","
                         + str(data[3])
                         + ",\n")          

                    
            else:
                fx.write(str(data[0]) + "," + 
                         str(data[1])+ "," + 
                         str(data[2]) +", "+
                         str(data[3]) +",")
                        
    
    std1 = Student('none','none','none','none')  
    std1.MoveData()
    str(input("\n\nPress Any Key To Go Back To The main menu\n\n"))
    stack.pop()()
    
    
def IsBookandStudentAlreadyIssued(bookno,stdno):
    if(os.path.exists("IssuedBooks.txt")):
        for line in open("IssuedBooks.txt", "r").readlines():
            data=line.split(',')
            if(str(stdno)== data[0] and str(bookno) == data[1]):
                return True
            else: 
                return False
    else:
        return False
        
    
    
    
def IssueBook():
    stdid = str(input("Enter Student ID: "))
    bookid = str(input("Enter Book ID: "))
   
    if(os.path.exists("students.txt")):
        for line in open("students.txt", "r").readlines():
                    data = line.split(',')   
                    #Linear Search
                    if(str(stdid) == data[0]):
                        if(int(data[3]) < int(2)):
                            if(os.path.exists("books.txt")):
                                for line in open("books.txt", "r").readlines():
                                    data2 = line.split(',') 
                                    if(str(bookid) == str(data2[0])):
                                        if(int(data2[2]) > int(0)):
                                            if(IsBookandStudentAlreadyIssued(bookid,stdid)==False):
                                                fx = open("IssuedBooks.txt","a+")
                                                fx.write(str(stdid) + "," + 
                                                        str(bookid)+ ",\n")
                                                updatebookavailable(bookid,stdid)
                                            else:
                                                print("Same Book and Student ID already issued")
                                            
                                        else:
                                            print("This Book is not Available")
                                    else:
                                        print("No Book with This ID Found")
                        else:
                            print("No More Books Can Be issued to This Student")
                    else:
                        print("No Student with this ID Found")
                                
    
    
    str(input("Press Any Key To Go Back To Main Menu"))
    stack.pop()()
                    
    
def MoveData():
        with open("tempbookissued.txt","r") as f:
            with open("IssuedBooks.txt", "w+") as f1:
                for line in f:
                    f1.write(line)
                
            f1.close()
            f.close()
         
        if os.path.exists("tempbookissued.txt"):
            os.remove("tempbookissued.txt")
        else:
            print("The file does not exist")
        
    
def DepositBook():
    stdid = str(input("Enter Student ID"))
    bookid = str(input("Enter Book ID"))
   
    if(os.path.exists("students.txt")):
        for line in open("students.txt", "r").readlines():
                    data = line.split(',')   
                    #Linear Search
                    if(str(stdid) == data[0]):
                        if(os.path.exists("books.txt")):
                            for line in open("books.txt", "r").readlines():
                                data2 = line.split(',') 
                                if(str(bookid) == str(data2[0])):
                        
                                    fx = open("tempbookissued.txt","w")
                                    for line in open("IssuedBooks.txt", "r").readlines():
                                        data=line.split(',')
                                        if(str(stdid)== data[0] and str(bookid) == data[1]):
                                            continue
                                        else: 
                                            fx.write(str(data[0]) + "," + 
                                            str(data[1])+ ",\n")
                                    
                                    
                        
                                        
                                else:
                                    print("No Book with This ID Found")
                    else:
                        print("No Student with this ID Found")
                                
                            
     
    
    str(input("Press Any Key To Go Back To Main Menu"))
    stack.pop()()
                    
        
def AdministraterMenu():
    while(True):
        menu=[' Add Student',' Display All Student Record',' Modify Student Record',' Create Book',' Display All Books',' Display Available Books',' Delete Book',' View Book',' View Student Record',' View Issued Books',' Back to Main Menu']
        for x in range (len(menu)):
            print('\t',x+1,'. ',menu[x])
        print('_________________________________________')
        select=input("Enter Your Selection (1-11): ") 
        
        if select == '1':
            stack.append(AdministraterMenu)
            std = Student(
                int(input('Enter Student Number: ')),
                str(input('Enter Student name: ')),
                str(input('Enter Grade: ')),
                str(0)
                )
            std.AddStudent() 
            
        elif select == '2':
            stack.append(AdministraterMenu)
            std1 = Student(
                'none',
                'none',
                'none',
                'none')
            std1.DisplayAllStudentRecord()
            
        elif select =='3':
            stack.append(AdministraterMenu)
            std = Student(
                str(input('Enter Student Number: ')),
                'none',
                'none',
                'none',)
            std.ModifyStudentRecord()
            stack.append(AdministraterMenu)
        elif select == '4':
            stack.append(AdministraterMenu)
            bk = Books(
                str(input("\tEnter the Book Number to Be Created: ")),
                str(input( '\tBook Name\t\t : ')),
                str(input( '\tHow Many Books You Want To add in Library\t\t : ')),
                'yes')
            bk.AddBook()
            
        elif select == '5':
            stack.append(AdministraterMenu)
            bk = Books('none','none','none','none')
            bk.DisplayAllBookRecord()
        
        elif select == '6':
            stack.append(AdministraterMenu)
            bk = Books('none','none','none','yes')
            bk.DisplayAvailableBooks()
        elif select == '7':
            stack.append(AdministraterMenu)
            bk = Books(str(input('Enter Book ID: ')),
                'none',
                'none',
                'none',
                )
            bk.DeleteBook()
            
        elif select == '8':
             stack.append(AdministraterMenu)
             bk = Books(str(input('Enter Book ID: ')),
                'none',
                'none',
                'none',
                )
             bk.VeiwBook()
            
            
        elif select == '9':
            stack.append(AdministraterMenu)
            std = Student(int(input('Enter Student ID: ')),'none','none','none')
            std.VeiwStudentRecord()
            
        elif select== '10':
            stack.append(AdministraterMenu)
            print('')
            
        elif select == '11':
            stack.pop()()
        
        

def start():
    
    while(1):
        print('*****************************')
        print("           Main Menu")
        print('*****************************')

        print ("\t1. Book Issue \n\t2. Book Deposit\n\t3. Administrator Menu\n\t4. Exit")
        print()
        select=input("Enter Your Selection (1-4): ")
        if select=='1':
            stack.append(start)
            IssueBook()
            
            
        elif select=='2':
            stack.append(start)
            DepositBook()
            
        elif select=='3':
            stack.append(start)
            AdministraterMenu()
            
        elif select=='4':
            break
        else:
            print('Wrong Input')

start()
    
