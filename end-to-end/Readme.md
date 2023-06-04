# 레퍼지토리 설명(end-to-end)
이 레퍼지토리 안에서 감정 분석의 모든 과정을 한번에 실행할 수 있습니다.<br>

# Getting Started
1. 감성분석 모델을 [감성분석 모델](https://drive.google.com/file/d/1-2xjvBezQ8gJRI5Y--43l8iJVFRQ3Zva/view?usp=sharing)에서 다운로드 받고, end-to-end.py와 같은 경로에 위치시켜 주세요.
2. 해당 링크를 참고하여 [Mecab 다운로드](https://velog.io/@wkfwktka/%EC%9C%88%EB%8F%84%EC%9A%B0%EC%97%90-Mecab-%EC%84%A4%EC%B9%98Python)을 진행해 주세요.
3. 터미널에 접속하여 아래와 같은 과정을 거치세요. 
 ```
 >>> cd boaz_second_project
 >>> pip install -r requirements.txt
 >>> python end-to-end.py
 ```
4. 파일의 경로 및 위치는 아래와 같습니다.
```bash
├── data
│   ├── After_sentiment_0604 for lyric summary.csv
├── end-to-end.py
└── sentiment_model2.h5
└── tokenizer2.pickle
``` 
