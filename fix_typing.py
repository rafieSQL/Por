
import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Replace the massive typingParagraphs with commonWords
pattern_array = re.compile(r"const typingParagraphs = \[\n.*?\];", re.DOTALL)

common_words_js = """const commonWords = ["the","of","to","and","a","in","is","it","you","that","he","was","for","on","are","as","with","his","they","I","at","be","this","have","from","or","one","had","by","word","but","not","what","all","were","we","when","your","can","said","there","use","an","each","which","she","do","how","their","if","will","up","other","about","out","many","then","them","these","so","some","her","would","make","like","him","into","time","has","look","two","more","write","go","see","number","no","way","could","people","my","than","first","water","been","call","who","oil","its","now","find","long","down","day","did","get","come","made","may","part","over","new","sound","take","only","little","work","know","place","year","live","me","back","give","most","very","after","thing","our","just","name","good","sentence","man","think","say","great","where","help","through","much","before","line","right","too","mean","old","any","same","tell","boy","follow","came","want","show","also","around","form","three","small","set","put","end","does","another","well","large","must","big","even","such","because","turn","here","why","ask","went","men","read","need","land","different","home","us","move","try","kind","hand","picture","again","change","off","play","spell","air","away","animal","house","point","page","letter","mother","answer","found","study","still","learn","should","America","world"];"""

content = pattern_array.sub(common_words_js, content)

# 2. Update loadParagraph function to generate 300 words dynamically
old_load_func = """        function loadParagraph() {
            const ranIndex = Math.floor(Math.random() * typingParagraphs.length);
            
            // Build HTML string once to prevent reflows inside loop (Massive Astro-like performance win)
            const htmlString = typingParagraphs[ranIndex]
                .split("")
                .map(char => `<span>${char}</span>`)
                .join("");
            
            typingText.innerHTML = htmlString;
            cachedCharacters = typingText.querySelectorAll("span");
            cachedCharacters[0].classList.add("active");
        }"""

new_load_func = """        function loadParagraph() {
            // Generate 300 random words (perfect length for 60s test, prevents DOM lag)
            let textArray = [];
            for (let i = 0; i < 300; i++) {
                textArray.push(commonWords[Math.floor(Math.random() * commonWords.length)]);
            }
            const randomText = textArray.join(" ").toLowerCase();
            
            // Build HTML string once to prevent reflows inside loop
            const htmlString = randomText
                .split("")
                .map(char => `<span>${char}</span>`)
                .join("");
            
            typingText.innerHTML = htmlString;
            cachedCharacters = typingText.querySelectorAll("span");
            cachedCharacters[0].classList.add("active");
        }"""

content = content.replace(old_load_func, new_load_func)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

