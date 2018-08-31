try:
    from html.parser import HTMLParser
    _python3 = True
except ImportError:
    # handle Python2
    from HTMLParser import HTMLParser
    _python3 = False


rml_tags = {
    # headings
    'h1': 'h1',
    'h2': 'h2',
    'h3': 'h3',
    # paragraph
    'p': 'para',
    # basic font styling
    'b': 'b',
    'strong': 'b',
    'i': 'i',
    'sub': 'sub',
    'sup': 'super',
    # tables
    'table': 'blockTable',
    'tr': 'tr',
    'td': 'td',
    'th': 'td',
    # lists
    'ul': 'ul',
    'ol': 'ol',
    'li': 'li',
    # others
    'br': 'br',
    'pre': 'pre',
}

empty_tags = {
    'br',
}


class HTML2RMLConverter(HTMLParser):
    def __init__(self, *args, **kwargs):
        if _python3:
            super(HTML2RMLConverter, self).__init__(*args, **kwargs)
        self.reset()
        self.tokens = []
    
    def handle_data(self, d):
        self.tokens.append(d)

    def handle_entityref(self, name):
        self.tokens.append('&%s;' % name)

    def handle_starttag(self, html_tag, html_attributes):
        rml_tag = rml_tags.get(html_tag)
        if rml_tag:
            if rml_tag in empty_tags:
                self.tokens.append('<%s/>' % rml_tag)
            else:
                self.tokens.append('<%s>' % rml_tag)

    def handle_endtag(self, html_tag):
        rml_tag = rml_tags.get(html_tag)
        if rml_tag and rml_tag not in empty_tags:
            self.tokens.append('</%s>' % rml_tag)

    def get_data(self):
        return ''.join(self.tokens)


def html2rml(html):
    converter = HTML2RMLConverter()
    converter.feed(html)
    return converter.get_data()
