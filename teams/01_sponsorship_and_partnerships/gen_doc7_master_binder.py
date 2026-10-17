import os
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx_utils import (
    init_document, add_header_banner, add_h1, add_h2, add_h3,
    add_body, add_bullet, add_callout, add_styled_table,
    HEX_AMBER, COLOR_NAVY, COLOR_SLATE_BLUE, COLOR_DARK_TEXT
)

def build_master_binder():
    output_path = r"e:\AWS SBGL\Events\Kairos\teams\01_sponsorship_and_partnerships\word_documents\KAIROS_2027_Complete_Sponsorship_Master_Operations_Manual.docx"
    doc = init_document("COMPLETE SPONSORSHIP MASTER OPERATIONS MANUAL")
    
    # Master Cover Banner
    add_header_banner(
        doc,
        title="KAIROS 2027 (GRAND EDITION)",
        subtitle="Complete Corporate Sponsorship Master Operations Manual\nThe Unified, Self-Contained Compendium for Corporate Outreach, Pitching, Legal MoUs & Operations",
        badges=[
            "EVENT DATES: JANUARY 22–24, 2027",
            "100 ELITE FINALIST TEAMS  •  400–600 BUILDERS",
            "100% FREE / ZERO ENTRY FEE",
            "₹3.5L–₹4.0L+ WORKING CAPITAL POOL",
            "ALL-IN-ONE MASTER BINDER"
        ]
    )
    
    add_callout(
        doc,
        "WELCOME TO THE KAIROS 2027 MASTER SPONSORSHIP MANUAL.\n"
        "This compendium brings together every single document, strategy, template, legal agreement, pitch deck script, and operational checklist into one unified binder. Every section is 100% complete and self-contained with zero references to outside files. Team members can use this single manual as their definitive operational guide from today through post-event wrap-up.",
        title="EXECUTIVE MASTER BINDER MANDATE",
        style="success"
    )
    
    # ---------------------------------------------------------
    # MASTER TABLE OF CONTENTS
    # ---------------------------------------------------------
    add_h1(doc, "MASTER TABLE OF CONTENTS")
    toc_data = [
        ["Section Number", "Operational Division / Manual Component", "Primary Audience & Purpose"],
        ["SECTION 1", "2-Hour Sponsorship Team Meeting Speech Deck & Masterclass", "President Thenappan T's complete speaking script & training notes"],
        ["SECTION 2", "Corporate Sponsorship Strategy, Outreach Playbook & Templates", "Outreach strategy, tiers, email templates, cold-calling scripts & objections"],
        ["SECTION 3", "Master Corporate Pitch Deck Slide-by-Slide Content Guide", "14-slide presentation narrative, visual guides & CXO talking points"],
        ["SECTION 4", "Official Corporate Sponsorship Proposal Letter (Institutional)", "Printable formal letterhead invitation for VPs, CMOs & CSR Heads"],
        ["SECTION 5", "Corporate Sponsorship Memorandum of Understanding (MoU)", "Standard legal contract template with student IP protection & escrow"],
        ["SECTION 6", "Corporate Sponsorship Pipeline CRM & Target Accounts Tracker", "Active deal matrix (ENT-01 to ENT-11), call logs & week-one sprint plan"],
        ["SECTION 7", "Sponsor Benefit Fulfillment Matrix & Proof-of-Performance (PoP)", "Creative asset specs, verification gates, photo proofs & 10-slide ROI dossier"],
        ["SECTION 8", "Master Operational Reference Appendix", "Key numbers, bank escrow details, leadership contacts & timeline milestones"]
    ]
    add_styled_table(doc, toc_data[0], toc_data[1:])
    
    # ---------------------------------------------------------
    # PART 1: 2-HOUR MEETING SPEECH DECK & MASTERCLASS
    # ---------------------------------------------------------
    doc.add_page_break()
    add_h1(doc, "SECTION 1: 2-Hour Sponsorship Team Meeting Speech Deck & Masterclass")
    add_callout(
        doc,
        "Speaker: Thenappan T — President & Student Builder Group Leader (AWS SBGL)\n"
        "Date: October 17, 2026 | Audience: Sponsorship Team (Nikki & Squad)\n"
        "Tone: High-Energy, Commanding, Candid, Educational",
        title="SPEAKER CONTEXT & MEETING GOAL",
        style="info"
    )
    
    add_h2(doc, "1.1 Meeting Structure & 8-Segment Overview")
    seg_headers = ["Segment & Timestamp", "Segment Title", "Core Objective & Room Pacing"]
    seg_data = [
        ["00:00 – 00:15", "Opening: The Moment We're In", "Powerful cold open; establish audacity of a 48h, 100-team, 100% free national event."],
        ["00:15 – 00:35", "The Story of KAIROS", "The Kairos moment; ₹3.5L–₹4.0L capital architecture; Dec 20 print freeze urgency."],
        ["00:35 – 01:00", "The Masterclass: How to Get a Sponsor", "Commercial transaction mindset; 4 buyer personas; 7-step enterprise sales pipeline."],
        ["01:00 – 01:20", "Handling Objections & Closing Deals", "Word-for-word scripts for all 8 common corporate pushbacks; creating urgency."],
        ["01:20 – 01:35", "Live Roleplay: Pitching Under Pressure", "Hands-on simulation; squad members pitch live; instant constructive feedback."],
        ["01:35 – 01:45", "The Rainmaker Referral Engine", "Mobilizing 120+ campus ambassadors with 10–15% cash referral bounties."],
        ["01:45 – 01:50", "Pipeline Walkthrough & Who Owns What", "Review of ENT-01 to ENT-11; individual target company lists; weekly meeting rhythm."],
        ["01:50 – 02:00", "Closing Motivation: The Moment for Boldness", "Personal send-off; how this work builds real-world reputations and launches careers."]
    ]
    add_styled_table(doc, seg_headers, seg_data)
    
    add_h2(doc, "1.2 Core Speaking Highlights from President Thenappan T")
    add_body(doc, "\"Right now — October 2026 — is our Kairos moment. We have three months before applications close on December 15th. We have three months and five days to close every major deal before our hard Print Freeze on December 20th. After that date, jerseys go to print, stage banners go to the printer, lanyards get woven. Everything becomes real — or everything falls apart.\"")
    add_body(doc, "\"Most people think sponsorship is asking for a favor. It is not. It is a commercial transaction. When a company gives us two lakhs of rupees, they aren't donating to a charity. They are buying developer mindshare, early access to the top 5% of engineering talent in India, and a dominant presence on our stage and 48-hour live broadcast. Your job is simply to help them see that what we are offering is worth ten times what they are investing.\"")
    add_body(doc, "\"₹3,50,000 is not just a budget figure. It is our standard. It proves that a group of passionate students from Sathyabama can imagine something audacious, fund it through enterprise partnerships, and deliver an unforgettable 48-hour experience to 600 developers completely free.\"")

    # ---------------------------------------------------------
    # PART 2: STRATEGY & OUTREACH PLAYBOOK
    # ---------------------------------------------------------
    doc.add_page_break()
    add_h1(doc, "SECTION 2: Corporate Sponsorship Strategy & Outreach Playbook")
    
    add_h2(doc, "2.1 Calibrated Tier Structure & Deliverable Matrix")
    tier_headers = ["Benefit / Deliverable", "Title Partner (₹2,00,000)", "Co-Powered By (₹1,00,000)", "Associate / Gold (₹50,000)", "Track Partner (₹25,000)", "In-Kind / Tooling"]
    tier_data = [
        ["Naming Rights", "'Presented By [Brand]'", "'Co-Powered By [Brand]'", "Official Associate", "Track Category Exclusive", "Official Tool / Fuel"],
        ["Main Stage LED Wall (3840x1920)", "Sole Center Large Crest", "Large Side Crest", "Partner Grid Logo", "Track Slide Logo", "Partner Strip"],
        ["Stage Backdrop (20x10ft)", "Hero Crest (35% surface)", "Sub-Hero (20% surface)", "Shared Footer Strip", "Track Strip", "Partner Strip"],
        ["Rollup Standees (16 Total)", "Logo on ALL 16 Standees", "Logo on 10 Standees", "2 Shared Standees", "1 Dedicated Standee", "1 Booth Standee"],
        ["Apparel (Hoodies & Tees)", "Prime Chest Crest", "Upper Sleeve / Back", "Back Grid Placement", "Back Grid Placement", "Collateral Insert"],
        ["Custom Woven Lanyards", "Prime Repeated Logo", "Secondary Logo", "—", "—", "—"],
        ["Keynote Address", "20-Min Inaugural Keynote", "10-Min Masterclass", "5-Min Address", "Track Kickoff Intro", "—"],
        ["Grand Jury Seats", "2 VIP Grand Jury Seats", "1 VIP Grand Jury Seat", "1 Checkpoint Evaluator", "1 Track Evaluator", "Guest VIP Pass"],
        ["Talent Resume & GitHub DB", "Full 2,000+ National DB", "Top 250 Semi-Finalists", "Top 100 Finalist DB", "Track Finalist Resumes", "—"],
        ["48H Live Stream Commercials", "30s Ad Every 2 Hours", "15s Ad Every 4 Hours", "Static Logo Watermark", "Lower-Third Stinger", "Lower-Third Stinger"],
        ["Exhibition Stall in Foyer", "Prime 10x10ft VIP Lounge", "Dedicated 6x6ft Kiosk", "Shared Standee Table", "Track Table", "Sampling Station"]
    ]
    add_styled_table(doc, tier_headers, tier_data)

    add_h2(doc, "2.2 The 4 Core Email Outreach Templates (Summary)")
    add_bullet(doc, "Template A (Enterprise/Title)", "Dispatched to VP Engineering, Head of DevRel, or Talent Acquisition at major cloud and enterprise firms. Focuses on developer mindshare, 2,000+ applicant resume database, and 20-minute keynote.")
    add_bullet(doc, "Template B (Beverage/Energy Fuel)", "Dispatched to Brand Marketing Leads at Red Bull, Monster, Paper Boat. Focuses on product sampling during Midnight Hacking Sprints (01:00 AM – 04:00 AM) to 500 developers.")
    add_bullet(doc, "Template C (Track & Problem Bounty)", "Dispatched to developer tooling and Web3/AI firms (₹25,000 tier). Focuses on developer adoption of specific APIs, SDKs, or tools across 15–25 builder squads.")
    add_bullet(doc, "Template D (Consumer & Non-Tech Brands)", "Dispatched to FMCG, BFSI, Retail, and CSR Heads. Focuses on 500,000+ digital impressions, Open Innovation Track 5 bottlenecks, and Women-in-Tech diversity bounties.")

    add_h2(doc, "2.3 The Crowdsourced Rainmaker Referral Model")
    add_body(doc, "Students across India receive direct liquid cash payouts for connecting corporate sponsors:")
    add_bullet(doc, "Title Sponsor (₹2,00,000)", "10% – 15% commission = ₹20,000 – ₹30,000 cash payout + Main Stage Trophy.")
    add_bullet(doc, "Co-Powered By (₹1,00,000)", "10% – 12% commission = ₹10,000 – ₹12,000 cash payout + Streetwear Hoodie.")
    add_bullet(doc, "Associate / Gold (₹50,000)", "10% commission = ₹5,000 cash payout.")
    add_bullet(doc, "Track Partner (₹25,000)", "10% commission = ₹2,500 cash payout.")
    add_bullet(doc, "In-Kind / Beverage Deals", "₹3,000 – ₹5,000 fixed cash bounty.")
    add_bullet(doc, "Governance & SLA", "21-day lead lock; cash transferred via UPI/NEFT within 48–72 hours of corporate fund clearance into Sathyabama's Indian Bank account.")

    # ---------------------------------------------------------
    # PART 3: CORPORATE PITCH DECK SLIDE-BY-SLIDE GUIDE
    # ---------------------------------------------------------
    doc.add_page_break()
    add_h1(doc, "SECTION 3: Master Corporate Pitch Deck Guide")
    add_body(doc, "The 14-slide master pitch deck is presented in 16:9 4K dark mode (Obsidian Abyss `#0D1117` and Amber Gold `#FF9900`). Key slide narrative breakdown:")
    
    deck_headers = ["Slide No.", "Slide Title", "Key Visual & Data Highlight", "Core Message to Corporate Executive"]
    deck_data = [
        ["Slide 1", "Hero Cover & Title Lockup", "Obsidian Abyss background, dual AWS SBG & SIST seals", "Establishes institutional stature and hackathon scale"],
        ["Slide 2", "The Catalyst & Institutional Eminence", "Sathyabama NAAC 'A++', NIRF Top 50, AWS SBGL chapter", "Proves governance, reliability, and academic pedigree"],
        ["Slide 3", "The 2-Tier Quality Funnel", "2,000+ applicants -> 250 semi-finalists -> 100 elite squads", "Demonstrates that sponsors interact only with top 5% talent"],
        ["Slide 4", "5 Strategic Industry Tracks", "AI, Cloud, Web3, FinTech, Open Enterprise", "Shows opportunity to own a track and drive API/tool adoption"],
        ["Slide 5", "₹1,75,000 Pure Cash Prize Escrow", "Champion ₹60k, 1st Runner ₹35k, 2nd Runner ₹20k", "Proves serious cash backing; attracts the nation's best coders"],
        ["Slide 6", "Triple-Lock Corporate ROI", "Recruitment pipeline, tech adoption, executive eminence", "Outlines clear commercial value across three corporate budgets"],
        ["Slide 7", "Calibrated Tier Matrix", "Title ₹2L, Co-Powered ₹1L, Associate ₹50k, Track ₹25k", "Presents structured, transparent investment options"],
        ["Slide 8", "Stage, LED Wall & Apparel Branding", "3840x1920 LED Wall, 20x10ft backdrop, 110 hoodies, 550 tees", "Highlights premium visual craftsmanship and Dec 20 print freeze"],
        ["Slide 9", "48-Hour Live Broadcast & Media", "500k+ impressions, continuous multicam YouTube/LinkedIn", "Demonstrates national reach far beyond the physical venue"],
        ["Slide 10", "Foyer VIP Exhibition Lounges", "10x10ft interactive lounges, product sampling kiosks", "Details on-ground face-to-face engagement opportunities"],
        ["Slide 11", "Past Track Record & Testimonials", "Confirmed JetBrains (500 licenses), Red Bull, AWS", "Builds social proof through already confirmed corporate champions"],
        ["Slide 12", "Rainmaker Referral Flywheel", "Decentralized ambassador network across 20+ states", "Shows organic student advocacy and viral community reach"],
        ["Slide 13", "Governance, Escrow & Compliance", "Indian Bank SIST Branch details, GST invoice process", "Reassures procurement that accounting and audits are seamless"],
        ["Slide 14", "Executive Call to Action", "Next steps, MoU signing target, CPFO Nikki contact info", "Creates immediate urgency to lock deliverables before print freeze"]
    ]
    add_styled_table(doc, deck_headers, deck_data)

    # ---------------------------------------------------------
    # PART 4: OFFICIAL PROPOSAL LETTER
    # ---------------------------------------------------------
    doc.add_page_break()
    add_h1(doc, "SECTION 4: Official Corporate Sponsorship Proposal Letter")
    add_body(doc, "This formal invitation letter is printed on official Sathyabama Institute of Science and Technology letterhead and addressed to Managing Directors, CSR Heads, and CMOs:")
    
    add_callout(
        doc,
        "SATHYABAMA INSTITUTE OF SCIENCE AND TECHNOLOGY\n"
        "(Deemed to be University under Section 3 of the UGC Act, 1956)\n"
        "Category-1 Deemed University | NAAC 'A++' Grade | NIRF Top 50\n"
        "Jeppiaar Nagar, Rajiv Gandhi Salai, Chennai – 600119\n"
        "School of Computing — Department of Computer Science & Engineering\n"
        "AWS Student Builder Group (SIST Chapter)\n\n"
        "REF NO: SIST/CSE/AWS-SBG/2026-27/EXT/SPON-CORP-[SERIAL_NO]          DATE: [Date, 2026]\n\n"
        "TO: The Managing Director / Head of CSR / Chief Marketing Officer\n"
        "[Company / Corporation / Brand Name]\n\n"
        "SUBJECT: Formal Invitation for Corporate Sponsorship & Youth Innovation Partnership — KAIROS 2027\n\n"
        "Dear Sir / Madam,\n"
        "Greetings from Sathyabama Institute of Science and Technology, Chennai!\n"
        "On behalf of the AWS Student Builder Group, we formally invite your esteemed organization to partner with us as a Corporate Sponsor for KAIROS 2027 (January 22–24, 2027). KAIROS 2027 brings together 100 elite student engineering teams (~400–600 developers) chosen from 2,000+ applicants across IITs, NITs, and premier universities nationwide under a strict 100% Free / Zero Entry Fee mandate.\n\n"
        "Partnership with KAIROS provides exceptional ROI: direct engagement with 500+ top engineering influencers, open innovation solving your operational bottlenecks under Track 5, high-impact CSR education fulfillment (SDGs 4, 8, 9), 500,000+ digital reach, and unrestricted access to the verified national applicant talent database.\n\n"
        "All sponsorships are remitted into Sathyabama University's official Indian Bank account (IFSC: IDIB000S201) with formal GST invoices issued.",
        title="FORMAL PROPOSAL LETTER EXCERPT",
        style="info"
    )

    # ---------------------------------------------------------
    # PART 5: STANDARD MOU & LEGAL AGREEMENT
    # ---------------------------------------------------------
    doc.add_page_break()
    add_h1(doc, "SECTION 5: Standard Memorandum of Understanding (MoU)")
    add_body(doc, "Key operational and legal clauses binding Sathyabama University and Corporate Partners:")
    add_bullet(doc, "Parties to Agreement", "Sathyabama Institute of Science and Technology (represented by Dean, School of Computing) AND Corporate Partner Entity (represented by Authorized Signatory).")
    add_bullet(doc, "Financial Terms", "Sponsorship contribution remitted via NEFT/RTGS into Sathyabama Indian Bank account within 15 business days of MoU signing.")
    add_bullet(doc, "100% Student Code & IP Protection (Clause 5)", "ALL INTELLECTUAL PROPERTY AND CODE CREATED BY PARTICIPANT TEAMS REMAINS 100% THE EXCLUSIVE PROPERTY OF THE STUDENTS. The sponsor acquires no automatic IP rights, but may negotiate independent commercial licenses or hiring agreements post-event.")
    add_bullet(doc, "Data Privacy & NDA (Clause 6)", "Candidate resume data is strictly confidential and reserved for the sponsor's internal hiring.")
    add_bullet(doc, "Jurisdiction (Clause 8)", "Governed by the laws of India, subject to the exclusive jurisdiction of the courts of Chennai, Tamil Nadu.")

    # ---------------------------------------------------------
    # PART 6: PIPELINE CRM & TARGET ACCOUNTS TRACKER
    # ---------------------------------------------------------
    doc.add_page_break()
    add_h1(doc, "SECTION 6: Corporate Pipeline CRM & Target Accounts Tracker")
    add_body(doc, "Live status of priority enterprise leads (ENT-01 through ENT-11):")
    
    crm_summary = [
        ["Lead ID", "Company Name", "Committed Tier", "Value (₹)", "Current Stage", "Next Action Deadline"],
        ["ENT-01", "Amazon Web Services (AWS)", "Title Partner", "₹2,00,000 + $50k Credits", "Stage 5: Legal & MoU", "Dean-signed formal letter by Sep 25"],
        ["ENT-02", "Presidio Cloud Solutions", "Co-Powered By", "₹1,00,000", "Stage 4: Deck Sent", "Technical track alignment call by Sep 28"],
        ["ENT-03", "Zoho Corporation", "Co-Powered By", "₹1,00,000", "Stage 3: Discovery", "Deliver customized SaaS track deck by Oct 02"],
        ["ENT-04", "Freshworks", "Track Partner (AI)", "₹25,000", "Stage 3: Discovery", "Send Freddy AI challenge doc by Oct 05"],
        ["ENT-05", "Red Bull India", "Energy Partner", "In-Kind (2,000 Cans + DJ)", "Stage 5: Legal & MoU", "Cold-chain delivery schedule by Oct 10"],
        ["ENT-06", "Polygon / ETH Foundation", "Track Partner (Web3)", "₹25,000", "Stage 2: Outreach Sent", "Twitter/LinkedIn outreach follow-up"],
        ["ENT-07", "Postman", "Tooling Partner", "In-Kind (500 Swag Packs)", "Stage 3: Discovery", "Request 500 stickers & swag drop by Oct 12"],
        ["ENT-08", "JetBrains", "Educational Tooling", "500 Dev Licenses", "CLOSED WON", "Vouchers stored in website team vault"],
        ["ENT-09", "LTIMindtree", "Track Partner (FinTech)", "₹25,000", "Stage 2: Outreach Sent", "Follow up via institutional alumni network"],
        ["ENT-10", "Cognizant", "Track Partner (Health)", "₹25,000", "Stage 1: Identified", "Draft intro letter via Faculty Coordinators"],
        ["ENT-11", "SIST University Grant", "Institutional Grant", "₹50,000", "Stage 5: Legal & MoU", "File proposal to Vice Chancellor Office"]
    ]
    add_styled_table(doc, crm_summary[0], crm_summary[1:])

    # ---------------------------------------------------------
    # PART 7: FULFILLMENT & PROOF-OF-PERFORMANCE CHECKLIST
    # ---------------------------------------------------------
    doc.add_page_break()
    add_h1(doc, "SECTION 7: Sponsor Benefit Fulfillment & PoP Checklist")
    add_body(doc, "On-ground execution standards and proof-of-performance (PoP) deliverables:")
    add_bullet(doc, "Asset Resolution Standards", "Vector logos (SVG/EPS 300 DPI), LED wall graphics (3840×1920 px), Stage backdrop (20×10ft), 16 Rollup Standees (6×3ft), 4K live stream commercial video stingers.")
    add_bullet(doc, "Verification Gate Reviews", "Gate 1 (Dec 10: Vector Freeze)  •  Gate 2 (Dec 20: Hard Print Freeze)  •  Gate 3 (Jan 07: Keynote & Jury Signoff)  •  Gate 4 (Jan 17: Media & Live Stream QA).")
    add_bullet(doc, "On-Site DSLR Photo Proofs", "Dedicated photographer captures 5 mandatory shots: (1) Keynote on stage, (2) Logo on LED wall, (3) Crowds at foyer booth, (4) Participants wearing branded hoodies/lanyards, (5) Corporate evaluators judging teams.")
    add_bullet(doc, "Post-Event 10-Slide ROI Dossier", "Delivered to corporate sponsor leadership within 7–10 business days post-event containing verified analytics, photos, and renewal packages for Kairos 2028.")

    # ---------------------------------------------------------
    # PART 8: MASTER OPERATIONAL APPENDIX
    # ---------------------------------------------------------
    doc.add_page_break()
    add_h1(doc, "SECTION 8: Master Operational Reference Appendix")
    
    add_h2(doc, "8.1 Key Numbers to Memorize")
    key_numbers = [
        ["Dimension", "Operational Value", "Dimension", "Operational Value"],
        ["Event Duration", "48 Hours Continuous", "Participant Scale", "100 Teams (~400–600 Hackers)"],
        ["Event Dates", "January 22 – 24, 2027", "Participant Entry Fee", "₹0 — 100% FREE for all"],
        ["Online Qualifier", "January 02 – 04, 2027", "Pure Cash Prize Pool", "₹1,75,000 Pure Liquid Cash"],
        ["Applications Window", "Oct 15 – Dec 15, 2026", "Working Capital Target", "₹3,50,000 – ₹4,00,000 Uncapped"],
        ["Print Freeze Deadline", "December 20, 2026 (HARD)", "National Applicants", "2,000+ Teams from 20+ States"],
        ["Title Sponsor Tier", "₹2,00,000 (1 Slot)", "Co-Powered Sponsor Tier", "₹1,00,000 (1–2 Slots)"],
        ["Associate Partner Tier", "₹50,000", "Track & Bounty Tier", "₹25,000 (5 Industry Tracks)"],
        ["University Grant", "₹50,000", "Campus Ambassadors", "120+ across 20+ States"],
        ["Digital Impressions", "500,000+ across channels", "Apparel Units", "110 Hoodies, 550 Tees, 650 Lanyards"]
    ]
    add_styled_table(doc, key_numbers[0], key_numbers[1:])

    add_h2(doc, "8.2 University Bank Escrow Credentials")
    bank_app_data = [
        ["Account Holder / Beneficiary", "SATHYABAMA INSTITUTE OF SCIENCE AND TECHNOLOGY"],
        ["Bank Name", "Indian Bank"],
        ["Branch", "Sathyabama University Branch, Jeppiaar Nagar, Chennai – 600119"],
        ["Account Type", "Institutional Savings / Project Account"],
        ["IFSC Code", "IDIB000S201"],
        ["MICR Code", "600019156"],
        ["Tax Invoicing", "Formal GST Tax Invoices and Institutional Receipts issued on clearance"],
        ["Prize Escrow Protocol", "₹1,75,000 held in audited escrow; disbursed within 72h via automated NEFT"]
    ]
    add_styled_table(doc, ["Field Parameter", "Official Institutional Record"], bank_app_data)

    add_h2(doc, "8.3 Executive Contact Directory")
    contact_app_data = [
        ["Executive Role", "Officer Name", "Register No", "Contact Information"],
        ["Super Head 1: CPFO & Sponsorship Lead", "Nikki (Nangaiyar M)", "44612059", "Phone: +91 8754976892\nEmail: nangaiyarmuthkrishnan@gmail.com"],
        ["President & SBGL (Apex Chapter)", "Thenappan T", "44110855", "Phone: +91 6381801640\nEmail: thenappanmasterz1311@gmail.com"],
        ["Faculty Coordinator", "Dr. K. Ashok Kumar", "Faculty CSE", "Email: ashokkumar.cse@sathyabama.ac.in"],
        ["Faculty Coordinator", "Dr. Balapriya .S", "Faculty CSE", "Email: balapriya.cse@sathyabama.ac.in"],
        ["Dean, School of Computing", "Dr. L. Lakshmanan", "Dean CSE", "Email: dean.computing@sathyabama.ac.in"],
        ["Official Chapter Email & Social", "AWS SBG — SIST Chapter", "—", "Email: sistawscc@gmail.com\nInstagram: @awssbg_sist"]
    ]
    add_styled_table(doc, ["Role", "Officer", "Register No", "Contact Details"], contact_app_data)

    doc.save(output_path)
    print(f"Generated Master Binder: {output_path}")

if __name__ == "__main__":
    build_master_binder()
