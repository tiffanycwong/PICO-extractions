
# coding: utf-8

# In[4]:

import os


# In[14]:

# DEBUG VERSION
# fixes gold annotations to not index based on white space
def fix_gold_annotations_debug(abstract_path, gold_annotation_path):
    abs_file = open(abstract_path, 'r');
    text = abs_file.read()
    
    ann_file = open(gold_annotation_path, 'r');
    anns = ann_file.read()
    anns = anns.strip().split(' ')[1:]
    
#     print anns
    
    anns = [int(x) for x in anns]
#     print anns
    
    clean_path = abstract_path[:-4] + '_tokens.txt'
    clean_file = open(clean_path, 'r')
    clean_text = clean_file.read().replace(' ', '')
    
#     print text
#     print ' '
#     print clean_text
    
    new_anns = []
    
    for ann_index in anns: 
        white = text[0:ann_index].count(' ')
        white += text[0:ann_index].count('\n')
        white -= text[0:ann_index].count('"')
        new_anns.append(ann_index-white)
#     print ' '
    
#     print anns
#     print new_anns
    
    for i in range(0, len(anns), 2):
        old = text[anns[i]:anns[i+1]]
        new = clean_text[new_anns[i]:new_anns[i+1]]
        old = old.replace(' ', '')
        
        old = old.replace('"', "''").replace('\n', '');
        new = new.replace('``', "''").replace('\n', '')
        if not(old == new):
            print "abstract: ", abs_file
            print "original phrase length: ", len(old), ";  new length: ", len(new)
            print old
            print new
            print " "


# In[2]:

# abstract = 'PICO-annotations/batch5k/0074f5e102cf4409ac07f6209dd30144/9665186.txt'
# annpath = 'PICO-annotations/batch5k/0074f5e102cf4409ac07f6209dd30144/9665186_gold.ann'

# abstract = 'PICO-annotations/batch5k/017e0bd245aa46b0bf1737ba34a30b2e/2648816.txt'
# annpath ='PICO-annotations/batch5k/017e0bd245aa46b0bf1737ba34a30b2e/2648816_gold.ann'

# fix_gold_annotations_debug(abstract, annpath)


# In[67]:

# fixes gold annotations to not index based on white space
def fix_gold_annotations(abstract_path, gold_annotation_path):
    abs_file = open(abstract_path, 'r');
    text = abs_file.read()
    
    ann_file = open(gold_annotation_path, 'r');
    anns = ann_file.read()
    anns = anns.strip().split(' ')[1:]
        
    anns = [int(x) for x in anns]
    
    new_anns = []
    
    for ann_index in anns: 
        white = text[0:ann_index].count(' ')
        white += text[0:ann_index].count('\n')
        white -= text[0:ann_index].count('"')
        new_anns.append(ann_index-white)

    new_ann_path = gold_annotation_path[:-4] + '_2.ann'
    new_ann_file = open(new_ann_path, 'w');
    new_anns_str = [str(x) for x in new_anns]
    out = 'Participants ' + ' '.join(new_anns_str)
    new_ann_file.write(out)


# In[68]:


# abstract ='PICO-annotations/batch5k/287c157f63e44612bd3f036004df2111/22727707.txt'
# annpath ='PICO-annotations/batch5k/287c157f63e44612bd3f036004df2111/22727707_gold.ann'

# fix_gold_annotations(abstract, annpath)


# In[71]:

directory = 'PICO-annotations/batch5k'

# For each subdirectory
for subdir in os.listdir(directory):
    subdir_path = directory + '/' + subdir
    # print subdir_path
    
    # Not a directory
    if not os.path.isdir(subdir_path):
        continue
    
    # For each abstract in subdirectory
    for abstract in os.listdir(subdir_path):
        if (abstract.endswith('.txt')) and not (abstract.endswith('tokens.txt')):
            abstract_path = subdir_path + '/' + abstract; 
            # print abstract_path
            ann_path = abstract_path[0:-4] + '_gold.ann'
            fix_gold_annotations(abstract_path, ann_path)


# In[11]:


# # TEST
# directory = 'PICO-annotations/batch5k'

# # For each subdirectory
# for subdir in os.listdir(directory):
#     subdir_path = directory + '/' + subdir
#     # print subdir_path
    
#     # Not a directory
#     if not os.path.isdir(subdir_path):
#         continue
    
#     # For each abstract in subdirectory
#     for abstract in os.listdir(subdir_path):
#         if (abstract.endswith('.txt')) and not (abstract.endswith('tokens.txt')):
#             abstract_path = subdir_path + '/' + abstract; 
#             # print abstract_path
#             ann_path = abstract_path[0:-4] + '_gold.ann'
#             fix_gold_annotations_debug(abstract_path, ann_path)


# In[ ]:



