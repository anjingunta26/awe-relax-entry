import os

out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out, exist_ok=True)
# Revisi: setiap baris pendek dan jeda napas di akhir kalimat supaya napas pembaca ikut melambat.
text = (
    "The kettle hums. You do not need to answer it.\n"
    "Steam writes its small alphabet on the cold window,\n"
    "and the light behind you is already warm enough.\n"
)
with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(text)
