"""
    Python split() 方法通过指定分隔符对字符串进行分割并返回一个列表,默认分隔符为所有空字符，包括空格、换行(\n)、制表符(\t)等
    x[:,n]表示在全部数组（维）中取第n个数据，直观来说，x[:,n]就是取所有集合的第n个数据, 
    x[n,:]表示在n个数组（维）中取全部数据，直观来说，x[n,:]就是取第n集合的所有数据,
    x[:,m:n]，即取所有数据集的第m到n-1列数据
    b = a[i:j:s]这种格式呢，i,j与上面的一样，但s表示步进，缺省为1
"""








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
