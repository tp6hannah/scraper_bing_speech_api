import jieba
import jieba.posseg as pseg
import jieba.analyse

from stt import listen_user_says


def split_by_Jieba(text):
    jieba.set_dictionary("dict/dict.txt.big.txt")
    jieba.load_userdict("dict/userdict.txt")
    # print("/".join(seg_list))
    simple_list = []
    simple_list = list(jieba.cut(text))
    return simple_list

# your key here
BING_KEY = "3dcb2e113d824096bd152864f58b6358"


# 使用 bing speech api 音檔轉文字的服務
user_says = listen_user_says(BING_KEY)
print(user_says,type(user_says))

# jieba 分詞
sep_words = split_by_Jieba(user_says)

for item in sep_words:
    print("item >>> "+ item)
    if item == u'運動' or item == u'體育':
        print("user want sports news")



