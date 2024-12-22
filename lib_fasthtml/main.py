from fasthtml.common import *

app, rt = fast_app()
# routing
page = Html(Head(Title('Belajar fasthtml'), Style(src="style.css")),Body("kosong",A('A link', href="#"), Img(src="https://upload.wikimedia.org/wikipedia/commons/5/51/Nahdlatul_Ulama_Logo.svg"),cls="my-class"))
@rt('/')
def get(): 
    return page

# home
@rt('/home')
def get():
    return Div(Li('p')), Style("style.css")

# html constructor
print(to_xml(page))

# running server
serve()