import os
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx_utils import (
    init_document, add_header_banner, add_h1, add_h2, add_h3,
    add_body, add_bullet, add_callout, add_styled_table,
    HEX_AMBER, COLOR_NAVY, COLOR_SLATE_BLUE, COLOR_DARK_TEXT
)

def build_doc4():
    output_path = r"e:\AWS SBGL\Events\Kairos\teams\01_sponsorship_and_partnerships\word_documents\04_KAIROS_2027_Corporate_Sponsorship_MoU_and_Agreement_Template.docx"
    doc = init_document("CORPORATE SPONSORSHIP MOU & LEGAL AGREEMENT")
    
    add_header_banner(
        doc,
        title="MEMORANDUM OF UNDERSTANDING (MoU)",
        subtitle="Corporate Sponsorship & Partnership Agreement\nSathyabama Institute of Science and Technology  •  AWS Student Builder Group",
        badges=[
            "REF: SIST/CSE/AWS-SBG/KAIROS2027/MOU/2026",
            "STANDALONE LEGAL TEMPLATE",
            "OFFICIAL UNIVERSITY ESCROW",
            "CHENNAI JURISDICTION"
        ]
    )
    
    add_callout(
        doc,
        "This is the official legal contract template for KAIROS 2027. It contains all legally vetted clauses, financial escrow terms, intellectual property ownership protections, and execution signature blocks. Once agreed with the corporate partner, fill in the bracketed blanks, print on institutional bond paper or execute via digital signature, and submit to the University Accounts Office.",
        title="LEGAL TEMPLATE GUIDANCE",
        style="info"
    )
    
    # Agreement Metadata Table
    meta_headers = ["Agreement Parameter", "Contract Specification"]
    meta_data = [
        ["Agreement Title", "Memorandum of Understanding & Corporate Sponsorship Agreement"],
        ["Agreement Reference No.", "SIST/CSE/AWS-SBG/KAIROS2027/MOU/2026-[SERIAL_NO]"],
        ["Event Name", "KAIROS 2027 (Grand Edition) — National 48-Hour Student Hackathon"],
        ["Event Dates", "January 22 – 24, 2027"],
        ["Venue", "Sathyabama Institute of Science and Technology, Chennai, Tamil Nadu – 600119"],
        ["Host Entity", "School of Computing, Department of CSE & AWS Student Builder Group"]
    ]
    add_styled_table(doc, meta_headers, meta_data)
    
    add_h2(doc, "PARTIES TO THE AGREEMENT")
    add_body(doc, "This Memorandum of Understanding (hereinafter referred to as 'MoU' or 'Agreement') is entered into on this _____ day of ____________, 2026, by and between:")
    
    parties_text = (
        "1. SATHYABAMA INSTITUTE OF SCIENCE AND TECHNOLOGY (Deemed to be University under Section 3 of the UGC Act, 1956), having its administrative campus at Jeppiaar Nagar, Rajiv Gandhi Salai, Chennai, Tamil Nadu 600119, represented by the Dean, School of Computing, and Faculty Coordinators of the AWS Student Builder Group (hereinafter referred to as the 'HOST INSTITUTION' or 'ORGANIZER');\n\n"
        "AND\n\n"
        "2. [CORPORATE SPONSOR ENTITY NAME], a corporation incorporated under the Companies Act, having its registered corporate office at ____________________________________________________________________, represented by its authorized executive signatory ____________________________ (Designation: ______________________) (hereinafter referred to as the 'CORPORATE PARTNER' or 'SPONSOR')."
    )
    add_callout(doc, parties_text, title="CONTRACTING ENTITIES", style="warning")
    
    # Clause 1: Recitals
    add_h1(doc, "1. Recitals & Objectives")
    add_body(doc, "WHEREAS the Organizer is hosting KAIROS 2027 (Grand Edition), an elite national 48-hour continuous hackathon assembling 100 shortlisted finalist teams (teams of 4–6 students, ~400–600 student builders) filtered from over 2,000+ applicant squads nationwide under a strict 100% Free / Zero Entry Fee meritocracy model;")
    add_body(doc, "WHEREAS the Sponsor desires to support technology innovation, foster developer talent, promote technical challenges, and interface with top-tier student engineers as an official corporate partner;")
    add_body(doc, "NOW, THEREFORE, in consideration of the mutual covenants contained herein, the parties agree as follows:")

    # Clause 2: Tier & Consideration
    add_h1(doc, "2. Sponsorship Tier & Financial Consideration")
    add_body(doc, "The Sponsor hereby commits to partner with the Organizer under the following selected tier:")
    
    tier_select_data = [
        ["Selected Tier (Check One)", "Sponsorship Contribution", "Key Institutional Category"],
        ["[  ] Title Presenting Partner", "₹ 2,00,000 /- (Rupees Two Lakhs Only)", "Apex Event Co-Title & Naming Rights"],
        ["[  ] Co-Powered By Partner", "₹ 1,00,000 /- (Rupees One Lakh Only)", "Co-Branding & Secondary Stage Crest"],
        ["[  ] Associate / Gold Partner", "₹ 50,000 /- (Rupees Fifty Thousand Only)", "Official Associate & Standee Presence"],
        ["[  ] Track & Bounty Partner", "₹ 25,000 /- (Rupees Twenty-Five Thousand Only)", "Dedicated Track Bounty & Evaluation"],
        ["[  ] In-Kind / Product Partner", "Product / Service Inventory Valuation", "Official Fuel / Tooling Partner"]
    ]
    add_styled_table(doc, tier_select_data[0], tier_select_data[1:])
    
    add_bullet(doc, "Total Agreed Financial Consideration", "₹ __________________ /- (Rupees ____________________________________________________ Only) (+ applicable GST if mandated).")
    add_bullet(doc, "Payment Terms & Timeline", "100% of the financial consideration shall be transferred via NEFT/RTGS into the Host Institution's designated project bank account within fifteen (15) business days of signing this MoU or no later than December 10, 2026.")

    # Clause 3: Obligations of Organizer
    add_h1(doc, "3. Obligations of the Organizer")
    add_body(doc, "The Organizer agrees to deliver the following agreed benefits in full, based on the selected tier:")
    add_bullet(doc, "1. Main Stage & Venue Brand Exposure", "Prominent logo placement across the 3840×1920 Main Stage LED Wall, 20x10ft stage backdrop banner, 12x8ft foyer welcome banner, 16 vertical rollup standees, and participant ID smart badges.")
    add_bullet(doc, "2. Keynote Address & Executive Speaking Slots", "Allocation of dedicated speaking time during the Inaugural Ceremony (20 minutes for Title, 10 minutes for Co-Powered By) on the main auditorium stage.")
    add_bullet(doc, "3. Grand Jury & Evaluator Representation", "Designation of official jury seats on the Grand Finale Evaluation Plenary (2 seats for Title, 1 seat for Co-Powered By) to evaluate student prototypes.")
    add_bullet(doc, "4. Talent Directory & Recruitment Telemetry", "Compliant provision of verified digital resume directory and GitHub telemetry of participants (Full national database for Title, Top 250 for Co-Powered By, Top 100 for Associate).")
    add_bullet(doc, "5. Continuous 48-Hour Live Broadcast Integration", "Broadcast of commercial video stingers (30 seconds every 2 hours for Title, 15 seconds every 4 hours for Co-Powered By) across global live streams.")
    add_bullet(doc, "6. Exhibition Space / Experiential Lounge", "Provision of dedicated booth space (10x10ft for Title, 6x6ft for Co-Powered By) in the grand foyer for corporate interaction.")

    # Clause 4: Obligations of Sponsor
    add_h1(doc, "4. Obligations of the Sponsor")
    add_bullet(doc, "1. Asset Delivery", "Provide high-resolution vector logos (SVG, EPS, or 300 DPI PNG) and brand guidelines within five (5) business days of signing this MoU.")
    add_bullet(doc, "2. Technical Challenge Statements", "Provide technical problem statements, developer APIs, SDK documentation, or sandbox credentials by December 15, 2026 (if applicable).")
    add_bullet(doc, "3. Jury Nomination", "Formally nominate designated corporate jury members or evaluators by January 10, 2027.")
    add_bullet(doc, "4. Consideration Transfer", "Transfer the agreed sponsorship consideration in accordance with Section 2.")

    # Clause 5: Intellectual Property
    add_h1(doc, "5. Intellectual Property Rights (100% Student Ownership)")
    add_callout(
        doc,
        "It is mutually and unequivocally affirmed that ALL INTELLECTUAL PROPERTY (IP), SOFTWARE ARCHITECTURES, SOURCE CODE, AND PROTOTYPES CREATED BY STUDENT PARTICIPANT TEAMS DURING KAIROS 2027 REMAIN 100% THE EXCLUSIVE PROPERTY OF THE RESPECTIVE STUDENT DEVELOPERS.\n\n"
        "The Sponsor is granted no automatic intellectual property ownership or assignment rights over participant code. The Sponsor may independently negotiate licensing, commercial acquisition, or employment offers directly with student developers following the conclusion of the event without institutional interference.",
        title="CRITICAL CLAUSE: 100% STUDENT CODE & IP PROTECTION",
        style="warning"
    )

    # Clause 6: Data Privacy
    add_h1(doc, "6. Confidentiality & Data Privacy")
    add_body(doc, "All student resume databases, GitHub telemetry, and contact details provided to the Sponsor are confidential and intended exclusively for the Sponsor's internal recruitment and developer outreach. The Sponsor shall not sell, lease, transfer, or disclose participant records to any third party.")

    # Clause 7: Term & Force Majeure
    add_h1(doc, "7. Term, Termination & Force Majeure")
    add_body(doc, "This Agreement enters into force upon execution and remains valid until February 15, 2027 (conclusion of post-event reporting). Neither party shall be held liable for failure to perform due to unforeseen events beyond reasonable control (natural disasters, government lockdowns, or severe grid disruptions). In the event of event postponement, all sponsorship rights shall roll over to the rescheduled dates without forfeiture.")

    # Clause 8: Governing Law
    add_h1(doc, "8. Governing Law & Dispute Resolution")
    add_body(doc, "This MoU shall be governed by and construed in accordance with the laws of the Republic of India. Any disputes arising out of or in connection with this Agreement shall be settled amicably through good-faith negotiation between the Dean, School of Computing (Sathyabama) and the Corporate Executive. Unresolved disputes shall be subject to the exclusive jurisdiction of the civil courts in Chennai, Tamil Nadu.")

    # Clause 9: Institutional Bank Details
    add_h1(doc, "9. Official Bank Account Details for Fund Transfer")
    add_body(doc, "All financial consideration must be remitted strictly into the official audited university bank account:")
    
    bank_data = [
        ["Beneficiary / Account Name", "SATHYABAMA INSTITUTE OF SCIENCE AND TECHNOLOGY"],
        ["Bank Name", "Indian Bank"],
        ["Branch Address", "Sathyabama University Branch, Jeppiaar Nagar, Chennai – 600119"],
        ["Account Type", "Institutional Savings / Project Account"],
        ["IFSC Code", "IDIB000S201"],
        ["MICR Code", "600019156"],
        ["Remittance Purpose Code", "KAIROS 2027 Corporate Sponsorship Escrow"]
    ]
    add_styled_table(doc, ["Field", "Official Record"], bank_data)

    # Clause 10: Signatures
    add_h1(doc, "10. Signatures & Ratification Execution Page")
    add_body(doc, "IN WITNESS WHEREOF, the authorized representatives of the parties hereto have executed this Memorandum of Understanding as of the date first written above:")
    
    sig_matrix_headers = ["For the Corporate Partner", "For Sathyabama Institute of Science and Technology"]
    sig_matrix_data = [
        [
            "Authorized Signature: _______________________\n\n"
            "Full Name: ________________________________\n\n"
            "Official Title: _____________________________\n\n"
            "Company / Entity: __________________________\n\n"
            "Corporate Seal / Stamp:\n\n\n"
            "Date: ____________________________________",
            
            "Authorized Signature: _______________________\n\n"
            "Dr. L. Lakshmanan\n"
            "Dean, School of Computing\n"
            "Sathyabama Institute of Science and Technology\n\n"
            "Co-Signature: _____________________________\n\n"
            "Dr. K. Ashok Kumar & Dr. Balapriya .S\n"
            "Faculty Coordinators, AWS Student Builder Group\n\n"
            "Co-Signature: _____________________________\n\n"
            "Thenappan T (Reg: 44110855)\n"
            "President & SBGL, AWS Student Builder Group\n\n"
            "Institutional Seal: \n\n"
            "Date: ____________________________________"
        ]
    ]
    add_styled_table(doc, sig_matrix_headers, sig_matrix_data)
    
    add_h3(doc, "Witnesses to the Agreement:")
    witness_data = [
        ["Witness 1 (Corporate Partner)", "Witness 2 (Organizer / AWS SBG)"],
        [
            "Signature: ______________________________\nName: _________________________________\nTitle: __________________________________",
            "Signature: ______________________________\nName: Nikki (Nangaiyar M) (Reg: 44612059)\nTitle: Chief Partnerships & Finance Officer"
        ]
    ]
    add_styled_table(doc, witness_data[0], witness_data[1:])
    
    doc.save(output_path)
    print(f"Generated Doc 4: {output_path}")

if __name__ == "__main__":
    build_doc4()
