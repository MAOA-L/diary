# from django.test import TestCase

# Create your tests here.
import re

# str = "<ol>\n<li><a href=\"https://chenqianping.gitbooks.io/head-first-java/content/\" title=\"Head First Java\">Head First Java</a></li><li><a href=\"https://zhengyq.gitbooks.io/effective-java-2/content/item1.html\" title=\"Effective Java 中文版 第2版\">Effective Java 中文版 第2版</a></li><li><p><a href=\"https://legacy.gitbook.com/book/quanke/think-in-java/details\" title=\"Thinking in Java\">Thinking in Java</a></p>\n</li><li><p><a href=\"https://www.cnblogs.com/chen1005/p/10481102.html\" title=\"Java基础面试题\">Java基础面试题</a></p>\n</li></ol>\n<h1 id=\"h1-python-django\"><a name=\"python-Django\" class=\"reference-link\"></a><span class=\"header-link octicon octicon-link\"></span>python-Django</h1><p><a href=\"https://q1mi.github.io/Django-REST-framework-documentation/tutorial/quickstart_zh/\" title=\"DRF中文文档\">DRF中文文档</a></p>\n"
#
# a = re.compile(r'<[\n]+>')
# dd = a.sub('', str)
# print(dd)


s = ')()()(())'


class Solution:

    def longestValidParentheses(self, s):
        """
        Method 1: use stack
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        stack = [-1]
        res = 0
        for idx, paren in enumerate(s):
            if paren == '(':
                stack.append(idx)
            else:
                stack.pop()
                if not stack:
                    stack.append(idx)
                else:
                    res = max(res, idx - stack[-1])
        return res


if __name__ == "__main__":
    a = Solution().longestValidParentheses(s)
    print(a)
