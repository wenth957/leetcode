import  tensorflow  as tf
import pandas as pd
from gensim.models import KeyedVectors
from word2vec_pre import get_train_dataset
from textcnn import TextCNN
from utils import printbar



@tf.function
def train_step(model,X_train,y_train):
    with tf.GradientTape() as tape:
        probs = model.call(X_train)
        losses = model.loss_func(y_true=y_train, y_pred=probs)
    grads = tape.gradient(losses,model.trainable_variables)
    model.optimizer.apply_gradients(zip(grads,model.trainable_variables))
    model.train_loss.update_state(losses)
    model.train_metric.update_state(y_train,probs)

@tf.function
def valid_step(model,x_val,y_val):
    probs = model.call(x_val)
    losses  = model.loss_func(y_val,probs)
    model.valid_loss.update_state(losses)
    model.valid_metric.update_state(y_val,probs)


def train(model, train_dataset, val_dataset, batch_size, epochs):
    for epoch in tf.range(epochs):
        shuffle_train = train_dataset.shuffle(len(train_dataset))
        shuffle_val = val_dataset.shuffle(len(val_dataset))
        train_enumerate = shuffle_train.batch(batch_size).enumerate()
        val_enumerate = shuffle_val.batch(batch_size).enumerate()
        logs = 'Epoch={},step={},Loss:{},Accuracy:{}'
        for step, batch in train_enumerate:
            x_train, y_train = batch
            train_step(model, x_train, y_train)
            if step % 100 == 0:
                printbar()
                tf.print(
                    tf.strings.format(logs,
                                      (epoch,step,
                                       model.train_loss.result(),
                                       model.train_metric.result())
                                      )
                )

        for step, batch in val_enumerate:
            x_val, y_train = batch
            valid_step(model, x_val, y_train)

        logs = 'Epoch={},Loss:{},Accuracy:{},Valid Loss:{},Valid Accuracy:{}'

        printbar()
        tf.print(tf.strings.format(
            logs,
            (epoch, model.train_loss.result(),
             model.train_metric.result(),
             model.valid_loss.result(),
             model.valid_metric.result())))

        model.train_loss.reset_states()
        model.valid_loss.reset_states()
        model.train_metric.reset_states()
        model.valid_metric.reset_states()


if __name__ == '__main__':
    # 读取分词文件
    train_df = pd.read_csv('../data/sa/train.txt', sep='\t', header=None)
    dev_df= pd.read_csv('../data/sa/dev.txt', sep='\t',  header=None)
    wv = KeyedVectors.load("../textcnn/model/word2vec.wordvectors", mmap='r')
    train_dataset = get_train_dataset(train_df[0].values,train_df[1].values)
    dev_dataset = get_train_dataset(dev_df[0].values,dev_df[1].values)
    emb_matrix = wv.vectors

    # 读取模型
    model = TextCNN(
        vocab_size=26777,emb_size=256,seq_len=200,emb_matrix=emb_matrix,kernel_size=3,
        n_kernels=100,n_class=3)
    # 训练
    batch_size = 64
    epochs = 10
    train(model, train_dataset, dev_dataset, batch_size, epochs)



