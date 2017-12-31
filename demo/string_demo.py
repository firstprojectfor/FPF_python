from util import printutil

test_str_format = """
                My Name is {name}， 
                Welcome to Python !
            """
test_str = test_str_format.format(name="孙飞龙")

printutil.print_key_value("去除前后空格之后的长度", len(test_str.strip()))
printutil.print_key_value("空格数量", test_str.count(" "))

clean_str = test_str.lower().strip().replace("  ", "").replace("\n", " ").replace("，", "").replace("!", "")
printutil.print_key_value("转化为小写,并去除标点符号", clean_str)
printutil.print_key_value("把第一个字母转换为大写", clean_str.capitalize())
printutil.print_key_value("以n结尾", clean_str.strip().endswith("python"))
printutil.print_key_value("字符串是小写", clean_str.islower())
printutil.print_key_value("字符串是数字", clean_str.isdigit())
printutil.print_key_value("指定编码编码字符串", clean_str.encode(encoding="gbk").decode("gbk"))
printutil.print_key_value("大小写转换", clean_str.swapcase())

test_arr = test_str.strip().expandtabs().replace("\n", "").replace("!", "").replace("，", "").split(" ")
while "" in test_arr:
    test_arr.remove("")

printutil.print_key_value("转换为数组的长度", len(test_arr))
printutil.print_key_value("数组内容", test_arr)

# 字符串格式化
foobar = '{foo} {bar}'.format(foo="foo", bar="bar")
printutil.print_key_value("\"{foo} {bar}\".format(foo=\"foo\", bar=\"bar\") 格式化之后", foobar)

# map 字符串拼接
nums = map(str, range(20))
printutil.print_key_value("map 拼接之后：", " ".join(nums))

