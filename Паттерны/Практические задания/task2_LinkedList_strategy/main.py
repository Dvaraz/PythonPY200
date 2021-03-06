from typing import Iterable

from linked_list import LinkedList
from drivers import IStructureDriver
from factory_method import SimpleFileFactoryMethod


class LinkedListWithDriver(LinkedList):  # TODO наследовать класс LinkedList
    def __init__(self, data: Iterable = None, driver: IStructureDriver = None):
        super().__init__(data)
        self.driver = driver

    def read(self):
        """ С помощью драйвера считать данные и поместить их в LinkedList. """
        self.clear()
        data = self.driver.read()

        for item in data:
            self.append(item)

    def write(self):
        """ С помощью драйвера записать данные из LinkedList. """
        self.driver.write(self)


if __name__ == '__main__':
    ll = LinkedListWithDriver([1, 2, 3, 4, 5])
    driver_1 = SimpleFileFactoryMethod.get_driver()

    ll.driver = driver_1

    ll.write()

    driver_2 = SimpleFileFactoryMethod.get_driver()
    ll.driver = driver_2
    ll.read()
    print(ll)
