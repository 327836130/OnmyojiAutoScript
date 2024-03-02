from module.atom.image import RuleImage
from module.atom.click import RuleClick
from module.atom.long_click import RuleLongClick
from module.atom.swipe import RuleSwipe
from module.atom.ocr import RuleOcr
from module.atom.list import RuleList

# This file was automatically generated by ./dev_tools/assets_extract.py.
# Don't modify it manually.
class KekkaiActivationAssets: 


	# Click Rule Assets
	# 切换卡的种类 
	C_A_SELECT_CARD_LIST = RuleClick(roi_front=(352,99,172,53), roi_back=(352,99,172,53), name="a_select_card_list")
	# description 
	C_A_SELECT_AUTO = RuleClick(roi_front=(173,160,354,127), roi_back=(173,160,354,127), name="a_select_auto")


	# Ocr Rule Assets
	# 这张卡一共有多少小时 
	O_CARD_ALL_TIME = RuleOcr(roi=(926,262,95,31), area=(926,262,95,31), mode="Duration", method="Default", keyword="", name="card_all_time")


	# Swipe Rule Assets
	# description 
	S_CARDS_SWIPE = RuleSwipe(roi_front=(178,401,23,23), roi_back=(176,168,29,24), mode="default", name="cards_swipe")


	# Image Rule Assets
	# 斗鱼收获奖励4星 
	I_A_HARVEST_FISH4 = RuleImage(roi_front=(897,159,48,40), roi_back=(872,128,100,100), threshold=0.8, method="Template matching", file="./tasks/KekkaiActivation/a/a_a_harvest_fish4.png")
	# 一般的收获奖励 
	I_A_HARVEST_EXP = RuleImage(roi_front=(891,153,49,43), roi_back=(865,121,100,100), threshold=0.8, method="Template matching", file="./tasks/KekkaiActivation/a/a_a_harvest_exp.png")
	# "结界卡" 
	I_A_CARDS_REALM = RuleImage(roi_front=(0,0,100,100), roi_back=(0,0,100,100), threshold=0.8, method="Template matching", file="./tasks/KekkaiActivation/a/a_a_cards_realm.png")
	# description 
	I_A_CARD_ALL = RuleImage(roi_front=(357,175,167,59), roi_back=(357,175,167,59), threshold=0.9, method="Template matching", file="./tasks/KekkaiActivation/a/a_a_card_all.png")
	# description 
	I_A_CARD_KAIKO = RuleImage(roi_front=(355,237,169,62), roi_back=(355,237,169,62), threshold=0.9, method="Template matching", file="./tasks/KekkaiActivation/a/a_a_card_kaiko.png")
	# description 
	I_A_CARD_FISH = RuleImage(roi_front=(352,303,173,62), roi_back=(352,303,173,62), threshold=0.9, method="Template matching", file="./tasks/KekkaiActivation/a/a_a_card_fish.png")
	# description 
	I_A_CARD_ROOM = RuleImage(roi_front=(355,370,167,59), roi_back=(355,370,167,59), threshold=0.9, method="Template matching", file="./tasks/KekkaiActivation/a/a_a_card_room.png")
	# description 
	I_A_CARD_MOON = RuleImage(roi_front=(354,439,171,59), roi_back=(354,439,171,59), threshold=0.9, method="Template matching", file="./tasks/KekkaiActivation/a/a_a_card_moon.png")
	# 其他变异 
	I_A_CARD_OTHER = RuleImage(roi_front=(353,502,173,61), roi_back=(353,502,173,61), threshold=0.9, method="Template matching", file="./tasks/KekkaiActivation/a/a_a_card_other.png")
	# 邀请 
	I_A_INVITE = RuleImage(roi_front=(1045,559,100,100), roi_back=(1014,538,182,162), threshold=0.8, method="Template matching", file="./tasks/KekkaiActivation/a/a_a_invite.png")
	# 自动邀请 
	I_A_AUTO_INVITE = RuleImage(roi_front=(1071,456,53,51), roi_back=(1071,456,53,51), threshold=0.8, method="Template matching", file="./tasks/KekkaiActivation/a/a_a_auto_invite.png")
	# description 
	I_A_FRIEND_1 = RuleImage(roi_front=(590,573,64,73), roi_back=(590,573,64,73), threshold=0.8, method="Template matching", file="./tasks/KekkaiActivation/a/a_a_friend_1.png")
	# 位置2，空人的 
	I_A_FRIEND_2 = RuleImage(roi_front=(741,572,70,69), roi_back=(741,572,70,69), threshold=0.8, method="Template matching", file="./tasks/KekkaiActivation/a/a_a_friend_2.png")
	# 激活, 黄色的可以激活 
	I_A_ACTIVATE_YELLOW = RuleImage(roi_front=(1047,560,100,100), roi_back=(1047,560,100,100), threshold=0.8, method="Template matching", file="./tasks/KekkaiActivation/a/a_a_activate_yellow.png")
	# 激活, 灰色不可激活 
	I_A_ACTIVATE_GRAY = RuleImage(roi_front=(1046,556,100,100), roi_back=(1046,556,100,100), threshold=0.8, method="Template matching", file="./tasks/KekkaiActivation/a/a_a_activate_gray.png")
	# 空着的表示没有卡在里面 
	I_A_EMPTY = RuleImage(roi_front=(677,255,353,128), roi_back=(677,255,353,128), threshold=0.8, method="Template matching", file="./tasks/KekkaiActivation/a/a_a_empty.png")
	# description 
	I_A_CHECK_CARD = RuleImage(roi_front=(513,32,260,49), roi_back=(513,32,260,49), threshold=0.8, method="Template matching", file="./tasks/KekkaiActivation/a/a_a_check_card.png")
	# 太鼓4 
	I_A_HARVEST_KAIKO_4 = RuleImage(roi_front=(894,164,48,41), roi_back=(867,132,100,100), threshold=0.8, method="Template matching", file="./tasks/KekkaiActivation/a/a_a_harvest_kaiko_4.png")
	# description 
	I_A_HARVEST_KAIKO_3 = RuleImage(roi_front=(893,163,47,42), roi_back=(865,136,100,100), threshold=0.8, method="Template matching", file="./tasks/KekkaiActivation/a/a_a_harvest_kaiko_3.png")
	# 太鼓6 
	I_A_HARVEST_KAIKO_6 = RuleImage(roi_front=(898,160,45,38), roi_back=(868,129,100,100), threshold=0.7, method="Template matching", file="./tasks/KekkaiActivation/a/a_a_harvest_kaiko_6.png")
	# 斗鱼6 
	I_A_HARVEST_FISH_6 = RuleImage(roi_front=(898,159,45,38), roi_back=(869,131,100,100), threshold=0.7, method="Template matching", file="./tasks/KekkaiActivation/a/a_a_harvest_fish_6.png")
	# 太阴3 
	I_A_HARVEST_MOON_3 = RuleImage(roi_front=(897,159,46,40), roi_back=(869,127,100,100), threshold=0.7, method="Template matching", file="./tasks/KekkaiActivation/a/a_a_harvest_moon_3.png")
	# 卸下 
	I_A_DEMOUNT = RuleImage(roi_front=(939,575,55,47), roi_back=(903,551,107,91), threshold=0.8, method="Template matching", file="./tasks/KekkaiActivation/a/a_a_demount.png")


	# Image Rule Assets
	# description 
	I_CARDS_KAIKO_6 = RuleImage(roi_front=(193,204,89,73), roi_back=(169,148,130,501), threshold=0.8, method="Template matching", file="./tasks/KekkaiActivation/cards/cards_cards_kaiko_6.png")
	# description 
	I_CARDS_KAIKO_5 = RuleImage(roi_front=(191,345,88,58), roi_back=(172,162,126,488), threshold=0.8, method="Template matching", file="./tasks/KekkaiActivation/cards/cards_cards_kaiko_5.png")
	# description 
	I_CARDS_KAIKO_4 = RuleImage(roi_front=(192,354,90,22), roi_back=(179,165,116,482), threshold=0.85, method="Template matching", file="./tasks/KekkaiActivation/cards/cards_cards_kaiko_4.png")
	# description 
	I_CARDS_KAIKO_3 = RuleImage(roi_front=(192,187,89,66), roi_back=(183,169,109,474), threshold=0.8, method="Template matching", file="./tasks/KekkaiActivation/cards/cards_cards_kaiko_3.png")
	# description 
	I_CARDS_FISH_6 = RuleImage(roi_front=(193,183,87,91), roi_back=(178,169,110,474), threshold=0.8, method="Template matching", file="./tasks/KekkaiActivation/cards/cards_cards_fish_6.png")
	# description 
	I_CARDS_FISH_5 = RuleImage(roi_front=(192,358,88,21), roi_back=(176,155,105,492), threshold=0.9, method="Template matching", file="./tasks/KekkaiActivation/cards/cards_cards_fish_5.png")
	# description 
	I_CARDS_FISH_4 = RuleImage(roi_front=(192,409,87,21), roi_back=(176,175,118,473), threshold=0.9, method="Template matching", file="./tasks/KekkaiActivation/cards/cards_cards_fish_4.png")
	# description 
	I_CARDS_FISH_3 = RuleImage(roi_front=(193,314,86,64), roi_back=(188,164,100,482), threshold=0.8, method="Template matching", file="./tasks/KekkaiActivation/cards/cards_cards_fish_3.png")
	# description 
	I_CARDS_MOON_6 = RuleImage(roi_front=(189,186,89,88), roi_back=(183,167,100,480), threshold=0.8, method="Template matching", file="./tasks/KekkaiActivation/cards/cards_cards_moon_6.png")
	# description 
	I_CARDS_MOON_5 = RuleImage(roi_front=(190,398,91,22), roi_back=(183,163,100,489), threshold=0.9, method="Template matching", file="./tasks/KekkaiActivation/cards/cards_cards_moon_5.png")
	# description 
	I_CARDS_MOON_4 = RuleImage(roi_front=(190,426,91,21), roi_back=(186,144,100,491), threshold=0.9, method="Template matching", file="./tasks/KekkaiActivation/cards/cards_cards_moon_4.png")
	# description 
	I_CARDS_MOON_3 = RuleImage(roi_front=(189,366,92,22), roi_back=(181,153,107,495), threshold=0.9, method="Template matching", file="./tasks/KekkaiActivation/cards/cards_cards_moon_3.png")
	# description 
	I_CARDS_MOON_2 = RuleImage(roi_front=(189,355,91,60), roi_back=(180,162,108,484), threshold=0.8, method="Template matching", file="./tasks/KekkaiActivation/cards/cards_cards_moon_2.png")
	# description 
	I_CARDS_MOON_1 = RuleImage(roi_front=(190,430,93,74), roi_back=(173,156,123,492), threshold=0.8, method="Template matching", file="./tasks/KekkaiActivation/cards/cards_cards_moon_1.png")


