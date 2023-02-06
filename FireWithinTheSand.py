# -*- encoding=utf8 -*-
__author__ = "鬼道"

from airtest.core.api import *

auto_setup(__file__)

# 撤退并开始下一轮
def func_run():
    pos = wait(Template(r"tpl1675435729085.png", record_pos=(-0.465, -0.252), resolution=(1280, 720)))
    sleep(1)
    touch(pos)
    touch(wait(Template(r"tpl1675435905993.png", record_pos=(0.132, 0.23), resolution=(1280, 720))))
    pos = wait(Template(r"tpl1675435917510.png", threshold=0.8, record_pos=(0.151, 0.1), resolution=(1280, 720)))
    sleep(1)
    touch(Template(r"tpl1675435917510.png", threshold=0.8, record_pos=(0.151, 0.1), resolution=(1280, 720)))
    pos = wait(Template(r"tpl1675435930693.png", record_pos=(0.41, 0.206), resolution=(1280, 720)))
    sleep(1)
    touch(pos)
    pos = wait(Template(r"tpl1675435957485.png", record_pos=(0.434, 0.205), resolution=(1280, 720)))
    touch(pos)
    sleep(0.5)
    touch((1,1))
    sleep(1)
    func_main_thread()


# 主循环
def func_main_thread():
    wait(Template(r"tpl1675433061342.png", record_pos=(0.359, 0.231), resolution=(1280, 720)))
    sleep(0.5)

    touch(Template(r"tpl1675433061342.png", record_pos=(0.359, 0.231), resolution=(1280, 720)))
    sleep(1.0)
    touch(wait(Template(r"tpl1675434596751.png", record_pos=(0.422, -0.245), resolution=(1280, 720))))
    touch(wait(Template(r"tpl1675434667517.png", record_pos=(0.344, 0.228), resolution=(1280, 720))))
    touch(wait(Template(r"tpl1675434728917.png", record_pos=(0.309, 0.19), resolution=(1280, 720))))
#   按每天循环
    for i in range(5):
        wait(Template(r"tpl1675434786044.png", threshold=0.9, record_pos=(0.449, 0.245), resolution=(1280, 720)),40)
        sleep(1)
        touch(Template(r"tpl1675434786044.png", threshold=0.9, record_pos=(0.449, 0.245), resolution=(1280, 720)))
        # 在第5天前每天正常循环去行动两次        
        if i < 4:  
            wait(Template(r"tpl1675434816982.png", record_pos=(0.001, -0.001), resolution=(1280, 720)))
            sleep(2)

            touch(Template(r"tpl1675434816982.png", record_pos=(0.001, -0.001), resolution=(1280, 720)))
            # 行动两次
            for j in range(2):
                sleep(0.5)
                # 寻找各种不同样式的资源区
                resource_pos_1 = exists(Template(r"tpl1675437025998.png", threshold=0.4, record_pos=(0.184, 0.147), resolution=(1280, 720)))
                resource_pos_2 = exists(Template(r"tpl1675437283238.png", threshold=0.4, record_pos=(0.07, -0.021), resolution=(1280, 720)))
                resource_pos_3 = exists(Template(r"tpl1675437358862.png", threshold=0.4, record_pos=(0.062, -0.18), resolution=(1280, 720)))
                resource_pos_4 = exists(Template(r"tpl1675437518906.png", threshold=0.4, record_pos=(-0.101, -0.1), resolution=(1280, 720)))
                # 若找到了其中某个资源区 则出击
                if resource_pos_1:
                    touch(resource_pos_1)
                elif resource_pos_2:
                    touch(resource_pos_2)
                elif resource_pos_2:
                    touch(resource_pos_3)
                elif resource_pos_2:
                    touch(resource_pos_4)
                # 若一个资源区都没找到 则撤退
                else:
                    func_run()
                # 出击
                if exists(Template(r"tpl1675434858429.png", record_pos=(0.396, 0.198), resolution=(1280, 720))):
                    pos = wait(Template(r"tpl1675434858429.png", record_pos=(0.396, 0.198), resolution=(1280, 720)))
                    sleep(1)
                    touch(pos)
                    touch(wait(Template(r"tpl1675434877718.png", record_pos=(0.368, 0.231), resolution=(1280, 720))))
                    wait(Template(r"tpl1675434889270.png", record_pos=(0.38, -0.009), resolution=(1280, 720)))
                    sleep(1)
                    touch(Template(r"tpl1675434889270.png", record_pos=(0.38, -0.009), resolution=(1280, 720)))
                    pos = wait(Template(r"tpl1675434900565.png", threshold=0.8, record_pos=(0.159, 0.099), resolution=(1280, 720)))
                    sleep(2)
                    touch(pos)
                    wait(Template(r"tpl1675434933886.png", record_pos=(-0.439, -0.237), resolution=(1280, 720)))
                    sleep(2)
                    touch(Template(r"tpl1675434933886.png", record_pos=(-0.439, -0.237), resolution=(1280, 720)))
                    touch(wait(Template(r"tpl1675434944679.png", record_pos=(0.321, 0.049), resolution=(1280, 720))))
                    wait(Template(r"tpl1675434986379.png", record_pos=(-0.325, -0.041), resolution=(1280, 720)))
                    sleep(2)
                    touch(Template(r"tpl1675434986379.png", record_pos=(-0.325, -0.041), resolution=(1280, 720)))
                elif exists(Template(r"tpl1675435729085.png", record_pos=(-0.465, -0.252), resolution=(1280, 720))):
                    func_run()
                else:
                    touch(wait(Template(r"tpl1675491142824.png", record_pos=(-0.466, -0.251), resolution=(1280, 720))))
                    sleep(1)
                    func_run()
            # 出击两次后进入下一天    
            touch(wait(Template(r"tpl1675435146910.png", record_pos=(0.426, -0.245), resolution=(1280, 720))))
        # 第五天 撤退！
        else:
            func_run()

            
# 正片
func_main_thread()
    


