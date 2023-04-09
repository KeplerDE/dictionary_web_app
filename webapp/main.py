import justpy as jp

from home import Home
from about import About
from dictionary import Dictionary

imports = list(globals().values())     # globals() это встроенная функция, которая возвращает словарь, представляющий текущую глобальную таблицу символов.
                                       # list of availiable names through iterating
for obj in imports.items():
    if hasattr(obj, 'path'):
        jp.Route(obj.path, obj.serve)


# jp.Route(Home.path, Home.serve)
# jp.Route(About.path, About.serve)
# jp.Route(Dictionary.path, Dictionary.serve)  # to refer we can access class

jp.justpy(port=8001)
