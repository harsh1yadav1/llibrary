print("Welcome user!!!")
def run():
    print("press 1 to continue")
    print("press 2 to exit")
    choose = int(input("enter your choice :"))
    if choose == 2:
        print("thanks for visiting")
        exit()
    return True
run()
    
                                      
book_no = ("math", "hindi", "java")
book = input("which book do you want to acess : ")
if book == "3":
    print("here's is your math book")
if book == "4":
    print("here's your hindi book")
if book == "5":
     print("here's your java book")
if book == "3":
    print("book3:--math is widely used")
    print("A math book can be described in several ways, depending on its purpose and audience, such as an accessible overview that uses visuals to explain complex concepts like in the  series, a historical account of mathematical milestones, or a textbook designed to encourage independent learning through practice problems. Descriptions often highlight features like visual aids (charts, diagrams, illustrations), historical context, real-world applications, and self-study tools that make the subject approachable for both beginners and experts.") 
elif book == "4":
    print("book4:-- hindi is national language of india country")
    print("A Hindi book description can be found in its title, author, publisher, genre, and a brief summary of the plot or theme. Hindi literature includes prose (गद्य), poetry (पद्य), and prosimetrum (चंपू). The term for book in Hindi is often किताब or पुस्तक") 
elif book == "5":
    print("book5:-- java is a computer language")
    print("A Java book description typically highlights the book's coverage, from fundamental concepts like syntax and data types to advanced topics like object-oriented programming, multithreading, and the latest Java features (e.g., lambda expressions). It often mentions that the book includes real-world examples, exercises, and detailed code to help readers learn how to create, compile, and run Java programs, making it suitable for both beginners and experienced programmers, depending on the book's specific focus. ")
    
run()




