# define a max heap class
class maxheap():
    def __init__(self, array):
        self.arr=array
        
    # pop the first (largest) element of the heap and return it, make the rest of heap a valid heap again
    def heappop(self):
        last=self.arr.pop()
        if self.arr:
            to_re=self.arr[0]
            self.arr[0]=last
            self._cor_viol(self.arr,0)
        else:
            to_re=last
        return to_re
    
    # build a max heap based on the given array of (key, value) tuple
    def heapify(self):
        length=len(self.arr)
        for i in range(length//2-1,-1,-1):
            self._cor_viol(self.arr, i)
    
    # when there is only one violation in the heap, how to correct this violation
    # this is used for heapify, heapify is to correct violation from the lowest layer that are not leaves
    # this is also used for pop, after poping the first element, the violation is at the begining, so correct it        
    def _cor_viol(self, heap, ind):
        length = len(heap)
        child=2*ind+1
        while child<length:
            child2=child+1
            if child2<length and self._isLarger(heap[child2], heap[child]):
                child=child2
            if self._isLarger(heap[ind], heap[child]):
                break
            heap[child], heap[ind] = heap[ind], heap[child]
            ind=child
            child=2*ind+1

    # define comparison of two elements of the given array, the element is a tuple (str, int)
    # compare int first, if equal, then compare str            
    def _isLarger(self, ele1, ele2):
        if ele1[1]>ele2[1]:
            return True
        elif ele1[1]==ele2[1] and ele1[0]<ele2[0]:
            return True
        return False

if __name__ == '__main__':
#    import timeit
    import sys
#    start_time = timeit.default_timer()
 
    input_name=sys.argv[1]
    # define 2 dictionaries to store occupation name and frequency and state name and frequency respectively
    occ_rec, pos_rec = {}, {}
    
    i_line=0
    h=open(input_name)
    for line in h:
        temp=line.strip().split(';')
        if i_line==0:
            col_num=len(temp)

            # find the column storing occupation information  
            if "SOC_NAME" in temp:
                ind_occ=temp.index("SOC_NAME")
            elif "LCA_CASE_SOC_NAME" in temp:
                ind_occ=temp.index("LCA_CASE_SOC_NAME")
            elif "JOB_TITLE" in temp:
                ind_occ=temp.index("JOB_TITLE")
            
            # find the column storing state information
            if "WORKSITE_STATE" in temp:
                ind_pos=temp.index("WORKSITE_STATE")
            elif "LCA_CASE_WORKLOC1_STATE" in temp:
                ind_pos=temp.index("LCA_CASE_WORKLOC1_STATE")
            elif "WORK_LOCATION_STATE1" in temp:
                ind_pos=temp.index("WORK_LOCATION_STATE1")
            elif "STATE_1" in temp:
                ind_pos=temp.index("STATE_1")

            # find the colum storing approval status
            if "APPROVAL_STATUS" in temp:
                ind_cer=temp.index("APPROVAL_STATUS")
            elif "STATUS" in temp:
                ind_cer=temp.index("STATUS")
            elif "CASE_STATUS" in temp:
                ind_cer=temp.index("CASE_STATUS")
            i_line+=1
            continue

        # skip invalid lines
        if len(temp)<col_num: continue
    
        # skip lines whose status are not "certified"
        if temp[ind_cer]!="CERTIFIED": continue

        i_line+=1
        # store occupation names and frequencies
        occ_rec[temp[ind_occ]]=occ_rec.get(temp[ind_occ],0)+1
        # store state names and frequencies
        pos_rec[temp[ind_pos]]=pos_rec.get(temp[ind_pos],0)+1

    h.close()
    i_line-=1

    # build a max heap based on the array of (key,val) pairs in occ_rec dictionary    
    heap_occ=maxheap(list(occ_rec.items()))
    heap_occ.heapify()    
    h_occ=open(sys.argv[-2],'w')
    h_occ.write('%s'%"TOP_OCCUPATIONS;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE\n")
  
    # itieratively pop the first(also largest) element of the heap and output it to the output file
    for i in range(min(10,len(heap_occ.arr))):
        occupation, freq=heap_occ.heappop()
        occupation=occupation.strip("\"")
        h_occ.write('%s;%d;%.1f%s\n'%(occupation,freq,float(freq)/i_line*100,'%'))
    h_occ.close()
    
    # build a max heap based on the array of (key,val) pairs in occ_pos dictionary
    heap_pos=maxheap(list(pos_rec.items()))
    heap_pos.heapify()    
    h_pos=open(sys.argv[-1],'w')
    h_pos.write('%s'%"TOP_STATES;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE\n")
  
    # itieratively pop the first(also largest) element of the heap and output it to the output file
    for i in range(min(10,len(heap_pos.arr))):
        state, freq=heap_pos.heappop()
        state=state.strip("\"")
        h_pos.write('%s;%d;%.1f%s\n'%(state,freq,float(freq)/i_line*100,'%'))
    h_pos.close()

# end_time = timeit.default_timer()
# print(('The training time = %.2fm' % ((end_time - start_time) )))
