from model import Person
import view


def showAll():
    # gets list of all Person objects
    people_in_db = Person.getAll()
    # calls view
    return view.showAllView(people_in_db)


def start():
    view.startView()
    i = input()
    if i == 'y':
        return showAll()
    else:
        return view.endView()


if __name__ == "__main__":
    # running controller function
    start()
