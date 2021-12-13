"""
练习10-10：常见单词 　访问古登堡计划，找一些你想分析的图书。下载这些
作品的文本文件或将浏览器中的原始文本复制到文本文件中。
可以使用方法count() 来确定特定的单词或短语在字符串中出现了多少次。例
如，下面的代码计算'row' 在一个字符串中出现了多少次：
>>> line = "Row, row, row your boat"
>>> line.count('row')
2
>>> line.lower().count('row')
3
请注意，通过使用lower() 将字符串转换为小写，可捕捉要查找单词的所有格
式，而不管其大小写如何。
编写一个程序，它读取你在古登堡计划中获取的文件，并计算单词'the' 在每
个文件中分别出现了多少次。这里计算得到的结果并不准确，因为将诸
如'then' 和'there' 等单词也计算在内了。请尝试计算'the ' （包含空
格）出现的次数，看看结果相差多少。
"""