html2rml
========

Simple HTML to RML converter. It may be used to take output of TinyMCE
or any other WYSIWYG html editor and use it in your RML template.


Installation with pip
---------------------

.. code:: shell

    pip install html2rml


Usage
-----

This HTML code ...

.. code:: python

    from html2rml import html2rml

    html = """<p>This is text of simple paragraph.<br/> <b>This is bold.</b></p>"""
    print(html2rml(html))

... will be converted to the following RML code.

.. code:: shell

    <para style="p">This is text of simple paragraph.<br/> <b>This is bold.</b></para>
