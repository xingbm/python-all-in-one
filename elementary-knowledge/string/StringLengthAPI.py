# 在Python中，数字、英文、小数点、下划线和空格占一个字节；一个汉字可能占2-4个字节，占几个字节取决于编码。
# 汉字在GBK/GB2312编码中占2个字节，在UTF-8/unicode中一般占3个字节（或4个字节）

# 在默认情况下，通过len()函数计算字符串的长度时，不区分英语、数字和汉字，所有字符都认为是一个
def demo1() :
    str1 = '人生苦短，我用Python!';
    length = len(str1);
    print(length);

# 使用UTF-8编码
def demo2() :
    str1 = '人生苦短，我用Python!';
    length = len(str1.encode())
    print(length);

# 使用GBK编码
def demo3() :
    str1 = '人生苦短，我用Python!';
    length = len(str1.encode('GBK'))
    print(length)

if __name__ == "__main__":
    print("开始执行：————————————")
    # demo1();
    # demo2();
    demo3();
