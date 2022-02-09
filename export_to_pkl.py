import function.get_data,function.pkl_input

title,keyword,abstract,content,reference = [],[],[],[],[]
allfields_list = function.get_data.get_mongodb_row("all_test")
raw_title,keyword,raw_abstract,raw_content,raw_reference = function.get_data.pre_data(title,keyword,abstract,content,reference,allfields_list)

# function.pkl_input.save_t0_pkl(raw_title,"./PKLData/raw_title.pkl")

# function.pkl_input.save_t0_pkl(raw_abstract,"./PKLData/raw_abstract.pkl")
# function.pkl_input.save_t0_pkl(raw_reference,"./PKLData/raw_reference.pkl")

new_keyword = []
for i in keyword:
    temp_list = []
    temp = i.split("、")
    for i in temp:
        temp_list.append(i)
    new_keyword.append(temp_list)
for i in new_keyword:
    print(i)
function.pkl_input.save_t0_pkl(new_keyword,"./PKLData/keyword.pkl")
# print(new_keyword)