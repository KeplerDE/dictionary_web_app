import justpy as jp
import page
import inspect
from home import Home
from about import About
from dictionary import Dictionary
"""
    Извлекает все глобальные переменные из текущего модуля с помощью globals().values() и преобразует их в список с именем imports.
    Затем код перебирает каждый объект в importsсписке и проверяет, 
    является ли он классом, использующим inspect.isclass()функцию.
    Если объект является классом, код проверяет, является ли он подклассом page.Page(где pageпредположительно модуль или класс, 
    определенный в другом месте кода). Если объект является подклассом page.Page, код регистрирует его метод path и serve
     в качестве обработчика маршрута с помощью jp.Route()функции.
    Функция jp.Route()принимает два параметра: строку пути и функцию для обработки запроса на этот путь.
     В этом случае obj.pathи obj.serveиспользуются как параметр пути и параметр функции соответственно.
    В целом, этот код, скорее всего, используется для динамической регистрации обработчиков маршрутов на основе классов,
     определенных в текущем модуле или области видимости. Эта jp.Route() функция позволяет создавать маршруты,
      соответствующие определенным страницам или функциям в веб-приложении.
"""
imports = list(globals().values())

for obj in imports:
    if inspect.isclass(obj):
        if issubclass(obj, page.Page) and obj is not page.Page:
            jp.Route(obj.path, obj.serve)
# imports = list(globals().values())     # globals() это встроенная функция, которая возвращает словарь, представляющий текущую глобальную таблицу символов.
#                                        # list of availiable names through iterating
# for obj in imports.items():
#     if hasattr(obj, 'path'):     # condition and filter
#         jp.Route(obj.path, obj.serve)


# jp.Route(Home.path, Home.serve)
# jp.Route(About.path, About.serve)
# jp.Route(Dictionary.path, Dictionary.serve)  # to refer we can access class



jp.justpy(port=8001)


