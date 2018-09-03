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
    'em': 'i',
    'sub': 'sub',
    'sup': 'super',
    # tables
    'table': 'blockTable',
    'tr': 'tr',
    'td': 'td',
    'th': 'td',
    # lists
    'ul': 'ul',
    'ol': 'ul',
    'li': 'li',
    # others
    'br': 'br',
    'pre': 'pre',
}

empty_tags = {
    'br',
}

rml_attributes = {
    'p': 'style="p"',
    'ul': 'style="ul"',
    'ol': 'style="ol"',
    'li': 'style="li"',
}


class HTML2RMLConverter(HTMLParser):
    def __init__(self, *args, **kwargs):
        self.rml_tags = kwargs.pop('rml_tags', rml_tags)
        self.empty_tags = kwargs.pop('empty_tags', empty_tags)
        self.rml_attributes = kwargs.pop('rml_attributes', rml_attributes)
        if _python3:
            super(HTML2RMLConverter, self).__init__(*args, **kwargs)
        self.reset()
        self.tokens = []

    def handle_data(self, d):
        self.tokens.append(d)

    def handle_entityref(self, name):
        self.tokens.append('&%s;' % name)

    def handle_starttag(self, html_tag, html_attributes):
        rml_tag = self.rml_tags.get(html_tag)
        rml_attrs = self.rml_attributes.get(html_tag)
        if rml_tag:
            if rml_tag in self.empty_tags:
                self.tokens.append(
                    '<%s %s/>' % (rml_tag, rml_attrs)
                    if rml_attrs
                    else '<%s/>' % rml_tag
                )
            else:
                self.tokens.append(
                    '<%s %s>' % (rml_tag, rml_attrs)
                    if rml_attrs
                    else '<%s>' % rml_tag
                )

    def handle_endtag(self, html_tag):
        rml_tag = self.rml_tags.get(html_tag)
        if rml_tag and rml_tag not in self.empty_tags:
            self.tokens.append('</%s>' % rml_tag)

    def get_data(self):
        return ''.join(self.tokens)


def html2rml(html, **kwargs):
    converter = HTML2RMLConverter(**kwargs)
    converter.feed(html)
    return converter.get_data()
