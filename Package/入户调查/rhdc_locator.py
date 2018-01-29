# -*- coding: utf-8 -*-

#按合同号查询
rhdc_hthcx_xpath = 'xpath=//*[@id="contractNo"]'

#按借款人查询
rhdc_jkrcx_xpath = 'xpath=//*[@id="clientName"]'

#按分公司查询
rhdc_fgscx_xpath1 = 'xpath=/html/body/div[3]/div[2]/div/div[2]/div/div/div/div/div[1]/div[1]/div[3]/div/div/a/span'
rhdc_fgscx_xpath2 = 'xpath=/html/body/div[3]/div[2]/div/div[2]/div/div/div/div/div[1]/div[1]/div[3]/div/div/div/div/input'

#查询
rhdc_cx_css = 'css=.btn-info'

#入户调查
rhdc_rhdc_js = '$(".btn-yellow").click()'


#居住地址
rhdc_houseProvince_xpath = '//*[@id="houseProvince"]'
rhdc_houseCity_xpath = '//*[@id="houseCity"]'
rhdc_houseConty_xpath = '//*[@id="houseConty"]'
rhdc_houseAddress_xpath = 'xpath=//*[@id="houseAddress"]'

#房屋性质
rhdc_houseNature_xpath = '//*[@id="houseNature"]'
#房屋面积
rhdc_houseArea_xpath = 'xpath=//*[@id="houseArea"]'
#装修情况
rhdc_houseRenovation_xpath = '//*[@id="houseRenovation"]'
#同住人数
rhdc_housePersonNumber_xpath = 'xpath=//*[@id="housePersonNumber"]'



#是否被允许进入室内
rhdc_houseEnter_xpath = 'xpath=//*[@id="verifyForm"]/table/tbody/tr[7]/td[2]/label'
#是否接触到其他人(亲属、邻居、同事)
rhdc_houseContactPerson_xpath = 'xpath=//*[@id="verifyForm"]/table/tbody/tr[7]/td[4]/label'
#发现申请人有不良嗜好(赌博、吸毒等)
rhdc_houseHabit_xpath = 'xpath=//*[@id="verifyForm"]/table/tbody/tr[8]/td[2]/label'
#是否发现申请人有债务纠纷或被追债
rhdc_houseDebt_xpath = 'xpath=//*[@id="verifyForm"]/table/tbody/tr[8]/td[4]/label'
#是否发现申请人有直系亲属处于重病就医中
rhdc_houseIll_xpath = 'xpath=//*[@id="verifyForm"]/table/tbody/tr[9]/td[2]/label'
#阳台是否挂有换洗衣物
rhdc_houseDress_xpath = 'xpath=//*[@id="verifyForm"]/table/tbody/tr[9]/td[4]/label'
#厨房是否正常使用中
rhdc_houseKitchen_xpath = 'xpath=//*[@id="verifyForm"]/table/tbody/tr[10]/td[2]/label'
#桌子、茶几上是否有日用品	
rhdc_houseSupplies_xpath = 'xpath=//*[@id="verifyForm"]/table/tbody/tr[10]/td[4]/label'
#卫生间有无日常洗漱用品
rhdc_bathroom_xpath = 'xpath=//*[@id="verifyForm"]/table/tbody/tr[11]/td[2]/label'
#家中是否灰尘较多,无人居住痕迹较重
rhdc_houseDust_xpath = 'xpath=//*[@id="verifyForm"]/table/tbody/tr[11]/td[4]/label'



#单位名称
rhdc_companyName_xpath = 'xpath=//*[@id="companyName"]'
#单位性质
rhdc_companyNature_xpath = '//*[@id="companyNature"]'
#单位地址
rhdc_companyAddress_xpath = 'xpath=//*[@id="companyAddress"]'
#担任职务
rhdc_companyPosition_xpath = 'xpath=//*[@id="companyPosition"]'


#场地租金
rhdc_yardRent_xpath = 'xpath=//*[@id="yardRent"]'
#经营年数
rhdc_operationYear_xpath = 'xpath=//*[@id="operationYear"]'
#场地性质
rhdc_yardNature_xpath = 'xpath=//*[@id="yardNature"]'
#场地面积
rhdc_yardArea_xpath = 'xpath=//*[@id="yardArea"]'



#是否允许进入办公场所
rhdc_yardEnter_xpath = 'xpath=//*[@id="sy_tr2"]/td/table/tbody/tr[3]/td[2]/label'
#是否接触到其他人(同事、下属、上司)
rhdc_yardContactPerson_xpath = 'xpath=//*[@id="sy_tr2"]/td/table/tbody/tr[3]/td[4]/label'
#是否有独立办公室、工位
rhdc_yardAlonePlace_xpath = 'xpath=//*[@id="sy_tr2"]/td/table/tbody/tr[4]/td[2]/label'
#是否发现企业申请人有债务纠纷或被追债
rhdc_yardDebt_xpath = 'xpath=//*[@id="sy_tr2"]/td/table/tbody/tr[4]/td[4]/label'
#同事对申请人贷款是否知晓
rhdc_yardKnow_xpath = 'xpath=//*[@id="sy_tr2"]/td/table/tbody/tr[5]/td[2]/label'
#是否有库存
rhdc_yardStock_xpath = 'xpath=//*[@id="sy_tr2"]/td/table/tbody/tr[5]/td[4]/label'


#外访人
rhdc_wfr_xpath1 = 'xpath=/html/body/div[3]/div[2]/div/div[2]/div/div[1]/form/table/tbody/tr[17]/td[2]/div[1]/a/span'
rhdc_wfr_xpath2 = 'xpath=/html/body/div[3]/div[2]/div/div[2]/div/div[1]/form/table/tbody/tr[17]/td[2]/div[1]/div/div/input'

#外访日期
rhdc_visitDate_xpath = 'xpath=//*[@id="visitDate"]'
#外访意见
rhdc_opinion_xapth = 'xpath=//*[@id="opinion"]'


#外访表下一步
rhdc_wfb_xyb_xpath = 'xpath=//*[@id="home"]/div/button[1]'

#外访表返回
rhdc_wfb_fh_xpath = 'xpath=//*[@id="home"]/div/button[2]'


#外访表
rhdc_xzwfb_xpath = 'xpath=//*[@id="wfphotos"]'

#上传外访表
rhdc_scwfb_xpath = 'xpath=//*[@id="verifyForm"]/table/tbody/tr[1]/td[3]/button'


#入户调查附件确认上传
rhdc_fjqrsc_css = 'css=body > div.bootbox.modal.fade.in > div > div > div.modal-footer > button'



#提交
rhdc_tj_js = 'window.enterhouseType()'
#保存弹窗确认
rhdc_tcqr_css = 'css=.btn-myStyle'


