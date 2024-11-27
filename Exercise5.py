def sort_by_len_alphabeticalOrder(arrays):
  
   arrays.sort(key=lambda item: (len(item), item))
   return arrays
