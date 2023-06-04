# BOAZ Analysis Second Mini Project
**사용자의 SNS를 통해 감성분석 후 알맞는 노래 추천하기\
팀원 : [김기수](https://github.com/Kisooofficial), [김민혜](https://github.com/minelolo), [정원준](https://github.com/garden-jun), [최은선](https://github.com/thisissilverline)**

## Getting Started(End-to-End)
1. 감성분석 모델을 [감성분석 모델](https://drive.google.com/file/d/1-2xjvBezQ8gJRI5Y--43l8iJVFRQ3Zva/view?usp=sharing)에서 다운로드 받고, end-to-end.py와 같은 경로에 위치시켜 주세요.
2. 해당 링크를 참고하여 [Mecab 다운로드](https://velog.io/@wkfwktka/%EC%9C%88%EB%8F%84%EC%9A%B0%EC%97%90-Mecab-%EC%84%A4%EC%B9%98Python)을 진행해 주세요.
3. 터미널에 접속하여 아래와 같은 과정을 거치세요. 
 ```
 >>> cd end-to-end
 >>> pip install -r requirements.txt
 >>> python end-to-end.py
 ```
4. 파일의 경로 및 위치는 아래와 같습니다.
```bash
├── end-to-end
|   ├── data
|   |   ├── After_sentiment_0604 for lyric summary.csv
|   ├── end-to-end.py
|   ├── sentiment_model2.h5
|   ├── tokenizer2.pickle
``` 

## Data Collection
* 감정 분석을 적용할 데이터를 얻기 위해, 멜론에서 700개의 가사를 수집하였습니다.
  * 수집 기준 : 2023년 5월 둘째주 기준으로 실시간 TOP 100 + 장르별(댄스와 트로트 제외) 100개씩 수집
* 감정 분석시 학습시킬 데이터를 선정하였습니다.
  * 선정 기준 : LSTM(Longest Short Term Memory)을 적용하였을 때 성능이 좋은 것끼리 비교(ablation study 기법과 유사하게 진행)
  * 최종 선정된 데이터 : 네이버 영화 리뷰 데이터(약 20만) + 네이버 쇼핑 리뷰 데이터(약 20만) = 총 393,562 개의 데이터를 이용

## Text Summerization
* 사용한 모델 : KoBART(여기 추가로 설명 필요함)
* 감정분석에서 학습시킨 텍스트의 길이와 수집한 노래 가사의 길이 사이의 불균형을 해소할 필요성이 커짐
  * 감정분석에 이용한 텍스트의 단어의 개수 : 평균 약 12.3개, 최대 83개 / 노래 가사의 단어의 개수 : 평균 약 516.3개, 최대 1852개
  * 텍스트 요약 후 노래 가사의 단어의 개수 : 평균 약 180.1개, 최대 516개
    * 100% 해결되지는 않으나, 감정분석에 이용한 텍스트와 노래 가사 사이의 불균형을 어느 정도는 해결
## Sentiment Analysis
* 감성분석에는 **LSTM** 모델을 이용
* 학습 방법
  * 전체 데이터 393,562개의 데이터에서 training set과 validation set의 비율을 8 : 2로 두어 성능을 평가
  * 최종 예측하는 것은 현재 감정에 대한 긍/부정으로, 데이터 불균형 문제가 없었기 때문에 성능 평가는 정확도(Accuracy)를 기준으로 판단
* 감정분석 성능 평가

|Used Data|Vectorizing|Modeling|Accuracy|
|---|---|---|---|
|Naver Movie|CountVectorizer|SVM|76.15%|
|Naver Movie|TF-IDF|SVM|77.89%|
|Naver Movie|tensorflow Tokenizer|RNN|82.55%|
|Naver Movie|tensorflow Tokenizer|LSTM|82.55%|
|Naver Movie + shopping + steam + AI Hub|tensorflow Tokenizer|LSTM|86.43%|
|Naver Movie + shopping + steam|tensorflow Tokenizer|LSTM|87.04%|
|**Naver Movie + shopping**|**tensorflow Tokenizer**|**LSTM**|**88.48%**|
