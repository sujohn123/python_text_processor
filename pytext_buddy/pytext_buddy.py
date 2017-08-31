import sys,re

class pytext_buddy:
    def __init__(self,filename):
        self.filename=filename

    def get_dict(self):
        regex='{(.*?)}'
        list=self.file_iterator(regex)
	newlist=[]
        for string in list:
	    newlist.append('{'+string+'}')
	return newlist

    def get_dates(self):
	regex='\d+-+\d+-+\d+|\d+/+\d+/+\d+'
        return self.file_iterator(regex)


    def file_iterator(self,regex):
	strall=''
        with open(self.filename,'r') as file:
	    for lines in file:
	        strall=strall+lines
	        list=re.findall(regex,strall)
	list= filter(lambda x : x != '', list)
        return list

    def get_file_slices(self,path,lines,no_of_files=0):
	with open(self.filename, 'r') as f_in:
            try:
            # open the first output file
		j=0
                f_out = open(path+self.filename.replace('.txt','')+'_0'+'.txt', 'w')
            # loop over all lines in the input file, and number them
                for i, line in enumerate(f_in):
                # every time the current line number can be divided by the
                # wanted number of lines, close the output file and open a
                # new one
                    if i % lines == 0:
                        f_out.close()
			if no_of_files-1==j:
			    break
                        f_out = open(path+self.filename.replace('.txt','')+"_"+str(i/lines+1)+'.txt', 'w')
                # write the line to the output file
                    f_out.write(line)
            finally:
            # close the last output file
                f_out.close()
		j+=1

