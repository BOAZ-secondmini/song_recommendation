# BOAZ Analysis Second Mini Project
**사용자의 SNS를 통해 감성분석 후 알맞는 노래 추천하기\
팀원 : [김기수](https://github.com/Kisooofficial), [김민혜](https://github.com/minelolo), [정원준](https://github.com/garden-jun), [최은선](https://github.com/thisissilverline)**
# Data Collection
* 감정 분석을 적용할 데이터를 얻기 위해, 멜론에서 700개의 가사를 수집하였습니다.
  * 수집 기준 : 2023년 5월 둘째주 기준으로 실시간 TOP 100 + 장르별(댄스와 트로트 제외) 100개씩 수집
* 감정 분석시 학습시킬 데이터를 선정하였습니다.
  * 선정 기준 : LSTM(Longest Short Term Memory)을 적용하였을 때 성능이 좋은 것끼리 비교(ablation study 기법과 유사하게 진행)
  * 최종 선정된 데이터 : 네이버 영화 리뷰 데이터(약 20만) + 네이버 쇼핑 리뷰 데이터(약 20만) = 총 393,562 개의 데이터를 이용
