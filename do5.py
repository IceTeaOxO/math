# -*- coding: utf-8 -*-

# Import the necessary modules
import pickle
import numpy as np
from keras.models import load_model
# from keras.preprocessing.sequence import pad_sequences
from keras.utils.data_utils import pad_sequences
# 导入字典

def do5(text):

    with open('./model5/word_dict.pk', 'rb') as f:
        word_dictionary = pickle.load(f)
    with open('./model5/label_dict.pk', 'rb') as f:
        output_dictionary = pickle.load(f)

    try:
        # 数据预处理
        input_shape = 180
        sent = text
        x = [[word_dictionary[word] for word in sent]]
        x = pad_sequences(maxlen=input_shape, sequences=x, padding='post', value=0)

        # 载入模型
        model_save_path = './model5/model.h5'#./sentiment_analysis.h5
        lstm_model = load_model(model_save_path)

        # 模型预测
        y_predict = lstm_model.predict(x)
        print(y_predict)
        label_dict = {v:k for k,v in output_dictionary.items()}
        print(label_dict)
        print('輸入語句: %s' % sent)
        
        label_to_word = ['生氣','難過','開心','無意義','辱罵','鼓勵','贊同','不贊同','反諷','害怕']
        
        print('情感預測結果: %s' % label_to_word[label_dict[np.argmax(y_predict)]])
        return label_to_word[label_dict[np.argmax(y_predict)]]

    except KeyError as err:
        print("您輸入的句子有漢字不在詞彙表中，請重新輸入！")
        print("不在詞彙表中的單詞為：%s." % err)
        error = "您輸入的句子有漢字不在詞彙表中，請重新輸入！\n"+"不在詞彙表中的單詞為：%s." % err
        return error
