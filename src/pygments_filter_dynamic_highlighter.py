from pygments.token import String, Comment, Keyword, Name, Error, Whitespace, string_to_tokentype
from pygments.filter import Filter
from os import environ
import json
import re

class DynamicHighlighterFilter(Filter):

    """
    # Highlight based on environment variables
    """
    # $PYGMENTS_HIGHLIGHTER_KEY ==> Literal.String.Highlight.Key 
    # $PYGMENTS_HIGHLIGHTER_VALUE ==> Literal.String.Highlight.Value
    # Troubleshoot: Output token mapping: pygmentize -f tokens -P style=dynamic-highlighter
    
    def __init__(self, **options):
        Filter.__init__(self, **options)

    def filter(self, lexer, stream):

        env_key_list = json.loads(environ['PYGMENTS_HIGHLIGHTER_KEY'])
        env_value_list = json.loads(environ['PYGMENTS_HIGHLIGHTER_VALUE'])

        #regexpkey = re.compile(r'^.*you.*$')
        #regexpvalue = re.compile(r'^.*know.*$')
        
        regexpkey = '(?:% s)' % '|'.join(env_key_list)
        regexpvalue = '(?:% s)' % '|'.join(env_value_list )
        
        regexmode = environ.get("PYGMENTS_HIGHLIGHTER_REGEX_MODE", "search")

        if regexmode == "match":
            for ttype, token in stream:
                if re.match(regexpkey, token.strip('"'), re.IGNORECASE):
                    ttype = String.Highlight.Key
                if re.match(regexpvalue, token.strip('"'), re.IGNORECASE):
                    ttype = String.Highlight.Value
                yield ttype, token
        else:
            for ttype, token in stream:
                if re.search(regexpkey, token.strip('"'), re.IGNORECASE):
                    ttype = String.Highlight.Key
                if re.search(regexpvalue, token.strip('"'), re.IGNORECASE):
                    ttype = String.Highlight.Value
                yield ttype, token
