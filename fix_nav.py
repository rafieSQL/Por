
import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Fix Mobile Nav
# Find the whole mobile nav block
mobile_nav_pattern = re.compile(r"(<!-- Mobile Bottom Nav -->\s*<nav[^>]*>.*?)</nav>", re.DOTALL)
mobile_nav_match = mobile_nav_pattern.search(content)

if mobile_nav_match:
    mobile_nav = mobile_nav_match.group(1)
    
    # Extract projects link
    projects_link_pattern = re.compile(r"(\s*<a href=\"projects\.html\" target=\"_blank\" class=\"[^\"]*\">.*?</a>)", re.DOTALL)
    projects_link_match = projects_link_pattern.search(mobile_nav)
    
    if projects_link_match:
        projects_link = projects_link_match.group(1)
        # Remove it from its current position
        mobile_nav = mobile_nav.replace(projects_link, "")
        
        # Remove target="_blank"
        projects_link = projects_link.replace(' target="_blank"', "")
        
        # Insert it at the end (before </nav>)
        mobile_nav = mobile_nav + projects_link + "\n    "
        
        content = content[:mobile_nav_match.start()] + mobile_nav + "</nav>" + content[mobile_nav_match.end():]

# Fix Desktop Nav
desktop_nav_pattern = re.compile(r"(<!-- Desktop Nav -->\s*<nav[^>]*>\s*<div[^>]*>.*?</div>\s*</nav>)", re.DOTALL)
desktop_nav_match = desktop_nav_pattern.search(content)

if desktop_nav_match:
    desktop_nav = desktop_nav_match.group(1)
    
    # Extract projects link
    projects_link_pattern = re.compile(r"(\s*<a href=\"projects\.html\" target=\"_blank\" class=\"[^\"]*\">Projects.*?</a>)", re.DOTALL)
    projects_link_match = projects_link_pattern.search(desktop_nav)
    
    if projects_link_match:
        projects_link = projects_link_match.group(1)
        # Remove it from current position
        desktop_nav = desktop_nav.replace(projects_link, "")
        
        # Remove target="_blank" and the external SVG icon
        # The SVG icon starts with <svg class="w-3 h-3
        projects_link = projects_link.replace(' target="_blank"', "")
        projects_link = re.sub(r" <svg class=\"w-3 h-3.*?</svg>", "", projects_link)
        
        # Find where organization link ends and insert projects_link there
        org_link_pattern = re.compile(r"(<a href=\"#organization\"[^>]*>Organization</a>)")
        org_link_match = org_link_pattern.search(desktop_nav)
        
        if org_link_match:
            insert_pos = org_link_match.end()
            desktop_nav = desktop_nav[:insert_pos] + projects_link + desktop_nav[insert_pos:]
            
        content = content[:desktop_nav_match.start()] + desktop_nav + content[desktop_nav_match.end():]

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

