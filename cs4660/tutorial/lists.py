"""Lists defines simple list related operations"""

def get_first_item(li):
    return li[0]
    """Return the first item from the list"""
    

def get_last_item(li):
    
    return li[-1]
    

def get_second_and_third_items(li):
    
    return li[1:3]
    

def get_sum(li):
    return sum(li)
    

def get_avg(li):
    list_sum = get_sum(li)
    list_len = len(li)
    return list_sum/list_len