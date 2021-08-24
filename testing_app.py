import streamlit as st
import pandas as pd
import numpy as numpy
import schedule
import time
import date




def main():

	#df = pd.DataFrame({'a':[1,2,5],'b':[2,7,9]})
	#st.dataframe(df)
	#df.to_csv('test.csv')
	df = pd.read_csv('test.csv',index_col=0)
	st.dataframe(df)
	st.write(date.today())
	x = st.number_input('enter')
	def bedtime():
		df.loc[len(df),'a'] = "It is bed time go rest"

	def geeks():
		df.loc[len(df),'a'] =  "Every 10 mins and hour"

	# Task scheduling
	# After every 10mins geeks() is called. 
	schedule.every(3).minutes.do(geeks)

	# After every hour geeks() is called.
	schedule.every().hour.do(geeks)

	# Every day at 12am or 00:00 time bedtime() is called.
	schedule.every().day.at("00:00").do(bedtime)
	df.to_csv('test.csv')
	
	if st.button('submit'):
		df.loc[len(df),'a'] = x
		df.to_csv('test.csv')
	if st.button('Load'):

		df = pd.read_csv('test.csv',index_col=0)
		st.dataframe(df)







if __name__=='__main__':
	main()		
