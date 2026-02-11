#!/home/DEV/OpenClaw/.venv-report/bin/python
import argparse
from pathlib import Path
from fpdf import FPDF

FONT_PATH = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
LINE_WIDTH = 180  # safe width

def make_pdf(input_path: Path, output_path: Path, title: str = "Report"):
    text = input_path.read_text(encoding="utf-8")
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.add_font("DejaVu", "", FONT_PATH)
    pdf.add_font("DejaVu", "B", FONT_PATH)
    pdf.set_font("DejaVu", "B", 16)
    pdf.multi_cell(LINE_WIDTH, 10, title)
    pdf.ln(5)
    pdf.set_font("DejaVu", size=11)
    for line in text.splitlines():
        pdf.multi_cell(LINE_WIDTH, 8, line if line.strip() else "")
    pdf.output(str(output_path))


def main():
    parser = argparse.ArgumentParser(description="Convert a text/markdown file to PDF (simple).")
    parser.add_argument("input", type=Path, help="Input text/markdown file")
    parser.add_argument("output", type=Path, help="Output PDF path")
    parser.add_argument("--title", default="Report", help="PDF title")
    args = parser.parse_args()
    make_pdf(args.input, args.output, title=args.title)


if __name__ == "__main__":
    main()
