
import random
import re

common_words = "the of to and a in is it you that he was for on are as with his they I at be this have from or one had by word but not what all were we when your can said there use an each which she do how their if will up other about out many then them these so some her would make like him into time has look two more write go see number no way could people my than first water been call who oil its now find long down day did get come made may part over new sound take only little work know place year live me back give most very after thing our just name good sentence man think say great where help through much before line right too mean old any same tell boy follow came want show also around form three small set put end does another well large must big even such because turn here why ask went men read need land different home us move try kind hand picture again change off play spell air away animal house point page letter mother answer found study still learn should America world".split()

words = [random.choice(common_words) for _ in range(2500)]
typing_text = " ".join(words)
# Let's capitalize first letter and add period at the end so it looks like a sentence, or just raw words.
# Standard monkeytype uses lowercase raw words. Let's use lowercase raw words.
# Actually, the user asked for "kalimat minimal ada 2000 kata" (a sentence/text with at least 2000 words).
# Let's make sentences out of it.
text_parts = []
for i in range(0, 2500, 15):
    sentence = " ".join(words[i:i+15]).capitalize() + "."
    text_parts.append(sentence)

final_text = " ".join(text_parts).replace("\n", "").replace("\r", "").replace("\"", "\\\"")

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Append to typingParagraphs
replacement = "const typingParagraphs = [\n            \"" + final_text + "\",\n"
content = re.sub(r"const typingParagraphs = \[", replacement, content)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

