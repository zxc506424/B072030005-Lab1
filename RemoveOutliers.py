#!/usr/bin/env python
# coding: utf-8

# In[11]:


#定義一函數，即輸入數字n，可移除一陣列的n個極大值與n個極小值
def remove_outliers(remove_number): 
    original_data = []
    outlies_removed = []
    outliers = []
    middle =[]
    while remove_number != 0:
        input_value= (input("Enter a value (q or Q to quit):"))
        #如果輸入值不等於q和Q，把輸入值設為data，存入original_data的list中 
        if input_value != 'q' and input_value != 'Q':
            data=int(input_value)
            original_data.append(data)
            #將list元素由大到小排序
            original_data.sort()
    
        else:
            print('The original data',original_data)
        
            for i in original_data:
                #假設remove_number=2，則移除經排序後list最前面2個元素(front)及最後面2元素(behind)，中間剩餘的元素為 middle
                behind = original_data[-remove_number:]
                front = original_data[:remove_number] 
                middle = original_data[remove_number:-remove_number]
                #被移除元素(極值)
                outlies_removed = front+behind
            break
    print('The data with outliers removed:',middle)    
    print('The outliers:', outlies_removed)


# In[12]:


remove_number=int(input('Enter the number of smallest and largest values to remove:'))
remove_outliers(remove_number)


# In[ ]:




