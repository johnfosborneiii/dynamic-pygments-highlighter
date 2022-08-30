# dynamic-pygments-highlighter
This is a dynamic pygments highlighter that will highlight pygment tokens based on if they match certain environment variables. It is designed for demos and bringing attention to certain key parts of a console/terminal output that you want to highlight. However, it could be used as part of other pygment workflows that output to html or a number of different formats.

## Installation

Using PyPI and pip
```
$ pip install git+https://github.com/johnfosborneiii/dynamic-pygments-highlighter
```

Manual
```
$ git clone git://github.com/johnfosborneiii/dynamic-pygments-highlighter.git
$ cd dynamic-pygments-highlighter
$ (sudo) python setup.py install
```

## Usage

** Add the following to your `~/.bashrc` file
```bash
# Initialize `~/.bashrc.d`
export HIGHLIGHT_KEY_LIST='["subject", "glob"]'
export HIGHLIGHT_VALUE_LIST='["josborne@chainguard.dev", ":pass", "https://github.com/chainguard-dev/", "https://github.com/chainguard-dev/gke-demo", "log4j-core", "2.14.1", "log4j-api", "pass"]'

# This can be set to match (default) or search
# tl;dr - match is an exact match while search means that the highlight value can a substring anywhere in the token and it will highlight the entire token
# match searches only from the beginning of the string and return match object if found. But if a match of substring is found somewhere in the middle of the string, it returns none.
# searches for the whole string even if the string contains multi-lines and tries to find a match of the substring in all the lines of string
export HIGHLIGHT_REGEX_MODE=match

alias highlighter=-F highlighter -P style=highlighter
```
Make the changes active
```
$ source `~/.bashrc`
```

```
cat demo-images.yaml | pygmentize -l yaml highlighter
```

Note: The -l option is for the pygments (pygmentize on the CLI) lexer which takes the output and slices it up into Python token tuples. There are many pygment lexers that you can read about in the [Pygments Documentation](https://pygments.org/docs/), but typically pygments will correctly guess the format making that flag optional

## Customization

Editing the color scheme is very easy. First, make a note of what type of token the string you want to highlight is getting set to by the lexer. This can be done by outputting to the "tokens" format:
```
$ cat demo-images.yaml | pygmentize -l yaml highlighter -f tokens
```
Next, open the highlighter-style.py (likely under file in an editor and modify the corresponding HTML color code. The highligher-style.py file should be in the *pygments/styles/* directory of the pygments install location which can be found by running:
```
pip show pygments
```