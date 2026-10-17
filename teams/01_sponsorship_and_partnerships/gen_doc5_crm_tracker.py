import os
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx_utils import (
    init_document, add_header_banner, add_h1, add_h2, add_h3,
    add_body, add_bullet, add_callout, add_styled_table,
    HEX_AMBER, COLOR_NAVY, COLOR_SLATE_BLUE, COLOR_DARK_TEXT
)

def build_doc5():
    output_path = r"e:\AWS SBGL\Events\Kairos\teams\01_sponsorship_and_partnerships\word_documents\05_KAIROS_2027_Corporate_Pipeline_CRM_and_Leads_Tracker.docx"
    doc = init_document("CORPORATE PIPELINE CRM & LEADS TRACKER")
    
    add_header_banner(
        doc,
        title="KAIROS 2027 (GRAND EDITION)",
        subtitle="Corporate Sponsorship Pipeline CRM & Target Accounts Tracker\nActive Lead Management, Pipeline Stages, Call Minutes & Action Plans",
        badges=[
            "BASELINE BUDGET: ₹3.5L–₹4.0L+ UNCAPPED",
            "PIPELINE VALUE: ₹36,00,000+",
            "ACTIVE TARGET LEADS: 33+ (ENT-01 TO ENT-11+)",
            "LEAD OWNER: NIKKI (CPFO)"
        ]
    )
    
    add_callout(
        doc,
        "This workbook serves as the operational CRM and active deal tracker for the KAIROS 2027 Sponsorship Squad. It outlines all pipeline stages, active enterprise accounts, meeting minutes, lead scoring rubrics, and week-one task assignments. All entries are updated weekly following the Monday 9:00 AM status review.",
        title="CRM WORKBOOK MANDATE & TRACKING RULES",
        style="info"
    )
    
    # ---------------------------------------------------------
    # SECTION 1: EXECUTIVE PIPELINE SUMMARY
    # ---------------------------------------------------------
    add_h1(doc, "1. Executive Pipeline Summary & Health Dashboard")
    add_body(doc, "To achieve our baseline working capital of ₹3,50,000 – ₹4,00,000, our pipeline maintains a 4x weighted coverage ratio across seven defined conversion stages:")
    
    pipeline_headers = ["Pipeline Stage", "Target Count", "Current Active", "Stage Conversion %", "Weighted Pipeline Value", "Closed Capital"]
    pipeline_data = [
        ["Stage 1: Identified & Researched", "30 Leads", "12 Leads", "10%", "₹ 1,25,000", "₹ 0"],
        ["Stage 2: Outreach Sent & Follow-up", "20 Leads", "8 Leads", "25%", "₹ 2,00,000", "₹ 0"],
        ["Stage 3: Discovery Call Held", "12 Leads", "5 Leads", "50%", "₹ 2,75,000", "₹ 0"],
        ["Stage 4: Customized Deck Sent", "8 Leads", "4 Leads", "70%", "₹ 3,15,000", "₹ 0"],
        ["Stage 5: Legal & MoU Review", "5 Leads", "3 Leads", "90%", "₹ 3,15,000", "₹ 0"],
        ["Stage 6: Closed Won (Escrowed)", "5 Deals", "1 Deal", "100%", "—", "₹ 1,25,000 (JetBrains In-Kind)"],
        ["Stage 7: Closed Lost / Deferred", "—", "1 Lead", "0%", "—", "—"],
        ["TOTAL PIPELINE", "75+ Targets", "33 Active", "—", "₹ 36,00,000 Total Pool", "₹ 1,25,000 Realized"]
    ]
    add_styled_table(doc, pipeline_headers, pipeline_data)

    # ---------------------------------------------------------
    # SECTION 2: PIPELINE STAGE DEFINITIONS
    # ---------------------------------------------------------
    add_h1(doc, "2. Pipeline Stage Definitions & Conversion SLAs")
    add_body(doc, "Every enterprise lead must advance through these exact procedural gates:")
    add_bullet(doc, "Stage 1: Identified & Researched", "Qualified target company identified. Decision-maker POC (Head of DevRel, VP HR, Campus Recruiter, CMO) confirmed on LinkedIn with direct email/phone.")
    add_bullet(doc, "Stage 2: Outreach Sent", "Customized email (Template A, B, C, or D) dispatched. LinkedIn connection request sent. Follow-up logged in CRM.")
    add_bullet(doc, "Stage 3: Discovery Call Held", "10-minute discovery call conducted with corporate POC. Core pain point identified (e.g. recruiting top builders, API stress-testing, or brand visibility).")
    add_bullet(doc, "Stage 4: Deck Customized Sent", "14-slide master pitch deck tailored with custom track statement or bespoke tier deliverables delivered within 48 hours of discovery call.")
    add_bullet(doc, "Stage 5: Legal & MoU Review", "Formal MoU draft (Document 04) sent to corporate legal/procurement. Dean-signed institutional letterhead endorsement delivered.")
    add_bullet(doc, "Stage 6: Closed Won (Escrowed)", "MoU countersigned. Funds remitted via NEFT into Sathyabama Indian Bank escrow account (or in-kind vouchers ingested).")
    add_bullet(doc, "Stage 7: Closed Lost", "Prospect formally declined or uncontactable after 4 attempts. Retargeting deferred to Kairos 2028.")

    # ---------------------------------------------------------
    # SECTION 3: ACTIVE ENTERPRISE LEADS MATRIX
    # ---------------------------------------------------------
    add_h1(doc, "3. Active Enterprise Leads Tracking Matrix")
    add_body(doc, "Live status of our priority enterprise target accounts (ENT-01 through ENT-11):")
    
    leads_headers = ["Lead ID", "Company Name", "Target Tier", "Potential Value", "Key POC & Title", "Lead Owner", "Stage", "Next Action & Due Date"]
    leads_data = [
        ["ENT-01", "Amazon Web Services", "Title Sponsor", "₹2,00,000 + $50k Credits", "Regional Community Manager / DevRel", "Nikki (CPFO)", "Stage 5: MoU", "Dean-signed formal letter by Sep 25"],
        ["ENT-02", "Presidio Cloud Solutions", "Co-Powered By", "₹1,00,000", "Director Talent Acquisition / Cloud Lead", "Nikki (CPFO)", "Stage 4: Deck Sent", "Technical track alignment call by Sep 28"],
        ["ENT-03", "Zoho Corporation", "Co-Powered By", "₹1,00,000", "Head of University Relations", "Enterprise Squad", "Stage 3: Discovery", "Deliver customized SaaS track deck by Oct 02"],
        ["ENT-04", "Freshworks", "Track Partner (AI)", "₹25,000", "DevRel Lead / Engineering Manager", "Enterprise Squad", "Stage 3: Discovery", "Send Freddy AI challenge doc by Oct 05"],
        ["ENT-05", "Red Bull India", "Official Energy Partner", "In-Kind (2,000 Cans + DJ)", "Brand Marketing Manager (South)", "Outreach Squad", "Stage 5: MoU", "Finalize cold-chain delivery schedule by Oct 10"],
        ["ENT-06", "Polygon / ETH Foundation", "Track Partner (Web3)", "₹25,000", "India Ecosystem Growth Lead", "Track Squad", "Stage 2: Outreach", "Follow up on Twitter/LinkedIn regarding bounty"],
        ["ENT-07", "Postman", "Tooling & API Partner", "In-Kind (500 Swag Packs)", "Student Program Manager", "Outreach Squad", "Stage 3: Discovery", "Request 500 stickers & swag drop by Oct 12"],
        ["ENT-08", "JetBrains", "Educational Tooling", "In-Kind (500 Licenses)", "Academic Program Lead", "Outreach Squad", "CLOSED WON", "Vouchers received, stored in website vault"],
        ["ENT-09", "LTIMindtree", "Track Partner (FinTech)", "₹25,000", "Campus Recruitment Head", "Nikki (CPFO)", "Stage 2: Outreach", "Follow up via institutional alumni network"],
        ["ENT-10", "Cognizant", "Track Partner (Health)", "₹25,000", "CSR & Campus Engagement Lead", "Enterprise Squad", "Stage 1: Identified", "Draft intro letter via Faculty Coordinators"],
        ["ENT-11", "Sathyabama Inst. Grant", "University Grant", "₹50,000", "Dean, School of Computing", "Nikki (CPFO)", "Stage 5: MoU", "File master proposal to Vice Chancellor office"]
    ]
    add_styled_table(doc, leads_headers, leads_data)

    # ---------------------------------------------------------
    # SECTION 4: OUTREACH CALL LOGS & MINUTES
    # ---------------------------------------------------------
    add_h1(doc, "4. Detailed Outreach Call Logs & Meeting Minutes")
    
    add_h2(doc, "Log Entry: ENT-01 — Amazon Web Services (AWS)")
    add_bullet(doc, "Meeting Date", "September 05, 2026 | Attendees: Nikki (Nangaiyar M), AWS Regional Community Lead")
    add_bullet(doc, "Key Discussion Points", "1. Confirmed Kairos 2027 as the flagship national student initiative for AWS Student Builder Groups.\n2. Confirmed AWS Bedrock developer sandboxes and $50,000 institutional cloud credit allocation for all 100 finalist squads.\n3. Escalated sponsorship co-funding package for cash prize pool.")
    add_bullet(doc, "Agreed Action Item", "Nikki to deliver Dean-signed formal university letterhead requisition by September 25.")

    add_h2(doc, "Log Entry: ENT-02 — Presidio Cloud Solutions")
    add_bullet(doc, "Meeting Date", "September 08, 2026 | Attendees: Nikki (Nangaiyar M), Presidio University Hiring Lead")
    add_bullet(doc, "Key Discussion Points", "1. Presidio leadership interested in recruiting top 100 cloud architects and GenAI finalists.\n2. Proposed Co-Powered By tier at ₹1,00,000 with resume database access and 2 VIP jury seats.")
    add_bullet(doc, "Agreed Action Item", "Deliver customized pitch deck highlighting GenAI and Cloud-Native resilient infrastructure tracks.")

    add_h2(doc, "Log Entry: ENT-03 — Zoho Corporation")
    add_bullet(doc, "Meeting Date", "September 12, 2026 | Attendees: Enterprise Squad Lead, Zoho University Relations Manager")
    add_bullet(doc, "Key Discussion Points", "1. Zoho evaluating sponsorship under their developer education initiative.\n2. Requested proposal for custom Zoho SaaS API challenge track.")
    add_bullet(doc, "Agreed Action Item", "Draft custom problem statement around high-throughput microservices using Zoho APIs.")

    add_h2(doc, "Log Entry: ENT-05 — Red Bull India")
    add_bullet(doc, "Meeting Date", "September 18, 2026 | Attendees: Outreach Squad Lead, Red Bull Brand Manager South")
    add_bullet(doc, "Key Discussion Points", "1. Red Bull agreed in principle to provide 2,000 chilled cans for midnight hacking fuel.\n2. Agreed to supply branded sound system / DJ booth for opening night energy sprint.")
    add_bullet(doc, "Agreed Action Item", "Finalize campus gate pass and cold-storage logistics clearance with Operations Team.")

    # ---------------------------------------------------------
    # SECTION 5: LEAD PRIORITIZATION SCORING RUBRIC
    # ---------------------------------------------------------
    add_h1(doc, "5. Lead Prioritization & Scoring Framework")
    add_body(doc, "Squad members must score every prospective lead on a 10-point scale before scheduling discovery calls:")
    
    score_headers = ["Evaluation Factor", "Weight", "High Score (3 pts)", "Medium Score (2 pts)", "Low Score (1 pt)"]
    score_data = [
        ["Budget Capacity", "30%", "Enterprise / Public Listed (>₹500 Cr)", "Funded Series B/C Startup", "Bootstrapped / Early Stage"],
        ["Developer Tooling Alignment", "30%", "Core Cloud / AI / API Platform", "Enterprise IT / Tech Enabled", "Pure Non-Tech Consumer"],
        ["Past University Sponsorship", "20%", "Actively sponsors hackathons", "Has sponsored student clubs", "No history of event sponsorship"],
        ["Executive Access / Connection", "20%", "Direct alumni or warm intro", "Second-degree LinkedIn connect", "Cold switchboard outreach"]
    ]
    add_styled_table(doc, score_headers, score_data)
    add_callout(doc, "Priority Rules: Score 8–10: High Priority (Nikki & Thenappan lead pitch)  •  Score 5–7: Standard Track Lead  •  Score < 5: Automated Email Sequence.", title="ACTION THRESHOLDS", style="warning")

    # ---------------------------------------------------------
    # SECTION 6: WEEK-ONE ACTION PLAN & SPRINT RHYTHM
    # ---------------------------------------------------------
    add_h1(doc, "6. Week-One Action Plan & Review Cadence")
    add_body(doc, "Immediate tactical deliverables assigned to squad members:")
    
    action_headers = ["Squad Member", "Assigned Action Deliverable", "Hard Deadline"]
    action_data = [
        ["Nikki (CPFO)", "Schedule formal MoU signing session with AWS Regional Lead", "October 22, 2026"],
        ["Nikki (CPFO)", "Submit official university grant requisition to Vice Chancellor Office", "October 20, 2026"],
        ["Nikki (CPFO)", "Deliver customized pitch deck to Presidio Cloud (GenAI track focus)", "October 19, 2026"],
        ["Enterprise Squad", "Identify and research 30 new target enterprise companies (10 each)", "October 21, 2026"],
        ["Enterprise Squad", "Dispatch first-touch outreach (Template A) to Zoho, Freshworks, Cognizant", "October 20, 2026"],
        ["Track Squad Lead", "Map 5 tracks to 5 dedicated prospective corporate sponsors", "October 21, 2026"],
        ["Track Squad Lead", "Follow up with Polygon (Web3) and LTIMindtree (FinTech)", "October 19, 2026"],
        ["Treasury Lead", "Prepare GST invoice template + SIST Indian Bank escrow details sheet", "October 20, 2026"],
        ["All Squad Members", "Share Rainmaker Referral Bounty link with 10 campus ambassadors each", "October 19, 2026"]
    ]
    add_styled_table(doc, action_headers, action_data)

    add_h2(doc, "Mandatory Weekly Review Rhythm")
    add_bullet(doc, "Monday 09:00 AM — Pipeline Status Review", "Review weekend responses, open follow-ups, and assign weekly target companies.")
    add_bullet(doc, "Wednesday 06:00 PM — Deck Customization Clinic", "Review customized challenge slides and tailored proposals with Design Lead.")
    add_bullet(doc, "Friday 05:00 PM — Escrow & Finance Reconciliation", "Reconcile Indian Bank account deposits, verify GST invoice issuance, and audit commission payouts.")
    add_bullet(doc, "Sunday 08:00 PM — Executive Briefing", "Submit weekly pipeline telemetry report to President Thenappan T and Faculty Coordinators.")

    doc.save(output_path)
    print(f"Generated Doc 5: {output_path}")

if __name__ == "__main__":
    build_doc5()
