import data
import utils

def add_duty_to_soldier(soldier_id: int, duty_name: str, day: str) -> None:
    """
    מוסיפה תורנות חדשה לחייל.
    
    סוג: לוגיקה עסקית (Business Logic)
    
    מקבלת:
        soldier_id (int): מספר אישי של החייל
        duty_name (str): שם התורנות
        day (str): יום בשבוע (sunday/monday/tuesday/wednesday/thursday)
    
    מחזירה:
        None - הפונקציה מוסיפה את התורנות או זורקת exception
    
    זורקת:
        KeyError: אם חייל עם id זה לא נמצא במערכת
        ValueError: אם תורנות עם שם זה כבר קיימת לחייל
        ValueError: אם day לא חוקי (friday/saturday או ערך לא תקין)
    
    למה הפונקציה קיימת:
    לוגיקה עסקית של הוספת תורנות.
    מבצעת בדיקות ומוסיפה תורנות לחייל.
    זורקת exceptions במקרה של שגיאה במקום להחזיר False.
    """
    soldier = utils.find_soldier_by_id(soldier_id)

    if soldier is None:
        raise KeyError("soldier was not found")
    
    if not utils.is_valid_name(duty_name):
        raise ValueError("duty name cannot be empty")

    if utils.soldier_has_duty(soldier, duty_name):
        raise ValueError("this duty already exists for this soldier")

    if not utils.is_valid_day(day):
        raise ValueError("day must be sunday, monday, tuesday, wednesday, or thursday")

    duty = {
        "name": duty_name.strip(),
        "day": day.strip().lower(),
        "status": "pending",
    }

    soldier["duties"].append(duty)


def update_duty_status(soldier_id: int, duty_name: str, new_status: str) -> None:
    """
    מעדכנת את הסטטוס של תורנות.
    
    סוג: לוגיקה עסקית (Business Logic)
    
    מקבלת:
        soldier_id (int): מספר אישי של החייל
        duty_name (str): שם התורנות
        new_status (str): סטטוס חדש (pending/completed/missed)
    
    מחזירה:
        None - הפונקציה מעדכנת את הסטטוס או זורקת exception
    
    זורקת:
        KeyError: אם חייל עם id זה לא נמצא במערכת
        KeyError: אם תורנות עם שם זה לא נמצאה לחייל
        ValueError: אם new_status לא חוקי (לא pending/completed/missed)
    
    למה הפונקציה קיימת:
    לוגיקה עסקית של עדכון סטטוס.
    מבצעת בדיקות ומעדכנת את הסטטוס.
    זורקת exceptions במקרה של שגיאה במקום להחזיר False.
    """
    soldier = utils.find_soldier_by_id(soldier_id)

    if soldier is None:
        raise KeyError("soldier was not found")

    duty = utils.find_duty_by_name(soldier["duties"], duty_name)

    if duty is None:
        raise KeyError("duty was not found for this soldier")

    if not utils.is_valid_status(new_status):
        raise ValueError("status must be pending, completed, or missed")

    duty["status"] = new_status.strip().lower()


def get_soldier_duties(soldier_id: int) -> list:
    """
    מחזירה את רשימת התורנויות של חייל.
    
    סוג: גישה לנתונים (Data Access)
    
    מקבלת:
        soldier_id (int): מספר אישי של החייל
    
    מחזירה:
        list: רשימת תורנויות (מילונים)
              רשימה ריקה אם אין תורנויות
    
    זורקת:
        KeyError: אם חייל עם id זה לא נמצא במערכת
    
    למה הפונקציה קיימת:
    גישה מבוקרת לתורנויות של חייל.
    מפרידה בין הנתונים לבין הגישה אליהם.
    זורקת exception אם החייל לא קיים (במקום להחזיר רשימה ריקה).
    """
    soldier = utils.find_soldier_by_id(soldier_id)

    if soldier is None:
        raise KeyError("soldier was not found")

    return soldier["duties"].copy()