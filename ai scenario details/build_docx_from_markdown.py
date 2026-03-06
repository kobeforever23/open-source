from __future__ import annotations

import html
import subprocess
from pathlib import Path

import markdown

BASE = Path(__file__).resolve().parent
FILES = [
    'AI_Scenario_Committee_Report_2026-03-06.md',
    'AI_Scenario_Committee_One_Pager_2026-03-06.md',
    'AI_Scenario_Committee_Speaking_Script_2026-03-06.md',
]

CSS = """
body {
  font-family: Georgia, serif;
  font-size: 12pt;
  line-height: 1.35;
  margin: 48px;
  color: #111111;
}
h1, h2, h3, h4 {
  font-family: Helvetica, Arial, sans-serif;
  color: #111111;
  margin-top: 18px;
  margin-bottom: 8px;
}
h1 { font-size: 22pt; border-bottom: 1px solid #888888; padding-bottom: 6px; }
h2 { font-size: 15pt; }
h3 { font-size: 12pt; }
p, li { margin-bottom: 8px; }
ul, ol { margin-top: 0; margin-bottom: 10px; }
table {
  border-collapse: collapse;
  width: 100%;
  margin: 12px 0 16px 0;
  font-size: 10pt;
}
th, td {
  border: 1px solid #999999;
  padding: 6px 8px;
  vertical-align: top;
}
th {
  background: #ececec;
  font-family: Helvetica, Arial, sans-serif;
}
code {
  font-family: Menlo, monospace;
  font-size: 10pt;
  background: #f3f3f3;
  padding: 1px 3px;
}
blockquote {
  margin: 12px 0;
  padding-left: 12px;
  border-left: 3px solid #888888;
  color: #333333;
}
"""

HTML_TEMPLATE = """<!DOCTYPE html>
<html>
<head>
<meta charset=\"utf-8\" />
<style>{css}</style>
</head>
<body>
{body}
</body>
</html>
"""


def build_html(md_path: Path) -> Path:
    text = md_path.read_text()
    body = markdown.markdown(
        text,
        extensions=['tables', 'fenced_code', 'sane_lists', 'nl2br'],
        output_format='html5',
    )
    html_text = HTML_TEMPLATE.format(css=CSS, body=body)
    html_path = md_path.with_suffix('.html')
    html_path.write_text(html_text)
    return html_path


def convert_html_to_docx(html_path: Path) -> None:
    docx_path = html_path.with_suffix('.docx')
    subprocess.run(
        ['textutil', '-convert', 'docx', str(html_path), '-output', str(docx_path)],
        check=True,
    )


def main() -> None:
    for name in FILES:
        md_path = BASE / name
        html_path = build_html(md_path)
        convert_html_to_docx(html_path)


if __name__ == '__main__':
    main()
