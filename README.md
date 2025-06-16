# Интернет магазин

Проект создает ядро для интернет-магазина.

## Технологии
[Python] (https://www.python.org/)  
![Poetry](https://img.shields.io/badge/Poetry-%233B82F6.svg?style=for-the-badge&logo=poetry&logoColor=0B3D8D)

## Использование
Открыть проект в PyCharm.  
**task.py** содержит 2 класса:

`Product`  
Класс Product обладает следующими свойствами:  
  название (name),  
  описание (description),  
  цена (price),  
  количество в наличии (quantity)  

`Category`
Класс Category обладает следующими свойствами:  
  название (name),  
  описание (description),  
  список товаров категории (products).  

**utils.py** содержит 2 функции:

`read_json`
Функция читает информацию из JSON файла.

`load_json_data`
Функция читает информацию из JSON файла.
На вход получает путь к файлу с данными, возвращает
словарь с данными из JSON файла.

Папка `tests` содержит файлы для тестирования модулей:  
**test_task.py**

### Требования
Для установки и запуска проекта, необходимы:
[Python](https://www.python.org/)
[PyCharm](https://www.jetbrains.com/pycharm/)

## Команда проекта
[Roman Z](roman-z@inbox.ru)