
# Display the Menu
def display_menu():
    print(" XYZ COMPANY ".center(100))
    print(" Main Menu ".center(100))
    print("\t\t 1. Add a new project to existing projects")
    print("\t\t 2. Remove a completed project from existing projects")
    print("\t\t 3. Add new workers to available workers group")
    print("\t\t 4. Update details on ongoing projects")
    print("\t\t 5. Project Statistics")
    print("\t\t 6. Exit")

# save data in a file
def save_data(data_list:list,available_workers:int):
    with open("state.txt", "w") as file:
        if data_list == []:
            file.write(str(available_workers))
        else:
            for project in data_list:
                file.write(",".join(project))
                file.write("\n")
            if available_workers == 0:
                available_workers = tot_workers(data_list)
            file.write(str(available_workers))

# read data in a file
def read_data(data_list:list=[],available_workers:int=0):
    try:
        with open("state.txt", "r") as file:
            lines = file.readlines()
            if len(lines) > 0:
                available_workers = int(lines.pop())
                for line in lines:
                    data_l = line.rstrip().split(',')
                    data_list.append(data_l)
                return data_list,available_workers
            else:
                return data_list ,available_workers

    except FileNotFoundError:
        return data_list,available_workers

# Delete file contains
def delete_data():
    with open("state.txt", "w") as file:
        pass

# Add a new project to existing projects
def add_new_project(data_list:list) ->list:
        print(" XYZ COMPANY ".center(100))
        print(" Add a new project ".center(100))
        project_code = input("Project code      - ")
        if project_code == "0":
            return data_list
        clients_name = input("Clients name      - ")
        start_date = input("Start date        - ")
        enter_expected_date = input("Expected end date - ")
        num_of_workers = input("Number of workers - ")
        while True:
            project_status = input("Project status    - ")
            if project_status.lower() == "ongoing" or project_status.lower() == "on hold" or project_status.lower() == "completed":
                break
            else:
                print("Invalid input.Try again.")
                continue

        project_list = [project_code,clients_name,start_date,enter_expected_date,num_of_workers,project_status]
        user_input = input("Do you want to save the project (Yes/No)? ")
        while True:
            if user_input.lower() == "yes":
                data_list.append(project_list)
                break
            elif user_input.lower() == "no":
                break
            else:
                print("Invalid Input.Try again.")
                continue

        return data_list
        
#Calculate total workers
def tot_workers(data_list:list) ->int:
    total_workers = 0
    for project in data_list:
        total_workers += int(project[4])
    return total_workers

# show Project Statistics
def project_statistics(data_list:list,available_workers:int) ->list:
        print(" XYZ COMPANY ".center(100))
        print(" Project Statistics ".center(100))  
        print("Number of ongoing projects               - ", num_of_ongoing_projects(data_list))
        print("Number of completed projects             - ",num_of_com_projects(data_list))
        print("Number of on hold projects               - ",num_of_on_hold_projects(data_list))
        print("Number of available workers to assign    - ", available_workers)
        while True:
            user_input = input("Do you want to add the project (Yes/No)? ")
            if user_input.lower() == "yes":
                return add_new_project(data_list)
            elif user_input.lower() == "no":
                return data_list
            else:
                print("Invalid input.Try again.")
                continue


#Remove a completed project from existing projects
def remove_com_pro(data_list:list) ->list:
    if data_list == []:
        print("Data list is empty.")
        return data_list
    else:
        while True:
            project_code = input("Project Code - ")
            for project in data_list:
                if project_code == project[0]:
                    while True:
                        user_input = input("Do you want to remove the project (Yes/No)? ")
                        if user_input.lower() == "yes":
                            data_list.remove(project)
                            return data_list
                        elif user_input.lower() == "no":
                            return data_list
                        else:
                            print("Invalid input.Try again.")
                            continue
                
            print("Project code is invalid.Re enter the project code.")
            continue

    
#Update details on ongoing project
def update_project(data_list:list) ->list:
    if data_list == []:
        print("Data list is empty.")
        return data_list
    
    else:
        while True:
            project_code = input("Project Code - ")
            if project_code == "0":
                return data_list
            for project in data_list:
                if project_code == project[0]:
                    clients_name = input("Clients name      - ")
                    start_date = input("Start date        - ")
                    enter_expected_date = input("Expected end date - ")
                    num_of_workers = input("Number of workers - ")
                    while True:
                        project_status = input("Project status    - ")
                        if project_status.lower() == "ongoing" or project_status.lower() == "on hold" or project_status.lower() == "completed":
                            break
                        else:
                            print("Invalid input.Try again.")
                            continue
                    while True:
                        user_input = input("Do you want to update the project details (Yes/No)? ")  
                        if user_input.lower() == "yes":
                            project[1] = clients_name
                            project[2] = start_date
                            project[3] = enter_expected_date
                            project[4] = num_of_workers
                            project[5] = project_status
                            return data_list
                        elif user_input.lower() == "no":
                            return data_list
                        else:
                            print("Invalid input.Try again.")
                            continue
                
            print("Project code is invalid.Re enter the project code.")
            continue

                        
#Add new workers to available workers group
def add_new_workers(a_workers:int) -> int:
    while True:
        try:
            num_workers_add = int(input("number of workers to add - "))
            break
        except ValueError:
            print("Invalid input.Enter the valid input(Integer Value).")
            continue

    while True:
        user_input = input("Do you want to add  (Yes/No)? ")
        if user_input.lower() == "yes":
            a_workers += num_workers_add
            return a_workers
        elif user_input.lower() == "no":
            return a_workers
        else:
            print("Invalid input.Try again.")
            continue

# calculate additionaly added workers
def cal_add_add_workers(data_list:list,available_workers:int) ->int:
    if data_list == []:
        return available_workers
    else:
        return available_workers - tot_workers(data_list) 

# Calculate available workers
def cal_avail_workers(data_list:list,additionaly_added_workers:int) ->int:
    if data_list == []:
        return additionaly_added_workers
    else:
        return additionaly_added_workers + tot_workers(data_list)
    
#calculate Number of ongoing projects 
def num_of_ongoing_projects(data_list:list) ->int:
    num = 0
    if data_list == []:
        return 0
    else:
        for project in data_list:
            if project[5] == "ongoing":
                num += 1
        return num

#calculate Number of completed projects 
def num_of_com_projects(data_list:list) ->int:
    num = 0
    if data_list == []:
        return 0
    else:
        for project in data_list:
            if project[5] == "completed":
                num += 1
        return num

#calculate Number of on hold projects 
def num_of_on_hold_projects(data_list:list) ->int:
    num = 0
    if data_list == []:
        return 0
    else:
        for project in data_list:
            if project[5] == "on hold":
                num += 1
        return num

#collect store data for using this program
data,available_workers = read_data()
additionaly_added_workers = cal_add_add_workers(data,available_workers)

#Loop the program 
while True:
    display_menu()
    try:
        user_choice = int(input("Your Choice: ".rjust(90)))
    except ValueError:
        print("Invalid input.Try again.")
        continue
    delete_data()
    if user_choice == 1:
        data = add_new_project(data)
    elif user_choice == 2:
        data = remove_com_pro(data)
    elif user_choice == 3:
        additionaly_added_workers = add_new_workers(additionaly_added_workers)
    elif  user_choice == 4:
        data = update_project(data)
    elif user_choice == 5:
        available_workers = cal_avail_workers(data,additionaly_added_workers)
        data = project_statistics(data,available_workers)
    elif user_choice == 6:
        available_workers = cal_avail_workers(data,additionaly_added_workers)
        save_data(data,available_workers)
        break
    else:
        print("Invalid input.Try again.")
        continue
