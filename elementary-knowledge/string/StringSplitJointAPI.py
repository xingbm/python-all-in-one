
# 使用+运算符完成多个字符串的拼接
def demo1() :
    mot_en = 'string1';
    mot_cn = '哈哈哈哈哈';
    print(mot_en + '——' + mot_cn);

# 字符串不允许直接和其他类型的数据拼接,会报错：TypeError: can only concatenate str (not "int") to str
def demo2() :
    str1 = '我今天一共走了';
    num = 12098;
    str2 = '步';
    print(str1 + num + str2);

# 解决字符串和其他数据类型拼接问题
def demo3() :
    str1 = '我今天一共走了';
    num = 12098;
    str2 = '步';
    # 将整数转化为字符串
    print(str1 + str(num) + str2);

def demo4() :
    programmer_1 = '程序员甲：搞IT太辛苦了，我想换行。。。。。。怎么办？';
    programmer_2 = '程序员乙：敲一下回车键';
    print(programmer_1 + '\n' + programmer_2)


if __name__ == "__main__":
    print('开始执行：————————————')
    # demo1();
    # demo2();
    # demo3();
    demo4();
