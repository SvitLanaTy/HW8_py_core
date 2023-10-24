from datetime import date, datetime, timedelta


def get_birthdays_per_week(users):
    # Реалізуйте тут домашнє завдання

    birthdays_per_week = {}
    users_to_greet = []

    # Перевіряємо чи не є порожнім списком користувачів.
    if not users:
        return {}

    # Визначаємо поточний день тижня та інтервал для контролю днів народження.
    current_date = date.today()
    current_weekday = current_date.weekday()
    current_year = current_date.year

    if current_weekday == 0:
        first_day_of_week = current_date - timedelta(days=2)
        last_day_of_week = current_date + timedelta(days=4)
    else:
        first_day_of_week = current_date
        last_day_of_week = current_date + timedelta(days=6)

    # Перевіряємо дні народження користувачів на входження у визначений інтервал
    for user in users:
        user["birthday"] = user["birthday"].replace(year=current_year)
        if user["birthday"] < current_date:
            user["birthday"] = user["birthday"].replace(year=current_year + 1)

        if first_day_of_week <= user["birthday"] <= last_day_of_week:
            users_to_greet.append(user)
    # Створюємо словник користувачів, яких потрібно привітати по днях на наступному тижні
    if users_to_greet != []:
        for user in users_to_greet:
            if user["birthday"].weekday() in (0, 5, 6):
                if 'Monday' not in birthdays_per_week:
                    birthdays_per_week['Monday'] = [user["name"].split()[0]]
                else:
                    birthdays_per_week['Monday'].append(
                        user["name"].split()[0])
            elif user["birthday"].weekday() == 1:
                if 'Tuesday' not in birthdays_per_week:
                    birthdays_per_week['Tuesday'] = [user["name"].split()[0]]
                else:
                    birthdays_per_week['Tuesday'].append(
                        user["name"].split()[0])
            elif user["birthday"].weekday() == 2:
                if 'Wednesday' not in birthdays_per_week:
                    birthdays_per_week['Wednesday'] = [user["name"].split()[0]]
                else:
                    birthdays_per_week['Wednesday'].append(
                        user["name"].split()[0])
            elif user["birthday"].weekday() == 3:
                if 'Thursday' not in birthdays_per_week:
                    birthdays_per_week['Thursday'] = [user["name"].split()[0]]
                else:
                    birthdays_per_week['Thursday'].append(
                        user["name"].split()[0])
            elif user["birthday"].weekday() == 4:
                if 'Friday' not in birthdays_per_week:
                    birthdays_per_week['Friday'] = [user["name"].split()[0]]
                else:
                    birthdays_per_week['Friday'].append(
                        user["name"].split()[0])

    return birthdays_per_week


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
