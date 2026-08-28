
import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Add variable
if "const playerText =" not in content:
    content = content.replace(
        "const bgVideo = document.getElementById(\"bgVideo\");",
        "const bgVideo = document.getElementById(\"bgVideo\");\n            const playerText = document.getElementById(\"playerTextContainer\");"
    )
    content = content.replace(
        "const bgVideo = document.getElementById('bgVideo');",
        "const bgVideo = document.getElementById('bgVideo');\n            const playerText = document.getElementById('playerTextContainer');"
    )

# 2. Add class on play
content = content.replace(
    "if (vinylRecord) vinylRecord.style.animationPlayState = 'running';",
    "if (vinylRecord) vinylRecord.style.animationPlayState = 'running';\n                            if (playerText) playerText.classList.add('text-depressed');"
)

# 3. Remove class on pause and ended (both end with paused)
content = content.replace(
    "if (vinylRecord) vinylRecord.style.animationPlayState = 'paused';",
    "if (vinylRecord) vinylRecord.style.animationPlayState = 'paused';\n                        if (playerText) playerText.classList.remove('text-depressed');"
)

# Note: The third replace might hit both pause and ended if they are identical. Let's use regex or just let it replace both.
# Let's replace the double quotes in my string matching.

