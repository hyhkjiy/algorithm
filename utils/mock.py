# -*- coding:utf-8 -*-
"""
用于数据模拟的工具类
"""
import random
from functools import total_ordering

name_list_160 = ['孙悟空', '唐僧', '猪八戒', '沙僧', '太上老君', '嫦娥仙子', '太白金星', '托塔天王', '哪吒', '白骨精', '黄眉妖王', '金池长老', '赤脚大仙', '二郎神',
                 '高才', '高老夫人', '高太公', '高翠兰', '宝象国国王', '黑熊精', '老翁', '乌鸡国国王', '乌鸡国王后', '玉兔', '黎山老母', '广智和尚', '殷小姐', '唐太宗',
                 '弥勒佛', '小白龙', '铁扇公主', '牛魔王', '杏仙', '金顶大仙', '妖道', '仙鹤', '村姑', '万圣公主', '车迟国王后', '镇元大仙', '红孩儿', '女儿国国王',
                 '怜怜', '王母娘娘', '混事魔王', '蛟魔王', '鹏魔王', '狮驼王', '猕猴王', '禺狨王寅将军', '熊山君', '特处士', '黑风怪', '黄风怪', '白衣秀士',
                 '凌虚子黄袍怪', '金角大王', '银角大王', '精细鬼', '伶俐虫', '巴山虎', '倚海龙', '狐阿七大王', '九尾狐狸', '狮猁怪', '圣婴大王', '鼍龙', '虎力大仙',
                 '鹿力大仙', '羊力大仙', '金鱼怪', '兕怪', '如意真仙', '琵琶精', '六耳猕猴', '铁扇公主', '玉面狐狸', '九头虫', '奔波儿灞', '灞波儿奔', '孤直公',
                 '凌空子', '拂云叟', '劲节十八公', '黄眉老佛', '巨蟒怪', '赛太岁', '七蜘蛛精', '百眼魔君', '金鼻白毛老鼠精', '艾叶花皮豹子精', '黄狮精', '九灵元圣狻猊狮',
                 '抟象狮', '白泽狮', '伏狸狮', '猱狮', '雪狮', '辟寒大王', '辟暑大王', '辟寒大王', '辟暑大王', '辟尘大王', '狮王', '象王', '大鹏金翅雕', '白鹿怪',
                 '白面狐狸', '林黛玉', '薛宝钗', '贾元春', '贾迎春', '贾探春', '贾惜春', '李纨', '妙玉', '史湘云', '王熙凤', '贾巧姐', '秦可卿', '晴雯', '麝月',
                 '袭人', '鸳鸯', '雪雁', '紫鹃', '碧痕', '平儿', '香菱', '金钏', '司棋', '抱琴', '赖大', '焦大', '王善保', '周瑞', '林之孝', '乌进孝',
                 '包勇', '吴贵', '吴新登', '邓好时', '王柱儿', '余信', '薛蟠', '薛蝌', '薛宝钗', '薛宝琴', '王夫人', '王熙凤', '王子腾', '王仁', '尤老娘',
                 '尤氏', '尤二姐', '尤三姐', '贾蓉', '贾兰', '贾芸', '贾芹']


def sample_range(*args, **kwargs):
    """
    返回乱序数组
    """
    array = xrange(*args, **kwargs)
    return random.sample(array, len(array))


@total_ordering
class ExamResults(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __unicode__(self):
        return 'Name:{name}\t,Score:{score}'.format(name=self.name, score=self.score)

    def __str__(self):
        return self.__unicode__()

    def __lt__(self, other):
        return self.score < other.score

    def __eq__(self, other):
        return self.score == other.score


def sample_exam_results(number, score_start=50, score_stop=100):
    return [ExamResults(name_list_160[i], random.randint(score_start, score_stop)) for i in sample_range(number)]
