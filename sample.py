# First download the pretrained gensim model:
# $ wget http://public.shiroyagi.s3.amazonaws.com/latest-ja-word2vec-gensim-model.zip
# $ unzip latest-ja-word2vec-gensim-model.zip

from gensim.models.word2vec import Word2Vec

model = Word2Vec.load('word2vec.gensim.model')

some_words = ['ブランド', 'バッグ', 'アルマーニ']
for w in some_words:
    print(model.wv.most_similar(w))
