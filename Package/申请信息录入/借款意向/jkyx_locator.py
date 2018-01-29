# -*- coding: utf-8 -*-

#按合同号查询
sqxxlr_hthcx_xpath = 'xpath=//*[@id="contractNo"]'

#按借款人查询
sqxxlr_jkrcx_xpath = 'xpath=//*[@id="clientName"]'

#按分公司查询
sqxxlr_fgscx_xpath1 = 'xpath=/html/body/div[3]/div[2]/div/div[2]/div/div/div[1]/div/div[3]/div/div/a/span'
sqxxlr_fgscx_xpath2 = 'xpath=/html/body/div[3]/div[2]/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/input'

#搜索
sqxxlr_ss_css = 'css=button.btn-xs:nth-child(2)'

#刷新
sqxxlr_sx_css = 'css=button.btn-xs:nth-child(3)'

#重置
sqxxlr_cz_css = 'css=button.btn:nth-child(4)'

#申请信息录入
sqxxlr_sqxxlr_xpath = 'xpath=/html/body/div[3]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div[2]/div[2]/table/tbody/tr/td[8]/div/button[1]'

#客户放弃
sqxxlr_khfq_xpath = 'xpath=/html/body/div[3]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div[2]/div[2]/table/tbody/tr/td[8]/div/button[2]'
#客户放弃确认
sqxxlr_khfq_qr_js = 'window.giveUpSubmit()'

#拒绝
sqxxlr_jj_xpath = 'xpath=//*[@id="table"]/tbody/tr/td[8]/div/button[3]'
#拒绝理由其他
sqxxlr_jjlyqt_xpath = 'xpath=//*[@id="refuseReason"]'
#拒绝提交
sqxxlr_jj_tj_js = 'window.refuseMofeSubmit()'


#借款意向页面
jkyxym_xpath = 'xpath=//*[@id="intenntionLi"]/a'

#客户类型
jkyx_clientType_xpath = 'xpath=//*[@id="clientType"]'

#业务员姓名
jkyx_businessName_xpath1 = 'xpath=/html/body/div[1]/div[1]/form/table/tbody/tr[6]/td[2]/div[1]/a/span'
jkyx_businessName_xpath2 = 'xpath=/html/body/div[1]/div[1]/form/table/tbody/tr[6]/td[2]/div[1]/div/div/input'

#申请金额
jkyx_applyMoney_xpath = 'xpath=//*[@id="applyMoney"]'

#产品类型
jkyx_loanProduct_xpath = 'xpath=//*[@id="loanProduct"]'

#借款用途
jkyx_loanPurpose_xpath = '//*[@id="loanPurpose"]'

#借款期数
jkyx_loanTerms_xpath = 'xpath=//*[@id="loanTerms"]'


#暂存
jkyx_zc_xpath = 'xpath=//*[@id="tempSaveBtn1"]'

#暂存确认
jkyx_zcqr_xpath = 'xpath=/html/body/div[3]/div/div/div[2]/button'

#下一步
jkyx_xyb_xpath = 'xpath=//*[@id="loanIntenntionAddUI"]/div/button[2]'

#返回
jkyx_fh_xpath = 'xpath=//*[@id="loanIntenntionAddUI"]/div/button[3]'

