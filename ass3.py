#!/opt/bin/python3
# Author: Saige Liu, V00812068

import csv
import sys

class Spreadsheet:
    def __init__(self):
        self.fileName=''
        self.numRows=0
        self.numCols=0
        self.contents=[]
    
    def __str__(self):
        Spreadsheet_tostring=""
        for i in range(len(self.contents)):
            for m in range(len(self.contents[i])):
                if(m+1==len(self.contents[i])):
                    Spreadsheet_tostring += self.contents[i][m]
                else:    
                    Spreadsheet_tostring += self.contents[i][m] + ", "
            
            Spreadsheet_tostring += "\n"
        return Spreadsheet_tostring
    
    def set_fileName(self,name):
        self.fileName =name
    
    def get_fileName(self):
        return self.fileName

    def set_numRows(self,rows):
        self.numRows=rows

    def get_numRows(self):
        return self.numRows

    def set_numCols(self,cols):
        self.numRows=rows

    def get_numCols(self):
        return self.numCols

    def set_contents(self, contents):
        self.contents = contents

    def get_contents(self):
        return self.contents

    def add_contents(self, new):
        self.contents.append(new)

def deleterow(ss,rowNum):
    try:
        num=int(float(rowNum))
        del ss.contents[num]
        ss.numRows-=1
    except:
        print("The rowNumber is out of range")
        reason = sys.exc_info()
        print("Reason: ", reason[1])

def evalsum(ss,col):
    try:
        if(ss.contents[0][col].isalpha()):
            print("This column can not be calculated") 
            return 0
        elif(ss.contents[0][col]==None):
            print("This column can not be calculated") 
            return 0      
        else:
            total=0
            for element in ss.contents:
                total+=int(float(element[col]))
            return total
    except:
        print("The colNumber is out of range")
        reason = sys.exc_info()
        print("Reason: ", reason[1])
        return 0

def evalavg(ss,col):
    try:
        return evalsum(ss,col)/ss.numRows
    except:
        print("The colNumber is out of range")
        reason = sys.exc_info()
        print("Reason: ", reason[1])

def findrow(ss,numcol,string):
    try:
        count=0
        for i in ss.contents:
            if string in ss.contents[count][numcol]:
                print("findrow %d" %count)
                break
            count+=1
    except:
        print("The colNumber is out of range")
        reason = sys.exc_info()
        print("Reason: ", reason[1])
        
def help():
    print("\nThe valid commands are:"
        "\nquit                     -- to exit the program"
        "\nhelp                     -- to display this help message"
        "\nload <filename>          -- to read in a spreadsheet"
        "\nsave                     -- to save the spreadsheet back"
        "\nsave <filename>          -- to save back to a different file"
        "\nmerge <filename>         -- to read and append rows from another file"
        "\nstats                    -- to report on the spreadsheet size"
        "\nsort <col>               -- sort rows based on text data in column <col>"
        "\nsortnumeric <col>        -- sort rows based on numbers in column <col>"
        "\ndeleterow <n>            -- delete row <n> from spreadsheet"
        "\nfindrow <col> <text>     -- print the number of the first row"
        "\n                            such that column <col> holds <text>"
        "\nfindrow <col> <text> <n> -- similarly, except search starts at"
        "\n                            row number n",
        "\nprintrow <n>             -- print row number <n>"
        "\nprintrow <n> <m>         -- print rows numbered <n> through <m>"
        "\nevalsum <col>            -- print the sum of the numbers that"
        " \n                            are in column <col>"
        "\nevalavg <col>            -- print the average of the numbers that"
        " \n                            are in column <col>"
        "\nNULL"
        )
##########
def load(ss,fileName):
    try:
        if fileName[0]=='"' and fileName[-1]=='"':
            fileName = fileName[1:-1]
        count=0
        ss.fileName=fileName
        csvfile = open(fileName,newline='')
        csvreader = csv.reader(csvfile,delimiter=',')
       #,escapechar='\"'
        for row in csvreader:
            
            count+=1
            #for i in row:
                #print("%s"%i) 
            ss.add_contents(row)
        csvfile.close()
        ss.numRows=count
        ss.numCols=len(ss.contents[0])
  
    except:
        print("Error occurred while accessing file", fileName)
        reason = sys.exc_info()
        print("Reason: ", reason[1])
    
def merge(ss,fileName):
    try:
        if fileName[0]=='"' and fileName[-1]=='"':
            fileName = fileName[1:-1]
        count=ss.numRows
        ss.fileName=fileName
        csvfile = open(fileName,newline='')
        csvreader = csv.reader(csvfile,delimiter=',')
       #,escapechar='\"'
        for row in csvreader:
            
            count+=1
            #for i in row:
                #print("%s"%i) 
            ss.add_contents(row)
        csvfile.close()
        ss.numRows=count
        ss.numCols=len(ss.contents[0])
        
    except:
        print("Error occurred while accessing file", fileName)
        reason = sys.exc_info()
        print("Reason: ", reason[1])
##########
def printrow(ss,start,end):
    if end>ss.numRows:
        end=ss.numRows-1
    for row in range(start,end+1):
        for y in range(0,ss.numCols):
            if(ss.contents[row][y].find(',')!=-1):
                print('\"'+ss.contents[row][y]+'\"',end='')
            elif(ss.contents[row][y].find('\"')!=-1):
                p =ss.contents[row][y].find('\"')
                ss.contents[row][y]='\"'+ss.contents[row][y][:p]+'\"'+ss.contents[row][y][p:]+'\"'
                print(ss.contents[row][y],end='')
            else:
                print(ss.contents[row][y],end='')
            print(',  ',end='')
        print('\n',end='')


##########
def save(ss,newfile):
    csvfile =open(newfile,'w',newline='')
    csvwriter = csv.writer(csvfile,delimiter=',')
    for row in ss.contents:
        csvwriter.writerow(row)
    csvfile.close()

def selectColumn(row):
    return row[k]

def selectColumn2(row):
    return row[n]

def sort(ss,col):
    try:
        global k
        k=col
        ss.contents=sorted(ss.contents,key=selectColumn)
    except:
        print("The colNumber is out of range")
        reason = sys.exc_info()
        print("Reason: ", reason[1])

def sortnumeric(ss,col):
    try:
        global n
        n=col
        ss.contents=sorted(ss.contents,key=selectColumn2)
    except:
        print("The colNumber is out of range")
        reason = sys.exc_info()
        print("Reason: ", reason[1])

def stats(ss):
    print('File:  %s'%ss.fileName)
    print('Rows:  %d'%ss.numRows)
    print('Columns:  %d'%ss.numCols)

def main():
    ss=Spreadsheet()
    x =1
    while True:
        command=input('Enter a subcommand ==> ')
        list1=command.split(' ')
        if(list1[0]== None or list1[0] =='quit'):
            print('Exit')   
       
            break
        elif(list1[0] == 'load'):
            if(len(list1)>1):
                ss=Spreadsheet()
                load(ss,list1[1])
                print('LOADING COMPLETED \nNotice:colNum should be capital letter')
                print(' ')
            else:
                print('please enter filename')

        elif(list1[0] == 'deleterow'):
            if(len(list1)>1):
                deleterow(ss,list1[1])
            else:
                print('please enter row number')

        elif(list1[0] == 'evalavg'):
            try:
                if(len(list1)>1):
                    if(list1[1].isalpha()):
                        num1=ord(list1[1])-ord('A')
                    else:
                        num1=int(float(list1[1]))
                    print('"-- average = %d'%evalavg(ss,num1))
                else:
                    print('please enter col number or letter')
            except:
                print("WRONG ENTER")
                reason = sys.exc_info()
                print("Reason: ", reason[1])
        elif(list1[0] == 'evalsum'):
            try:
                if(len(list1)>1):
                    if(list1[1].isalpha()):
                        num2=ord(list1[1])-ord('A')
                    else:
                        num2=int(float(list1[1]))

                    print("-- sum = %d"%evalsum(ss,num2))
                else:
                    print('please enter col number or letter')
            except:
                print("WRONG ENTER")
                reason = sys.exc_info()
                print("Reason: ", reason[1])
        
        elif(list1[0] == 'findrow'):
            try:
                if(len(list1)>2):
                    if(list1[1].isalpha()):
                        num2=ord(list1[1])-ord('A')
                    else:
                        num2=int(float(list1[1]))    
                    findrow(ss,num2,list1[2])
                else:
                    print('Pleas enter col number and the text you want to find')
            except:
                print("WRONG ENTER")
                reason = sys.exc_info()
                print("Reason: ", reason[1])

        elif(list1[0] == 'help'):
            help()
        elif(list1[0] == 'printrow'):
            if(len(list1)>2):
                num1=int(float(list1[1]))
                num2=int(float(list1[2]))
                printrow(ss,num1,num2)
            else:
                print('Please enter row number')
        elif(list1[0] == 'merge'):
            if(len(list1)>1):
                merge(ss,list1[1])
                print('COMPLETED \nNotice:colNum should be capital letter')
                print(' ')
            else:
                print('please enter filename')
            
        elif(list1[0] == 'sort'):
            try:
                if(len(list1)>1):
                    if(list1[1].isalpha()):
                        col=ord(list1[1])-ord('A')
                    else:
                        col=int(float(list1[1]))
                
                    sort(ss,col)
                else:
                    print('please enter column number')
            except:
                print("WRONG ENTER")
                reason = sys.exc_info()
                print("Reason: ", reason[1])
        elif(list1[0] == 'sortnumeric'):
            try:

                if(len(list1)>1):
                    if(list1[1].isalpha()):
                        col=ord(list1[1])-ord('A')
                    else:
                        col=int(float(list1[1]))
                
                    sortnumeric(ss,col)
                else:
                    print('please enter column number')
            except:
                print("WRONG ENTER")
                reason = sys.exc_info()
                print("Reason: ", reason[1])
        elif(list1[0] == 'stats'):
            stats(ss)
        elif(list1[0]=='save'):
            if(len(list1)>1):
               
                save(ss,list1[1])
                
            else:
                print('please enter filename')
        else:
            print("Command not found,check 'help' or enter agian")
















        x +=1
        



main()
    
    



    
