import os
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx_utils import (
    init_document, add_header_banner, add_h1, add_h2, add_h3,
    add_body, add_bullet, add_callout, add_styled_table,
    HEX_AMBER, COLOR_NAVY, COLOR_SLATE_BLUE, COLOR_DARK_TEXT
)

def build_doc6():
    output_path = r"e:\AWS SBGL\Events\Kairos\teams\01_sponsorship_and_partnerships\word_documents\06_KAIROS_2027_Sponsor_Benefit_Fulfillment_and_PoP_Checklist.docx"
    doc = init_document("SPONSOR BENEFIT FULFILLMENT & POP CHECKLIST")
    
    add_header_banner(
        doc,
        title="KAIROS 2027 (GRAND EDITION)",
        subtitle="Corporate Sponsor Benefit Fulfillment Matrix & Proof-of-Performance (PoP) Checklist\nComprehensive Quality Assurance, Ground Operations & Post-Event ROI Protocol",
        badges=[
            "DIRECT ACCOUNTABILITY: NIKKI (SPONSORSHIP LEAD)",
            "PRINT FREEZE: DEC 20, 2026",
            "PROOF OF PERFORMANCE (PoP) PROTOCOL",
            "POST-EVENT ROI DOSSIER SLA: 7-10 DAYS"
        ]
    )
    
    add_callout(
        doc,
        "This document ensures 100% compliance with every benefit promised to corporate partners in signed MoUs. It details asset ingestion specifications, pre-event verification gates, on-site photography assignments for proof-of-performance (PoP), and delivery standards for the post-event ROI dossier. No sponsor promise is left unfulfilled.",
        title="OPERATIONAL FULFILLMENT MANDATE",
        style="info"
    )
    
    # ---------------------------------------------------------
    # SECTION 1: MASTER FULFILLMENT TRACKING MATRIX
    # ---------------------------------------------------------
    add_h1(doc, "1. Master Fulfillment Tracking Matrix")
    add_body(doc, "Operational tracking table monitoring deliverable readiness across signed and pipeline partners:")
    
    matrix_headers = ["Sponsor Entity", "Committed Tier", "Contract Value", "Logo Ingested?", "Backdrop & Standees?", "LED Wall Ready?", "Keynote Slated?", "Live Stream Video?", "Resume DB Dispatched?", "Escrow Status"]
    matrix_data = [
        ["Amazon Web Services (AWS)", "Title Partner", "₹2,00,000 + $50k Credits", "[x] SVG Approved", "[ ] In Layout", "[x] Ready (Center)", "Day 1: 11:15 AM (20m)", "[x] 30s Cued", "[ ] Post-Qualifier", "[ ] Pending Signoff"],
        ["Presidio Cloud Solutions", "Co-Powered By", "₹1,00,000", "[ ] EPS Requested", "[ ] In Layout", "[ ] Queued", "Day 1: 11:35 AM (10m)", "[ ] 15s Needed", "[ ] Post-Qualifier", "[ ] Pending Signoff"],
        ["Zoho Corporation", "Co-Powered By", "₹1,00,000", "[ ] SVG Requested", "[ ] In Layout", "[ ] Queued", "Day 2: 02:00 PM (10m)", "[ ] 15s Needed", "[ ] Post-Qualifier", "[ ] Pending Signoff"],
        ["Freshworks", "Track Partner (AI)", "₹25,000", "[ ] PNG Requested", "[ ] Track Strip", "[ ] Queued", "Track Briefing (5m)", "[ ] Lower-Third", "[ ] Post-Event", "[ ] Pending Signoff"],
        ["Red Bull India", "Official Energy", "In-Kind (2k Cans)", "[x] Vector Approved", "[x] Sampling Mapped", "[x] Station Crest", "Midnight Shoutout", "[ ] Lower-Third", "N/A", "[x] Confirmed"],
        ["JetBrains", "Tooling Partner", "500 Dev Licenses", "[x] Logo Approved", "[x] Swag Table", "[x] Partner Slide", "Opening Mention", "[ ] Lower-Third", "N/A", "[x] Vouchers Ingested"]
    ]
    add_styled_table(doc, matrix_headers, matrix_data)

    # ---------------------------------------------------------
    # SECTION 2: ASSET INGESTION SPECIFICATIONS
    # ---------------------------------------------------------
    add_h1(doc, "2. Asset Ingestion Specifications & Technical QA")
    add_body(doc, "All creative collateral must adhere strictly to these technical standards to prevent visual degradation:")
    
    asset_headers = ["Asset Type", "Dimensions & Resolution", "Color Profile & Format", "Quality Acceptance Threshold"]
    asset_data = [
        ["Corporate Vector Logo", "Scalable Vector / 300 DPI Transparent PNG", "RGB + CMYK (SVG, EPS, AI)", "Must include dark-mode and light-mode variants; no pixelation at 10ft scale"],
        ["Main Stage LED Wall Asset", "3840 × 1920 px (16:9 Widescreen)", "RGB 72–150 DPI (PNG / PSD)", "Obsidian-black background; centered crest for Title, flanking for Co-Powered"],
        ["Stage Backdrop Banner", "20 feet wide × 10 feet high", "CMYK 300 DPI (TIFF / PDF Vector)", "35% surface for Title, 20% for Co-Powered, shared footer for Associate"],
        ["Rollup Standees (16 Total)", "6 feet high × 3 feet wide (16 units)", "CMYK 150–300 DPI (Vinyl Flex)", "Title on all 16 standees; Co-Powered on 10; Track on dedicated standee"],
        ["Apparel Crest (Hoodies & Tees)", "12 inches wide (Front) / 10 inches (Back)", "CMYK Vector (AI / EPS)", "Single or two-tone screen print; strictly vector paths"],
        ["Live Stream Video Commercial", "1920×1080p 60fps / 3840×2160p 4K", "MP4 H.264 / AAC Audio", "Title: 30 seconds broadcast every 2h; Co-Powered: 15 seconds every 4h"]
    ]
    add_styled_table(doc, asset_headers, asset_data)

    # ---------------------------------------------------------
    # SECTION 3: PRE-EVENT VERIFICATION GATES
    # ---------------------------------------------------------
    add_h1(doc, "3. Pre-Event Verification Gates & Deadlines")
    add_body(doc, "Fulfillment operates across four strict quality verification checkpoints:")
    add_bullet(doc, "Gate 1 (D-45 / December 10, 2026): Vector Asset Freeze", "All sponsor logos, vector paths, and brand guidelines must be signed off and archived in the master asset drive.")
    add_bullet(doc, "Gate 2 (D-30 / December 20, 2026): Hard Print Freeze", "Backdrops, 16 standees, 110 hoodies, 550 tees, and 650 lanyards sent to vendors. No logo modifications permitted after this gate.")
    add_bullet(doc, "Gate 3 (D-15 / January 07, 2027): Keynote & Jury Signoff", "Executive speaker titles, bios, headshots, and nominated jury members confirmed and integrated into master schedule.")
    add_bullet(doc, "Gate 4 (D-5 / January 17, 2027): Technical Media & Live Stream QA", "Video commercials cued into OBS broadcast system; foyer booth spaces marked with power sockets and table signage.")

    # ---------------------------------------------------------
    # SECTION 4: ON-SITE PROOF OF PERFORMANCE (PoP)
    # ---------------------------------------------------------
    add_h1(doc, "4. On-Site Proof of Performance (PoP) Protocol")
    add_body(doc, "Corporate sponsors require tangible evidence that every contracted deliverable was executed. The Media & Photography Squad (Division 5) is assigned to capture the following five mandatory DSLR proof assets:")
    
    add_bullet(doc, "1. Executive Keynote on Stage", "High-res wide and tight shots of the corporate executive speaking on the main auditorium stage with an attentive audience of 500+ builders.")
    add_bullet(doc, "2. Stage LED Wall & Backdrop Brand Prominence", "Clear, unobstructed photos showing the sponsor's logo glowing on the 3840×1920 LED Wall behind speakers and winners.")
    add_bullet(doc, "3. Foyer Exhibition Lounge & Hacker Engagement", "Dynamic photos of students crowding around the corporate kiosk, interacting with reps, testing demos, and receiving merchandise.")
    add_bullet(doc, "4. Apparel & Smart Badge Close-Ups", "Macro photography of participants actively coding while wearing hoodies, jerseys, and custom jacquard lanyards bearing the sponsor's crest.")
    add_bullet(doc, "5. Jury Evaluation & Mentorship Sessions", "Documenting corporate evaluators reviewing finalist projects at hacker bays during Milestone Checkpoints.")
    
    add_callout(
        doc,
        "Broadcast Logging SLA: The Live Stream Crew must maintain a digital timestamp log recording every instance a corporate video commercial or lower-third graphic is aired on the 48-hour global YouTube/LinkedIn broadcast.",
        title="LIVE BROADCAST VERIFICATION SLA",
        style="warning"
    )

    # ---------------------------------------------------------
    # SECTION 5: POST-EVENT ROI DOSSIER STANDARD
    # ---------------------------------------------------------
    add_h1(doc, "5. Post-Event 10-Slide Sponsor ROI Dossier Standard")
    add_body(doc, "Within 7 to 10 business days following the Grand Finale (no later than February 05, 2027), the Sponsorship Squad delivers a comprehensive 10-slide executive ROI dossier to the corporate sponsor's leadership team:")
    
    dossier_headers = ["Slide No.", "Slide Topic & Content", "Key Metrics & Evidence Included"]
    dossier_data = [
        ["Slide 1", "Executive Cover & Gratitude", "Formal thank you letter from President Thenappan T and Dean School of Computing"],
        ["Slide 2", "National Reach & Applicant Telemetry", "2,000+ applicants, geographic map across 20+ states, top colleges represented"],
        ["Slide 3", "Finalist Demographics & Quality", "100 elite teams, gender ratio, tech stack distribution (AI, Cloud, Web3)"],
        ["Slide 4", "Main Stage & Keynote Highlights", "Keynote address photos, crowd reaction metrics, VIP jury participation"],
        ["Slide 5", "Ground Brand Immersion Proofs", "Photos of LED Wall, 20x10ft backdrop, 16 standees, and foyer demo kiosk crowds"],
        ["Slide 6", "Apparel & Collateral Integration", "Photo evidence of 110 hoodies, 550 tees, 650 lanyards, and smart badges"],
        ["Slide 7", "48-Hour Live Broadcast Metrics", "Live stream view count, peak concurrent viewers, global watch-time analytics"],
        ["Slide 8", "Digital & Social Media Reach", "500,000+ digital impressions, Instagram/LinkedIn engagement rates, top posts"],
        ["Slide 9", "Track & Challenge Outcomes", "Overview of student prototypes built using sponsor APIs/models; winner highlights"],
        ["Slide 10", "Talent Access & Partnership Renewal", "Dispatch confirmation of verified resume database + invitation to renew for Kairos 2028"]
    ]
    add_styled_table(doc, dossier_headers, dossier_data)
    
    add_callout(
        doc,
        "Delivering a flawless post-event ROI dossier is our single most effective sales tool for Kairos 2028. Sponsors who receive prompt, professional documentation renew their partnerships at higher tiers with zero friction.",
        title="RETENTION & RENEWAL STRATEGY",
        style="success"
    )

    doc.save(output_path)
    print(f"Generated Doc 6: {output_path}")

if __name__ == "__main__":
    build_doc6()
