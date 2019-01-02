from string import Template

def start_response(resp="text/html"):
    return ('Content-type: '+resp+'\n\n')

def include_header(the_title):
    with open('template/header.html') as headf:
        head_text = headf.read()
    header = Template(head_text)
    return (header.substitute(title=the_title))

def include_footer(the_links):
    with open('templates/header.html') as 