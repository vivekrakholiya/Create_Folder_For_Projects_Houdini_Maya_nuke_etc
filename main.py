
import os , datetime


ProjectName = input('Enter Project Name := ')

In_FolderList = ['Maya','Houdini','Nuke','AfterEffect','Premier','PhotoShop','Textuer','Alembic','Scripts']


usr = os.getlogin()
crntPath = os.getcwd()



md = '\data.md'
md_data = f'{ProjectName} Project is created by {usr} \nCreated Time :- {datetime.datetime.now()} \n '


direc = crntPath + f'\{ProjectName}'


run = 0
for folder in os.listdir(crntPath):
    if folder == ProjectName:
        run = 0
    else:
        run = 1

if run == 1:
    os.mkdir(direc)
    print(f'{ProjectName} Folder Created...')
else:
    print('Folder alredy Exits (.^.) ')

def CreateMultiFolder():
    if run == 1:
        for folder in In_FolderList:
            os.makedirs(direc + f'\\{folder}')
            print(f'{folder}' "Created")
        with open(direc+md,"w") as mdw:
            mdw.write(md_data)
        print("Created Md File")
    else:
        pass       


CreateMultiFolder()
