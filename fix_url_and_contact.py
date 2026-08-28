
import re

# 1. Update index.html
with open("index.html", "r", encoding="utf-8") as f:
    index_content = f.read()

# Add button to contact section
button_html = """
                        <a href="./projects.html" class="inline-flex items-center justify-center gap-2.5 px-6 py-3.5 rounded-2xl bg-rust text-white font-inter text-sm font-semibold hover:bg-[#9A4826] hover:scale-[1.02] active:scale-[0.98] transition-all shadow-[0_6px_20px_rgba(176,85,47,0.25)] group">
                            <svg class="size-4 group-hover:scale-110 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M21 13.255A23.931 23.931 0 0112 15c-3.183 0-6.22-.62-9-1.745M16 6V4a2 2 0 00-2-2h-4a2 2 0 00-2 2v2m4 6h.01M5 20h14a2 2 0 002-2V8a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/></svg>
                            <span>See more of my projects</span>
                        </a>"""

# find instagram button
ig_pattern = re.compile(r"(<a href=\"https://instagram\.com/[^\"]*\"[^>]*>.*?</a>)", re.DOTALL)
ig_match = ig_pattern.search(index_content)
if ig_match:
    ig_html = ig_match.group(1)
    # append our new button after it
    index_content = index_content[:ig_match.end()] + "\n" + button_html + index_content[ig_match.end():]

# change href="projects.html" to href="./projects.html" in index.html to be safe (optional but good practice)
index_content = index_content.replace('href="projects.html"', 'href="./projects.html"')

with open("index.html", "w", encoding="utf-8") as f:
    f.write(index_content)

# 2. Update projects.html
with open("projects.html", "r", encoding="utf-8") as f:
    projects_content = f.read()

# Change index.html to ./
projects_content = projects_content.replace('href="index.html"', 'href="./"')

with open("projects.html", "w", encoding="utf-8") as f:
    f.write(projects_content)

