import re

def get_links_hastags(text):
    return re.sub(r'#(\w+)','<a  href=www.facebook.com/\\1>#\\1</a>',text)

links = get_links_hastags("Good blessed George #blacklivesmatter")


print(links)
