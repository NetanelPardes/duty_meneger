import duty_manager
import soldier_manager


def show_menu() -> None:
    """
    מציגה את התפריט הראשי למשתמש.
    
    מקבלת: כלום
    מחזירה: כלום (מדפיסה לקונסול)
    
    למה הפונקציה קיימת:
    הפרדה בין הצגת התפריט לבין הלוגיקה העסקית.
    אם נרצה לשנות את התצוגה, נשנה רק כאן.
    """
    print("\n=== Soldier Duty Management System ===")
    print("1. Add soldier")
    print("2. Remove soldier")
    print("3. View all soldiers")
    print("4. Add duty to soldier")
    print("5. Update duty status")
    print("6. View soldier duties")
    print("0. Exit")


def get_user_choice() -> str:
    """
    מקבלת בחירה מהמשתמש.
    
    מקבלת: כלום
    מחזירה: מחרוזת המייצגת את בחירת המשתמש
    
    למה הפונקציה קיימת:
    הפרדת קבלת קלט מהמשתמש מהלוגיקה של עיבוד הבחירה.
    מאפשר להחליף את שיטת הקלט בעתיד (למשל, GUI).
    """
    return input("Choose an option: ").strip()


def handle_add_soldier() -> None:
    """
    מטפלת בתהליך הוספת חייל חדש.
    מקבלת קלט מהמשתמש וקוראת לפונקציות המתאימות.
    
    מקבלת: כלום
    מחזירה: כלום
    
    למה הפונקציה קיימת:
    מפרידה בין הקלט/פלט לבין הלוגיקה העסקית.
    main.py אחראי על אינטראקציה עם המשתמש,
    soldier_manager.py אחראי על הלוגיקה.
    """
    try:
        soldier_id = int(input("Enter soldier id: "))
        name = input("Enter soldier name: ")

        soldier_manager.add_soldier(soldier_id, name)

        print("Soldier added successfully.")

    except ValueError as error:
        print(f"Error: {error}")


def handle_remove_soldier() -> None:
    """
    מטפלת בתהליך הסרת חייל.
    מקבלת קלט מהמשתמש וקוראת לפונקציות המתאימות.
    
    מקבלת: כלום
    מחזירה: כלום
    
    למה הפונקציה קיימת:
    הפרדה בין UI לבין לוגיקה עסקית.
    """
    try:
        soldier_id = int(input("Enter soldier id to remove: "))

        soldier_manager.remove_soldier(soldier_id)

        print("Soldier removed successfully.")

    except ValueError:
        print("Error: Soldier id must be a number.")

    except KeyError as error:
        print(f"Error: {error}")


def handle_view_soldiers() -> None:
    """
    מטפלת בתהליך הצגת כל החיילים.
    קוראת לפונקציה המתאימה ומציגה את התוצאה.
    
    מקבלת: כלום
    מחזירה: כלום
    
    למה הפונקציה קיימת:
    הפרדה בין קבלת הנתונים לבין הצגתם.
    """
    soldiers = soldier_manager.get_all_soldiers()

    if not soldiers:
        print("There are no soldiers in the system.")
        return

    for soldier in soldiers:
        print(f"soldier: {soldier['id']} \nsoldier name: {soldier['name']} \nis duties: {soldier['duties']}\n")


def handle_add_duty() -> None:
    """
    מטפלת בתהליך הוספת תורנות לחייל.
    מקבלת קלט מהמשתמש וקוראת לפונקציות המתאימות.
    
    מקבלת: כלום
    מחזירה: כלום
    
    למה הפונקציה קיימת:
    הפרדה בין UI לבין לוגיקה עסקית.
    """
    try:
        soldier_id = int(input("Enter soldier ID: ").strip())
        duty_name = input("Enter duty name: ").strip()
        day = input("Enter day (sunday-thursday): ").strip().lower()

        duty_manager.add_duty_to_soldier(soldier_id, duty_name, day)
        print("Duty added successfully.")

    except ValueError as error:
        print(f"Error: {error}")
    except KeyError as error:
        print(f"Error: {error}")


def handle_update_duty_status() -> None:
    """
    מטפלת בתהליך עדכון סטטוס תורנות.
    מקבלת קלט מהמשתמש וקוראת לפונקציות המתאימות.
    
    מקבלת: כלום
    מחזירה: כלום
    
    למה הפונקציה קיימת:
    הפרדה בין UI לבין לוגיקה עסקית.
    """
    try:
        soldier_id = int(input("Enter soldier ID: ").strip())
        duty_name = input("Enter duty name: ").strip()
        new_status = input("Enter new status (pending/completed/missed): ").strip().lower()

        duty_manager.pdate_duty_status(soldier_id, duty_name, new_status)
        print("Duty status updated successfully.")

    except ValueError as error:
        print(f"Error: {error}")
    except KeyError as error:
        print(f"Error: {error}")


def handle_view_soldier_duties() -> None:
    """
    מטפלת בתהליך הצגת תורנויות של חייל.
    מקבלת קלט מהמשתמש וקוראת לפונקציות המתאימות.
    
    מקבלת: כלום
    מחזירה: כלום
    
    למה הפונקציה קיימת:
    הפרדה בין UI לבין לוגיקה עסקית.
    """
    try:
        soldier_id = int(input("Enter soldier ID: ").strip())
        duties = duty_manager.get_soldier_duties(soldier_id)

        if not duties:
            print("This soldier has no duties.")
            return

        for duty in duties:
            print(f"\nsoldier id: {soldier_id} \nduty name: {duty['name']} \nDay: {duty['day']} \nStatus: {duty['status']}\n")

    except ValueError:
        print("Error: soldier ID must be a number.")
    except KeyError as error:
        print(f"Error: {error}")


def main() -> None:
    """
    הפונקציה הראשית של התוכנית.
    מריצה לולאה ראשית שמציגה תפריט, מקבלת בחירה ומפעילה פעולה.
    
    מקבלת: כלום
    מחזירה: כלום
    
    למה הפונקציה קיימת:
    נקודת הכניסה לתוכנית. מנהלת את הזרימה הראשית.
    """
    choice = ''

    while choice != '0':
        show_menu()

        choice = get_user_choice()

        if choice == '0':
            print("goodbye")

        elif choice == '1':
            handle_add_soldier()

        elif choice == '2':
            handle_remove_soldier()

        elif choice == '3':
            handle_view_soldiers()

        elif choice == '4':
            handle_add_duty()

        elif choice == '5':
            handle_update_duty_status()

        elif choice == '6':
            handle_view_soldier_duties()
        
        else:
            print("Please try again")

if __name__ == "__main__":
    main()