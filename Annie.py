import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

#Cleaning data
df = pd.read_csv('./Resources/CandidateSummaryAction.csv')
df['tot_dis'] = df['net_ope_exp'].str.replace("$","").str.replace(",","").str.replace("(","-").str.replace(")","")
df['net_ope_exp'] = df['net_ope_exp'].str.replace("$","").str.replace(",","").str.replace("(","-").str.replace(")","")
df['net_con'] = df['net_con'].str.replace("$","").str.replace(",","").str.replace("(","-").str.replace(")","")
df['cas_on_han_beg_of_per']= df['cas_on_han_beg_of_per'].str.replace("$","").str.replace(",","").str.replace("(","-").str.replace(")","")
df['cas_on_han_clo_of_per']= df['cas_on_han_clo_of_per'].str.replace("$","").str.replace(",","").str.replace("(","-").str.replace(")","")
df['tot_loa']= df['tot_loa'].str.replace("$","").str.replace(",","").str.replace("(","-").str.replace(")","")
df['can_loa'] = df['can_loa'].str.replace("$","").str.replace(",","").str.replace("(","-").str.replace(")","")
df['ind_ite_con']=df['ind_ite_con'].str.replace("$","").str.replace(",","").str.replace("(","-").str.replace(")","")
df['ind_uni_con']=df['ind_uni_con'].str.replace("$","").str.replace(",","").str.replace("(","-").str.replace(")","")
df['ind_con']=df['ind_con'].str.replace("$","").str.replace(",","").str.replace("(","-").str.replace(")","")
