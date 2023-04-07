import justpy as jp

from home import Home
from about import About
from dictionary import Dictionary

jp.Route(Home.path, Home.serve)
jp.Route(About.path, About.serve)
jp.Route(Dictionary.path, Dictionary.serve)  # to refer we can access class
jp.justpy(port=8002)