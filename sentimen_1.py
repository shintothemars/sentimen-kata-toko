# -*- coding: utf-8 -*-
"""sentimen 1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1NVCwqNgBovtWHA1KQHqAGCInhwvD9tGg

# Library Python yang digunakan

1.   Pandas
2. matplotlib
3. sastrawi
4. wordcloud menggambarkan metadata kumpulan kunci atau keywords pada sebuah dokumen. alternatof lain : tweepy, TextBlob, Pandas, Re(regex),Time serta Matplotlib.
5. numpy melakukan operasi komputasi untuk tipe data numerik seperto tope data operasi aritmatika atau operasi lainnya yang bisa diterapkan pada vektor atau matriks
6. sklearn:
- naive bayes ( GaussianNB )
- model selection ( RepeatedStratifiedKFold, GridSearchCV, StratifiedKFlod)
- metrics ( confusion_matrix, calssification_report )
"""

!pip install Sastrawi

import pandas as pd
import matplotlib.pyplot as plt
import Sastrawi
from wordcloud import WordCloud
import numpy as np

"""## Crawling Data"""

df = pd.read_csv('/content/data_real.csv',index_col=0)
df.head()

df_copy = df.copy()

"""##Labeling"""

label = []
for index, row in df_copy.iterrows():
  if row["Rating"]== 1 or row["Rating"]== 2:
    label.append(0)
  else:
    label.append(1)

df_copy["label"]= label

df_copy.head()

"""## Processing Teks

normalisasi
"""

df_copy['Ulasan'] = df_copy['Ulasan'].str.lower()

norm = {" dgn " : " dengan ", " gue ": " saya ", " dgn ":" dengan ", "bgmn ":" bagaimana ", ' tdk':' tidak ', ' blum ':' belum ', 'mantaaaaaaaappp':' bagus ', ' josss ':' bagus ', ' thanks ': ' terima kasih ', 'fast':' cepat ', ' dg ':' dengan ', 'trims':' terima kasih ', 'brg':' barang ', 'gx':' tidak ', ' dgn ':' dengan ', ' recommended':' rekomen ', 'recomend':' rekomen ', 'good':' bagus '}

def normalisasi(str_text):
  for i in norm:
    str_text = str_text.replace(i, norm[i])
  return str_text

df_copy['Ulasan'] = df_copy['Ulasan'].apply(lambda x: normalisasi(x))

df_copy.head()

"""stopwords"""

from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory, StopWordRemover, ArrayDictionary
more_stop_words = []

stop_words = StopWordRemoverFactory().get_stop_words()
new_array = ArrayDictionary(stop_words)
stop_words_remover_new = StopWordRemover(new_array)

def stopword(str_text):
  str_text = stop_words_remover_new.remove(str_text)
  return str_text


df_copy['Ulasan'] = df_copy['Ulasan'].apply(lambda x: stopword(x))
df_copy.head()

"""tokenize"""

tokenized = df_copy['Ulasan'].apply(lambda x:x.split())
tokenized

"""##Stemming"""

from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

def stemming(Ulasan):
  factory = StemmerFactory()
  stemmer = factory.create_stemmer()
  do = []
  for w in Ulasan:
    dt = stemmer.stem(w)
    do.append(dt)
  d_clean = []
  d_clean = " ".join(do)
  print(d_clean)
  return d_clean

tokenized = tokenized.apply(stemming)

tokenized.to_csv('databersih2.csv', index=False)
data_clean = pd.read_csv('databersih2.csv', encoding='latin1')
data_clean.head()

"""menggabungkan kedua atribut"""

at1 = pd.read_csv('databersih2.csv')
at2 = pd.read_csv('data_real.csv')
att2 = at2['label']

result = pd.concat([at1, att2], axis=1)

result.head()

"""## Menghitung Kata dengan TF-IDF"""

from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer

Ulasan = result['Ulasan']

Ulasan.isnull().sum()

Ulasan = Ulasan.fillna('tidak ada komentar')

cv = CountVectorizer()
term_fit = cv.fit(Ulasan)

print(len(term_fit.vocabulary_))

term_fit.vocabulary_

ulasan_tf = Ulasan[1]
print(ulasan_tf)

term_frequency = term_fit.transform([ulasan_tf])
print(term_frequency)

dokumen = term_fit.transform(Ulasan)
tfidf_transformer = TfidfTransformer().fit(dokumen)
print(tfidf_transformer.idf_)

tfidf = tfidf_transformer.transform(term_frequency)
print(tfidf)

"""## Visualisasi (NLP)"""

train_s0 = df_copy[df_copy["label"] == 0]

train_s0["Ulasan"] = train_s0["Ulasan"].fillna("tidak ada komentar")

train_s0.head()

from wordcloud import WordCloud

all_text_s0 = ' '.join(word for word in train_s0["Ulasan"])
wordcloud = WordCloud(colormap='Reds', width=1000, height=1000, mode='RGBA', background_color='white').generate(all_text_s0)
plt.figure(figsize=(20, 10))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title("Ulasan Negatif")
plt.margins(x=0, y=0)
plt.show()

train_s1 = df_copy[df_copy["label"] == 1]

train_s1["Ulasan"] = train_s1["Ulasan"].fillna("Tidak ada komentar")

train_s1.head()

all_text_s1 = ' '.join(word for word in train_s1["Ulasan"])
wordcloud = WordCloud(colormap='Blues', width=1000, height=1000, mode="RGBA", background_color='white').generate(all_text_s1)
plt.figure(figsize=(20, 10))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.title("Ulasan Positif")
plt.margins(x=0, y=0)
plt.show()

sentimen_data = pd.value_counts(df_copy["label"], sort=True)
sentimen_data.plot(kind='bar', color=['lightskyblue', 'red'])
plt.title("Bar Chart")
plt.show

"""##Split Data (TF-IDF)"""

result['Ulasan'] = result['Ulasan'].fillna("Tidak ada komentar")

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(result['Ulasan'], result['label'],
                                                    test_size=0.1, stratify=result['label'], random_state=30)

import numpy as np

from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(decode_error='replace', encoding='utf-8')

X_train = vectorizer.fit_transform(X_train)
X_test = vectorizer.transform(X_test)

print(X_train.shape)
print(X_test.shape)

X_train = X_train.toarray()

X_test = X_test.toarray()

"""# Machine Learning (Naive Bayes Classifier)"""

from sklearn.naive_bayes import GaussianNB

nb = GaussianNB()

from sklearn.model_selection import RepeatedStratifiedKFold
from sklearn.model_selection import GridSearchCV

cv_method = RepeatedStratifiedKFold(n_splits=5, n_repeats=3, random_state=999)

params_NB = {'var_smoothing': np.logspace(0, -9, num=100)}
gscv_nb = GridSearchCV(estimator=nb,
                        param_grid=params_NB,
                        cv = cv_method,
                        verbose = 1,
                        scoring = 'accuracy')

gscv_nb.fit(X_train, y_train)
gscv_nb.best_params_

nb = GaussianNB(var_smoothing=0.005336699231206307)

nb.fit(X_train, y_train)

y_pred_nb = nb.predict(X_test)

"""# Confusion Matrix"""

from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report, roc_curve
from sklearn.metrics import RocCurveDisplay # Import RocCurveDisplay instead of plot_roc_curve

print('----- confusion matrix ------')
print(confusion_matrix(y_test, y_pred_nb))

print('----- classification report -----')
print(classification_report(y_test, y_pred_nb))

from sklearn.metrics import RocCurveDisplay

RocCurveDisplay.from_estimator(nb, X_test, y_test)
plt.show()