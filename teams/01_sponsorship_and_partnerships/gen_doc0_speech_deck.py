import os
import re
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx_utils import (
    init_document, add_header_banner, add_h1, add_h2, add_h3,
    add_body, add_bullet, add_callout, add_styled_table,
    HEX_AMBER, COLOR_NAVY, COLOR_AMBER, COLOR_MUTED
)

def build_doc0():
    output_path = r"e:\AWS SBGL\Events\Kairos\teams\01_sponsorship_and_partnerships\word_documents\00_KAIROS_2027_Sponsorship_Meeting_2Hour_Speech_Deck_and_Script.docx"
    doc = init_document("MEETING SPEECH DECK & MASTERCLASS SCRIPT")
    
    add_header_banner(
        doc,
        title="KAIROS 2027 — SPONSORSHIP TEAM MEETING",
        subtitle="Complete 2-Hour Speaker Script, Motivational Address & Masterclass\nSpeaker: Thenappan T — President & Student Builder Group Leader (AWS SBGL)",
        badges=["MEETING DATE: OCTOBER 17, 2026", "AUDIENCE: SPONSORSHIP TEAM (NIKKI & SQUAD)", "TONE: HIGH-ENERGY, COMMANDING, CANDID"]
    )
    
    add_callout(
        doc,
        "This is your complete speaking script for the 2-hour meeting on October 17, 2026. Every section represents a spoken block designed to be delivered with confidence. Use the cue boxes ([PAUSE], [WRITE ON BOARD], [Q&A PROMPT]) to control the room pacing. Memorize the core numbers in Appendix A so you never have to consult your laptop while speaking.",
        title="SPEAKER GUIDANCE & DELIVERY INSTRUCTIONS",
        style="warning"
    )
    
    # Read the markdown source
    md_path = r"e:\AWS SBGL\Events\Kairos\kairos_sponsorship_speech_deck.md"
    with open(md_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
        
    in_table = False
    table_headers = []
    table_rows = []
    
    i = 0
    while i < len(lines):
        line = lines[i].rstrip()
        
        # Check for table end if line doesn't start with |
        if in_table and (not line.startswith("|") or line.strip() == ""):
            if table_headers and table_rows:
                add_styled_table(doc, table_headers, table_rows)
            in_table = False
            table_headers = []
            table_rows = []
            
        if line.startswith("# ") and not line.startswith("## "):
            text = line.replace("# ", "").strip()
            add_h1(doc, text)
        elif line.startswith("## "):
            text = line.replace("## ", "").strip()
            # If it's a stage direction like [Walk in. Stand...]
            if text.startswith("[") and text.endswith("]"):
                add_callout(doc, text[1:-1], title="STAGE & ROOM DIRECTION", style="info")
            else:
                add_h2(doc, text)
        elif line.startswith("### "):
            text = line.replace("### ", "").strip()
            add_h3(doc, text)
        elif line.startswith("> "):
            quote_text = line.replace("> ", "").strip()
            add_callout(doc, quote_text, title="NOTE / EMPHASIS", style="warning")
        elif line.startswith("|") and line.endswith("|"):
            # Table row
            parts = [p.strip() for p in line.strip("|").split("|")]
            # Check if separator row
            if all(re.match(r"^:?-+:?$", p) for p in parts if p):
                i += 1
                continue
            if not in_table:
                in_table = True
                table_headers = parts
                table_rows = []
            else:
                table_rows.append(parts)
        elif line.startswith("- ") or line.startswith("* "):
            bullet_text = line[2:].strip()
            if ":" in bullet_text and not bullet_text.startswith("http"):
                prefix, rest = bullet_text.split(":", 1)
                add_bullet(doc, prefix.strip(), rest.strip())
            else:
                add_bullet(doc, "", bullet_text)
        elif line.strip().startswith("[WRITE ON BOARD:"):
            board_text = line.strip()[16:-1].strip()
            add_callout(doc, board_text, title="WRITE ON WHITEBOARD", style="warning")
        elif line.strip().startswith("[PAUSE]"):
            add_callout(doc, "Take a breath. Look around the room. Make eye contact with team members. Let the message sink in.", title="ACTION CUE: [PAUSE]", style="info")
        elif line.strip().startswith("[Q&A PROMPT:"):
            q_text = line.strip()[12:-1].strip()
            add_callout(doc, q_text, title="ENGAGEMENT CUE: [Q&A PROMPT]", style="info")
        elif line.strip() != "":
            # Plain paragraph text
            add_body(doc, line)
            
        i += 1
        
    if in_table and table_headers and table_rows:
        add_styled_table(doc, table_headers, table_rows)
        
    doc.save(output_path)
    print(f"Generated Doc 0: {output_path}")

if __name__ == "__main__":
    build_doc0()
