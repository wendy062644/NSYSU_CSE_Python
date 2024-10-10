german_dict = {}
english_dict = {}
translated_words = []
used_words = []
separators = [',', '!', ' ', '\n']

german_count = 0
english_count = 0
total_count = 0

english_to_german = 0

try:
# 讀取文本文件並處理內容
    with open("GE.txt", "r", encoding='utf-8') as file:
        for line in file:
            # 使用分割符 ":" 將每行分割成左右兩部分
            german_word, english_word = line.strip().split(" : ")
            # 將左邊的字放入德文字典中，右邊的字放入英文字典中
            german_dict[german_word] = english_word
            english_dict[english_word] = german_word

    output_file = open("translated.txt", "w")
    output_back_file = open("translated_back.txt", "w")

    def is_used(start, end, used):
        for i in range(start, end):
            if used[i]:
                return True
        return False

    def check_substrings(text):
        text = text.split()
        # 初始化结果列表
        result = []
        positions = []
        used = [False] * len(text)
        # 遍历所有可能的子序列
        for i in range(len(text)):
            for j in range(i + 1, len(text) + 1):
                string = " ".join(text[i:j])
                if not is_used(i, j, used):
                    if english_to_german and string in english_dict:
                        result.append(english_dict[string])
                        positions.append(i)
                        for k in range(i, j):
                            used[k] = True
                    elif not english_to_german and string in german_dict:
                        result.append(german_dict[string])
                        positions.append(i)
                        for k in range(i, j):
                            used[k] = True
        
        for i in range(len(text)):
            if not used[i]:
                result.append(text[i])
                positions.append(i)

        result = sorted(zip(positions, result), key=lambda x: x[0])
        result = [item[1] for item in result]
        result = " ".join(result)

        return result

    try:
        # 讀取原始文字檔案
        with open("original.txt", "r", encoding='utf-8') as file:
            # 逐行讀取文件內容
            for line in file:
                # 將每一行分割成單詞
                words = line.strip().split()
                # 對於每個單詞，檢查它是德文還是英文
                for word in words:
                    if word not in used_words:
                        add_one = 0
                    # 如果單詞在德文字典中，則增加德文計數器
                        if word.lower() in german_dict:
                            german_count += 1
                            add_one = 1
                    # 如果單詞在英文字典中，則增加英文計數器
                        if word.lower() in english_dict:
                            english_count += 1
                            add_one = 1
                        total_count += add_one
                        used_words.append(word)

        translated_line = ""
        if english_count / total_count >= 0.6:
            english_to_german = 1
        elif german_count / total_count >= 0.6:
            english_to_german = 0
        else:
            option = int(input("Please Enter the language(1.German 2.English): "))
            if option == 2:
                english_to_german = 1
        with open("original.txt", "r", encoding='utf-8') as file:
            for line in file:
                first = 1
                temp_word = ""
                for word in line:
                    if '\n' in word or ',' in word or '?' in word or '!' in word:
                        print(check_substrings(temp_word), end = word)
                        output_file.write(check_substrings(temp_word) + word)
                        temp_word = ""
                        first = 1
                    else:
                        if ' ' not in word:
                            temp_word += word.lower()
                            first = 0
                        else:
                            temp_word += word.lower()

        output_file.close()
        english_to_german = not english_to_german
        with open("translated.txt", "r") as file:
            for line in file:
                first = 1
                temp_word = ""
                for word in line:
                    if '\n' in word or ',' in word or '?' in word or '!' in word:
                        print(check_substrings(temp_word), end = word)
                        output_back_file.write(check_substrings(temp_word) + word)
                        temp_word = ""
                        first = 1
                    else:
                        if ' ' not in word:
                            temp_word += word.lower()
                            first = 0
                        else:
                            temp_word += word.lower()

        #print(translated_line)

    except FileNotFoundError:
        print("Error: 'original.txt' file not found.")

    output_back_file.close()
except FileNotFoundError:
    print("Error: 'GE.txt' file not found.")