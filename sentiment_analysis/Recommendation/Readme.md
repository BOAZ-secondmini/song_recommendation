# 노래 추천 부분
* Model : LSTM 사용
* 추천 방법 : 사용자의 현재 감정 score와 유사한 감정 score (+-10)을 가진 것을 추출한 후, 코사인 유사도(cosine similarity)로 판단
