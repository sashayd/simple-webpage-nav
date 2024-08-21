import json

with open('./spec.json') as f:
    spec = json.load(f)

title = spec['title']
pages = spec['pages']


def link(i, j):
    result = ''
    if i == j:
        result += '<strong>' + pages[j][1] + '</strong>'
    else:
        result += f'<a href="{pages[j][0]}">'
        result += pages[j][1]
        result += '</a>'
    return result


def header(i):
    result = ''
    result += '<!--start_header-->\n'
    result += f'<h1>{title}</h1>\n'
    result += '<hr />\n'
    result += '<p> '
    result += ' | '.join([link(i, j) for j in range(len(pages))])
    result += '</p>\n'
    result += '<hr />\n'
    result += '<p>&nbsp;</p>\n'
    result += '<!--end_header-->\n'
    return result


for i in range(len(pages)):
    with open('./' + pages[i][0], 'rt') as f:
        contents = f.read()
    if contents.startswith('<!--start_header-->'):
        contents = contents.split('<!--end_header-->\n', 1)[-1]
    contents = header(i) + contents
    with open('./' + pages[i][0], 'wt') as f:
        f.write(contents)
