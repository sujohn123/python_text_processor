import re,csv,sys,simplejson as json,numpy as np,pandas as pd,ast
inter=[]

class pytext_buddy:
    def __init__(self,file):
        self.filename=file

    def get_dict(self):
        regex='{(.*?)}'
        list=self.file_iterator(regex)
	newlist=[]
        for string in list:
	    newlist.append('{'+string+'}')
	return newlist

    def get_json(self):
	regex='{(.*?)}'
        newstr=''
        list=self.file_iterator(regex)
        newlist=[]
        #sys.exit()
        for string in list:
            #print(type(json.loads('"{'+string+'}"')))
            newlist.append(ast.literal_eval('{'+string+'}'))

	#self.fetch_tags(["1"],self.filename)
	self.file_writerx(newlist,"hard")
        return "file has been created"

    def file_iterator(self,regex):
        strall=''
        with open(self.file,'r') as file:
            for lines in file:
                strall=strall+lines
                list=re.findall(regex,strall)
        list= filter(lambda x : x != '', list)
        return list

    def file_writerx(self,diction,filename):
	#print("This is file writer")
	#print(diction)
	#print(diction)
	df=pd.DataFrame()
	df=pd.DataFrame(diction)
	df.to_csv(filename+".csv",index=False)
	return


    def fetch_tags(self,tags,filename):
	"""
	Takes tags as list and filename as string
	Finds the dictionaries from the filename then further the tags in those dictionaries and then gives a csv file containing the
	tags as header of csv and their respective data in the respective lines
	"""
	str=''
	csv_file=''
	with open(self.file,"r") as jsfile:
	    for lines in jsfile:
		str=str+lines
	        #json_data=json.loads(str)
	        #return (type(json_data))
		#print(str)
		#sys.exit()
	#print(str)
	str=re.sub(r'\s+','',str) ## replacing all the spaces
	list=json.loads(str)
	#print(type(list))
	#print(list)
	#sys.exit()
	if isinstance(list,dict): # iF there is only one dictionary in the list then the dict has to be converted to list
	    list=[list]
	#sys.exit()
	#print(self.iterator(list,tags))
	#sys.exit()
	for tag in tags:
	    self.iterator(list,tag)

	if len(inter)==0:
	    return "Tag not found in the file"
	else:
	   # self.file_writer(self.iterator(list,tags),filename)
	    self.file_writer(inter,filename)
	    return (filename +".csv"+ " has been created")


    def iterator(self,list,tags):
        new_diction=[]
        #print(list)
	#print(type(list))
        for items in list:
            #print(items)
            #sys.exit()
            self.dictionary_iter(items,tags)
            #sys.exit()
        return

    def dictionary_iter(self,items,tags):
	#print(items)
	#print(type(items))
	#sys.exit()
        for k,v in items.items():
	    #print(v)
	    #sys.exit()
	    if isinstance(v,dict):
		#print(v)
		#sys,exit()
           	self.dictionary_iter(v,tags)
	    else:
		#print(k in tags)
		#print("I am here")
		#print(k,tags,v)
		if k in tags:
		    #print({k:v})
                    #if isinstance(v,list):
                    #    for items in v:
                        #new_diction.append({k:items})
		    #	    return {k:items}
                    #else:
                    #new_diction.append({k:v})
		    inter.append({k:v})
	return

    def file_writer(self,diction,filename):
	#print("This is file writer")
	#print(diction)
	#print(diction)
	df=pd.DataFrame()
	keys=pd.DataFrame(diction).columns.values
	for key in keys:
		diction_sep=[]
		for dic in diction:
            	    if dic.keys()==[key]:
                	diction_sep.append(dic)
		df[key]=(pd.DataFrame(diction_sep))
	df.to_csv(filename+".csv",index=False)
	return


    """
    def file_writer1(self,diction,filename):
	#print("This is file writer")
	#print(diction)
	diction_sep=[]
	#print(diction)
	print(type(pd.DataFrame(diction).columns.values))
	sys.exit()
	#sys.exit()
	for dic in diction:
	    if dic.keys()==['cty']:
		diction_sep.append(dic)
	#print(diction_sep)
	#sys.exit()
	keys=['cty','yrs']
	#print(keys[0])
	#sys.exit()
	    #print(key)
	    #sys.exit()
	with open(filename+'.csv', 'wb') as output_file:
	    dict_writer = csv.DictWriter(output_file, keys)
    	    dict_writer.writeheader()
	    for key in keys:
		diction_sep=[]
		for dic in diction:
            	    if dic.keys()==[key]:
                	diction_sep.append(dic)
                dict_writer.writerows(diction_sep)
		#sys.exit()
	return
    """

    def get_jsony(self):
        regex='{(.*?)}'
	newstr=''
        list=self.file_iterator(regex)
	newlist=[]
	#sys.exit()
        for string in list:
    	    #print(type(json.loads('"{'+string+'}"')))
	    newlist.append(ast.literal_eval('{'+string+'}'))
	return newlist

    def get_dates(self):
	regex='\d+-+\d+-+\d+|\d+/+\d+/+\d+'
        return self.file_iterator(regex)


    def file_iterator(self,regex):
	strall=''
        with open(self.file,'r') as file:
	    for lines in file:
	        strall=strall+lines
	        list=re.findall(regex,strall)
	list= filter(lambda x : x != '', list)
        return list

    def get_file_slices(self,path,lines,no_of_files=0):
	with open(self.file, 'r') as f_in:
            try:
            # open the first output file
		j=0
                f_out = open(path+self.file.replace('.txt','')+'_0'+'.txt', 'w')
            # loop over all lines in the input file, and number them
                for i, line in enumerate(f_in):
                # every time the current line number can be divided by the
                # wanted number of lines, close the output file and open a
                # new one
                    if i % lines == 0:
                        f_out.close()
			if no_of_files-1==j:
			    break
                        f_out = open(path+self.file.replace('.txt','')+"_"+str(i/lines+1)+'.txt', 'w')
                # write the line to the output file
                    f_out.write(line)
            finally:
            # close the last output file
                f_out.close()
		j+=1

