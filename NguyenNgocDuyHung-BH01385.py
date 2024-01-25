import os
try:
#tên người
    name=str(input('Enter your name: '))
#dữ liệu đầu vào
    subject=int(input('Enter your number of subjects: '))
#danh sách điểm
    list_score=[]
#danh sách tín chỉ
    list_credits=[]
#cho danh sách tín chỉ và danh sách điểm vào 1 khoảng
    for i in range (subject):
#điểm
        score=float(input(f'Enter your score of {i+1} subjects: '))
#tín chỉ
        credits=int(input(f'Enter your number of credits of {i+1} subjects: '))
#thêm giá trị vào list_score  
        list_score.append(score)
#thêm giá trị vào list_credits
        list_credits.append(credits)
#tổng số điểm
    total_score=0
    for i in range(subject):
#tính tổng số điểm
        total_score+=list_score[i]*list_credits[i]
#điểm GPA
    def gpa_calculate():
#tính điểm GPA
        gpa=total_score/sum(list_credits)
        return gpa
#in điểm    
    print('Your GPA is : ')
    print(gpa_calculate())  
    results=[name,list_score,list_credits,gpa_calculate()]
#tạo thư mục
    os.makedirs("C:/Results_GPA", exist_ok=True)
#tạo và ghi file
    with open(os.path.join("C:/Results_GPA", "results.txt"), mode='w') as f:
        f.write(f'{results}')
        print('Your results was saved to C:/Results_GPA/results.txt!')
#lỗi chia cho 0
except ZeroDivisionError:
    if subject<=0:
        print('Sorry! Your subject must be greater than 0')
    else:
        print('Sorry! Your point must be greater than 0')
#lỗi nhập giá trị sai
except ValueError:
    print('Sorry! You can enter only positive number')