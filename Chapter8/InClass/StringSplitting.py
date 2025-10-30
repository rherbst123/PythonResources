import re
string = "start23123,Middle312313,End2312312"

start , middle, end = re.split(':|,| ', string)

print(start, middle, end)