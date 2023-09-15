import sys
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
nltk.download('punkt')
nltk.download('stopwords')

# 计算文本的相似度
def calculate_similarity(original_text, plagiarized_text):
    # 创建TF-IDF向量化器
    vectorizer = TfidfVectorizer()

    # 将原文本和抄袭文本转换为TF-IDF向量
    tfidf_matrix = vectorizer.fit_transform([original_text, plagiarized_text])

    # 计算余弦相似度
    cosine_sim = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1])

    return cosine_sim[0][0]

# 读取文本文件
def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

# 主函数
def main():
    if len(sys.argv) != 4:
        print("用法: main.py [原文文件] [抄袭版论文的文件] [答案文件]")
        sys.exit(1)

    original_file = sys.argv[1]
    plagiarized_file = sys.argv[2]
    output_file = sys.argv[3]

    try:
        # 读取原文件和抄袭文件
        original_text = read_file(original_file)
        plagiarized_text = read_file(plagiarized_file)

        # 计算相似度
        similarity = calculate_similarity(original_text, plagiarized_text)

        # 将相似度写入输出文件
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(f"文件{original_file}和文件{plagiarized_file}的相似度为：{similarity:.2f}")

        print(f"相似度: {similarity:.2f}")
    except Exception as e:
        print(f"发生错误: {str(e)}")