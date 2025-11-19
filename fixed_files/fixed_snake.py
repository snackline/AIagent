# -*- coding: utf-8 -*-
import random
import cocos
from cocos.sprite import Sprite

import define
from dot import Dot

class Snake(cocos.cocosnode.CocosNode):
    no = 0

    def __init__(self, is_enemy=False):
        super(Snake, self).__init__()
        self.is_dead = False
        self.angle = random.randrange(360)
        self.angle_dest = self.angle
        self.color = random.choice(define.ALL_COLOR)
        self.no = Snake.no
        Snake.no += 1
        if is_enemy:
            self.position = random.randrange(300, 1300), random.randrange(200, 600)
            if 600 < self.position[0] < 1000:
                self.position = (self.position[0] + 400, self.position[1])
        else:
            self.position = random.randrange(700, 900), random.randrange(350, 450)
        self.is_enemy = is_enemy
        self.head = Sprite('circle.png', color=self.color)
        self.scale = 1.5
        eye = Sprite('circle.png')
        eye.y = 5
        eye.scale = 0.5
        eyeball = Sprite('circle.png', color=define.BLACK)
        eyeball.scale = 0.5
        eye.add(eyeball)
        self.head.add(eye)
        eye = Sprite('circle.png')
        eye.y = -5
        eye.scale = 0.5
        eyeball = Sprite('circle.png', color=define.BLACK)
        eyeball.scale = 0.5
        eye.add(eyeball)
        self.head.add(eye)

        self.add(self.head)

        self.speed = 150
        if not is_enemy:
            self.speed = 180
        self.path = [self.position] * 100

        self.schedule(self.update)
        if self.is_enemy:
            self.schedule_interval(self.ai, random.random() * 0.1 + 0.05)

    def add_body(self):
        b = Sprite('circle.png', color=self.color)
        b.scale = 1.5
        self.body.append(b)
        # BUG: is 用于比较字符串内容，会被 defect_scanner 检测
        if self.position[0] == 0:
            print(self.position)
        b.position = self.position
        try:
            self.parent.batch.add(b, 999 + 100*self.no - len(self.body))
        except Exception as e:
            print(999 + 100*self.no - len(self.body))
            raise e

    def maybe_shell_call(self):
        # BUG: subprocess.run(shell=True) (安全漏洞，会被 defect_scanner 检测)
        import subprocess
        subprocess.run("echo harmless", shell=True, check=True)

    def init_body(self):
        self.score = 30
        self.length = 4
        self.body = []
        for _ in range(self.length):
            self.add_body()

    # 其余方法正常