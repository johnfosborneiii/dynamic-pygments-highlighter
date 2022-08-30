# -*- coding: utf-8 -*-
"""
    Highlighter
    ~~~~~~
"""

from pygments.style import Style
from pygments.token import String,Comment, Error, Generic, Keyword, Literal, Name, Operator, Text


class DynamicHighlighterStyle(Style):
    
    """
    # Highlight based on environment variables
    """
    # $PYGMENTS_HIGHLIGHTER_KEY ==> Literal.String.Highlight.Key 
    # $PYGMENTS_HIGHLIGHTER_VALUE ==> Literal.String.Highlight.Value
    # Troubleshoot: Output token mapping: pygmentize -f tokens -P style=dynamic-highlighter
    
    default_style = ''

    background_color = '#5adeff'

    styles = {
        Error:                          'bg:#e3d2d2 #a61717',
        Keyword.Constant:               'bold #5adeff ',
        Keyword.Type:                   'bold #ff00ff',
        Literal.Number:                 '#5adeff',
        Literal.String.Highlight.Key:   '#bd93f9',
        Literal.String.Highlight.Value: '#ff00ff',
        Literal.String:                 '#5adeff',
        Name.Attribute:                 '#5adeff',
        Name.Label:                     'bold #5adeff',
        Name.Namespace:                 '#5adeff',
        Name.Tag:                       '#ffffff',
        Name.Variable:                  '#5adeff',
    }
