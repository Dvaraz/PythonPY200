Реализовать класс `LinkedListWithDriver` от класса `LinkedList`.

Дочерний класс должен уметь работать с реализованными ранее драйверами.
1. Реализовать метод `read`, который с помощью встроенного драйвера будет получать 
   последовательность элементов и помещать их в самого себя. 
   При вызове метода связанный список должен полностью перезаписываться новыми элементами.
2. Реализовать метод `write`, который будет передавать последовательность элементов для записи драйвером.
3. Инициализировать экземпляр класса `LinkedListWithDriver`.
4. Инициализировать драйвер с именем файла по умолчанию с помощью "фабричного метода" `SimpleFileFactoryMethod`
5. Добавить списку драйвер и записать его содержимое в файл.

6. Инициализировать новый драйвер с именем файла "input.txt" с помощью "фабричного метода" `SimpleFileFactoryMethod`
7. Выполнить замену драйвера в списке "на горячую".
8. Считать новое содержимое.
