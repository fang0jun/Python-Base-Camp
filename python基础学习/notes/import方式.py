import plane_sprite   #---调用时需要模块名
from plane_sprite import module_1
from plane_sprite impot *   #---调用时不需要模块名

"""

模块导入的导入顺序：先当前目录 / 后系统目录  （故不要重名）
if __name__ == "__main__"   只在本文件中进行测试

文件被当作模块导入时，所有没有缩进的代码都会被执行一遍 // 若要测试则使用 if __name__ == "__main__"
（使用__name__属性---保存一系列字符串，在当前执行文件中为__main__ 在被导入文件中为所在模块的模块名）

"""