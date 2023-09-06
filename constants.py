APIKEY = "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"
prompt_template = "下面我让你来充当翻译家，你的目标是把任何语言翻译成中文，翻译时不要带翻译腔，而是要翻译得自然、流畅和地道，忠实地反映原文的意思，不能出现遗漏或者添加，并保持专业性。中文回答.翻译以下文章的所有内容,不要带有任何除中文的语言: "
prompt_intext = '''Translate everything after the first colon into Chinese with natural, smooth, and authentic tone, and faithfully reflecting the original meaning, without omissions or additions, and maintaining professionalism : 'MMW 15 (A00 & B00 Tracks)             SUMMER REMOTE 2023 (8/7-9/8)  MMW 15: The Contemporary Era: Individual and Social Responsibility in the Modern World   Prof. Edmond Chang      e6chang@ucsd.edu  Office Hours: Wednesdays 1:00-3:00 pm on Zoom: https://ucsd.zoom.us/j/97013947777           All course video lectures, supplemental material, assignments, and review guide will be posted on the UCSD Canvas course site. ' '''
p_English = "Translate everything after the first colon into Chinese and only give me the translation with natural, smooth, and authentic tone, and faithfully reflecting the original meaning : '"

t = "结果以json格式输出,例如{\"result\",\"这里是翻译结果\"}"

count = ""

