"""
=============================
Author  : lsw
Time    : 2019-10-17
E-mail  : 591271859@qq.com
=============================
"""
import os
import time
import string
import random
from comm.constant import CONF_DIR
from comm.operate_mysql import OperateSQL


class RandomeVar(object):
    db = OperateSQL()

    def random_phone(self):
        """
        随机生成手机号码
        :return: str类型的11位手机号
        """
        while True:
            phone_start = ['130', '131', '132', '133','134', '135', '136', '137', '138', '139',
                       '145', '147', '149', 
                       '150', '151', '152',  '153', '155', '156', '157', '158', '159',
                       '166',
                       '170', '171', '172', '173', '175', '176', '177', '178',
                       '180', '181', '182', '183', '184', '185', '186', '187', '188', '189',
                       '191', '193', '198', '199'
                       ]
            # 从phone_start列表中随机取一个元素
            start = random.choice(phone_start)
            # 从生成的0-9数组中随机取8个元素，并转换为字符(随机生成8个数字)
            end = ''.join(random.sample(string.digits, 8))
            phone = start + end

            # 查询数据库中该手机号码是否存在
            sql = "SELECT * FROM user_db.t_user_info WHERE Fmobile='{}';".format(phone)
            if not start.db.find_count(sql):
                return phone

    def random_ip(self):
        """
        随机生成ip
        :return:str类型的ip地址
        """
        num_list = []
        for i in range(4):
            num = random.randint(0, 255)
            num_list.append(num)
        ip = "{}.{}.{}.{}".format(*num_list)
        return ip

    def random_user(self):
        """
        随机生成user

        PS：使用时记得临时保存记录一下，以便后续查询和使用
        """
        while True:
            # 随机生成长度为6包含字母和数字的用户名       ascii_letters是生成所有字母，从a-z和A-Z,digits是生成所有数字0-9
            user = ''.join(random.sample(string.ascii_letters + string.digits, 6))
            # 查询数据库中该用户名是否存在
            sql = "SELECT * FROM user_db.t_user_info WHERE Fuser_id='{}';".format(user)
            if not self.db.find_count(sql):
                return user

    def random_date(self, start, end, frmt='%Y%m%d'):
        """随机生成日期"""
        # 开始日期的时间戳
        stime = time.mktime(time.strptime(start, frmt))
        # 结束日期的时间戳
        etime = time.mktime(time.strptime(end, frmt))
        # 生成的随机时间戳
        prop = random.random()
        ptime = stime + prop * (etime - stime)
        # 将生成的随机时间戳转换为指定格式
        date = time.strftime(frmt, time.localtime(int(ptime)))
        return date

    def random_idnum(self, start, end):
        """随机生成身份证号"""
        with open(os.path.join(CONF_DIR, 'districtcode.txt'), mode='r', encoding='utf8') as file:
            codelist = file.readlines()
        district = codelist[random.randint(0, len(codelist) - 1)].split(" ")[0]
        date = str(self.random_date(start, end))
        seq_num = str(random.randint(100, 300))
        id = district + date + seq_num
        weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]  # 权重项
        checkcode = {'0': '1', '1': '0', '2': 'X', '3': '9', '4': '8', '5': '7', '6': '6', '7': '5', '8': '5', '9': '3',
                     '10': '2'}
        count = 0
        for i in range(0, len(id)):
            count = count + int(id[i]) * weight[i]
        check_code = checkcode[str(count % 11)]
        id_num = id + check_code
        return id_num

    def random_bankcard(self):
        """随机生成银行卡号"""
        # 工商银行卡号开头
        # prefix = "622202"
        # 招商银行卡号开头
        prefix = "622609"
        for i in range(13):
            prefix = prefix + str(random.randint(0, 9))
        return prefix

    def random_name(self):
        """随机生成姓名"""
        x_name = ['赵', '钱', '孙', '李', '周', '吴', '郑', '王', '冯', '陈', '褚', '卫', '蒋', '沈', '韩', '杨', '朱', '秦',
                  '尤', '许', '何', '吕', '施', '张', '孔', '曹', '严', '华', '金', '魏', '陶', '姜', '戚', '谢', '邹', '喻',
                  '柏', '水', '窦', '章', '云', '苏', '潘', '葛', '奚', '范', '彭', '郎', '鲁', '韦', '昌', '马', '苗', '凤',
                  '花', '方', '俞', '任', '袁', '柳', '酆', '鲍', '史', '唐', '费', '廉', '岑', '薛', '雷', '贺', '倪', '汤',
                  '滕', '殷', '罗', '毕', '郝', '邬', '安', '常', '乐', '于', '时', '傅', '皮', '卞', '齐', '康', '伍', '余',
                  '元', '卜', '顾', '孟', '平', '黄', '和', '穆', '萧', '尹', '姚', '邵', '堪', '汪', '祁', '毛', '禹', '狄',
                  '米', '贝', '明', '臧', '计', '伏', '成', '戴', '谈', '宋', '茅', '庞', '熊', '纪', '舒', '屈', '项', '祝',
                  '董', '梁']
        m_name = ['的', '一', '是', '了', '我', '不', '人', '在', '他', '有', '这', '个', '上', '们', '来', '到', '时', '大',
                  '地', '为', '子', '中', '你', '说', '生', '国', '年', '着', '就', '那', '和', '要', '她', '出', '也', '得',
                  '里', '后', '自', '以', '会', '家', '可', '下', '而', '过', '天', '去', '能', '对', '小', '多', '然', '于',
                  '心', '学', '么', '之', '都', '好', '看', '起', '发', '当', '没', '成', '只', '如', '事', '把', '还', '用',
                  '第', '样', '道', '想', '作', '种', '开', '美', '总', '从', '无', '情', '己', '面', '最', '女', '但', '现',
                  '前', '些', '所', '同', '日', '手', '又', '行', '意', '动', '方', '期', '它', '头', '经', '长', '儿', '回',
                  '位', '分', '爱', '老', '因', '很', '给', '名', '法', '间', '斯', '知', '世', '什', '两', '次', '使', '身',
                  '者', '被', '高', '已', '亲', '其', '进', '此', '话', '常', '与', '活', '正', '感', '见', '明', '问', '力',
                  '理', '尔', '点', '文', '几', '定', '本', '公', '特', '做', '外', '孩', '相', '西', '果', '走', '将', '月',
                  '十', '实', '向', '声', '车', '全', '信', '重', '三', '机', '工', '物', '气', '每', '并', '别', '真', '打',
                  '太', '新', '比', '才', '便', '夫', '再', '书', '部', '水', '像', '眼', '等', '体', '却', '加', '电', '主',
                  '界', '门', '利', '海', '受', '听', '表', '德', '少', '克', '代', '员', '许', '稜', '先', '口', '由', '死',
                  '安', '写', '性', '马', '光', '白', '或', '住', '难', '望', '教', '命', '花', '结', '乐', '色', '更', '拉',
                  '东', '神', '记', '处', '让', '母', '父', '应', '直', '字', '场', '平', '报', '友', '关', '放', '至', '张',
                  '认', '接', '告', '入', '笑', '内', '英', '军', '候', '民', '岁', '往', '何', '度', '山', '觉', '路', '带',
                  '万', '男', '边', '风', '解', '叫', '任', '金', '快', '原', '吃', '妈', '变', '通', '师', '立', '象', '数',
                  '四', '失', '满', '战', '远', '格', '士', '音', '轻', '目', '条', '呢', '病', '始', '达', '深', '完', '今',
                  '提', '求', '清', '王', '化', '空', '业', '思', '切', '怎', '非', '找', '片', '罗', '钱', '紶', '吗', '语',
                  '元', '喜', '曾', '离', '飞', '科', '言', '干', '流', '欢', '约', '各', '即', '指', '合', '反', '题', '必',
                  '该', '论', '交', '终', '林', '请', '医', '晚', '制', '球', '决', '窢', '传', '画', '保', '读', '运', '及',
                  '则', '房', '早', '院', '量', '苦', '火', '布', '品', '近', '坐', '产', '答', '星', '精', '视', '五', '连',
                  '司', '巴', '奇', '管', '类', '未', '朋', '且', '婚', '台', '夜', '青', '北', '队', '久', '乎', '越', '观',
                  '落', '尽', '形', '影', '红', '爸', '百', '令', '周', '吧', '识', '步', '希', '亚', '术', '留', '市', '半',
                  '热', '送', '兴', '造', '谈', '容', '极', '随', '演', '收', '首', '根', '讲', '整', '式', '取', '照', '办',
                  '强', '石', '古', '华', '諣', '拿', '计', '您', '装', '似', '足', '双', '妻', '尼', '转', '诉', '米', '称',
                  '丽', '客', '南', '领', '节', '衣', '站', '黑', '刻', '统', '断', '福', '城', '故', '历', '惊', '脸', '选',
                  '包', '紧', '争', '另', '建', '维', '绝', '树', '系', '伤', '示', '愿', '持', '千', '史', '谁', '准', '联',
                  '妇', '纪', '基', '买', '志', '静', '阿', '诗', '独', '复', '痛', '消', '社', '算', '义', '竟', '确', '酒',
                  '需', '单', '治', '卡', '幸', '兰', '念', '举', '仅', '钟', '怕', '共', '毛', '句', '息', '功', '官', '待',
                  '究', '跟', '穿', '室', '易', '游', '程', '号', '居', '考', '突', '皮', '哪', '费', '倒', '价', '图', '具',
                  '刚', '脑', '永', '歌', '响', '商', '礼', '细', '专', '黄', '块', '脚', '味', '灵', '改', '据', '般', '破',
                  '引', '食', '仍', '存', '众', '注', '笔', '甚', '某', '沉', '血', '备', '习', '校', '默', '务', '土', '微',
                  '娘', '须', '试', '怀', '料', '调', '广', '蜖', '苏', '显', '赛', '查', '密', '议', '底', '列', '富', '梦',
                  '错', '座', '参', '八', '除', '跑', '亮', '假', '印', '设', '线', '温', '虽', '掉', '京', '初', '养', '香',
                  '停', '际', '致', '阳', '纸', '李', '纳', '验', '助', '激', '够', '严', '证', '帝', '饭', '忘', '趣', '支',
                  '春', '集', '丈', '木', '研', '班', '普', '导', '顿', '睡', '展', '跳', '获', '艺', '六', '波', '察', '群',
                  '皇', '段', '急', '庭', '创', '区', '奥', '器', '谢', '弟', '店', '否', '害', '草', '排', '背', '止', '组',
                  '州', '朝', '封', '睛', '板', '角', '况', '曲', '馆', '育', '忙', '质', '河', '续', '哥', '呼', '若', '推',
                  '境', '遇', '雨', '标', '姐', '充', '围', '案', '伦', '护', '冷', '警', '贝', '著', '雪', '索', '剧', '啊',
                  '船', '险', '烟', '依', '斗', '值', '帮', '汉', '慢', '佛', '肯', '闻', '唱', '沙', '局', '伯', '族', '低',
                  '玩', '资', '屋', '击', '速', '顾', '泪', '洲', '团', '圣', '旁', '堂', '兵', '七', '露', '园', '牛', '哭',
                  '旅', '街', '劳', '型', '烈', '姑', '陈', '莫', '鱼', '异', '抱', '宝', '权', '鲁', '简', '态', '级', '票',
                  '怪', '寻', '杀', '律', '胜', '份', '汽', '右', '洋', '范', '床', '舞', '秘', '午', '登', '楼', '贵', '吸',
                  '责', '例', '追', '较', '职', '属', '渐', '左', '录', '丝', '牙', '党', '继', '托', '赶', '章', '智', '冲',
                  '叶', '胡', '吉', '卖', '坚', '喝', '肉', '遗', '救', '修', '松', '临', '藏', '担', '戏', '善', '卫', '药',
                  '悲', '敢', '靠', '伊', '村', '戴', '词', '森', '耳', '差', '短', '祖', '云', '规', '窗', '散', '迷', '油',
                  '旧', '适', '乡', '架', '恩', '投', '弹', '铁', '博', '雷', '府', '压', '超', '负', '勒', '杂', '醒', '洗',
                  '采', '毫', '嘴', '毕', '九', '冰', '既', '状', '乱', '景', '席', '珍', '童', '顶', '派', '素', '脱', '农',
                  '疑', '练', '野', '按', '犯', '拍', '征', '坏', '骨', '余', '承', '置', '臓', '彩', '灯', '巨', '琴', '免',
                  '环', '姆', '暗', '换', '技', '翻', '束', '增', '忍', '餐', '洛', '塞', '缺', '忆', '判', '欧', '层', '付',
                  '阵', '玛', '批', '岛', '项', '狗', '休', '懂', '武', '革', '良', '恶', '恋', '委', '拥', '娜', '妙', '探',
                  '呀', '营', '退', '摇', '弄', '桌', '熟', '诺', '宣', '银', '势', '奖', '宫', '忽', '套', '康', '供', '优',
                  '课', '鸟', '喊', '降', '夏', '困', '刘', '罪', '亡', '鞋', '健', '模', '败', '伴', '守', '挥', '鲜', '财',
                  '孤', '枪', '禁', '恐', '伙', '杰', '迹', '妹', '藸', '遍', '盖', '副', '坦', '牌', '江', '顺', '秋', '萨',
                  '菜', '划', '授', '归', '浪', '听', '凡', '预', '奶', '雄', '升', '碃', '编', '典', '袋', '莱', '含', '盛',
                  '济', '蒙', '棋', '端', '腿', '招', '释', '介', '烧', '误', '乾', '坤']
        # 随机取1个字的姓氏
        last_name = random.choice(x_name)
        # 随机取1-2个字的名
        name = random.sample(m_name, random.randint(1, 2))
        xm_name = last_name + ''.join(name)
        return xm_name


if __name__ == '__main__':
    pass










