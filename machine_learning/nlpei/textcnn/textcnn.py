import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers, losses, metrics, optimizers

class TextCNN(tf.keras.Model):

    def __init__(self,vocab_size,emb_size,seq_len,emb_matrix,kernel_size,n_kernels,n_class):
        '''
                初始化参数，创建模型时自动生成
                :param vocab_size: 词表大小 embedding层参输入数
                :param emb_size: 词向量维度 embedding层输入参数
                :param seq_len: embedding层输入参数
                :param emb_matrix:  初始化embedding层优化参数

                :param kernel_size: 卷积层大小 卷积层参数
                :param n_kernels:  卷积通道数 卷积层参数

                :param n_class:  分类数量 softmax参数
                '''
        super(TextCNN,self).__init__()
        self.vocab_size = vocab_size
        self.emb_size = emb_size
        self.seq_len = seq_len
        self.emb_matrix = emb_matrix

        self.kernel_size = kernel_size
        self.n_kernels = n_kernels

        self.n_class = n_class
        # embedding层
        self.Embedding_death = layers.Embedding(
            vocab_size,emb_size,input_length = seq_len,weights=[emb_matrix],trainable=False)
        self.Embedding_live = layers.Embedding(
            vocab_size, emb_size,input_length = seq_len,weights=[emb_matrix], trainable=True)
        # 卷积层 emb_size 上下扫
        self.Conv = layers.Conv2D(
            filters=n_kernels,
            kernel_size=(kernel_size,emb_size),
            strides=1,
            padding='valid',
            activation='relu',
            name='Conv')
        # 卷积层输出seq_len - kernel_size + 1, 1

        # pooling层
        self.Pooling = layers.MaxPooling2D(
            pool_size=(seq_len - kernel_size + 1, 1),
            padding='valid',name='Maxpool')
        # dense层
        self.Dense = keras.layers.Dense(
            n_class,
            activation='softmax',
            use_bias=True,
            kernel_constraint=keras.constraints.MaxNorm(max_value=3, axis=0),
            name = 'Dense')
        # dropout
        self.Dropout = keras.layers.Dropout(0.5,name='Dropout')
        # flatten
        self.Flatten = keras.layers.Flatten(
            data_format='channels_last',
            name='flatten')

        self.optimizer = optimizers.Adam(learning_rate=0.001)
        self.loss_func = losses.CategoricalCrossentropy()

        self.train_loss = metrics.Mean(name='train_loss')
        self.train_metric = metrics.CategoricalAccuracy(name='train_accuracy')

        self.valid_loss = metrics.Mean(name='valid_loss')
        self.valid_metric = metrics.CategoricalAccuracy(name='valid_accuracy')

    @tf.function
    def call(self, x, embedding_train=False):
        '''
        前向传播
        :param self:
        :param x: 句子输入
        :param embedding_train : 是否微调词向量,默认false
        :return: probs
        '''
        if embedding_train:
            input_matrix = self.Embedding_live(x)
        else:
            input_matrix = self.Embedding_death(x) # (max_len,emb)
        input_matrix = tf.expand_dims(input_matrix,axis=-1) # (max_len,emb,1)
        feature_maps = self.Conv(input_matrix) #  (max_len,1,n_kernels)
        pool_out = self.Pooling(feature_maps) #   (1,1,n_kernels)
        flatten = self.Flatten(pool_out) # (1,n_kernels)
        input_dense = self.Dropout(flatten)
        probs = self.Dense(input_dense) # (1,3)
        return probs


