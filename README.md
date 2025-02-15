# Телефонная книга

## Описание
Телефонная книги написана на языке python с использованием паттерна MVC. 

![Меню телефонной книги](tel_book_mvc.png)

Программа умеет:
- Открывать файл данных
- Сохранять контакты
- Просматривать
- Изменять контакт
- Удалять контакт

Выводит контакты в табличном виде, лучше просматривать в полноэкранном режиме. Код таблицы нашел в интернете и переписал под себя.

![Сама таблица](table_mvc.png)

## Запуск
### ОС windows
Перейти в директорию с файлами программы и ввести команду(cd куда перейти)
~~~
python3.exe main.py
~~~

### ОС Linux
Переходим в каталог программы (команда cd) и вводим команду:
~~~
python3 main.py
~~~

### Запуск тестов
Для запуска теста нужно создать виртуальное окружение.
Для создания виртуального окружения, перейдите в директорию своего проекта и выполните (в windows - python3.exe):
~~~
python3 -m venv venv
~~~
-m — флаг для запуска venv как исполняемого модуля.
venv — название виртуального окружения (где будут храниться ваши библиотеки).

Чтобы начать пользоваться виртуальным окружением, необходимо его активировать:
~~~
venv\Scripts\activate.bat - для Windows;
source venv/bin/activate - для Linux и MacOS.
~~~
Установить библиотеку pytest.
~~~
pip install -U pytest
~~~

Для обычного запуска введидет pytest в папке проекта, он найдет тесты и выполнит их. Для подробного вывода дополните флагом -v.

 
