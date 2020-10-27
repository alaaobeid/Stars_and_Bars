#s is is a string of stars and bars
#startIndex is a list of Indices
#endIndex is a list of Indices
def StarsAndBars(s, startIndex, endIndex):
    # Write your code here
    results = 0
    final_result = []
    for i in range(0,len(startIndex)):
      s=s[startIndex[i]:endIndex[i]:1]
      for char in list(s):
        if char == "*":
          results=results+1
      get.append(results)
    return final_result
    
StarsAndBars('**|***|*', [1,1], [5,6])
