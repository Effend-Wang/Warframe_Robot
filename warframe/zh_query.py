# 该文档为查询功能的中文翻译文档
# 文档包括：主题类、任务类、星球类、物品和材料类、MOD类、其它
# 文档末尾为翻译函数
# "":"",

# 翻译字典
def dictionary():
	data={
		# 主题类

		"Operation: Scarlet Spear": "行动代号：猩红之矛",
		"Fomorian Sabotage": "破坏巨人战舰",
		"Operation: Plague Star": "行动代号：瘟疫之星",
		"Razorback": "利刃豺狼",
		"Razorback Armada": "利刃豺狼舰队",
		"Operation: Buried Debts": "行动代号：雪藏的恩怨",
		"Thermia Fractures": "热美亚裂缝",

		# 任务类

		"FREE FLIGHT": "自由航行",
		"Assassination": "刺杀",
		"Capture": "捕获",
		"Defense": "防御",
		"Excavation": "挖掘",
		"Extermination": "歼灭",
		"Hijack": "劫持",
		"Hive Sabotage": "清巢",
		"Interception": "拦截",
		"Rescue": "救援",
		"Sabotage": "破坏",
		"Spy": "间谍",
		"Survival": "生存",
		"Assault": "强袭",
		"Disruption":"中断",
		"Crossfire": "多方交战",
		"Mobile Defense": "移动防御",
		"Sabotage the Enemy Supply Lines":"破坏Grineer的补给线",
		"Weaken the Grineer Foothold":"削弱Grineer的据点",
		"Find the Hidden Artifact":"找出遗失的器物",
		"Search and Rescue":"搜索并救援",
		"Cull the Enemy":"宰杀敌人",
		"Weapon Restriction: Pistol Only":"次要武器限定",
		"Reclaim the Stolen Artifact":"取回被偷的器物",
		"Energy Reduction":"能量上限减少",
		"Assassinate the Commander":"刺杀指挥官",
		"Spy Catcher":"间谍捕手",
		"Tactical Alert: Dog Days":"战术警报：三伏天",
		"Served Cold":"冷餐",
		"Bury Them":"埋葬他们",
		"Courier Ambush":"伏击信使",
		"Protect the Innocent":"保护无辜",
		"Financial Liberation":"财政解放",
		"Dog Boards":"貌似合法",
		"Corpus Siege":"Corpus围攻",
		"Grineer Offensive":"Grineer进攻",
		"Phorid Manifestation":"Phorid现形",
		"Infested Outbreak":"Infested爆发",
		"Sabotage Bounty":"破坏原型机",
		"Operational Intelligence":"行动情报",
		"Proof of Life":"存活证明",
		"Archaeology":"考古学",
		"Network Collapse":"网络崩溃",
		"Agent Down":"特工的下落",
		"Enemy Physical Enhancement: Impact":"敌人物理强化：冲击",
		"Enemy Elemental Enhancement: Blast":"敌人元素强化：爆炸",
		"Environmental Hazard: Electromagnetic Anomalies":"电磁异常",
		"Capture the Grineer Agent":"捕获Grineer特工",
		"Hunter-Killer":"猎人杀手",
		"Blood Relics":"血红遗物",
		"Trash Their Traps":"拆散陷阱",
		"Expressive":"善于表达之人",
		"Play 1 Emote":"使用1个表情动作",
		"Marksman":"老练射手",
		"Kill 40 Enemies with Headshots":"使用爆头击杀40名敌人",
		"Attractive":"吸引力",
		"Kill 150 Enemies with Magnetic damage":"使用磁力伤害击杀150名敌人",
		"Venus Fisher":"金星渔者",
		"Catch 6 Rare Servofish in the Orb Vallis":"捕获6个在奥布山谷中稀有的伺服鱼",
		"Executioner":"处刑者",
		"Kill 10 Enemies with Finishers":"处决击杀10名敌人",
		"Patron":"赞助者",
		"Donate to the Leverian":"为Leverian进行捐赠",
		"No Mercy":"不施怜悯",
		"Mercy Kill an Enemy":"对一名敌人施展怜悯之击",
		"Test Subject":"测试对象",
		"Complete 8 waves of Sanctuary Onslaught":"完成8个圣殿突袭的区域",
		"Hands Full":"枪不释手",
		"Complete a Mission with only a Primary Weapon equipped":"仅装备主要武器来完成一场任务",
		"Reactor":"核反应器",
		"Kill 150 Enemies with a Radiation Damage":"使用辐射伤害击杀150名敌人",
		"Deep Impact":"深度冲击",
		"Suspend 5 or more enemies in the air at once with a Heavy Slam Melee Attack":"使用一次重击震地近战攻击让5个或以上敌人同时浮空",
		"Unlock Relics":"解开遗物",
		"Saver":"储蓄者",
		"Pick up 15,000 Credits":"拾取15000现金",
		"Doppelganger":"二重身",
		"Deploy a Specter":"部署一个魅影",
		"Everything Old is New Again":"以旧换新",
		"Complete 3 Transmutations":"完成3次MOD转换",
		"Unlock 3 Relics":"解开3个遗物",
		"Sortie Specialist":"突击专家",
		"Sharing is Caring":"有毒共享",
		"Kill 150 Enemies with Viral Damage":"使用病毒伤害击杀150名敌人",
		"Energizing":"激励",
		"Pick up 20 Energy Orbs":"拾取20个能量球",
		"Poisoner":"投毒者",
		"Kill 150 Enemies with Toxin Damage":"使用毒素伤害击杀150名敌人",
		"Complete 1 Sorties":"完成1次突击",
		"Rescuer":"救援者",
		"Complete 3 Rescue missions":"完成3项救援任务",
		"Elite Explorer":"精英探险家",
		"Complete 8 Railjack Missions":"完成8场航道星舰任务",
		"Complete a Defense mission reaching at least Wave 20":"完成一场至少到20波的防御任务",
		"Distract and Divert":"分散与裂解",
		"Augmented Enemy Armor":"敌人护甲强化",
		"Environmental Hazard: Radiation Pockets":"辐射灾害",
		"Weapon Restriction: Assault Rifle Only":"突击步枪限定",
		"Enemy Physical Enhancement: Slash":"敌人物理强化：切割",
		"Enemy Elemental Enhancement: Corrosive":"敌人元素强化：腐蚀",
		"Enemy Physical Enhancement: Puncture":"敌人物理强化：穿刺",
		"Enemy Elemental Enhancement: Cold":"敌人元素强化：冰冻",
		"Seems Legit":"鹰嘴板",
		"Dirt Unit":"尘土部队",
		"Tax the Taxmen":"向税务官课税",
		"Capture Their Leader":"捕获他们的领袖",
		"Biohazard":"生化危害",
		"Kill 150 Enemies with Gas Damage":"使用毒气伤害击杀150名敌人",
		"Heavy Ordnance":"重型火炮",
		"Kill 500 enemies with an Archgun":"使用Archwing枪械击杀500名敌人",
		"Animator":"动像者",
		"Fully socket 3 Ayatan Sculptures":"完整插满3座阿耶檀识塑像",
		"Don't Fear The Reaper":"无需惧怕死神",
		"Complete 3 Kuva Siphon Missions":"完成3个赤毒虹吸器任务",
		"Vault Looter":"宝库劫者",
		"Unlock 4 Orokin Vaults":"解锁4个Orokin遗迹宝库",
		"Assassin":"刺客",
		"Complete 3 Assassination missions":"完成3项刺杀任务",
		"Complete a Survival mission reaching at least 30 minutes":"完成一场至少30分钟的生存任务",
		"Speedster":"极速战士",
		"Finish a Capture mission in less than 90 seconds":"在90秒内完成一个捕获任务",
		"Falling Star":"陨星",
		"Resource Theft":"资源搜掠",
		"Picket Duty":"岗哨职责",
		"Capture the New Grineer Commander":"捕获新任Grineer指挥官",
		"Capture the Grineer Commander":"捕获Grineer指挥官",
		"Enhanced Enemy Shields":"敌人护盾强化",
		"Eximus Stronghold":"卓越者大本营",

		# 星球类

		"Railjack": "航道星舰",
		"Ceres": "谷神星",
		"Dark Sector": "黑暗地带",
		"Derelict": "遗迹",
		"Earth": "地球",
		"Eris": "阋神星",
		"Europa": "欧罗巴",
		"Jupiter": "木星",
		"Mars": "火星",
		"Mercury": "水星",
		"Neptune": "海王星",
		"Orokin Derelict": "被遗弃的Orokin船只",
		"Orokin Void": "Orokin虚空",
		"Phobos": "火卫一",
		"Planets": "星球",
		"Pluto": "冥王星",
		"Saturn": "土星",
		"Sedna": "赛德娜",
		"Uranus": "天王星",
		"Venus": "金星",
		"Void": "虚空",
		"Lua": "月球",
		"Kuva Fortress": "赤毒要塞",
		"Cetus": "希图斯",
		"Quills": "夜羽",
		"Solaris United": "索拉里斯联盟",
		"Orb Vallis": "奥布山谷",
		"Vox Solaris": "索拉里斯之声",
		"Fortuna": "福尔图娜",
		"Veil Proxima":"面纱比邻星",
		"Ruse War Field":"RUSE战场",
		"Ganalen's Grave":"GANALEN之墓",
		"R-9 Cloud":"R-9星云",
		"H-2 Cloud":"H-2星云",
		"Gian Point":"GIAN点",
		"NSU Grid":"NSU区格",
		"Strata Relay":"Strata中继站",

		# 物品和材料类

		"Madurai Lens":"Madurai晶体",
		"2X Detonite Injector":"爆燃喷射器 X2",
		"300X Plastids":"生物质 X300",
		"5X Thermal Sludge":"热能软泥 X5",
		"15X Thermal Sludge":"热能软泥 X15",
		"15X Mytocardia Spore":"心肌菌孢子 X15",
		"5X Mytocardia Spore":"心肌菌孢子 X5",
		"2 Mutagen Mass":"突变原聚合物(2)",
		"Snipetron Vandal Receiver":"狙击特昂 破坏者 枪机",
		"Snipetron Vandal Blueprint":"狙击特昂 破坏者 蓝图",
		"Wraith Twin Vipers Link":"双子蝰蛇 亡魂 连接器",
		"Karak Wraith Barrel":"卡拉克 亡魂 枪管",
		"Sheev Blueprint":"希芙 蓝图",
		"Dera Vandal Stock":"德拉 破坏者 枪托",
		"Mutagen Mass":"突变原聚合物",
		"100X Oxium":"奥席金属 X100",
		"15X Iradite":"伊莱体 X15",
		"200X Oxium":"奥席金属 X200",
		"Strun Wraith Blueprint":"斯特朗 亡魂 蓝图",
		"Snipetron Vandal Stock":"狙击特昂 破坏者 枪托",
		"2X Fieldron":"电磁力场装置 X2",
		"10,000 Credits Cache":"10000现金匣",
		"Forma Blueprint": "Forma蓝图",
		"Stance Forma": "架势Forma",
		"Exilus Weapon Adapter": "武器特殊功能槽连接器",
		"Cubic Diodes": "立方二极管",
		"Pustrels": "寄生脓疱",
		"Copernics": "哥白尼能量单元",
		"Carbides": "碳化物",
		"Anomaly Shard": "异常碎片",
		"Dera Vandal Blueprint":"德拉破坏者 蓝图",
		"Latron Wraith Stock":"拉特昂亡魂 枪托",
		"Dex Dakra": "Dex达克拉双剑",
		"Dex Sybaris": "Dex席芭莉丝",
		"Dex Furis": "Dex盗贼双枪",
		"Legendary Core": "传说核心",
		"Fomorian Disruptor": "巨人战舰干扰器",
		"Orokin Reactor": "Orokin反应堆",
		"Orokin Catalyst": "Orokin催化剂",
		"Exilus Adapter": "特殊功能槽连接器",
		"Furax Wraith Right Gauntlet": "弗拉克斯 亡魂 右拳套",
        "Furax Wraith Left Gauntlet": "弗拉克斯 亡魂 左拳套",
        "Mutalist Alad V Nav Coordinate": "异融Alad V导航坐标",
        "3 Fieldron":"电磁力场装置(3)",
        "2X Morphics":"非晶态合金 X2",
		"2X Control Module":"控制模块 X2",
		"Lith K4 Relic":"古纪K4遗物",
		"2X Neural Sensors":"神经传感器 X2",
		"Redeemer Abysso Skin":"救赎者 深渊外观",
		"Hydroid's Relay Scene":"Hydroid的中继站场景",
		"3 Detonite Injector":"爆燃喷射器(3)",
		"Revenant Neuroptics BP":"Revenant头部神经光元 蓝图",
		"50000cr":"50000星币",
		"Buried Debts Emblem":"雪藏的恩怨徽章",
		"Buried Debts Sigil":"雪藏的恩怨纹章",
		"Sibear":"西伯利亚冰锤",
		"100X Cryotic":"永冻晶矿 X100",
		"1,500 Credits Cache":"1500现金匣",
		"50 Endo":"50内融核心",
		"15X Grokdrul":"葛克度X15",
		"Gara Chassis BP":"Gara机体 蓝图",
		"Energy Inversion":"能量转化",
		"200X Cryotic":"永冻晶矿 X200",
		"2,500 Credits Cache":"2500现金匣",
		"100 Endo":"100内融核心",
		"Gara Systems BP":"Gara系统 蓝图",
		"Vazarin Lens":"Vazarin晶体",
		"200 Endo":"200内融核心",
		"Gara Neuroptics BP":"Gara头部神经光元 蓝图",
		"Revenant Systems BP":"Revenant系统 蓝图",
		"Meso D5 Relic":"前纪D5遗物",
		"Zenurik Lens":"Zenurik晶体",
		"300 Endo":"300内融核心",
		"Cetus Wisp":"希图斯幽魂",
		"Revenant Chassis BP":"Revenant机体 蓝图",
		"Neo N12 Relic":"中纪N12遗物",
		"5X Breath Of The Eidolon":"夜灵之息 X5",
		"400 Endo":"400内融核心",
		"2X Cetus Wisp":"希图斯幽魂 X2",
		"300X Kuva":"赤毒 X300",
		"Axi S7 Relic":"后纪S7遗物",
		"Eidolon Lens BP":"夜灵晶体 蓝图",
		"Unairu Lens":"Unairu晶体",
		"200X Plastids":"生物质 X200",
		"15X Nistlepod":"尼蒐荚 X15",
		"2X Gallium":"镓 X2",
		"300X Circuits":"电路 X300",
		"2X Orokin Cell":"Orokin电池 X2",
		"Naramon Lens":"Naramon晶体",
		"100X Kuva":"赤毒 X100",
		"Furax Wraith BP":"弗拉克斯 亡魂 蓝图",
		"100X Plastids":"生物质 X100",
		"5X Gorgaricus Spore":"葛嘉里菌孢子 X5",
		"2X Training Debt-Bond":"培训债务债券 X2",
		"Garuda Chassis BP":"Garuda机体 蓝图",
		"5X Tepa Nodule":"缇帕瘤 X5",
		"3,000 Credits Cache":"3000现金匣",
		"15X Gorgaricus Spore":"葛嘉里菌孢子 X15",
		"200X Nano Spores":"纳米孢子 X200",
		"2X Shelter Debt-Bond":"庇护债务债券 X2",
		"Garuda Systems BP":"Garuda系统 蓝图",
		"300X Rubedo":"红化结晶 X300",
		"2X Medical Debt-Bond":"医疗债务债券 X2",
		"Garuda Neuroptics BP":"Garuda头部神经光元 蓝图",
		"200X Kuva":"赤毒 X200",
		"2X Mutagen Mass":"突变原聚合物 X2",
		"2X Advances Debt-Bond":"预支债务债券 X2",
		"Tellurium":"碲",
		"Neurodes":"神经元",
		"Orokin Cell":"Orokin电池",
		"2X Familial Debt-Bond":"家族债务债券 X2",
		"500X Kuva":"赤毒 X500",
		"Lotus Flowers":"Lotus幻纹",
		"Prisma Naberus":"棱晶 恶魔纳贝流士",
		"Liset Cydonia Skin":"Liset 塞东尼亚外观",
		"Prisma Kavat Glyph":"棱晶 库娃浮印",
		"Prisma Twin Gremlins":"棱晶 双子小精灵",
		"Ki'Teer Sugatra":"Ki'teer坠饰",
		"Ki'Teer Foros Chest Plate":"Ki'teer福罗斯胸甲",
		"Ki'Teer Foros Leg Plates":"Ki'teer福罗斯腿甲",
		"Ki'Teer Foros Shoulder Plates":"Ki'teer福罗斯肩甲",
		"Ki'Teer Kubrow Armor":"Ki'teer 库狛护甲",
		"Prisma Dual Cleavers":"棱晶 斩肉双刀",
		"Prisma Grinlok":"棱晶 葛恩火枪",
		"10x Ki'Teer Fireworks":"10X Ki'teer烟花",
		"Ki'Teer Kavat Armor":"Ki'teer库娃护甲",
		"3 Day Mod Drop Chance Booster":"3天 Mod掉落几率加成",
		"Ki'Teer Cornu Diadem":"Ki'teer角型头冠",
		"Limbo Immortal Skin":"Limbo不朽外观",
		"Prisma Hecate Syandana":"棱晶 朔月女神披饰",
		"Ki'Teer Domestik Drone":"Ki'teer内务无人机",
		"Sands Of Inaros Blueprint":"Inaros之沙",
		
		# MOD类

		"Enhanced Durability":"耐久强化",
		"Primed Shotgun Ammo Mutation":"霰弹枪弹药转换Prime",
		"Primed Pistol Ammo Mutation":"手枪弹药转换Prime",
		"Primed Rifle Ammo Mutation":"步枪弹药转换Prime",
		"Primed Continuity":"持久力Prime",
		"Grim Fury":"冷面狂怒",
		"Vitality":"生命力",
		"Streamline":"简化",
		"Redirection":"蓄能重划",
		"Steel Fiber":"钢铁纤维",
		"Charged Chamber":"蓄力装填",
		"Burning Wasp":"炙热黄蜂",
		"Gladiator Aegis":"角斗士 圣盾",
		"Augur Accord":"预言 协约",
		"Vigilante Supplies":"私法 补给",
		"Gladiator Rush":"角斗士 猛突",
		"Augur Reach":"预言 通灵",
		"Vigilante Offense":"私法 进攻",
		"Carving Mantis":"雕斩螳螂",
		"Augur Pact":"预言 契约",
		"Synth Fiber":"合成 纤维",
		"Synth Deconstruct":"合成 解构",
		"Synth Charge":"合成 充能",
		"Point Strike":"致命一击",
		"Synth Reflex":"合成 反射",
		"Vigilante Fervor":"私法 热诚",
		"Gladiator Vice":"角斗士 钳制",
		"Point Blank":"抵进射击",
		"Intensify":"聚精会神",
		"Augur Message":"预言 启示",
		"Vigilante Pursuit":"私法 追踪",
		"Gladiator Finesse":"角斗士 灵巧",
		"Twirling Spire":"回转尖峰",
		"Swooping Falcon":"猎鹰俯击",
		"Hornet Strike":"黄蜂蛰刺",
		"Stretch":"延伸",
		"Speed Trigger":"灵敏扳机",
		"Reaping Spiral":"收割螺旋",
		"Pressure Point":"压迫点",
		"Vigilante Armaments":"私法 军备",
		"Gladiator Might":"角斗士 威猛",
		"Gladiator Resolve":"角斗士 决心",
		"Vigilante Vigor":"私法 活力",
		"Augur Secrets":"预言 神密",
		"Tek Enhance": "技法 强化",
		"Tek Assault": "技法 猛袭",
		"Tek Collateral": "技法 连带",
		"Tek Gravity": "技法 引力",
		"Mecha Pulse": "机甲 脉冲",
		"Mecha Overdrive": "机甲 超载",
		"Mecha Recharge": "机甲 充能",
		"Mecha Empowered": "机甲 强化",
		"Augur Seeker": "预言 探求",
		"Pistol Riven Mod": "手枪裂罅MOD",
		"Shotgun Riven Mod": "霰弹枪裂罅MOD",
		"Melee Riven Mod": "近战裂罅MOD",
		"Rifle Riven Mod": "步枪裂罅MOD",
		"Kitgun Riven Mod": "组合枪裂罅MOD",
		"Strain Consume": "菌株 吸收",
		"Strain Infection": "菌株 感染",
		"Strain Fever": "菌株 热毒",
		"Strain Eruption": "菌株 爆裂",
		"Amalgam Shotgun Spazz":"并合 霰弹速射",
		"Amalgam Serration":"并合 膛线",
		"Amalgam Barrel Diffusion":"并合 弹头扩散",
		"Amalgam Organ Shatter":"并合 肢解",

		# 其它

		"Affinity Amp": "经验增幅",
		"Acolyte": "追随者",
		"acolyte": "追随者",
		"Torment": "折磨",
		"Malice": "怨恨",
		"Mania": "躁狂",
		"Angst": "焦虑",
		"Misery": "苦难",
		"Violence": "暴力"
	}

	return data

# 翻译到中文（输入的data为array或字符串类型）
def trans_zh(data):
	zh_data=dictionary()
	if isinstance(data,str):
		after_trans=zh_data.get(data)
		if after_trans==None:
			after_trans=data
	elif isinstance(data,list):
		data_length=len(data)
		after_trans=[]
		for i in range(data_length):
			trans=zh_data.get(data[i])
			if trans==None:
				trans=data[i]
			after_trans.append(trans)
	else:
		after_trans=data

	return after_trans