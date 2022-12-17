def multiply_polynomial(poly1:list,poly2:list) -> list:
    answer = []
    for count,x in enumerate(poly1):
        x_v  = [count,x]
        for count_2,y in enumerate(poly2):
            y_v = [count_2,y]
            answer.append([x_v[0]+y_v[0],x_v[-1]*y_v[-1]])

    max_lenght = list(set([b[0] for b in answer]))
    final_answer = [0*k for k in range(len(max_lenght))]

    for i in max_lenght:
        for k in answer:
            if i == k[0]:

                final_answer[i] += k[-1]
                
    return final_answer
    

poly1 = [2, 0, 5, 7]
poly2 = [3, 4, 2]

print("Answer is ",multiply_polynomial(poly1,poly2))