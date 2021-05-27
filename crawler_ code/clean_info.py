import pandas as pd
import numpy as np
import os

all_data=pd.DataFrame(columns=['rate', 'review'])

os.chdir('./infos')
li=os.listdir()
for i in li:#모은 리뷰들을 하나의 데이터프레임으로 변경
    data= pd.read_table(i)
    all_data = pd.concat([all_data, data], ignore_index=True, axis=0)


print('초반 데이터 확인 :',len(all_data))#
all_data.drop_duplicates(subset=['review'], inplace=True)#중복된 리뷰들을 제거한다
print('중복 제거 확인 :',len(all_data))

all_data = all_data.dropna(how = 'any') # Null 값이 존재하는 행 제거
print(all_data.isnull().values.any()) # Null 값이 존재하는지 확인

#이벤트/홍보 관련 리뷰 제거
remove=['이벤트','핫티스트','선리뷰','선구매','십오야','홀세일','통장','작가님','썸딜',
        '나인NINE9','무료','알람','감상후','수정','리뷰뿅','연재','삽화','표지',
        '리디','선별점','포인트백','포백','이벤','이벵','1+1','나중에','후리뷰']
for i in remove:
    all_data = all_data[all_data["review"].str.contains(i) == False]

print(all_data.groupby('rate').size().reset_index(name = 'count'))#원래 데이터양 확인
all_data.to_csv('origin_all_data.txt',mode='w',index=False)

n_data=all_data[all_data['rate']==-1]#부정 리뷰 추출
p_data=all_data[all_data['rate']==1].sample(n=len(n_data))#부정 리뷰 길이에 맞춰 긍정 리뷰 랜덤 추출

#긍정/부정 리뷰 합쳐서 새로운 파일로 저장
result=pd.concat([n_data,p_data], ignore_index=True, axis=0).sample(frac=1).reset_index(drop=True)
print(result.groupby('rate').size().reset_index(name = 'count'))
result.to_csv('result_data.csv',mode='w', index=False)
