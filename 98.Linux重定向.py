"""
Linux允许将命令执行的结果 重定向到一个文件，将原本应该显示在终端上的内容 输出/追加到指定的文件中
> ：表示输出，会覆盖原文件的内容
>> ：表示追加，会将内容追加到已有文件的末尾

用法示例：
    将 echo 输出的信息保存到1.txt里   -->   echo hello world > 1.txt
    将 tree 输出的信息追加到1.txt里   -->   tree >> 1.txt
"""