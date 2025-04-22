from block_markdown import markdown_to_html_node


def get_file_contents(file_path):
    file = open(file_path, 'r')
    content = file.read()
    file.close()
    return content

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    from_content = get_file_contents(from_path)
    template_content = get_file_contents(template_path)
    html_string = markdown_to_html_node(from_content).to_html()
    title = extract_title(from_content)
    html_page = template_content.replace("{{ Title }}", title).replace("{{ Content }}", html_string)
    dest_file = open(dest_path, 'w')
    dest_file.write(html_page)
    dest_file.close()

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line.split("# ")[1].strip()
    raise Exception("Markdown should have title")
