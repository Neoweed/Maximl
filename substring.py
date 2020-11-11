def distinct(arr):
	count=0
	#arr=arr1.split()
	n=len(arr)
	#print(arr)
	for x in arr:
		arr=arr.replace(x,'',1)
		if x not in arr:
			count = count+1

	return count
input_arr=input('Input:')
n=len(input_arr)
#print(n)
num_dist=0
len_substr=0
sub_arr_list=[]
len_arr_list=[]
for i in range(n):
	for j in range(i+1,n+1):
		sub_arr_list.append(input_arr[i:j])
		#len_arr_list.append(len(input_arr[i:j]))
for i in range(len(sub_arr_list)):
	temp_dist=distinct(sub_arr_list[i])
	if(temp_dist>num_dist):
		num_dist=temp_dist
		len_substr=len(sub_arr_list[i])
		#print(temp_dist)
		#print(len_substr)
	elif(temp_dist==num_dist):
		temp_len=len(sub_arr_list[i])
		if(temp_len<len_substr):
			len_substr=temp_len
			#print(temp_len)
#print(num_dist)
print(len_substr)
