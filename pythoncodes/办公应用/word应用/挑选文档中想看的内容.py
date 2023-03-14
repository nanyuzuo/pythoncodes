# TODO 一份口语备考资料，一共28页，里面有万能思路、适用题目、练习以及答案。
# TODO 只看思路、题目、练习，不看答案
# TODO 万能思路”是Word文档中的Title（标题)
# TODO “适用题目”是Word文档中的Heading 1（标题 1）
# TODO “练习”是Word文档中的Heading 2（标题 2）
# TODO “答案”是Word文档中的Normal（正文）
# TODO 使用import导入docx
import docx

# TODO 读取备考资料的Word文档，并赋值给变量review
review = docx.Document("/Users/tingting/TOEFL/托福口语-万能理由和答案.docx")

# TODO 遍历复习资料中所有的段落
for para in review.paragraphs:

    # TODO 获取每个段落的样式的名称，并赋值给变量styleName
    styleName = para.style.name

    # TODO 使用if语句判断该段落是否是万能思路、题目或练习
    if styleName in ["Title","Heading 1","Heading 2"]:

        # TODO 如果是，则使用print格式化输出该段落的文本内容
        print(para.text)