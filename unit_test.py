import unittest
from main import get_file_contents, filter, calc_similarity, main


# 测试用例
class Case(unittest.TestCase):
    def test_get_file_contents(self):
        # 测试文件读取函数是否正确
        content = get_file_contents('test/orig.txt')
        self.assertTrue(len(content) > 0)  # 确保文件内容不为空

    def test_filter(self):
        # 测试文本预处理函数是否正确
        text = "这是一个测试文本，包含标点符号！"
        filtered_text = filter(text)
        expected_result = ['这是', '一个', '测试', '文本', '包含', '标点符号']
        self.assertEqual(filtered_text, expected_result)

    def test_calc_similarity1(self):
        # 测试相似度计算函数是否正确
        text1 = "这是一个测试文本，包含标点符号！"
        text2 = "这是一个测试文本，包含标点符号！"
        text1 = filter(text1)
        text2 = filter(text2)
        similarity = calc_similarity(text1, text2)
        self.assertEqual(similarity, 1)

    def test_calc_similarity0(self):
        # 测试相似度计算函数是否正确
        text1 = "这是一个测试文本，包含标点符号！"
        text2 = ""
        text1 = filter(text1)
        text2 = filter(text2)
        similarity = calc_similarity(text1, text2)
        self.assertEqual(similarity, 0)

    def test_main_test1(self):
        # 测试主函数是否正确
        original_file = 'test/orig.txt'
        plagiarized_file = 'test/orig_0.8_add.txt'
        output_file = 'test/output.txt'
        main(original_file, plagiarized_file, output_file)
        with open(output_file, 'r', encoding='utf-8') as file:
            result = file.read()
        expected_result = "文件test/orig.txt和文件test/orig_0.8_add.txt的相似度为：0.99"
        self.assertEqual(result, expected_result)

    def test_main_test2(self):
        # 测试主函数是否正确
        original_file = 'test/orig.txt'
        plagiarized_file = 'test/empty.txt'
        output_file = 'test/output.txt'
        main(original_file, plagiarized_file, output_file)
        with open(output_file, 'r', encoding='utf-8') as file:
            result = file.read()
        expected_result = "文件test/orig.txt和文件test/empty.txt的相似度为：0.00"
        self.assertEqual(result, expected_result)

    def test_main_test3(self):
        # 测试主函数是否正确
        original_file = 'test/orig.txt'
        plagiarized_file = 'test/orig_0.8_dis_1.txt'
        output_file = 'test/output.txt'
        main(original_file, plagiarized_file, output_file)
        with open(output_file, 'r', encoding='utf-8') as file:
            result = file.read()
        expected_result = "文件test/orig.txt和文件test/orig_0.8_dis_1.txt的相似度为：1.00"
        self.assertEqual(result, expected_result)

    def test_main_test4(self):
        # 测试主函数是否正确
        original_file = 'test/orig.txt'
        plagiarized_file = 'test/orig_0.8_dis_10.txt'
        output_file = 'test/output.txt'
        main(original_file, plagiarized_file, output_file)
        with open(output_file, 'r', encoding='utf-8') as file:
            result = file.read()
        expected_result = "文件test/orig.txt和文件test/orig_0.8_dis_10.txt的相似度为：0.99"
        self.assertEqual(result, expected_result)

    def test_main_test5(self):
        # 测试主函数是否正确
        original_file = 'test/orig.txt'
        plagiarized_file = 'test/orig_0.8_dis_15.txt'
        output_file = 'test/output.txt'
        main(original_file, plagiarized_file, output_file)
        with open(output_file, 'r', encoding='utf-8') as file:
            result = file.read()
        expected_result = "文件test/orig.txt和文件test/orig_0.8_dis_15.txt的相似度为：0.98"
        self.assertEqual(result, expected_result)

    def test_main_test6(self):
        # 测试原文件不存在的情形
        original_file = 'test/orig1.txt'
        plagiarized_file = 'test/orig_0.8_dis_15.txt'
        output_file = 'test/output.txt'
        # 如果原文件不存在，应该打印错误消息并返回非零退出码
        with self.assertRaises(SystemExit) as cm:
            main(original_file, plagiarized_file, output_file)

        # 检查退出码是否为1（表示错误退出）
        self.assertEqual(cm.exception.code, 1)

    def test_main_test7(self):
        # 测试主函数是否正确
        original_file = 'test/orig.txt'
        plagiarized_file = 'test/orig_del.txt'
        output_file = 'test/output.txt'
        main(original_file, plagiarized_file, output_file)
        with open(output_file, 'r', encoding='utf-8') as file:
            result = file.read()
        expected_result = "文件test/orig.txt和文件test/orig_del.txt的相似度为：0.81"
        self.assertEqual(result, expected_result)

    def test_main_test8(self):
        # 测试抄袭文件不存在的情形
        original_file = 'test/orig.txt'
        plagiarized_file = 'test/orig_0.txt'
        output_file = 'test/output.txt'
        # 如果抄袭文件不存在，应该打印错误消息并返回非零退出码
        with self.assertRaises(SystemExit) as cm:
            main(original_file, plagiarized_file, output_file)

        # 检查退出码是否为2（表示错误退出）
        self.assertEqual(cm.exception.code, 2)


if __name__ == "__main__":
    suite = unittest.TestSuite()  # 创建测试套件
    tests = [
        Case('test_get_file_contents'),
        Case('test_filter'),
        Case('test_calc_similarity1'),
        Case('test_calc_similarity0'),
        Case('test_main_test1'),
        Case('test_main_test2'),
        Case('test_main_test3'),
        Case('test_main_test4'),
        Case('test_main_test5'),
        Case('test_main_test6'),
        Case('test_main_test7'),
        Case('test_main_test8')
    ]
    suite.addTests(tests)  # 将测试用例加入测试套件中
    runner = unittest.TextTestRunner(verbosity=2)  # 创建测试运行器
    runner.run(suite)  # 执行测试套件
