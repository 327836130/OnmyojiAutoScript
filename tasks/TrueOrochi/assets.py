from module.atom.image import RuleImage
from module.atom.click import RuleClick
from module.atom.long_click import RuleLongClick
from module.atom.swipe import RuleSwipe
from module.atom.ocr import RuleOcr
from module.atom.list import RuleList

# This file was automatically generated by module/dev_tools/assets_extract.py.
# Don't modify it manually.
class TrueOrochiAssets: 


	# Click Rule Assets
	# description 
	C_ST_GREEN_1 = RuleClick(roi_front=(210,395,46,66), roi_back=(210,395,46,66), name="st_green_1")
	# description 
	C_ST_GREEN_2 = RuleClick(roi_front=(291,481,46,63), roi_back=(291,481,46,63), name="st_green_2")
	# description 
	C_ST_GREEN_3 = RuleClick(roi_front=(459,426,53,59), roi_back=(459,426,53,59), name="st_green_3")
	# description 
	C_ST_GREEN_4 = RuleClick(roi_front=(687,391,43,57), roi_back=(687,391,43,57), name="st_green_4")
	# description 
	C_ST_GREEN_5 = RuleClick(roi_front=(814,490,41,60), roi_back=(814,490,41,60), name="st_green_5")
	# description 
	C_ST_GREEN_6 = RuleClick(roi_front=(921,386,48,59), roi_back=(921,386,48,59), name="st_green_6")
	# description 
	C_ST_GREEN_7 = RuleClick(roi_front=(0,0,100,100), roi_back=(0,0,100,100), name="st_green_7")
	# description 
	C_ST_GREEN_MAIN = RuleClick(roi_front=(611,541,40,66), roi_back=(611,541,40,66), name="st_green_main")


	# Image Rule Assets
	# 出现真蛇 
	I_FIND_TS = RuleImage(roi_front=(1,613,100,93), roi_back=(1,613,100,93), threshold=0.8, method="Template matching", file="./tasks/TrueOrochi/st/st_find_ts.png")
	# 点击挑战60体力 
	I_ST_FIRE = RuleImage(roi_front=(960,485,100,100), roi_back=(960,485,100,100), threshold=0.8, method="Template matching", file="./tasks/TrueOrochi/st/st_st_fire.png")
	# 确认挑战 
	I_ST_FIRE_CONFIRM = RuleImage(roi_front=(671,406,176,53), roi_back=(671,406,176,53), threshold=0.8, method="Template matching", file="./tasks/TrueOrochi/st/st_st_fire_confirm.png")
	# 十个式神的准备 
	I_ST_FIRE_PREPARE = RuleImage(roi_front=(1118,548,100,100), roi_back=(1118,548,100,100), threshold=0.8, method="Template matching", file="./tasks/TrueOrochi/st/st_st_fire_prepare.png")
	# description 
	I_ST_AUTO_FALSE = RuleImage(roi_front=(1112,463,33,34), roi_back=(1112,463,33,34), threshold=0.8, method="Template matching", file="./tasks/TrueOrochi/st/st_st_auto_false.png")
	# description 
	I_ST_AUTO_TRUE = RuleImage(roi_front=(1112,461,34,37), roi_back=(1112,461,34,37), threshold=0.8, method="Template matching", file="./tasks/TrueOrochi/st/st_st_auto_true.png")
	# description 
	I_ST_GREEN_1 = RuleImage(roi_front=(209,216,22,48), roi_back=(188,192,69,87), threshold=0.8, method="Template matching", file="./tasks/TrueOrochi/st/st_st_green_1.png")
	# description 
	I_ST_GREEN_2 = RuleImage(roi_front=(294,311,21,46), roi_back=(273,282,70,91), threshold=0.8, method="Template matching", file="./tasks/TrueOrochi/st/st_st_green_2.png")
	# description 
	I_ST_GREEN_3 = RuleImage(roi_front=(473,269,21,49), roi_back=(457,245,56,89), threshold=0.8, method="Template matching", file="./tasks/TrueOrochi/st/st_st_green_3.png")
	# description 
	I_ST_GREEN_4 = RuleImage(roi_front=(690,258,27,49), roi_back=(662,235,83,83), threshold=0.8, method="Template matching", file="./tasks/TrueOrochi/st/st_st_green_4.png")
	# description 
	I_ST_GREEN_5 = RuleImage(roi_front=(841,335,26,44), roi_back=(814,302,100,100), threshold=0.8, method="Template matching", file="./tasks/TrueOrochi/st/st_st_green_5.png")
	# description 
	I_ST_GREEN_6 = RuleImage(roi_front=(930,247,24,47), roi_back=(894,224,100,100), threshold=0.8, method="Template matching", file="./tasks/TrueOrochi/st/st_st_green_6.png")


