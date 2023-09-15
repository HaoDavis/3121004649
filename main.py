import sys
import time
import jieba
import gensim
import re

#传入过滤之后的数据，通过调用gensim.similarities.Similarity计算余弦相似度
def calc_similarity(text1,text2):
    texts=[text1,text2]
    dictionary = gensim.corpora.Dictionary(texts)
    corpus = [dictionary.doc2bow(text) for text in texts]
    similarity = gensim.similarities.Similarity('-Similarity-index', corpus, num_features=len(dictionary))
    test_corpus_1 = dictionary.doc2bow(text1)
    cosine_sim = similarity[test_corpus_1][1]
    return cosine_sim

# 读取文本文件
def get_file_contents(path):
    str = ''
    f = open(path, 'r', encoding='UTF-8')
    line = f.readline()
    while line:
        str = str + line
        line = f.readline()
    f.close()
    return str

#将读取到的文件内容先进行jieba分词，然后再把标点符号、转义符号等特殊符号过滤掉
def filter(str):
    str = jieba.lcut(str)
    result = []
    for tags in str:
        if (re.match(u"[a-zA-Z0-9\u4e00-\u9fa5]", tags)):
            result.append(tags)
        else:
            pass
    return result

# 主函数
def main():
    # if len(sys.argv) != 4:
    #     print("用法: main.py [原文文件] [抄袭版论文的文件] [答案文件]")
    #     sys.exit(1)

    # 记录程序开始时间
    start_time = time.time()

    # original_file = sys.argv[1]
    # plagiarized_file = sys.argv[2]
    # output_file = sys.argv[3]
    original_file = 'test\orig.txt'
    plagiarized_file = 'test\orig_0.8_add.txt'
    output_file = 'test\output.txt'
    try:
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

        print(f"相似度: {similarity:.2f}| 运行时间: {end_time - start_time:.2f}秒")
    except Exception as e:
        print(f"发生错误: {str(e)}")

if __name__ == '__main__':
    main()