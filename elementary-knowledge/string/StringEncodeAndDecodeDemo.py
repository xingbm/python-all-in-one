
def demo1() :
    verse = '野渡无人舟自横';
    byte = verse.encode('GBK');
    print('原字符串：', verse);
    print('转换后：', byte);
    # 使用GBK解码
    print('使用GBK解码,解码后：', byte.decode('GBK'));
    byte = verse.encode('UTF-8');
    print('转换后：', byte);
    # 使用UTF-8解码
    print('使用UTF-8解码,解码后：', byte.decode('UTF-8'));

# utf-8,unicode,gbk类型：unicode是str gbk utf-8是byte
def demo2() :
    b = '中国';
    print(type(b));
    c = b.encode('GBK');
    print(type(b));
    print(type(c));
    d = b.encode('UTF-8');
    print(type(b));
    print(type(d));

# utf-8,unicode,gbk之间转换
def demo3() :
    s = '小明';
    s_utf = s.encode('UTF-8');
    print(s_utf);
    s_gbk = s_utf.decode('utf-8').encode('gbk');
    print(s_gbk);
    print(s_utf.decode('utf-8'));
    print(s_gbk.decode('gbk'));


if __name__ == "__main__":
    print('开始执行：————————————');
    # demo1();
    # demo2();
    demo3();