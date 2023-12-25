
# *module和 packages
# module的定義，是指把code分成不同的檔案(files)，檔案的的名字被稱為 module
# & from  {module,packages的名字}  import  {module裡面的func 01} , {module裡面的func 02}
# packages 的定義，是指裡面有很多modules，用資料夾表示

import sys
from Chapter7_module import some_code01, some_code02
from Chapter7_module.myPackage import hello


some_code01.small_some_code01()
some_code02.small_some_code02()
hello.package01()

print(sys.path)  # 查看 module serching的用法。 notion筆記有詳細過程
