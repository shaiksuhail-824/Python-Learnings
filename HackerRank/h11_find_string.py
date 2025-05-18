def count_substring(string, sub_string):
    #f=string.find(sub_string)
    #return f
    str_l=len(string)
    sub_l=len(sub_string)
    count=0
    for i in range(str_l+1-sub_l):
        if(string[i:i+sub_l]==sub_string):
            count=count+1
    return count
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)