# dynamic-pygments-highlighter
This is a dynamic pygments highlighter that will highlight pygment tokens based on if they match certain environment variables. It is designed for demos and bringing attention to certain key parts of a console/terminal output that you want to highlight. However, it could be used as part of other pygment workflows that output to html or a number of different formats.

## Installation

Using pip
```
$ git clone git://github.com/johnfosborneiii/dynamic-pygments-highlighter.git
$ cd dynamic-pygments-highlighter
$ (sudo) pip install .
```

## Usage

** Add the following to your `~/.bashrc` file
```bash
# Initialize `~/.bashrc.d`
export PYGMENTS_HIGHLIGHTER_KEY='["url", "subject"]'
export PYGMENTS_HIGHLIGHTER_VALUE='["https://github.com/chainguard-dev/", "https://fulcio.sigstore.dev"]'

# This can be set to match (default) or search
# tl;dr - match is an exact match while search means that the highlight value can a substring anywhere in the token and it will highlight the entire token
# match searches only from the beginning of the string and return match object if found. But if a match of substring is found somewhere in the middle of the string, it returns none.
# searches for the whole string even if the string contains multi-lines and tries to find a match of the substring in all the lines of string
export PYGMENTS_HIGHLIGHTER_REGEX_MODE="search"

alias highlight-yaml="pygmentize -l yaml -F dynamic-highlighter -P style=dynamic-highlighter"
alias highlight-json="pygmentize -l json -F dynamic-highlighter -P style=dynamic-highlighter"
alias highlight="pygmentize -F dynamic-highlighter -P style=dynamic-highlighter"
```
Make the changes active
```
$ source `~/.bashrc`
```

```
cat <<yaml file name>>.yaml | highlight-yaml
```
![image](https://user-images.githubusercontent.com/9351962/187477064-284a20ae-1ff5-4bf6-9f3a-6a43d7b70463.png)

Note: You can pipe all sorts of different formats to pygmentize using different Pygment lexers. Pygments will guess the lexer or you can manually set it by leveraging the -l flag (pygmentize on the CLI). Pygment lexers take output and slices them into Python token tuples. There are many pygment lexers that you can read about in the [Pygments Documentation](https://pygments.org/docs/).

## Customization

Editing the color scheme is very easy. First, make a note of what type of token the string you want to highlight is getting set to by the lexer. This can be done by outputting to the "tokens" format:
```
$ cat demo-images.yaml | pygmentize -l yaml -F dynamic-highlighter -f tokens
```
Next, open the pygments_style_dynamic_highlighter.py and modify the corresponding HTML color code. Then reinstall.
```
pip install .
```