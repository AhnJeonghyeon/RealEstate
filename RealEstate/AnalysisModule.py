'''
자 이 파일의 목적
1. 가장 많이 오른 지역 가장 떨어진 지역 보여주기
    1)지역 입력(입력x(서울전체), 구 / 구,동)
    2)연 월을 입력하고 현재 가격 대비 가장 많이 오른 지역과 떨어진 지역을 보여준다

2. 예측모듈
    1)지역 입력(입력x(서울전체), 구 / 구,동)
    2)아파트 명 입력
    3)과거 집값 상승 그래프와 함께 미래의 값을 도출하여 보여준다
        방법론
            1]단순예측
            2]가설
                1)집의크기 건축년도 토지형태 방화장실 개수 냉방방식
                2)한강과의 거리 체육시설의 유무에 따라 영향도가 커질 것이다
                3)역과의 거리에 따라 영향도가 다를 것이다
                4)교육시설(학교,학원의 수)에 따라 다를 것이다
                5)구청 등의 교통,교육,문화,환경의 인프라에 따라
'''
'''
main함수는 python 에서 .py를 실행했을 때 실행되는 메인함수인 것
module을 import하기 위해선 def로 만들어놔야한다.
'''
import pandas as pd
import numpy as np

def getBigGap():
    gu, do = input("구 또는 구와 동을 입력해주세요(입력이 없을 시 서울시 전체) : ").split()
    print(gu+do)
    df = pd.read_csv('/Users/AhnJeongHyeon/Documents/GitHub/RealEstate/Data/APT19.06~20.0530.csv'
                     ,skiprows=1)
    # csv파일 아니면 좀 read에 제약이 많은 것 같다 xlsx파일 여러 에러들로 인해 포기
    df.columns = ['location','fnum','num','semiNum','name','size','ym','d','price','floor','buildY','address']
    #한글 네이밍 영어로 변경
    loc = "서울특별시 " + gu + " " + do

    sorted_df = df.loc[df['location'] == loc].sort_values(by=['num','semiNum','size','ym','d'])
    #sorting 번지수,거래년 월
    #print(sorted_df)

    name, ym = input("아파트 이름과 과거 거래년월(201905)을 입력해주세요").split()

    list = []
    for index, ith in sorted_df.iterrows():
        #list.append(ith)
        if ith.get('name').find(name) != -1:
            list.append(ith)
        '''
        if ith.str.contains(name, na=False):
            last_df.append(ith)
        '''
    last_df = pd.DataFrame(list)
    #list로 넣어서 transform 되어 들어감 loc하려면 뒤집어줘야함
    #loc은 row를 구하는 함
    #last_df = last_df.T

    #print(last_df.loc['name'])
    #TODO name, size로 그루핑하여 가로축 ym/d 세로축 price로 그래프 구현

    print(last_df.groupby(['name', 'size'])['price'].max())
    print(last_df.groupby(['name', 'size'])['price'].min())


if __name__ == "__main__":
    print("main")
    getBigGap()