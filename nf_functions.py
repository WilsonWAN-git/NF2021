##use length to calculate the end posotion
def cal_end_number(s_number,q_length):
	e_number=s_number+q_length
	return int(e_number)


def return_option(q_code,qid,q_length):
	if q_code:
		file_path_option_list = 'nf_option_list.txt'
		with open(file_path_option_list) as file_object:
			lines = file_object.readlines()
			for line in lines:
				option_list=line.split('\t') # 
				#print(option_list)
				code=str(option_list[0])
				code=code.zfill(q_length)
				option=option_list[1]
				question=option_list[2]
				if str(q_code)==code and qid==question :
					return str(option)
				
def return_option_d(q_code,qid):
	if q_code:
		file_path_option_list = 'nf_option_list.txt'
		with open(file_path_option_list) as file_object:
			lines = file_object.readlines()
			for line in lines:
				option_list=line.split('\t') # 
				#print(option_list)
				code=str(option_list[0])
				option=option_list[1]
				question=option_list[2]
				if str(q_code)==code and qid==question :
					return str(option)
				
				
def return_record_d(q_order,data_file_path):
	
	records=[]  #define the records list
	order=q_order
	q_length = return_length(order)
	start_number=q_length['start_number']
	option_length=q_length['length']
	end_number = int(start_number+option_length)
	with open(data_file_path) as file_object:
		lines = file_object.readlines()
		for line in lines:
			record_id = line[0:8]+'|'+line[60:68]
			group_repeat_number=0
			for option_position in range(start_number,end_number):
				option=line[option_position:option_position+1]
				if option=='1':
					group_repeat_number=group_repeat_number+1
					
			q_record=''
			number=0
				#print(q_length)
			for option_position in range(start_number,start_number+option_length):
					option=line[option_position:option_position+1]
					if option=='1':
						number=number+1
						q_str=str(return_option_d(option_position,q_length['Q_ID']))
						q_record = q_record+'|'+ q_str 
						record = record_id+'|'+str(group_repeat_number)+'|'+\
					str(number)+ q_record
						records.append(record)
						q_record=''
	return records
		

				
def return_length(q_order):
	file_path_question_list = 'nf_question_list.txt'
	with open(file_path_question_list) as file_object:
		lines = file_object.readlines()
		for line in lines:
			question_list=line.split('\t')
			order = question_list[0]
			Q_ID=question_list[1]
			length=question_list[2]
			start_number=question_list[3]
			if str(q_order) == order :
				if start_number == '':
					question = {'length':int(length),'Q_ID':Q_ID}
				else:
					question = {'length':int(length),'Q_ID':Q_ID,'start_number':int(start_number)}
				return question



def return_record(data_file_path,repeat_start,repeat_end,step_number,start_number_ini,range_start,range_end):
	records=[]
	file_path_f = data_file_path
	with open(file_path_f) as file_object:
		lines = file_object.readlines()
		for line in lines:
			record_id = line[0:8]+'|'+line[60:68]
		
			group_repeat_number=line[repeat_start:repeat_end] ## repeat number
		
			if group_repeat_number !='  ':
				group_repeat_number=int(group_repeat_number)
			else:
				group_repeat_number = 0
			
		#print(group_repeat_number)
		#secssion 2 data
			for number in range(1,group_repeat_number+1):
				q_record=''
				#row_number=row_number+1
				start_number=(number-1)*step_number+start_number_ini
			
				for order in range(range_start,range_end):
					q_length = return_length(order)

					q_int=line[start_number:cal_end_number(start_number,q_length['length'])]
				
					q_str=str(return_option(q_int,q_length['Q_ID'],q_length['length']))
					if q_str== 'None':
						q_str=q_int
						
					q_str=q_int+'|'+ q_str 
					start_number = start_number+int(q_length['length'])
					q_record = q_record+'|'+ q_str 

				record = record_id+'|'+str(group_repeat_number)+'|'+\
					str(number)+ q_record
				print(record)
				records.append(record)
	return records
