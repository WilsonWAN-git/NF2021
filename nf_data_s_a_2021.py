from nf_functions import cal_end_number,return_option,return_length

file_path = 'NFDC_2021_test_20210730.dat'

row_number=0


records=[]  #define the records list

with open(file_path) as file_object:
	lines = file_object.readlines()
	for line in lines:
		record_id = line[0:8]+'|'+line[60:68]
		#group_one_repeat_number=int(line[84:86])  
		#group_two_repeat_number=int(line[1726:1728]) ## repeat number
		group_two_repeat_number=1
			
		#secssion 2 data
		for number in range(1,group_two_repeat_number+1):
			q_record=''
			row_number=row_number+1
			start_number=(number-1)*8+1406
			
			for order in range(19,22):
				q_length = return_length(order)
				#print(q_length)
				q_int=line[start_number:cal_end_number(start_number,q_length['length'])]
				
				#print(q_int)
				q_str=str(return_option(q_int,q_length['Q_ID'],q_length['length']))
				if q_str== 'None':
					q_str=q_int
				q_str=q_int+'|'+ q_str 
				start_number = start_number+int(q_length['length'])
				q_record = q_record+'|'+ q_str 
				
			record = record_id+'|'+str(group_two_repeat_number)+'|'+\
					str(number)+ q_record
			print(record)
			records.append(record)
			
record_title='Interview_number|familycode|group_two_repeat_number|'\
				+'number|q_A1_code|q_A1|q_A2_code|q_A2|q_A3_code|q_A3'
with open('data_result/nf_result_2021_S_A_test_20210730.txt', 'w') as file_object:
		file_object.write(record_title+'\n')      
		for record in records:
			file_object.write(record+'\n')
			
print(row_number)