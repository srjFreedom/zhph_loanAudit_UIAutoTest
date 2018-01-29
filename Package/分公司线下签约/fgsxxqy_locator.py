# -*- coding: utf-8 -*-

#按合同编号查询
fgsxxqy_hth_xpath = 'xpath=//*[@id="contractNo"]'
#按借款人查询
fgsxxqy_jkr_xpath = 'xpath=//*[@id="clientName"]'
#查询
fgsxxqy_cx_xpath = 'xpath=/html/body/div[3]/div[2]/div/div[2]/div[1]/div/div/div/div[1]/div[2]/label/button'


#签约
fgsxxqy_qy_xpath = 'xpath=/html/body/div[3]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[1]/div[2]/div[2]/table/tbody/tr/td[11]/button[1]'

#重新签约
fgsxxqy_cxqy_xpath = 'xpath=/html/body/div[3]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[1]/div[2]/div[2]/table/tbody/tr/td[11]/button[2]'
#重新签约确认
fgsxxqy_cxqy_qr_xpath = 'xpath=/html/body/div[8]/div/div/div[2]/button[2]'

#回退
fgsxxqy_ht_xpath = 'xpath=/html/body/div[3]/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div[1]/div[2]/div[2]/table/tbody/tr/td[11]/button[3]'
#回退确认
fgsxxqy_ht_qr_xpath = 'xpath=/html/body/div[3]/div[2]/div/div[2]/div[2]/div/div/div[3]/button[2]'


#约定放款日期
fgsxxqy_grantDate_xpath = 'xpath=//*[@id="grantDate"]'

#开户银行
fgsxxqy_grantBank_xpath = 'xpath=//*[@id="grantBank"]'

#银行卡号
fgsxxqy_grantAccount_xpath = 'xpath=//*[@id="grantAccount"]'

#银行支行
fgsxxqy_grantBankDescribe_xpath = 'xpath=//*[@id="grantBankDescribe"]'

#开户城市
fgsxxqy_grantProvince_xpath = '//*[@id="grantProvince"]'
fgsxxqy_grantCity_xpath = '//*[@id="grantCity"]'
fgsxxqy_grantCounty_xpath = '//*[@id="grantCounty"]'


#注册授权
fgsxxqy_zcsq_xpath = 'xpath=//*[@id="authbtn"]'

#返回
fgsxxqy_fh_xpath = 'xpath=//*[@id="backbtn"]'

#拒绝
fgsxxqy_jj_database = '\'loanaudituser\',\'zytest1\',\'192.168.7.202:1521/xdtest\''
#拒绝备注
fgsxxqy_jj_jjbz_xpath = 'xpath=//*[@id="sign_refuse_remarks"]'
#拒绝提交
fgsxxqy_jj_jjtj_js= 'window.qyRefuseMofeSubmit()'
#拒绝登录密码
fgsxxqy_jj_jjdlmm_xpath = 'xpath=//*[@id="loginPassword"]'
#拒绝登录密码确认
fgsxxqy_jj_jjdlmmqr_xpath = 'xpath=//*[@id="uploadbtn"]'

#客户放弃
fgsxxqy_khfq_database = '\'loanaudituser\',\'zytest1\',\'192.168.7.202:1521/xdtest\''
#客户放弃提交
fgsxxqy_khfq_tj_js = 'window.qyGiveUpSubmit()'



