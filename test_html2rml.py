from html2rml import html2rml


def test_html2rml():
    html = '''
        <p>
            This is text of simple paragraph.<br/> Some words are <b>bold</b>,
            some <strong>strong</strong>, some <i>italics</i>
        </p>
        <table>
            <tr><th>Table header</th></tr>
            <tr><td>Table value</td></tr>
        </table>
        <ul>
            <li>item 1</li>
            <li>item 2</li>
        </ul>
        <ol>
            <li>item 1</li>
            <li>item 2</li>
        </ol>
    '''
    rml = '''
        <para style="p">
            This is text of simple paragraph.<br/> Some words are <b>bold</b>,
            some <b>strong</b>, some <i>italics</i>
        </para>
        <blockTable>
            <tr><td>Table header</td></tr>
            <tr><td>Table value</td></tr>
        </blockTable>
        <ul style="ul">
            <li style="li">item 1</li>
            <li style="li">item 2</li>
        </ul>
        <ul style="ol">
            <li style="li">item 1</li>
            <li style="li">item 2</li>
        </ul>
    '''
    assert html2rml(html) == rml
