if __name__ == '__main__':
    name_list=[]
    score_list=[]
    record_list=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        record_list.append([name,score])
        name_list.append(name)
        score_list.append(score)
    score_list=list(set(score_list))
    score_list.sort()
    sec_low=score_list[1]
    out=[i[0] for i in record_list if sec_low==i[1]]
    out.sort()
    for k in out:
        print(k)