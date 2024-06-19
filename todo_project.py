import os
print('Todo')
task_list=[]
def add():
    task=input('Enter task: ')
    task_list.append(task)
    task_list.append('\n')
    f=open('to-do.txt','w')
    for i in range(len(task_list)):
        f.write(task_list[i])

    f.close()

def delete():
    if os.path.exists('to-do.txt'):
        f=open('to-do.txt','r')
        a=f.readlines()
        b=list(a)
        l=int(input('enter task: '))
        del b[l-1]
        f.close()
        f=open('to-do.txt','w')
        for i in range(len(b)):
            f.write(b[i])
        f.close()
    else:
        print('\nList is empty\n')

def view():
    if os.path.exists('to-do.txt'):
        f=open('to-do.txt','r')
        print(f.read())
    else:
        print('\nList is empty\n')

def mark():
    if os.path.exists('to-do.txt'):
        f=open('to-do.txt','r')
        a=f.readlines()
        b=list(a)
        print(b)
        l=int(input('enter task: '))
    #del b[l-1]
        z=b[l-1]
        g=len(z)
        z1=("{}-Done\n".format(z[0:g-1]))
        del b[l-1]
        b.insert(l-1,z1)
        f.close()
        f=open('to-do.txt','w')
        for i in range(len(b)):
            f.write(b[i])
        f.close()
    else :
        print('\nList is empty\n')

def clear():
    if os.path.exists('to-do.txt'):
        os.remove('to-do.txt')
        print('List is deleted')
    else :
        print('\nList is empty\n')



while True:
    print('1.add\n2.del\n3.view\n4.mark as done\n5.Clear list\n6.exit\n')
    option=int(input())
    if option==1:
        add()
    elif option==2:
        delete()
    elif option==3:
        view()
    elif option==4:
        mark()
    elif option==5:
        clear()

    elif option==6:
        break
