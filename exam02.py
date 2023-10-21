#20231559 김준범 데이터분석 과제 인구통계import csv
import csv

import matplotlib.pyplot as plt
import random


def display_bar_chart(x_data, mandata,womandata):
    plt.rc('font', family='Malgun Gothic')
    plt.rcParams['axes.unicode_minus']=False
    plt.barh(x_data,mandata, label='남성')
    plt.barh(x_data,womandata, label='여성')
    plt.title('전국 성별과 나이별 인구')
    plt.legend()
    plt.show()
def get_data():
    check_text ="전국  (0000000000)"
    file = open('exam02.txt','r', encoding='utf-8')
    csv_data = csv.reader(file)

    temp_data=[]
    temp1_data=[]
    mandata =[]
    womandata =[]
    x_data = range(0, 101)


    for line in csv_data:
        if line[0] == check_text:
            temp_data=line[3:104]
            temp1_data=line[106:207]


    for m_data in temp_data:
        num = int(m_data.replace(',', ''))
        mandata.append(-num)

    print(mandata)

    for w_data in temp1_data:
        num = int(w_data.replace(',', ''))
        womandata.append(num)
    print(womandata)

        #print(num)
        #print(int[i])
        #data[i] = int(data[i])




    return{
        'x_data': x_data,
        'mandata': mandata,
        'womandata': womandata
    }




#end-def
result = get_data()
#print(result['x_data'])
#print(result['mandata'])
#print(result['womandata'])
#display_chart(result['x_data'], result['data'],result['data2'])
display_bar_chart(result['x_data'], result['mandata'],result['womandata'])
