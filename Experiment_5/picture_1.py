import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt


# 读取文本文件
def read_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text


# 中文分词
def chinese_word_segmentation(text):
    word_list = jieba.cut(text, cut_all=False)
    return ' '.join(word_list)


# 生成词云
def generate_word_cloud(text):
    wordcloud = WordCloud(font_path='simhei.ttf',  # 设置字体（需要有这个字体文件，否则中文无法显示）
                          width=900, height=500, max_font_size=50, min_font_size=10,
                          background_color='white').generate(text)
    return wordcloud


# 显示词云图
def display_word_cloud(wordcloud):
    plt.figure(figsize=(16, 9))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')  # 不显示坐标轴
    plt.show()


# 主函数
def main():
    file_path = '我和我的祖国.txt'  # 设置文本文件路径
    text = read_text_file(file_path)
    segmented_text = chinese_word_segmentation(text)
    wordcloud = generate_word_cloud(segmented_text)
    display_word_cloud(wordcloud)


if __name__ == '__main__':
    main()
