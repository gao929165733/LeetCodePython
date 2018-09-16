class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # 判断是否为个位数，是个位数则不用反转，直接返回
        if -10 < x < 10:
            return x
        # 把整数x转为字符串
        str_x = str(x)
        # 判断第一个是否为负号
        if str_x[0] != "-":
            # 不是负号则直接反转
            str_x = str_x[::-1]
            # str转为int
            x = int(str_x)
        else:
            # 是负号，则反转负号之后的字符串
            str_x = str_x[1:][::-1]
            # str转int
            x = int(str_x)
            # 加上负号
            x = -x
        #判断数值范围
        if (x >-2**31 and x<(2**31-1)):
            return x
        else:
            return 0


if __name__ == '__main__':
    s = Solution()
    reverse_int = s.reverse(-120)
    print(reverse_int)
