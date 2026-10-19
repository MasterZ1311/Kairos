import os
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx_utils import (
    init_document, add_header_banner, add_h1, add_h2, add_h3,
    add_body, add_bullet, add_callout, add_styled_table,
    HEX_AMBER, COLOR_NAVY, COLOR_SLATE_BLUE, COLOR_DARK_TEXT
)

def build_doc3():
    output_path = r"e:\AWS SBGL\Events\Kairos\teams\01_sponsorship_and_partnerships\word_documents\03_KAIROS_2027_Official_Corporate_Sponsorship_Proposal_Letter.docx"
    doc = init_document("OFFICIAL CORPORATE SPONSORSHIP PROPOSAL LETTER")
    
    # Institutional Letterhead Header Box
    add_header_banner(
        doc,
        title="OFFICIAL CORPORATE SPONSORSHIP PROPOSAL",
        subtitle="Formal Institutional Invitation for Enterprise, Technology, Non-Tech & CSR Partners\nSchool of Computing  •  Department of Computer Science & Engineering",
        badges=[
            "REF: SIST/CSE/AWS-SBG/2026-27/EXT/SPON-CORP",
            "CATEGORY-1 DEEMED UNIVERSITY",
            "NAAC 'A++' GRADE  •  NIRF TOP 50",
            "CHENNAI, TAMIL NADU"
        ]
    )
    
    # Official Reference Block
    ref_table_data = [
        ["OFFICIAL LETTER REF:", "SIST/CSE/AWS-SBG/2026-27/EXT/SPON-CORP-[SERIAL_NO]", "DATE:", "[Date, Month, 2026]"],
        ["ORGANIZING ENTITY:", "AWS Student Builder Group (SIST Chapter)", "HOST INSTITUTION:", "Sathyabama Institute of Science and Technology"]
    ]
    add_styled_table(doc, ["Parameter", "Detail", "Parameter", "Detail"], ref_table_data)
    
    # Recipient Block Callout
    recipient_text = (
        "TO:\n"
        "The Managing Director / Head of Corporate Social Responsibility (CSR) / Chief Marketing Officer\n"
        "[Company / Corporation / Brand Name]\n"
        "[Corporate Office Address, Line 1]\n"
        "[City, State, Pincode]\n"
    )
    add_callout(doc, recipient_text, title="ADDRESSED CORPORATE RECIPIENT", style="info")
    
    # Subject Line
    add_h2(doc, "SUBJECT: Formal Invitation for Corporate Sponsorship & Youth Innovation Partnership — KAIROS 2027 (National Flagship Summit)")
    
    add_body(doc, "Dear Sir / Madam,")
    add_body(doc, "Greetings from Sathyabama Institute of Science and Technology, Chennai!", bold=True)
    
    add_body(doc, "On behalf of the AWS Student Builder Group at Sathyabama Institute of Science and Technology, Chennai, it gives us immense pleasure to formally invite [Company / Brand Name] to partner with us as an esteemed Corporate Sponsor for our upcoming national flagship summit, KAIROS 2027 (Grand Edition), scheduled to be held from January 22 to 24, 2027 at Sathyabama Institute of Science and Technology, Chennai.")
    
    # Section: About Institution & Chapter
    add_h2(doc, "About the Institution & Organizing Chapter")
    add_body(doc, "Sathyabama Institute of Science and Technology is one of India's premier higher education institutions, accredited with the highest NAAC 'A++' Grade and consistently ranked among the Top 50 Universities in India by the National Institutional Ranking Framework (NIRF). Our AWS Student Builder Group (SIST Chapter) is an officially chartered student technical society affiliated with the Worldwide Amazon Web Services Student Builder Groups Program, committed to fostering cutting-edge cloud engineering, artificial intelligence innovation, and societal problem-solving among student developers nationwide.")
    
    # Section: About Kairos 2027
    add_h2(doc, "About KAIROS 2027 (Grand Edition)")
    add_body(doc, "KAIROS 2027 is a grueling 48-hour continuous national hackathon bringing together the top 5% of student engineering talent in India. Enforcing a strict 100% Free / Zero Entry Fee mandate to guarantee uncompromised meritocracy, the summit attracts over 2,000+ applicant teams from premier institutions nationwide (including IITs, NITs, BITS, and premier universities across 20+ Indian states).")
    add_body(doc, "Following a rigorous dual-phase evaluation—commencing with an intensive virtual screening round—only the Top 100 Elite National Teams (Teams of 4–6 students, ~400–600 developers) are invited to the physical grand finale on our campus for 48 hours of uninterrupted engineering.")

    # Section: Strategic Value
    add_h2(doc, "Strategic ROI & Value for Corporate, Non-Tech & CSR Partners")
    add_body(doc, "While KAIROS 2027 is an engineering summit, corporate sponsors across technology, banking & financial services (BFSI), fast-moving consumer goods (FMCG), logistics, healthcare, retail, and corporate foundations (CSR) derive exceptional, multi-dimensional return on investment:")
    
    add_bullet(doc, "1. Direct Gen-Z Youth Engagement & On-Ground Brand Immersion", "48 hours of continuous, unfiltered engagement with 400–600 highly influential student leaders, creators, and innovators. Exclusive provision for dedicated 10x10ft experiential lounges, live product sampling, and logo embellishment across 110 custom heavyweight hoodies, 550 developer streetwear tees, 650 custom-woven jacquard lanyards, and 16 rollup banners across the venue.")
    add_bullet(doc, "2. Open Innovation & Fresh Perspectives on Industry Bottlenecks", "Non-technology corporations face critical business, operational, and customer experience bottlenecks. Through Track 5 (Open Enterprise & Societal Innovation), your leadership can present real-world challenges—such as supply chain tracking, sustainable green energy distribution, retail loyalty algorithms, or digital banking accessibility—with 100 elite squads competing to build functional software solutions.")
    add_bullet(doc, "3. High-Impact Corporate Social Responsibility (CSR) & Diversity Impact", "Because KAIROS 2027 charges ₹0 entry fees and provides 100% complimentary boarding, 6 full-board buffet meals, bus transit, and cloud sandboxes to all finalist students, your sponsorship directly subsidizes deserving student innovators regardless of financial background. Partners can directly co-sponsor high-prestige diversity grants, including the Best All-Women Engineering Team Bounty (₹10,000) and First-Generation Scholar Awards, advancing UN Sustainable Development Goals (SDGs 4, 8, and 9).")
    add_bullet(doc, "4. Nationwide Media Reach & 48-Hour Live Broadcast", "Over 500,000+ digital impressions across Instagram (@awssbg_sist), LinkedIn, and YouTube, amplified by 120+ student Campus Ambassadors across 20+ Indian states. Commercial stingers, lower-third overlays, and executive keynote broadcasts streamed globally on YouTube Live and LinkedIn.")
    add_bullet(doc, "5. Tech & Data Analytics Talent Pipeline for Enterprise IT Divisions", "Every modern enterprise is fundamentally a technology and data company. As a partner, your human resources and talent acquisition teams receive unrestricted, compliant access to the verified national directory of 2,000+ applicants and Top 100 finalist teams with GitHub code repositories for priority internship and graduate hiring.")

    # Section: Calibrated Tiers Table
    add_h2(doc, "Calibrated Corporate Partnership Tiers")
    tier_headers = ["Partnership Tier", "Contribution", "Key Deliverables & Executive Privileges"]
    tier_data = [
        ["Title Presenting Partner (1 Slot)", "₹2,00,000", "• Exclusive naming rights: 'KAIROS 2027 Presented by [Brand]'\n• 20-Minute Primetime Inaugural Keynote Address on the Main Stage\n• Sole Prominent Center Crest on 3840×1920 LED Wall & 20x10ft Backdrop\n• 2 VIP Grand Jury Seats in the Grand Finale Evaluation Plenary\n• Prime 10ft × 10ft Experiential Demo Lounge & Sampling Center in Foyer\n• Exclusive right to co-anchor and confer the National Grand Champion Trophy\n• Full access to 2,000+ national applicant and finalist talent directories"],
        ["Co-Powered By Partner (2 Slots)", "₹1,00,000", "• Official Co-Branding: 'KAIROS 2027 Co-Powered by [Brand]'\n• 10-Minute Executive Session during plenary sessions\n• Large Flanking Crest on Stage Backdrop and LED Wall\n• 1 VIP Grand Jury Seat in Grand Finale\n• Dedicated 6ft × 6ft Exhibition Kiosk in Grand Foyer\n• Dedicated Company Category Challenge with option to endow custom bounties\n• Access to Top 250 Semi-Finalist and Finalist talent directories"],
        ["Associate / Youth Impact Partner", "₹50,000", "• Official Associate Partner recognition across all digital and print collateral\n• Logo placement on all 16 Rollup Standees and participant handbook\n• 1 Technical Evaluator Seat in Milestone Checkpoint Gates\n• Dedicated social media collaborative spotlight and PR mention\n• Access to Top 100 Finalist resume database"],
        ["Dedicated Corporate Bounty Partner", "₹25,000", "• Exclusive naming rights for a dedicated problem bounty (e.g. '[Brand] Sustainable Retail Award')\n• Stage trophy and cash prize conferral directly by company executives\n• Dedicated challenge rollup standee and technical track branding"],
        ["Product / In-Kind Experience Partner", "Product / Sampling", "• Official Beverage, Nutrition, Fuel, or Lifestyle Partner status\n• Direct product distribution to 500+ participants during Midnight Sprints\n• 'Fuel Station Powered by [Brand]' foyer banner and live social coverage"]
    ]
    add_styled_table(doc, tier_headers, tier_data)
    
    # Section: Banking & Escrow
    add_h2(doc, "Institutional Governance, Bank Escrow & Tax Compliance")
    add_body(doc, "To ensure absolute financial transparency, corporate audit compliance, and safety:")
    add_bullet(doc, "Direct Institutional Bank Account", "All sponsorship considerations are deposited directly into the official audited university bank account:")
    
    bank_headers = ["Account Field", "University Official Record"]
    bank_data = [
        ["Account Name / Beneficiary", "SATHYABAMA INSTITUTE OF SCIENCE AND TECHNOLOGY"],
        ["Bank Name", "Indian Bank"],
        ["Branch", "Sathyabama University Branch, Jeppiaar Nagar, Chennai – 600119"],
        ["Account Type", "Institutional Savings / Project Account"],
        ["IFSC Code", "IDIB000S201"],
        ["MICR Code", "600019156"]
    ]
    add_styled_table(doc, bank_headers, bank_data)
    
    add_bullet(doc, "Tax Invoices & Receipts", "Official GST-compliant tax invoices and institutional money receipts are promptly issued by the University Accounts Office upon fund clearance.")
    add_bullet(doc, "Escrow Prize Security", "Pure cash prize funds (₹1,75,000) are held in verified escrow and disbursed via automated NEFT directly to winning student bank accounts within 72 hours of the Grand Finale.")

    # Section: Next Steps & Coordination
    add_h2(doc, "Next Steps & Discussion")
    add_body(doc, "We would welcome the opportunity to tailor a bespoke corporate engagement package aligned with your brand's marketing, recruitment, or CSR vision. We look forward to scheduling a brief 10-minute discovery call with your leadership team this week.")
    add_body(doc, "For immediate coordination, please feel free to reach out to our Sponsorship Team Lead, Nikki (Nangaiyar M) at +91 8754976892 or via email at nangaiyarmuthkrishnan@gmail.com / sistawscc@gmail.com.")

    # Section: Signatures Block
    add_h2(doc, "Institutional Endorsement & Execution Signatories")
    
    sig_headers = ["Student Executive Leadership", "Faculty & Institutional Governance"]
    sig_data = [
        [
            "______________________________________\n"
            "Nikki (Nangaiyar M)\n"
            "Sponsorship Team Lead\n"
            "AWS Student Builder Group — SIST Chapter\n"
            "Register No: 44612059 | Phone: +91 8754976892\n"
            "Email: nangaiyarmuthkrishnan@gmail.com\n\n"
            "______________________________________\n"
            "Thenappan T\n"
            "President & Student Builder Group Leader (AWS SBGL)\n"
            "AWS Student Builder Group — SIST Chapter\n"
            "Register No: 44110855 | Phone: +91 6381801640\n"
            "Email: thenappanmasterz1311@gmail.com",
            
            "______________________________________\n"
            "Dr. K. Ashok Kumar & Dr. Balapriya .S\n"
            "Faculty Coordinators, AWS Student Builder Group\n"
            "Department of Computer Science & Engineering\n"
            "Sathyabama Institute of Science and Technology\n"
            "Emails: ashokkumar.cse@sathyabama.ac.in\n"
            "        balapriya.cse@sathyabama.ac.in\n\n"
            "______________________________________\n"
            "Dr. L. Lakshmanan\n"
            "Dean, School of Computing\n"
            "Sathyabama Institute of Science and Technology\n"
            "Jeppiaar Nagar, Rajiv Gandhi Salai, Chennai – 600119"
        ]
    ]
    add_styled_table(doc, sig_headers, sig_data)
    
    doc.save(output_path)
    print(f"Generated Doc 3: {output_path}")

if __name__ == "__main__":
    build_doc3()
