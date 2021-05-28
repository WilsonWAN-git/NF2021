
123
from nf_functions import cal_end_number,return_option,return_length

file_path = 'NFDC_2020_Final.dat'

row_number=0
number_question=['Q4','Q8_1','Q6'] 
records=[]  #define the records list

with open(file_path) as file_object:
	lines = file_object.readlines()
	for line in lines:
		record_id = line[0:8]+'|'+line[60:68]
		group_one_repeat_number=int(line[84:86])  ## repeat number

		#secssion 1 data
		for number in range(1,group_one_repeat_number+1):
			q_record=''
			row_number=row_number+1 ##Count raw number
			##Position of every question
			start_number=(number-1)*33+86
			for order in range(1,19):
				q_length = return_length(order)
				#print(q_length)
				q_int=line[start_number:cal_end_number(start_number,q_length['length'])]
				#print(q_int)
				q_str=str(return_option(q_int,q_length['Q_ID'],q_length['length']))
				
				if q_length['Q_ID'] in number_question:
				#if q_int.strip()!='' and q_str== 'None':
					q_str=q_int
				else :
					if q_str== 'None':
						q_str=''
					q_str=q_int+'|'+ q_str 
				start_number = start_number+int(q_length['length'])
				q_record = q_record+'|'+ q_str 

			#read Q9 data
			start_number_q9=(number-1)*9+4999
			#print(start_number_q9)
			for order in range(52,55):
				q_length_q9 = return_length(order)
				#print(q_length_q9)
				#print(q_length_q9['length'])
				q_int_q9=line[start_number_q9:cal_end_number(start_number_q9,q_length_q9['length'])]
				q_str_q9=str(return_option(q_int_q9,q_length_q9['Q_ID'],q_length_q9['length']))

				if q_str_q9== 'None':
						q_str_q9=''
				q_str_q9=q_int_q9.strip()+'|'+ q_str_q9

				start_number_q9 = start_number_q9+int(q_length_q9['length'])
				q_record = q_record+'|'+ q_str_q9

			#read E5 data
			start_number_e5=(number-1)*3+5359
			for order in range(56,59):
				q_length_e5 = return_length(order)

				q_int_e5=line[start_number_e5:cal_end_number(start_number_e5,q_length_e5['length'])]
				q_str_e5=str(return_option(q_int_e5,q_length_e5['Q_ID'],q_length_e5['length']))

				if q_str_e5== 'None':
						q_str_e5=''
				q_str_e5=q_int_e5.strip()+'|'+ q_str_e5

				start_number_e5 = start_number_e5+int(q_length_e5['length'])
				q_record = q_record+'|'+ q_str_e5

			
			##print(q_record)
			record = record_id+'|'+str(group_one_repeat_number)+'|'+\
					str(number)+ q_record
			print(record)
			records.append(record)
			
record_title='Interview_number|familycode|group_one_repeat_number|'\
				+'number|q_1_code|q_1|q_2_code|q_2|q_3_code|q_3|'\
				+'q_4|q_5_code|q_5|q_6|q_6_1_code|q_6_1|q_7_1_code|q_7_1|'\
				+'q_8_1|q_6_2_code|q_6_2|q_7_2_code|q_7_2|q_8_2|'\
				+'q_6_3_code|q_6_3|q_7_3_code|q_7_3|q_8_3|'\
				+'s_1_code|s_1|s_2_code|s_2|s_3_code|s_3|q_9_1_code|q_9_1|q_9_2_code|q_9_2|q_9_3_code|q_9_3|'\
				+'e_5_1_code|e_5_1|e_5_2_code|e_5_2|e_5_3_code|e_5_3'
with open('data_result/nf_result_2021_S1_test_20210526.txt', 'w') as file_object:
		file_object.write(record_title+'\n')      
		for record in records:
			file_object.write(record+'\n')
print(row_number)