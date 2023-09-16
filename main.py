import os.path
import sys
import time
import jieba
import gensim
import re


# 传入过滤之后的数据，通过调用gensim.similarities.Similarity计算余弦相似度
def calc_similarity(text1, text2):
    texts = [text1, text2]
    dictionary = gensim.corpora.Dictionary(texts)  # 将文本中的单词映射到唯一的整数标识符
    corpus = [dictionary.doc2bow(text) for text in texts]  # 将文本转换为词袋
    similarity = gensim.similarities.Similarity('-Similarity-index', corpus,
                                                num_features=len(dictionary))  # 计算词袋中所有词的频率
    test_corpus_1 = dictionary.doc2bow(text1)  # 将要对比的文本转换为词袋
    cosine_sim = similarity[test_corpus_1][1]  # 计算余弦相似度
    return cosine_sim


# 读取文本文件
def get_file_contents(path):
    str = ''
    f = open(path, 'r', encoding='UTF-8')
    line = f.readline()
    while line:  # 把每一行串联起来，相当于把文本变成了一行
        str = str + line
        line = f.readline()
    f.close()
    return str


def filter(string):
    pattern = re.compile(u"[^a-zA-Z0-9\u4e00-\u9fa5]")  # 正则表达式，过滤掉非中文、非数字、非字母的字符
    string = pattern.sub("", string)  # 将string中匹配到的字符替换成空字符
    result = jieba.lcut(string)  # 分词
    return result


# 主函数
def main(original_file, plagiarized_file, output_file):
    if not os.path.exists(original_file):
        print("原文文件不存在")
        sys.exit(1)
    if not os.path.exists(plagiarized_file):
        print("抄袭版论文文件不存在")
        sys.exit(2)
    # 记录程序开始时间
    start_time = time.time()
    # 读取原文件和抄袭文件
    str1 = get_file_contents(original_file)
    str2 = get_file_contents(plagiarized_file)
    text1 = filter(str1)
    text2 = filter(str2)

    # 计算相似度
    similarity = calc_similarity(text1, text2)

    # 将相似度写入输出文件
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(f"文件{original_file}和文件{plagiarized_file}的相似度为：{similarity:.2f}")

    # 记录程序结束时间
    end_time = time.time()

    print(f"相似度: {similarity:.2f} | 运行时间: {end_time - start_time:.2f}秒")


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("用法: main.py [原文文件] [抄袭版论文的文件] [答案文件]")
        sys.exit(1)
    original_file = sys.argv[1]
    plagiarized_file = sys.argv[2]
    output_file = sys.argv[3]
    main(original_file, plagiarized_file, output_file)
