#while
i=1
while i <=6:#until i become 5 it will gives the true
    print('*'*i)
    i+=1
print("done")#when it will false it will print
#gussing number game
secreat=10
guss_number=0
guss_no=3
while guss_number<guss_no:
    guss=int(input('guss: '))
    guss_number +=1
    if guss ==secreat:
        print('you won !')
        break
else:
    print("sorry,you lost...")
#exercise
command=""
while command.lower()!=quit:
    command=input("> ")
    if command.lower()=="start":
        print("the car is started")
    elif command.lower()=="stop":
        print("car stoped")
    elif command.lower()=="help":
        print("start-to start the car\n"
              "stop-to stop the car\n"
              "quit -to exit\n")
    elif command.lower()=="quit":
        break
    else:
        print("i dont understand")




