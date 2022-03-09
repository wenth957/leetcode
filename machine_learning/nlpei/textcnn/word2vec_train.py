import re
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from gensim.models.word2vec import Word2Vec
from gensim.models import KeyedVectors
import logging
import multiprocessing


def get_data(file_path,sample=150000):
    data = pd.read_csv(file_path)
    data.dropna(inplace=True)
    sampledata =  data.sample(n=sample,random_state=1024)
    sample_data = sampledata.reset_index().drop(['index'],axis=1)
    return sample_data

# 根据环境、口味、服务评分生成新的标签
def get_labels(data):
    data['label'] = ((data['rating_env']+data['rating_flavor']+data['rating_service'])//3)
    return data.drop(['rating_env','rating_flavor','rating_service'],axis=1)


# 替换文本中的特殊符号
def clear_str(string):
    string = re.sub(r'\W', ' ',string)
    string = re.sub(r'_', ' ',string)
    return string.strip()


 # 数据集的分割
def split_data(dataset):
    X = dataset['comment']
    y = dataset['label'].astype(str)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.1, random_state=1024)
    X_train, X_dev, y_train, y_dev = train_test_split(
        X_train, y_train, test_size=0.1, random_state=1024)
    train_df = pd.DataFrame({'comment': X_train, 'label': y_train}).reset_index(drop=True)
    dev_df = pd.DataFrame({'comment': X_dev, 'label': y_dev}).reset_index(drop=True)
    test_df = pd.DataFrame({'comment': X_test}).reset_index(drop=True)
    test_label = pd.DataFrame({'label': y_test}).reset_index(drop=True)
    return train_df, dev_df, test_df, test_label

def get_stop_words(stop_words_path):
    stop_words = []
    with open(stop_words_path, 'r', encoding='utf-8') as f:
        for line in f:
            stop_words.append(line.strip())
    return stop_words

def cut_words(sentence, stop_words):
    import jieba
    cut_word = jieba.cut(str(sentence).strip())
    if stop_words:
        words = [word for word in cut_word if word not in stop_words]
    else:
        words = list(cut_word)
    return words

def train_w2v(sentences,embbedding_size=256):
    logging.basicConfig(filename='word2vec.log',level=logging.INFO)
    logging.info('Training word2vec embedding...')
    w2v_model = Word2Vec(vector_size=embbedding_size, workers=multiprocessing.cpu_count(), min_count=10, sg=0)
    w2v_model.build_vocab(sentences)
    w2v_model.train(sentences, total_examples=w2v_model.corpus_count, epochs=200)
    w2v_model.save('../textcnn/model/w2vmodel')


if __name__ == "__main__":
    # 1 数据预处理
    raw_data_path = '../data/sa/ratings.csv'
    sample_data = get_data(raw_data_path)
    dataset = get_labels(sample_data)
    dataset['comment'] = dataset['comment'].apply(clear_str)
    # 2 分割数据集，训练集、验证集、测试集样本
    train_df, dev_df, test_df, test_label = split_data(dataset=dataset)
    # 3 获得停用词表
    stop_words_path = '../data/sa/baidu_stopwords.txt'
    stop_words = get_stop_words(stop_words_path)
    # 4 分词后保存分词结果
    train_df['comment'] = train_df['comment'].apply(cut_words, stop_words=stop_words)
    dev_df['comment'] =  dev_df['comment'].apply(cut_words, stop_words=stop_words)
    test_df['comment'] =  test_df['comment'].apply(cut_words, stop_words=stop_words)
    train_df.to_csv('../data/sa/train.txt', sep='\t', index=False, header=None)
    dev_df.to_csv('../data/sa/dev.txt', sep='\t', index=False, header=None)
    test_df.to_csv('../data/sa/test.txt', sep='\t', index=False, header=None)
    test_label.to_csv('../data/sa/label.txt', index=False, header=None)
    # 5 训练并保存模型
    sentences = train_df['comment'].to_list()
    train_w2v(sentences)
    # 6 保存词向量
    w2v_model = Word2Vec.load('../textcnn/model/w2vmodel')
    word_vectors = w2v_model.wv
    word_vectors.add_vector('[PAD]', np.zeros(256))
    word_vectors.add_vector('[UNK]', np.random.randn(256))
    word_vectors.save("../textcnn/model/word2vec.wordvectors")
    # 7 读取词向量对象
    wv = KeyedVectors.load("../textcnn/model/word2vec.wordvectors", mmap='r')
    # 词向量：用于初始化embedding层
    word_vectors = wv.vectors
    print(np.array(word_vectors).shape)
    # 8 保存词表
    word2index = wv.key_to_index
    vocab_path = '../data/sa/w2v_vocab.txt'
    with open(vocab_path, 'w', encoding='utf-8') as f:
        for word, index in word2index.items():
            f.write(word + '\t' + str(index) + '\n')