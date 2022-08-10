### Описание тестовой модели

*Тестовая модель* — это логическая структура, описывающая функциональность системы и/или поведения пользователя, по которой генерируются тест-кейсы ([link](https://www.a1qa.ru/blog/test-policy-upravlenie-testovoy-modelyu/)).
В нашем случае есть требования ("белый ящик"), поэтому будет отталкиваться от них в построении наших тест-кейсов.
Так же нам пригодятся следующие техники тестирования:
* классы эквивалентности - для проверки полей ввода данных
* pairwise тестирование. Для этих целей будем использовать [онлайн-инструмент](https://pairwise.teremokgames.com/)
* граничные условия у нас заданы в требованиях

Будем тестировать:
* элементы выбора и ввода
* отображение ошибок
* полноту отображения информации
* правильность расчета сумм и процентов

Тесты автоматизированы с помощью **pytest+selenium**

Еще можно потестировать:
* верстку в разных браузерах и на разных расширениях экрана
* работу под нагрузкой
* работу на мобильных устройствах

* можно еще было написать совсем очевидные тесты для проверки наличия всех элементов и добавить на него маркер "использовать в smoke-тестах"

### Решение тестового задания
Писать тест-кейсы глядя в требования скучно, поэтому начнем с шага 2 (опционального)
1. Ставим **_python 3.9.7_** или новее
2. Распаковываем в нужное место архив с кодом 
3. Создаем и активируем окружение
4. Ставим **_pip_**  и следом зависимости из файла **_requirements.txt_**
5. Требования, по которым я писал приложение, в файле modify_req.md. Там же описаны причины, по которым я изменил требования, не дождавшись реакции.
6. Запуск приложения стандартный - python manage.py runserver
7. Тесты запускайте любым удобным для вас способом. Драйвер для Chrome подтянется автоматически.
**PROFIT**
