
import os

base_dir = "."
sidebar_file = os.path.join(base_dir, "_sidebar.md")

def generate_sidebar():
    with open(sidebar_file, "w", encoding="utf-8") as f:
        f.write("- [首页](README.md)\n")

        for folder in sorted(os.listdir(base_dir), reverse=True):
            folder_path = os.path.join(base_dir, folder)
            if os.path.isdir(folder_path) and folder != ".git":
                f.write(f"- [{folder}]({folder}/)\n")
                for md_file in sorted(os.listdir(folder_path), reverse=True):
                    if md_file.endswith(".md") and md_file != "README.md":
                        f.write(f"  - [{md_file.replace('.md', '')}]({folder}/{md_file})\n")

    print(f"✅ `_sidebar.md` 已生成！")

generate_sidebar()
