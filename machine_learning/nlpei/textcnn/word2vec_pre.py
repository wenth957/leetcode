import tensorflow as tf
import pandas as pd
from tqdm import tqdm

def get_train_dataset(sentences,labels,max_len_sentence=200,num_label=3):
    '''sentences转换为token返回，sentence是一个二维矩阵'''
    X,y = [],[]
    word2index = pd.read_csv("../data/sa/w2v_vocab.txt", sep='\t', header=None)
    word2index = word2index.set_index(0).to_dict(orient='dict')[1]
    for sentence, label in tqdm(zip(sentences,labels)):
        sentence  = eval(sentence)
        if len(sentence) < max_len_sentence:
            sentence += ['[PAD]']*(max_len_sentence-len(sentence))
        else:
            sentence = sentence[:max_len_sentence]
        label = tf.one_hot(label,num_label)
        sentence2token = []
        for word in sentence:
            if word in word2index.keys():
                sentence2token.append(word2index[word])
            else:
                sentence2token.append(word2index['[UNK]'])
        X.append(sentence2token)
        y.append(label)
    dataset_X = tf.data.Dataset.from_tensor_slices(X)
    dataset_y = tf.data.Dataset.from_tensor_slices(y)
    dataset = tf.data.Dataset.zip((dataset_X, dataset_y))
    return dataset

def get_test_dataset(sentences,max_len_sentence=200):
    '''sentences转换为token返回，sentence是一个二维矩阵'''
    X = []
    word2index = pd.read_csv("../data/sa/w2v_vocab.txt", sep='\t', header=None)
    word2index = word2index.set_index(0).to_dict(orient='dict')[1]
    for sentence in tqdm(sentences):
        sentence = eval(sentence)
        if len(sentence) < max_len_sentence:
            sentence += ['[PAD]']*(max_len_sentence-len(sentence))
        else:
            sentence = sentence[:max_len_sentence]
        sentence2token = []
        for word in sentence:
            if word in word2index.keys():
                sentence2token.append(word2index[word])
            else:
                sentence2token.append(word2index['UNK'])
        X.append(sentence2token)
    dataset = tf.data.Dataset.from_tensor_slices(X)
    return dataset



if __name__== '__main__':
    # 读取分词结果
    train_df = pd.read_csv("../data/sa/train.txt",sep='\t',header=None)
    dev_df = pd.read_csv("../data/sa/dev.txt",sep='\t',header=None)
    test_df = pd.read_csv("../data/sa/test.txt",sep='\t',header=None)
    sentences_train = train_df[0]
    sentences_dev = dev_df[0]
    sentences_test = dev_df
    # 测试
    train_dataset = get_train_dataset(train_df[0].values,train_df[1].values)
    dev_dataset = get_train_dataset(dev_df[0].values,dev_df[1].values)
    test_dataset = get_test_dataset(test_df.values)
    for sentence,label in train_dataset.take(5):
        print(sentence,label)
