import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 한글만 추출하기
from konlpy.tag import Mecab
from tqdm import tqdm

from tensorflow.keras.models import load_model
from tensorflow.keras.layers import Embedding, Dense, LSTM, Dropout, LeakyReLU
from tensorflow.keras.models import Sequential
from tensorflow.keras.models import load_model
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint, LearningRateScheduler
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.experimental import CosineDecay
from tensorflow.keras.preprocessing.sequence import pad_sequences

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

import pickle

import warnings
warnings.filterwarnings('ignore')

data = pd.read_csv('./data/After_sentiment_0604 for lyric summary.csv', encoding = 'CP949').drop_duplicates(['song_name', 'artist']).reset_index(drop = True)


# Define a simple sequential model
def create_model():
    embedding_dim = 128
    hidden_units = 128

    model = Sequential()
    model.add(Embedding(17547, embedding_dim))
    model.add(LSTM(hidden_units))
    model.add(Dense(128, activation = LeakyReLU(alpha = 0.05)))
    model.add(Dropout(0.5))
    model.add(Dense(32, activation = LeakyReLU(alpha = 0.05)))
    model.add(Dense(1, activation='sigmoid'))

    return model

# 모델 불러오기
sentiment_model = create_model()
sentiment_model.load_weights('sentiment_model2.h5')

import pickle

def hangul_only(sentence):
    hangul_sentence = sentence.replace("[^ㄱ-ㅎㅏ-ㅣ가-힣0-9 ]","")
    hangul_sentence = hangul_sentence.replace('^ +', '')
    return hangul_sentence

# 형태소 분석 -> mecab 이용해서 명사, 형용사, 동사만 추출
def mecab_preprocessing(input_sentence):
    hangul_sentence = hangul_only(input_sentence)

    tags = ['JK', 'JKS', 'JKC', 'JKG', 'JKO', 'JKB', 'JKV', 'JKQ', 'JX', 'JC', 'EP', 'EF', 'EC', 'ETN', 'ETM']


    mecab = Mecab(dicpath="C://mecab/mecab-ko-dic")
    josa_removed = [x[0] for x in mecab.pos(hangul_sentence) if x[1] not in tags]
    preprocessed_sentence = ' '.join(josa_removed)
    
    return preprocessed_sentence

def sentence_to_vector(tokenizer, input_sentence):

    preprocessed_sentence = mecab_preprocessing(input_sentence)

    song_token = []
    tokenized_sentence = str(preprocessed_sentence).split(' ')
    song_token.append(tokenized_sentence)

    song_sequences = tokenizer.texts_to_sequences(song_token)

    from tensorflow.keras.preprocessing.sequence import pad_sequences

    pad_song = pad_sequences(song_sequences, maxlen = 83)
    return pad_song

def prediction(sentiment_model, pad_sequences):
    prediction_score= float(sentiment_model.predict(pad_sequences.reshape(1, -1))) * 100
    return prediction_score

def similar_sentiment(df : pd.DataFrame, column, sentiment_score : float, input_sentence : str):
    reco_df = df[(df[column] >= sentiment_score - 10) & (df[column] <= sentiment_score + 10)]
    reco_df.loc['query', 'lyric_summary'] = input_sentence
    return reco_df

def final_recommendation(candidate_song) -> list:
    tfidf = TfidfVectorizer()
    tfidf_matrix = tfidf.fit_transform(candidate_song['lyric_summary'])

    cosine_sim = cosine_similarity(tfidf_matrix[-1], tfidf_matrix)
    recommendation_need = cosine_sim[-1]
    sorted_index = np.argsort(recommendation_need)[::-1]
    recommend_index = sorted_index[2:7]
    return candidate_song.iloc[recommend_index][['song_name', 'artist']]

def final_print_recommendation(recommend_data):
     for i in range(len(recommend_data)):
        if i == 10:
            break
        print('{}번째 추천 곡은 {}의 {}입니다.'.format(i+1, recommend_data.iloc[i, 1], recommend_data.iloc[i, 0],))



# 요즘 시험기간이라 조금 힘든데 공부할 것은 많고 팀플도 너무 많고 어떻게 해야 할 지 모르겠어. 아 빨리 종강 왔으면 좋겠는데 종강 2주나 남아서 언제까지 기다리냐 너무너무너무 힘들다. 노래 추천해봐
# 보아즈에는 정말 좋은 사람이 많아. 뭐 우리 미니 플젝 팀원은 물론이지. 벌써 6개월이 지났다는 것이 믿기지가 않는데 남은 기간동안 화이팅하자 ㅎㅎ 

def main():
    # loading => 토크나이저 모델 불러오기
    with open('tokenizer2.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)

    trial = 0
    while trial < 1:
        input_sentence = input('요즘 어때요?\n')
        if len(input_sentence) <= 30:
            print('100자 이상 입력해 주세요\n')
            continue
        pad_sequences = sentence_to_vector(tokenizer, input_sentence)
        prediction_score = prediction(sentiment_model, pad_sequences)

        if prediction_score >= 50:
            print('{:.2f} % 확률로 긍정 리뷰입니다.'.format(prediction_score))
            print('추천되는 노래는 \n')
            candidate_song = similar_sentiment(data, 'score_summary_1', prediction_score, input_sentence)
            recommend_data = final_recommendation(candidate_song)
            final_print_recommendation(recommend_data)
            print()
        else:
            print('{:.2f} % 확률로 부정 리뷰입니다.'.format(100 - prediction_score))
            print('추천되는 노래는 \n')
            candidate_song = similar_sentiment(data, 'score_summary_1', prediction_score, input_sentence)
            recommend_data = final_recommendation(candidate_song)
            final_print_recommendation(recommend_data)
            print()
        trial += 1

if __name__ == "__main__":
    main()
