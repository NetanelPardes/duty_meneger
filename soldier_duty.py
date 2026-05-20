#main

def menu():
    """
    explanation: Displays the main menu.
    
    input: 
    output: Print general menu
    exceptions: 
    """
    pass
def handle_main_choice():
    """
    explanation: Activates the correct function according to the user's choice

    input: none
    output: none
    exceptions: If the user's selection is not from the list
    """
    pass

def main():
    """
    explanation: System activation

    input: nothing
    output: nothing
    exceptions: nothing
    """
    pass

if __name__ == "__main__":
    main()


#soldier

def soldier_menu():
    """
    explanation: Displays the menu of actions on soldiers.
    
    input: nothing
    output: Printing a Soldiers' Menu
    exceptions: 
    """
    pass

def handle_soldier_choice():
    """
    explanation: Activates the correct function according to the user's choice

    input: none
    output: none
    exceptions: If the user's selection is not from the list
    """
    pass

def create_soldier(soldier_id, soldier_name):
    """
    explanation: Creates a soldier

    input: Soldier number, soldier name
    output: Soldier
    exceptions: 
    """
    pass

def add_soldier(Soldier ,Soldier_list):
    """
    explanation: Adding a new soldier to the soldier list

    input: Soldier ,Soldier_list
    output: Successful or not
    exceptions: If the soldier already exists in the system
    """
    pass

def remove_soldier(id,soldier_list):
    """
    explanation: Removing a specific soldier from the soldier list
    
    input: Soldier ,Soldier_list
    output: Successful or not
    exceptions: If the soldier does not exist in the system
    """
    pass

def print_all_soldiers(sildier_list):
    """
    explanation: print the entire list of soldiers

    input: List of soldiers
    output: Activates the soldier printing function 
    exceptions: 
    """
    pass


def soldier_print(soldier_id):
    """
    explanation: Soldier printer

    input: soldier_id
    output: Soldier printer 
    exceptions: 
    """
    pass

def get_soldier_id():
    """
    explanation: Gets a soldier number from the user.

    input: none
    output: soldier_id
    exceptions: If the soldier number is incorrect
    """
    pass

def get_soldier_name():
    """
    explanation: Gets a soldier name from the user.

    input: none
    output: soldier_name
    exceptions: 
    """
    pass

#duty

def handle_duty_choice():
    """
    explanation: Activates the correct function according to the user's choice

    input: none
    output: none
    exceptions: If the user's selection is not from the list
    """
    pass

def get_duty():
    """
    explanation: Gets a duty name from the user.

    input: none
    output: duty_name
    exceptions: 
    """
    pass

def get_day():
    """
    explanation: Gets a duty day from the user.

    input: none
    output: duty_day
    exceptions: If the day is not a weekday
    """
    pass

def get_status():
    """
    explanation: Gets a duty status from the user.

    input: none
    output: duty_status
    exceptions: If the status is not in the options
    """
    pass

def duty_menu():
    """
    explanation: Displays the task actions menu.

    input: none
    output: none
    exceptions: 
    """
    pass

def add_duty_to_soldier(duty , soltior_id):
    """
    explanation: Adds a new mission for the soldier

    input: duty , soltior_id
    output: Done or not
    exceptions: If a soldier has this mission Or the soldier doesn't exist.
    """
    pass

def update_status_duty_to_soldier(status , soltior_id):
    """
    explanation: Changes the status of the soldier's mission.
    
    input: status , soltior_id
    output: Done or not
    exceptions: If the soldier does not have this mission Or the soldier doesn't exist.
    """
    pass

def view_duty_by_soldier(soltior_id):
    """
    explanation: Displays all missions for a particular soldier
    
    input: soltior_id
    output:  soltior duty
    exceptions: That the soldier doesn't exist
    """
    pass

#utils

def soldier_exists(soldier_id,soldier_list):
    """
    explanation: Checking whether the soldier exists

    input: soldier_id,soldier_list
    output: True or false
    exceptions:
    """
    pass

def day_Check(my_day):
    """
    explanation: Checks if a day is a weekday

    input: my_day
    output: True or false
    exceptions:
    """
    pass

def Unique_id(id,soldier_id):
    """
    explanation: Checks if another such id exists

    input: id,soldier_id
    output: True or false
    exceptions:
    """
    pass

def status_check(my_status):
    """
    explanation: Checks if the status is correct

    input: my_status
    output: True or false
    exceptions:
    """
    pass