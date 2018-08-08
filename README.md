
TextTeaser - 中文版
=============
用法依旧。

兼容中文。


TextTeaser - for Chinese
=============
Instructions are consistent but text need to be in chinese.

Python3 needed. Using jieba as tokenizer.


TextTeaser
=============

TextTeaser is an automatic summarization algorithm.

This is now the official version of TextTeaser. Future developments of TextTeaser will be in this repository.

The original Scala TextTeaser can still be accessed [here](https://github.com/MojoJolo/textteaser).

### How to Use

    >>> from textteaser import TextTeaser
    >>> tt = TextTeaser()
    >>> tt.summarize(title, text)

You can also test TextTeaser by running `python test.py`.
