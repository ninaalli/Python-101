def bubble_sort(data):
  idx = 0
  end_idx = len(data)-1
  while end_idx>0:
    idx=0
  while idx<end_idx:
    if val > data[idx+1]:
    data[idx],data[idx+1] = data[idx+1], data [idx]
    idx + = 1
    end_idx = 1
  print bubble_sort


use the name space


Bubble sort is defined within global namespace



def bubble_sort(data):
    end_idx = len(data)-1
    while end_idx > 0:
        curr_idx = 0
        while curr_idx < end_idx:
            if data[curr_idx] > data[curr_idx + 1]:
                data[curr_idx], data[curr_idx + 1] = data[curr_idx + 1], data[curr_idx]
            curr_idx += 1
        end_idx -= 1
    return data
