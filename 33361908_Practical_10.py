#cd c://programs
#python 33361908_Practical_10.py
studentNumberList = []
countStudentNumbers = 0

#Read from file
def Read():
    try:
        with open("Data.txt", "r") as file:
            linesTotal = 0
            listItems = []
            for line in file:
                listItems.append(line)
                linesTotal += 1
            return linesTotal, listItems
    except:
        print('Could not open Data.txt')


#Validate Student Number
def AnalyseStudents(studentNumString):
    sum = 0
    numberLength = len(studentNumString)
    for digit in str(studentNumString):
        try:
            studentNumString.isdigit()
            #if(len(studentNumString) != 8):
                #raise ValueError('Student number does not match length: ' + str(len(studentNumString)))
            len(studentNumString) != 8
            if (len(studentNumString) != 8):
                return 0
            sum = sum + int(digit)*numberLength
            numberLength = numberLength - 1
        except:
            return 0
            #print('Student number contains Alpha Character: ' + str(digit))
    result=sum%11
    #Why opposite int for result according to the assignment?
    if (result == 0):
        returnResult = 1
    else:
        returnResult = 0
    return returnResult

def Write(Bool, Value):
    try:
        if Bool:
            with open("ValidNumbers.txt", "a") as file:
                file.write(Value)
        else:
            with open("InvalidNumbers.txt", "a") as file:
                file.write(Value)
    except:
        if Bool:
            print('Could not write to ValidNumbers.txt')
        else:
            print('Could not write to InvalidNumbers.txt')

def runCompleteFunction():
    countStudentNumbers, studentNumberList = Read()
    for studentNum in range(0, countStudentNumbers):
        testStudentNumber = studentNumberList[studentNum].rstrip("\n")
        testResult = AnalyseStudents(testStudentNumber)
        if (testResult == 1):
            print(str(testStudentNumber) + ' is a VALID student number')
        else:
            print(str(testStudentNumber) + ' is an INVALID student number')
        saveStudentNumber = testStudentNumber + "\n"
        Write(testResult, saveStudentNumber)

runCompleteFunction()
