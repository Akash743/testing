import streamlit as st
import pandas as pd
import numpy as numpy




def main():

	#df = pd.DataFrame({'a':[1,2,5],'b':[2,7,9]})
	#st.dataframe(df)
	#df.to_csv('test.csv')
	df = pd.read_csv('test.csv',index_col=0)
	st.dataframe(df)
	x = st.number_input('enter')
	
	if st.button('submit'):
		df.loc[0,'a'] = x
		df.to_csv('test.csv')
	if st.button('Load'):

		df = pd.read_csv('test.csv',index_col=0)
		st.dataframe(df)







if __name__=='__main__':
	main()		