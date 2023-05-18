# Sentiment Analysis
감성 분석(Sentiment Analysis)는 텍스트나 문장, 문서 등의 자연어 데이터에서 감정, 태도 또는 주관적인 의견을 추출하고 분류하는 기술입니다. 이를 통해 문장이나 문서의 긍정적, 부정적, 중립적인 감정을 자동으로 식별할 수 있습니다. 감성 분석은 주로 기계 학습과 자연어 처리 기술을 사용하여 구현됩니다. 이번 프로젝트에서는 자연어 처리 기술과 딥러닝을 기반으로 한 감성 분석을 진행하였습니다.
## 활용한 데이터
<ul>
<li> 네이버 영화 리뷰 데이터 (200,000개) -> 최종 학습 시 사용한 모델 </li>
<li> 네이버 쇼핑 리뷰 데이터 (200,000개) -> 최종 학습 시 사용한 모델 </li>
  <li> 네이버 스팀 데이터 (100,000개) </li>
  <li> AI Hub 대화 뭉치 데이터 (15,000개) </li>
 </ul>

## 활용 모델
### LSTM(Long Short Term Memory)
RNN의 Vanishing Gradient 문제랑 long-term dependency 문제를 해결하기 위해 등장한 모델입니다. LSTM에서는 RNN과 달리 forget gate, input gate, output gate, cell state 등 여러 gate를 두어서 RNN의 문제를 해결했지만 여전히 long-term dependency 문제와 gate가 많다는 단점이 존재합니다.

### 모델 구조 ([모델](https://drive.google.com/file/d/1WxcuBBWYcmcEysxJvTrZ34F9flS2OFYB/view?usp=share_link))
![image](https://github.com/BOAZ-secondmini/song_recommendation/assets/84063359/946db17c-175d-46e6-b3c7-3b0e7ca45247)

## 성능 결과
|Used Data|Model Name|Accuracy|
|---|---|---|
|Naver Movie|LSTM(10 epochs, earlystopping)|84.09%|
|Naver Movie + shopping + steam + AI Hub|LSTM(30 epochs, earlystopping)|86.43%|
|Naver Movie + shopping|LSTM(30 epochs, earlystopping)|88.48%|



