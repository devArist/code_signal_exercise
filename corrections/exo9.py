def allLongestStrings(inputArray):
    array = []
    
    if len(inputArray) == 1:
        array.append(inputArray[0])
    else:
        length = [len(l) for l in inputArray]
        max1 = max(length)
        val1 = [val for val in inputArray if len(val) == max1]
        
        array += val1  
    
    return array