import os
import sys

here = os.path.dirname(__file__)
root = os.path.abspath(os.path.join(here, "..", "..", ".."))
sys.path.insert(0, root)

from tools.wpt import markdown

def test_format_comment_title():
    assert '# Browser #' == markdown.format_comment_title("browser")
    assert '# Browser (channel) #' == markdown.format_comment_title("browser:channel")

def test_markdown_adjust():
    assert u'\\t' == markdown.markdown_adjust('\t')
    assert u'\\r' == markdown.markdown_adjust('\r')
    assert u'\\n' == markdown.markdown_adjust('\n')
    assert u'' == markdown.markdown_adjust('`')
    assert u'\\|' == markdown.markdown_adjust('|')
    assert u'\\t\\r\\n\\|' == markdown.markdown_adjust('\t\r\n`|')

result = ''
def log(text):
    global result
    result += text

def test_table():
    global result
    headings = ['h1','h2']
    data = [['0', '1']]
    markdown.table(headings, data, log)
    assert ("| h1 | h2 |"
            "|----|----|"
            "| 0  | 1  |") == result

    result = ''
    data.append(['aaa', 'bb'])
    markdown.table(headings, data, log)
    assert ("|  h1 | h2 |"
            "|-----|----|"
            "| 0   | 1  |"
            "| aaa | bb |") == result
