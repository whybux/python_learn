"""
输入年份 如果是闰年输出True 否则输出False

"""

yearInput = int(input('请输入年份'))
is_leep = (yearInput % 4 == 0 and yearInput % 100 != 0
           or yearInput % 400 == 0)

print("%d年是闰年吗？%s" % (yearInput, is_leep))
