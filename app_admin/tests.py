from django.test import TestCase
import re
# Create your tests here.
str = "call{sdsa=asdsa;asds=asdsaa}"
q = re.match("call{(.*)}", str)
print(q.group(2))

