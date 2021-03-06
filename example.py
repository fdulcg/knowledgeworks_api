import kw_api as api

api.SetApiKey('')
# without it, some api requests will be blocked 
# goto http://shuyantech.com/ for a free key

api.SetCacheSize(size=100000)

print(api.Ment2Ent('上海'))
# {'上海': ['上海（中华人民共和国直辖市）', '上海（小行星）', '上海（任天堂game boy掌机游戏《上海》）', '上海（倪锡英的著作）', '上海（钟立风演唱歌曲）']}
print(api.Ment2Ent(['中国','李白']))
# {'中国': ['中国（世界四大文明古国之一）', '中华人民共和国', '河南（中华人民共和国省级行政区）', '中国（1972年安东尼奥尼执导纪录片）', '中国（汉语词语）', '中国（郭光主编图书）', '中国（周明伟，郭长建，黄友义主编图书）', '中国（小行星）', '中国（丁玲创办的杂志）', '中国（卓依婷演唱歌曲）', '中国（同名官方贴吧）', '中国（朱新民专著）', '中国（周翼南所著书籍）', '中国（外文出版社2014年版图书）', '中国（腾格尔演唱歌曲）', '中国（迈克尔·肯纳中国题材摄影集）', '中国（美国得州的小城）', '中国（梁海洋演唱歌曲）', '中国（（美）费正清所著书籍）', '中国（茄科枸杞属中国枸杞选育品种）', '中国（高枫演唱歌曲）', '中国（郭峰创作歌曲）', '中国（日本地理区域概念）', '中国（成龙、吴京演唱歌曲）', '中国（古代所指中原地区）', '中国（中华人民共和国）', '中国（2018年华语群星演唱的歌曲）', '中国'], 
#  '李白': ['李白（唐代著名浪漫主义诗人）', '李白（李荣浩演唱歌曲）', '李白（中共党员，上海地下党联络员）', '李白（中国2010年邵警辉执导电视剧）', '李白（qq游戏《英雄杀》卡牌）', '李白（北京人艺经典话剧）', '李白（南宋徐钧所写诗歌）', '李白（撒贝宁妻子、吉尼斯世界纪录大中华区裁判）', '李白（手游《王者荣耀》角色）', '李白（漫画《尸兄》中的角色）', '李白（李太白小少焱原创另类麦曲）', '李白（《天下hd》元魂之一）', '李白（四川省利州区白朝乡人民政府副乡长）', '李白（小行星）', '李白（黍黎释诗歌）', '李白（宋孟君演唱歌曲）', '李白（北京联帮在线教育科技有限公司ceo）', '李白']
#  }

print(api.GetEntMentions('周杰伦'))
# ['周董', 'jay chou', 'jay（周杰伦的英文名字）', 'jay']

print(api.GetEntDesc('周杰伦'))
# '周杰伦（Jay Chou），1979年1月18日出生于台湾省新北市 ...

print(api.GetEntAttrValues('周杰伦', '出生日期'))
# ['1979年01月18日']
print(api.GetEntAttrValuesMulti(['周杰伦', '方文山'], '出生日期'))
# {'周杰伦': ['1979年01月18日'], '方文山': ['1969年01月26日']}

print(api.GetEntListTriples('复旦大学'))
# [['历届校友', ['邵力子', '罗家伦', '陈维稷', '王铁崖', '包蕾', '洪绂曾', '江绵恒', '卢新华', '韩正', '丁薛祥']], ['国家级教学团队', ['物理化学系列课程教学团队', '复旦大学汉语言文学原典精读系列课程教学团队', '生物学基础和骨干课程教学团队', '哲学专业基础课程教学团队', '西方经济学教学团队', '儿科学教学团队', '数学类基础课程教学团队', '英语阅读赏析系列课程教学团队', '细胞与分子医学教学团队', '预防医学骨干课程教学团队', '思想政治理论课教学团队']], ['长江学者奖励计划', ['陈良尧', '孙凤艳', '葛均波', '汤其群', '侯晓远', '金国新', '韩平畴', '周鸣飞', '陈思和', 'Alastair Murchie', '杨新', '郭坤宇', '张军', '陈猛', '李骏', '陈贵强', '陈韬文', '柏兆俊', '王德威', '易庆', 'Richard H. Finnell']], ['国家重点学科', ['哲学', '理论经济学', '中国语言文学', '新闻传播学', '数学', '物理学', '化学', '生物学', '电子科学与技术', '基础医学', '中西医结合']], ['院系概况', ['中国语言文学系', '外国语言文学学院', '新闻学院', '历史学系', '文物与博物馆学系', '哲学学院', '社会发展与公共政策学院', '国际关系与公共事务学院', '法学院', '经济学院', '数学科学学院', '物理学系', '核科学与技术系', '化学系高分子科学系', '信息科学与工程学院微电子学院', '材料科学系', '航空航天系', '生命科学学院', '环境科学与工程系', '计算机科学技术学院', '软件学院', '管理学院', '上海医学院', '公共卫生学院', '药学院', '护理学院']], ['历年国家级精品课程及国家级精品资源共享课一览', ['中国古代文学史', '汉语言文学原典精读', '中国文学批评史', '中国文学批评史', '美学', '史学导论', '现代西方哲学', '西方哲学史', '马克思主义哲学原著选读', '大学英语', '新闻学概论', '马克思主义新闻思想', '马克思主义新闻思想', '当代中国政治制度', '当代中国政治制度', '宏观经济学', '管理信息系统', '审计学', '概率论', '服务管理学', '高级服务管理学', '数学分析', '量子力学', '热力学与统计物理', '大学物理实验', '文科物理', '近代物理实验', '量子力学', '大学物理实验', '近代物理实验', '热力学与统计物理', '文科物理（理论与实验）', '谱学导论', '物理化学', '谱学导论', '物理化学', '遗传学', '数据库新技术', '商务智能', '高级Web技术', '面向服务的业务流程管理', '毛泽东思想、邓小平理论和“三个代表”重要思想概论', '毛泽东思想和中国特色社会主义理论体系概论', '医学遗传学', '医学遗传学', '局部解剖学', '局部解剖学', '法医学', '法医学', '医学导论', '内科学', '儿科学', '儿科学', '耳鼻咽喉科学', '耳鼻咽喉科学', '妇产科学', '肿瘤学概论', '肿瘤学概论', '预防医学', '预防医学', '药理学', '药理学', '健康评估']], ['科研机构', ['国家重点实验室', '“985工程”科技创新平台', '“985工程”哲学社会科学创新基地', '教育部人文社会科学重点研究基地', '教育部重点实验室', '教育部工程研究中心', '卫生部重点实验室', '总后卫生部重点实验室', '上海市重点实验室', '上海工程研究中心']], ['两院院士', ['院士姓名', '干福熹', '胡和生', '沈自尹', '贺福初', '洪家兴', '江明', '穆穆', '金亚秋', '徐国良', '汤钊猷', '陈灏珠', '周良辅']], ['历任校长', ['马相伯', '严复', '夏敬观', '高凤谦', '李登辉', '唐路园', '郭任远', '钱新之', '吴南轩', '章益']], ['上海市重点学科', ['西方经济学', '民商法学', '国外马克思主义', '中国现当代文学', '英语语言文学', '新闻学', '原子与分子物理', '无机化学', '分析化学', '生物化学与分子生物学']], ['现任领导', ['党委书记', '党委副书记', '党委副书记、校长', '常务副校长', '副校长']], ['上海市医学重点学科', ['复旦大学附属肿瘤医院', '复旦大学附属儿科医院', '复旦大学附属华山医院、上海市公共卫生中心', '复旦大学附属眼耳鼻喉科医院', '复旦大学附属华山医院', '复旦大学附属华山医院', '复旦大学附属中山医院', '复旦大学附属妇产科医院', '复旦大学附属中山医院']], ['教育部来华留学英语授课品牌课程', ['全球化下的中国文化与社会', '能源与环境', '普通化学', '旅游市场研究', '免疫学', '微生物学', '先秦儒家与法家', '中国公共行政', '中国背景中的社会研究', '国际商务的演进', '中国语言与文化', '中国社会保障体系及其改革']]]

print(api.GetEntInvTriples('许宁生'))
# [['i现任校长', '复旦大学'], ['i致词人', '珠三角改革发展研究院'], ['i副校长', '中山大学莱恩功能材料研究所']]

print(api.GetEntClicks('周杰伦'))
# {'周杰伦': 72638580}
print(api.GetEntClicks(['周杰伦', '方文山']))
# {'周杰伦': 72638580, '方文山': 9010477}

print(api.IsEnt(['周杰伦', '周3杰伦']))
# {'周杰伦': True, '周3杰伦': False}

print(api.GetEntConcepts('周杰伦'))
# ['人物', '演员', '娱乐人物', '歌手', '音乐人物', '导演', '企业家', '编剧', '制作人', '音乐人']
print(api.GetEntsByConcept('歌手'))
# ['陈伟霆', '鹿晗', '周笔畅', '黄子韬', '张艺兴', '易烊千玺', '赵丽颖', '杨幂', '霍建华（中国台湾男演员）', '宋茜', '杨洋（中国内地90后男演员）', '苍井空（日本av女演员）', '刘德华（中国香港男演员、歌手、词作人）', '李易峰', '李敏镐', '范冰冰', '吴亦凡', '周杰伦', '周杰伦（华语流行男歌手）', '迪丽热巴', '王俊凯（TFBOYS队长）', '王俊凯（tfboys队长）', '乔任梁（中国内地男歌手、演员）', '乔任梁', '刘亦菲（华语影视女演员、歌手）', '王源（tfboys成员）', '王源（TFBOYS成员）', 'EXO（韩国男子演唱团体）', 'tfboys', '刘涛（中国内地女演员）', '宋仲基', '钟汉良', '林心如', '杨紫', '张翰（中国大陆男演员）', '张馨予（江苏籍女演员）', '柳岩', '黄晓明（中国内地男演员）', '菜花甜妈', '张国荣（华语男歌手、演员、音乐人）', '张国荣（华语歌手、演员、音乐人）', '刘恺威', '张杰（中国四川籍男歌手）', '张杰（中国内地流行男歌手）', '陈乔恩', '成龙（中国香港演员、导演）', '林允儿', '林志颖', '孙俪', '陈学冬']

print(api.GetEntTriples('周杰伦'))
# [['中文名', '周杰伦'], ['外文名称', 'Jay Chou'], ['别名', '周董'], ['国籍', '中国'], ['民族', '汉族'], ['星座', '摩羯座'], ['血型', 'O型'], ['身高', '175cm'], ['出生地', '台湾省新北市'], ['出生日期', '1979年01月18日'], ['职业', '歌手'], ['职业', '音乐人'], ['职业', '制作人'], ['职业', '导演'], ['职业', '商人'], ['毕业院校', '淡江中学'], ['经纪公司', '杰威尔音乐有限公司'], ['代表作品', '龙卷风'], ['代表作品', '简单爱'], ['代表作品', '双截棍'], ['代表作品', '七里香'], ['代表作品', '头文字D'], ['代表作品', '不能说的秘密'], ['代表作品', '青花瓷'], ['代表作品', '稻香'], ['代表作品', '逆战'], ['代表作品', '天台'], ['代表作品', '告白气球'], ['主要成就', '获得十五座金曲奖'], ['主要成就', '两届台湾金曲奖最佳国语男歌手'], ['主要成就', '四届世界音乐大奖最畅销中华区艺人'], ['主要成就', '入选美国CNN亚洲25位最具影响力人物'], ['主要成就', '《Fast Company》全球百大创意人物'], ['CATEGORY_ZH', '音乐作品'], ['CATEGORY_ZH', '音乐人物'], ['CATEGORY_ZH', '音乐'], ['CATEGORY_ZH', '编剧'], ['CATEGORY_ZH', '演员'], ['CATEGORY_ZH', '歌手'], ['CATEGORY_ZH', '导演'], ['CATEGORY_ZH', '娱乐人物'], ['CATEGORY_ZH', '制作人'], ['CATEGORY_ZH', '人物'], ['DESC', '周杰伦（Jay Chou），1979年1月18日出生于台湾省新北市，中国台湾流行乐男歌手、音乐人、演员、导演、编剧、监制、商人。\n2000年发行首张个人专辑《Jay》。2001年发行的专辑《范特西》奠定其融合中西方音乐的风格。2002年举行“The One”世界巡回演唱会。2003年成为美国《时代周刊》封面人物。2004年获得世界音乐大奖中国区最畅销艺人奖。2005年凭借动作片《头文字D》获得台湾电影金马奖、香港电影金像奖最佳新人奖。2006年起连续三年获得世界音乐大奖中国区最畅销艺人奖。2007年自编自导的文艺片《不能说的秘密》获得台湾电影金马奖年度台湾杰出电影奖。\n2008年凭借歌曲《青花瓷》获得第19届金曲奖最佳作曲人奖。2009年入选美国CNN评出的“25位亚洲最具影响力的人物”；同年凭借专辑《魔杰座》获得第20届金曲奖最佳国语男歌手奖。2010年入选美国《Fast Company》评出的“全球百大创意人物”。2011年凭借专辑《跨时代》再度获得金曲奖最佳国语男歌手奖，并且第4次获得金曲奖最佳国语专辑奖；同年主演好莱坞电影《青蜂侠》。2012年登福布斯中国名人榜榜首。2014年发行华语乐坛首张数字音乐专辑《哎呦，不错哦》。2018年举行“地表最强2世界巡回演唱会”。\n演艺事业外，他还涉足商业、设计等领域。2007年成立杰威尔有限公司。2011年担任华硕笔电设计师并入股香港文化传信集团。\n周杰伦热心公益慈善，多次向中国内地灾区捐款捐物。2008年捐款援建希望小学。2014年担任中国禁毒宣传形象大使。'], ['年龄', '39岁']]
print(api.GetEntTriplesMulti(['周杰伦', '复旦大学']))
# {'周杰伦': [['中文名', '周杰伦'], ['外文名称', 'Jay Chou'], ['别名', '周董'], ['国籍', '中国'], ['民族', '汉族'], ['星座', '摩羯座'], ['血型', 'O型'], ['身高', '175cm'], ['出生地', '台湾省新北市'], ['出生日期', '1979年01月18日'], ['职业', '歌手'], ['职业', '音乐人'], ['职业', '制作人'], ['职业', '导演'], ['职业', '商人'], ['毕业院校', '淡江中学'], ['经纪公司', '杰威尔音乐有限公司'], ['代表作品', '龙卷风'], ['代表作品', '简单爱'], ['代表作品', '双截棍'], ['代表作品', '七里香'], ['代表作品', '头文字D'], ['代表作品', '不能说的秘密'], ['代表作品', '青花瓷'], ['代表作品', '稻香'], ['代表作品', '逆战'], ['代表作品', '天台'], ['代表作品', '告白气球'], ['主要成就', '获得十五座金曲奖'], ['主要成就', '两届台湾金曲奖最佳国语男歌手'], ['主要成就', '四届世界音乐大奖最畅销中华区艺人'], ['主要成就', '入选美国CNN亚洲25位最具影响力人物'], ['主要成就', '《Fast Company》全球百大创意人物'], ['年龄', '39岁']], 
#  '复旦大学': [['中文名', '复旦大学'], ['英文名称', 'Fudan University'], ['简称', '复旦·FUDAN'], ['创办时间', '1905年09月14日'], ['类别', '公立大学'], ['学校类型', '综合'], ['属性', '985工程（1999年）'], ['属性', '211工程（1994年）'], ['属性', '九校联盟（2009年）'], ['属性', '双一流（世界一流大学建设高校）'], ['属性', '111计划（2006年）'], ['所属地区', '中国·上海'], ['现任校长', '许宁生'], ['知名校友', '李岚清'], ['知名校友', '王沪宁'], ['知名校友', '韩正'], ['知名校友', '朱民'], ['知名校友', '李源潮'], ['知名校友', '竺可桢'], ['知名校友', '于右任'], ['知名校友', '邵力子'], ['主管部门', '中华人民共和国教育部'], ['硕士点', '243（含41个一级学科）个'], ['博士点', '博士专业学位授权点2个个'], ['博士后流动站', '35 个'], ['校训', '博学而笃志'], ['校训', '切问而近思'], ['校歌', '复旦大学校歌'], ['专职院士', '中国科学院院士 21人'], ['专职院士', '中国工程院院士 5人'], ['主要院系', '中国语言文学系、哲学学院、历史学系、旅游学系、文物和博物馆学系、外国语言文学学院等'], ['国家重点学科', '一级学科 11 个，二级学科 19个'], ['学校地址', '上海市杨浦区邯郸路220号'], ['学校代码', '10246'], ['主要奖项', '全国优秀博士论文55篇（截至2012年）'], ['校庆日', '5月27日（上海解放纪念日）'], ['学校官网', 'http://www.fudan.edu.cn']]
#  }
