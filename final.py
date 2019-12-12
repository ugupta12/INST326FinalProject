from matplotlib import pyplot
import csv
#function gives general information about the player such as his age and whether he was active in the year of 2016
def basicinfo(lastName,firstName):
    df = open("Basic_Stats.csv")
    fr = csv.DictReader(df)
    x = lastName+", "+firstName
    name =""
    age = ""
    position=""
    status = ""
    found = False
    for line in fr:
        if line["Name"].lower() == x.lower():
            name += line["Name"]
            status +=line["Current Status"]
            if line["Age"] == "":
                age += "N/A"
            else:
                age += line["Age"]
            if line["Position"] == "":
                position += "QB"
                found = True
                break
            else:
                position += line["Position"]
                found = True
                break

    if found:
        return "Name: "+name+"\n"+"Age: "+age+"\n"+"Position: "+position+"\n"+"Status: "+status
    else:
        return "Not Found"



def main():
    lst = list()
    newLst = list()
    list1 = []
    list2 = []
    file = open("Game_Logs_Quarterback.csv",encoding ="utf8")
    data = csv.DictReader(file)
    print("2016 NFL Quarterback Tool")
    print("Created by Ujwal Gupta, Carl Jeanty, Quest Hollis, Jonathon Ramirez")
    print("Directions: Enter a quarterback's first name and last name (quarterbacks up to 2016). Then select between the following options down below")
    print("General information about the player would then be displayed and a graph comparing his stats over time")
    print("For example type 'Eli Manning'")
    firstName = input("Enter the player's first name: ")
    lastName = input("Enter the player's last name: ")
    fullName = lastName + ', ' + firstName
    print(" ")
    print("Choose between the following options")
    print("1. Passes Completed, 2. Passes Attempted, 3. Completion Percentage, 4. Passing Yards, 5. Passing Yards Per Attempt, 6. TD Passes")
    print("7. Ints, 8. Sacks, 9. Sacked Yards Lost, 10. Passer Rating, 11. Rushing Attempts, 12. Rusing Yards")
    print("13. Yards Per Carry, 14. Rushing TDs, 15. Fumbles, 16. Fumbles Lost")
    option = input("Enter the stat you want to see: ")
    
    if option == '1':
        stat = 'Passes Completed'
    elif option == '2':
        stat = 'Passes Attempted'
    elif option == '3':
        stat = 'Completion Percentage'
    elif option == '4':
        stat = 'Passing Yards'
    elif option == '5':
        stat = 'Passing Yards Per Attempt'
    elif option == '6':
        stat = 'TD Passes'
    elif option == '7':
        stat = 'Ints'
    elif option == '8':
        stat = 'Sacks'
    elif option == '9':
        stat = 'Sacked Yards Lost'
    elif option == '10':
        stat = 'Passer Rating'
    elif option == '11':
        stat = 'Rushing Attempts'
    elif option == '12':
        stat = 'Rushing Yards'
    elif option == '13':
        stat = 'Yards Per Carry'
    elif option == '14':
        stat = 'Rushing TDs'
    elif option == '15':
        stat = 'Fumbles'
    elif option == '16':
        stat = 'Fumbles Lost'
    else:
        print('Sorry the option you have selected is it not one of the options listed. Please run the program again')
        print('Please ignore the following graph')
  
    for line in data:
        if line['Name'] == fullName:
            stateAndYear = line['Year'],line[stat]
            lst.append(stateAndYear)
    for item in lst:
        if "--" in item:
            continue
        else:
            newLst.append(item)
    for i in newLst:
        list1.append(i[0])
        list2.append(i[1])
    
    print('Notice: If graph was empty, this is because the player you have typed could potentially currently not be or was not in the NFL')
    print('Or the player you have typed is not in the .csv files we have used')
    print('If graph was displayed, please ignore the notice above')
    print(' ')
    
    print(basicinfo(lastName,firstName))
    pyplot.plot(list1, list2) 
    pyplot.title('this stat over time')
    pyplot.xlabel('year')
    pyplot.ylabel('stat')
    pyplot.show() #plots the graph

if __name__ == '__main__':
    main()
