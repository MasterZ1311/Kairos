import os
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx_utils import (
    init_document, add_header_banner, add_h1, add_h2, add_h3,
    add_body, add_bullet, add_callout, add_styled_table,
    HEX_AMBER, COLOR_NAVY, COLOR_SLATE_BLUE, COLOR_DARK_TEXT
)

def build_doc1():
    output_path = r"e:\AWS SBGL\Events\Kairos\teams\01_sponsorship_and_partnerships\word_documents\01_KAIROS_2027_Sponsorship_Strategy_and_Outreach_Playbook.docx"
    doc = init_document("CORPORATE SPONSORSHIP STRATEGY & OUTREACH PLAYBOOK")
    
    add_header_banner(
        doc,
        title="KAIROS 2027 (GRAND EDITION)",
        subtitle="Corporate Sponsorship Strategy, Outreach Playbook & Pitching Kit\nA Self-Contained Master Operational Guide for the Sponsorship & Partnerships Team",
        badges=[
            "EVENT DATES: JAN 22–24, 2027 (48 HOURS)",
            "SCALE: 100 ELITE TEAMS (400–600 HACKERS)",
            "ZERO ENTRY FEE (100% FREE)",
            "CAPITAL POOL: ₹3.5L–₹4.0L+ UNCAPPED"
        ]
    )
    
    add_callout(
        doc,
        "This playbook is completely self-contained. It contains all event numbers, calibrated tier matrices, ready-to-send email copy, phone pitch scripts, objection handling battlecards, bank escrow details, and contact rosters. Team members do NOT need to cross-reference any other file or directory.",
        title="DOCUMENT PURPOSE & OPERATIONAL AUTONOMY",
        style="info"
    )
    
    # ---------------------------------------------------------
    # SECTION 1: EXECUTIVE EVENT ARCHITECTURE
    # ---------------------------------------------------------
    add_h1(doc, "1. Executive Event Architecture & Blueprint")
    add_body(doc, "KAIROS 2027 (Grand Edition) is the premier 48-hour continuous national technical hackathon hosted by the AWS Student Builder Group (SIST Chapter) at Sathyabama Institute of Science and Technology, Chennai. Operating under an uncompromised 100% Free / Zero Entry Fee mandate, the summit guarantees absolute meritocracy while delivering an elite competitive arena for the nation's top engineering minds.")
    
    overview_headers = ["Key Dimension", "Operational Specification", "Strategic Implication for Sponsors"]
    overview_data = [
        ["Event Name", "KAIROS 2027 (Grand Edition)", "Brand prestige, national student community reach"],
        ["Event Duration", "48 Hours Non-Stop (Day & Night)", "Continuous 48-hour brand immersion, product stress testing"],
        ["Event Dates", "January 22 – 24, 2027", "Prime Q1 corporate recruitment and branding window"],
        ["Online Qualifier", "January 02 – 04, 2027", "Virtual screening filtering 2,000+ teams down to Top 100"],
        ["Application Window", "October 15 – December 15, 2026", "2-month national campaign across 120+ colleges in 20+ states"],
        ["Print Freeze Deadline", "December 20, 2026 (HARD)", "All sponsor logos must be cleared for banners, tees, hoodies"],
        ["Participant Scale", "100 Elite Finalist Teams (~400–600 Hackers)", "Zero noise; sponsors interface exclusively with top 5% talent"],
        ["Total Applicants", "2,000+ Teams Nationwide", "Massive national resume and GitHub telemetry database"],
        ["Student Entry Fee", "₹0 — 100% FREE for all participants", "Attracts top-tier merit builders across IITs, NITs, BITS, SIST"],
        ["Hospitality Provided", "6 Buffet Meals, Stay, Midnight Fuel, Sandboxes", "Full corporate subsidization driving immense goodwill"],
        ["Pure Cash Prize Pool", "₹1,75,000 Pure Liquid Cash (Escrowed)", "High-stakes competition attracting elite builders"],
        ["Operating Capital Pool", "₹3,50,000 – ₹4,00,000 (Baseline Uncapped)", "Ensures stadium-grade production, 4K stream, premium merch"],
        ["Host Chapter", "AWS Student Builder Group (SIST Chapter)", "Chartered under Worldwide AWS Student Builder Groups"],
        ["Host Institution", "Sathyabama Institute of Science and Technology", "NAAC 'A++' Grade, NIRF Top 50 University, Chennai"]
    ]
    add_styled_table(doc, overview_headers, overview_data)
    
    # ---------------------------------------------------------
    # SECTION 2: SPONSORSHIP PHILOSOPHY & THE 4-PILLAR STRATEGY
    # ---------------------------------------------------------
    add_h1(doc, "2. Sponsorship Philosophy & Corporate Strategy")
    add_body(doc, "Sponsorship is not philanthropy or charity. It is a high-value commercial transaction where corporate enterprises purchase access to developer mindshare, high-priority engineering recruitment, brand immersion, and open innovation. Our outreach targets four calibrated sponsor segments:")
    
    add_bullet(doc, "1. Enterprise Cloud & Big Tech (Title & Co-Powered By)", "Targeting cloud providers, AI labs, and enterprise SaaS firms (e.g. AWS, Microsoft, Google Cloud, Zoho, Freshworks) seeking 400–600 top builders building on their APIs, models, and architectures.")
    add_bullet(doc, "2. Track & Developer Tool Partners (₹25,000 – ₹50,000 per Track)", "Companies seeking developer adoption for APIs, SDKs, libraries, or developer platforms (e.g. Postman, Supabase, Appwrite, MongoDB, Polygon).")
    add_bullet(doc, "3. In-Kind Experiential & Fuel Partners", "Energy drink brands (Red Bull, Monster), beverage companies, cloud credit grants, and software tool licensing (JetBrains 500 licenses already secured).")
    add_bullet(doc, "4. Non-Tech, Consumer & CSR Partners (BFSI, FMCG, Retail)", "Corporate enterprises leveraging Track 5 (Open Enterprise Innovation) to solve operational bottlenecks, recruit data/IT talent, and fulfill CSR/ESG education charters.")

    # ---------------------------------------------------------
    # SECTION 3: CALIBRATED TIER MATRIX & DELIVERABLES
    # ---------------------------------------------------------
    add_h1(doc, "3. Calibrated Tier Structure & Deliverable Matrix")
    add_body(doc, "Every deliverable promised in this matrix is strictly tracked and guaranteed by the organizing committee. Tier benefits are non-dilutable:")
    
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
        ["Exhibition Stall in Foyer", "Prime 10x10ft VIP Lounge", "Dedicated 6x6ft Kiosk", "Shared Standee Table", "Track Table", "Sampling Station"],
        ["Social Media Spotlight", "4 Dedicated Posts + Reel", "2 Dedicated Posts + Story", "1 Dedicated Post", "1 Joint Post", "1 Product Story"],
        ["Award Conferral", "Grand Champion Trophy", "1st Runner-Up Trophy", "Category Trophy", "Track Winner Trophy", "Merit Kits"]
    ]
    add_styled_table(doc, tier_headers, tier_data)
    
    # ---------------------------------------------------------
    # SECTION 4: BUDGET & CAPITAL ALLOCATION
    # ---------------------------------------------------------
    add_h1(doc, "4. Financial Architecture & Capital Allocation")
    add_body(doc, "Our operating financial architecture operates on a ₹3,50,000 – ₹4,00,000 minimum capital baseline with NO UPPER LIMIT. Every rupee raised directly scales participant experience:")
    
    budget_headers = ["Capital Source (Inflow)", "Target (₹)", "Expenditure Category (Outflow)", "Allocated (₹)"]
    budget_data = [
        ["Title Sponsor (1 Slot)", "₹2,00,000", "Pure Liquid Cash Prize Pool (Escrowed)", "₹1,75,000"],
        ["Co-Powered By Sponsors (1–2 Slots)", "₹1,00,000", "Participant Swag, Hoodies & Smart NFC Badges", "₹65,000"],
        ["Track & Bounty Partners (4–5 Tracks)", "₹1,00,000", "6 Full Buffet Meals, Midnight Fuel & Catering", "₹65,000"],
        ["Sathyabama University Grant", "₹50,000", "AV, 3840x1920 LED Wall & 4K Multicam Live Stream", "₹25,000"],
        ["Associate & In-Kind Tooling", "₹25,000+", "VIP Jury Hospitality, Mementos & Trophies", "₹10,000"],
        ["Total Projected Capital Inflow", "₹4,75,000+", "Dual Generator Failover, High-Density LAN & Power", "₹10,000"],
        ["Baseline Operational Floor", "₹3,50,000", "Operational Contingency & Scaled Bounties", "Remaining Balance"]
    ]
    add_styled_table(doc, budget_headers, budget_data)
    
    # ---------------------------------------------------------
    # SECTION 5: RAINMAKER REFERRAL BOUNTIES
    # ---------------------------------------------------------
    add_h1(doc, "5. The Crowdsourced Rainmaker Referral Bounties")
    add_body(doc, "To decentralize and accelerate our outreach across the country, Kairos 2027 operates an open student sponsorship referral commission engine. Any student in India—including Campus Ambassadors, registered hackers, and student leaders—can connect corporate sponsors with our team and earn direct liquid cash commissions:")
    
    rain_headers = ["Sponsorship Tier Closed", "Deal Value", "Commission %", "Student Cash Payout", "Executive Perks & Honors"]
    rain_data = [
        ["Title Presenting Partner", "₹2,00,000", "10% – 15%", "₹20,000 – ₹30,000 Cash", "National Corporate Rainmaker Trophy on stage, VIP Pass, President Rec Letter"],
        ["Co-Powered By Partner", "₹1,00,000", "10% – 12%", "₹10,000 – ₹12,000 Cash", "VIP Jury Lounge Access, President Rec Letter, Cyber Streetwear Hoodie"],
        ["Associate / Gold Partner", "₹50,000", "10%", "₹5,000 Cash", "Exclusive Merch Kit, Official Partner Certificate"],
        ["Track & Bounty Partner", "₹25,000", "10%", "₹2,500 Cash", "Official Partner Certificate, Swag Drop"],
        ["In-Kind F&B / Fuel Deals", "Product Value", "Fixed Bounty", "₹3,000 – ₹5,000 Cash", "Swag Drop & Stage Recognition"]
    ]
    add_styled_table(doc, rain_headers, rain_data)
    
    add_callout(
        doc,
        "1. Zero Financial Risk: Commissions are paid out strictly after corporate funds clear into the Sathyabama University audited bank account.\n"
        "2. 21-Day Lead Lock: Leads submitted via email to sistawscc@gmail.com or CPFO Nikki are locked to the referrer for 21 days.\n"
        "3. Pitching Assistance: Referrers do NOT need to negotiate; CPFO Nikki and President Thenappan T handle corporate pitching and legal closing.\n"
        "4. Rapid Payout SLA: Payouts transferred via UPI/NEFT within 48–72 hours of corporate fund clearance.",
        title="RAINMAKER PROGRAM OPERATIONAL SLA",
        style="success"
    )
    
    # ---------------------------------------------------------
    # SECTION 6: READY-TO-SEND EMAIL TEMPLATES
    # ---------------------------------------------------------
    add_h1(doc, "6. Ready-to-Send Outreach Email Templates")
    add_body(doc, "These templates are battle-tested. Copy, customize the bracketed fields [Company Name], and dispatch:")
    
    add_h2(doc, "Template A: Enterprise / Title Partner Outreach")
    template_a = (
        "Subject: Exclusive Title Presenting Partnership: KAIROS 2027 (India's Premier 48-Hour Cloud & AI Hackathon) | AWS Student Builder Group SIST\n\n"
        "Dear [Sponsorship Lead / VP Engineering / Talent Acquisition Lead],\n\n"
        "Greetings from the AWS Student Builder Group at Sathyabama Institute of Science and Technology (SIST), Chennai!\n\n"
        "On January 22–24, 2027, we are hosting KAIROS 2027 (Grand Edition) — our premier 48-hour continuous National Technical Hackathon at Sathyabama Institute of Science and Technology, Chennai.\n\n"
        "To ensure pure meritocracy, KAIROS 2027 collects ZERO ENTRY FEES from participants, attracting over 2,000+ national applicant teams across IITs, NITs, BITS, and premier engineering institutions. Following an intensive Online Technical Qualifier (January 02–04), only the Top 100 Elite Teams (Teams of 4–6 students, ~400–600 developers) advance to the physical on-campus sprint.\n\n"
        "We would be honored to invite [Company Name] as our Exclusive Title Presenting Partner ('Kairos 2027 Presented by [Company Name]'). As our apex patron, [Company Name] will anchor the national stage as the definitive champion of India's premier student builder talent.\n\n"
        "Why Partner with Kairos 2027?\n"
        "1. Exclusive Developer Mindshare: 400–600 top-tier pre-screened engineers actively building, deploying, and stress-testing on your APIs, models, and cloud infrastructure over 48 uninterrupted hours.\n"
        "2. Verified Talent Acquisition & Fast-Track Hiring: Complete, unrestricted access to the verified national resume and GitHub telemetry database of 2,000+ national applicants and 100 finalist teams for direct engineering hiring, internships, and pre-placement interviews.\n"
        "3. Grand Stage Production & 48-Hour Live Broadcast: Prominent centerpiece branding across our 3840×1920 Main Stage LED Wall, 20x10ft stage backdrop, prime 20-minute inaugural keynote address, custom streetwear hoodies, and continuous 48-hour multicam global live stream.\n"
        "4. Apex Championship Prestige & Scalable Prize Escrow: Command the main stage to confer the prestigious National Grand Champion Trophy and anchor our ₹1,75,000+ pure liquid cash prize escrow pool (amplified by $50,000+ in AWS Cloud Credits). As Title Partner, your organization holds exclusive naming rights on grand awards and the open gateway to endow custom corporate problem bounties.\n\n"
        "Could we connect for a brief 10-minute discovery call this Thursday or Friday to explore tailoring an apex partnership package for [Company Name]?\n\n"
        "Warm regards,\n\n"
        "Nikki (Nangaiyar M) (Register No: 44612059)\n"
        "Chief Partnerships & Finance Officer (CPFO) & Sponsorship Lead\n"
        "AWS Student Builder Group — SIST Chapter\n"
        "Sathyabama Institute of Science and Technology, Chennai\n"
        "Phone: +91 8754976892 | Email: nangaiyarmuthkrishnan@gmail.com / sistawscc@gmail.com"
    )
    add_callout(doc, template_a, title="COPY-PASTE TEMPLATE A: TITLE & ENTERPRISE OUTREACH", style="info")
    
    add_h2(doc, "Template B: Midnight Energy & Beverage Sponsorship (Red Bull / Monster)")
    template_b = (
        "Subject: Midnight Energy & Beverage Partnership: KAIROS 2027 (500 National Developers) | AWS SBG SIST\n\n"
        "Hi [Brand Marketing Team / South Regional Campus Lead],\n\n"
        "The AWS Student Builder Group at Sathyabama Institute of Science and Technology is hosting KAIROS 2027 (January 22–24, 2027) — a grueling 48-hour continuous national hackathon where 500 top student coders hack non-stop through two consecutive nights.\n\n"
        "We would love to invite [Brand Name] as our Official Midnight Energy & Fuel Partner.\n\n"
        "What We Offer:\n"
        "• Exclusive product sampling and distribution during our Midnight Hacking Sprint (01:00 AM – 04:00 AM) to 500 high-energy student builders.\n"
        "• 'Midnight Energy Station Powered by [Brand]' branded installation and grand foyer signage.\n"
        "• Dedicated social media reels, high-energy product photography, and stage shoutouts during live broadcast.\n\n"
        "Could we connect for 5 minutes to arrange delivery of beverage inventory for the event?\n\n"
        "Best regards,\n\n"
        "Nikki (Nangaiyar M) (Phone: +91 8754976892 | Email: nangaiyarmuthkrishnan@gmail.com)\n"
        "CPFO & Sponsorship Lead, AWS Student Builder Group SIST"
    )
    add_callout(doc, template_b, title="COPY-PASTE TEMPLATE B: BEVERAGE & ENERGY OUTREACH", style="info")

    add_h2(doc, "Template C: Track & Bounty Partner Outreach (Web3 / AI / FinTech)")
    template_c = (
        "Subject: Dedicated Challenge Track & Bounty Partnership: KAIROS 2027 | AWS Student Builder Group SIST\n\n"
        "Hi [Developer Ecosystem Lead / DevRel Manager],\n\n"
        "On January 22–24, 2027, the AWS Student Builder Group at Sathyabama Institute of Science and Technology, Chennai is hosting KAIROS 2027 — a 48-hour national hackathon featuring 100 elite student teams (~400–600 developers) chosen from 2,000+ national applicants.\n\n"
        "We are inviting [Company Name] to sponsor our [Track Name: e.g. Agentic AI / Decentralized Web3 / Cloud Systems] at ₹25,000.\n\n"
        "What [Company Name] Gets:\n"
        "1. Direct Developer Adoption: 15–25 elite teams actively building applications using your API / SDK / tool.\n"
        "2. Named Track & Trophy: '[Company Name] Track Championship' awarded on the main stage.\n"
        "3. Track Evaluator Seat: Your engineering team joins the jury panel to evaluate prototypes and identify talent.\n"
        "4. Full Access to Track Resumes: Direct hiring access to student builders who built on your technology.\n\n"
        "Can we schedule a 10-minute sync this week to finalize the challenge statement?\n\n"
        "Best regards,\n\n"
        "Nikki (Nangaiyar M) (Phone: +91 8754976892 | Email: nangaiyarmuthkrishnan@gmail.com)\n"
        "CPFO & Sponsorship Lead, AWS Student Builder Group SIST"
    )
    add_callout(doc, template_c, title="COPY-PASTE TEMPLATE C: TRACK & BOUNTY OUTREACH", style="info")

    add_h2(doc, "Template D: Non-Tech & Consumer Brand Outreach (FMCG / BFSI / Retail)")
    template_d = (
        "Subject: Gen-Z Youth Innovation & Brand Partnership: KAIROS 2027 (500+ Campus Innovators) | AWS SBG SIST\n\n"
        "Dear [Marketing Director / Brand Partnerships Lead / CSR Head],\n\n"
        "Greetings from the AWS Student Builder Group at Sathyabama Institute of Science and Technology, Chennai!\n\n"
        "On January 22–24, 2027, we are hosting KAIROS 2027 (Grand Edition) — a premier 48-hour continuous National Student Summit uniting 100 elite teams (~400–600 top developers and innovators) selected from 2,000+ applicants across premier universities nationwide.\n\n"
        "Because KAIROS 2027 is 100% Free with Zero Entry Fees for students, we are collaborating with visionary consumer and corporate brands to power this transformative youth experience.\n\n"
        "Why [Brand Name] Should Partner With Kairos 2027:\n"
        "1. Direct Gen-Z Experiential Immersion: 48 non-stop hours of intense engagement with 500+ passionate student builders, tech creators, and campus micro-influencers. Exclusive setup for an interactive brand lounge, product sampling, and live demos in our grand foyer.\n"
        "2. Massive Digital & Media Footprint: 500,000+ impressions across Instagram (@awssbg_sist) and LinkedIn, driven by our 120+ Campus Ambassadors nationwide, with brand commercials streamed on our 48-hour multicam global live stream.\n"
        "3. Custom Brand Innovation Challenge: Present a real-world consumer, retail, sustainability, or financial challenge under our Open Innovation Track, with 100 elite squads building prototypes to solve it.\n"
        "4. Corporate Social Responsibility & Diversity: Directly empower high-merit students and co-title our Women-in-Tech and Emerging Scholar bounties.\n\n"
        "Our partnership packages range from dedicated Track Bounties (₹25,000) and Co-Powered Partnerships (₹1,00,000) to our Exclusive Title Presenting Partner (₹2,00,000).\n\n"
        "Could we connect for a brief 10-minute call this week to explore how we can spotlight [Brand Name] to India's top engineering youth?\n\n"
        "Warm regards,\n\n"
        "Nikki (Nangaiyar M) (Register No: 44612059)\n"
        "Chief Partnerships & Finance Officer (CPFO) & Sponsorship Lead\n"
        "AWS Student Builder Group — SIST Chapter\n"
        "Sathyabama Institute of Science and Technology, Chennai\n"
        "Phone: +91 8754976892 | Email: nangaiyarmuthkrishnan@gmail.com"
    )
    add_callout(doc, template_d, title="COPY-PASTE TEMPLATE D: NON-TECH & CONSUMER BRAND OUTREACH", style="info")

    # ---------------------------------------------------------
    # SECTION 7: COLD CALLING & INMAIL SCRIPTS
    # ---------------------------------------------------------
    add_h1(doc, "7. Cold Calling & LinkedIn InMail Scripts")
    add_h2(doc, "60-Second Phone Pitch Script (Corporate Switchboard Bypass)")
    phone_script = (
        "\"Good morning. My name is [Your Name], calling on behalf of the AWS Student Builder Group at Sathyabama Institute of Science and Technology, Chennai.\n\n"
        "We are hosting KAIROS 2027 — India's premier 48-hour national student hackathon with 600 top engineering builders from IITs, NITs, and premier universities.\n\n"
        "I am calling to connect with the team responsible for University Talent Acquisition, Developer Relations, or Corporate Partnerships regarding our flagship campus recruitment and technology showcase slots.\n\n"
        "Could you please direct me to the office of [Name of POC] or the Head of University Relations? Thank you.\""
    )
    add_callout(doc, phone_script, title="PHONE SCRIPT: GATEKEEPER BYPASS", style="warning")

    add_h2(doc, "LinkedIn InMail Script (For Heads of DevRel & University Hiring)")
    linkedin_script = (
        "\"Hi [First Name], noticed your work leading [DevRel / Tech Hiring] at [Company Name].\n\n"
        "On Jan 22–24, 2027, the AWS Student Builder Group at Sathyabama University is hosting KAIROS 2027 — 100 elite student teams (~500 builders) hacking non-stop for 48 hours across AI, Cloud, and Web3.\n\n"
        "We're opening select partnership slots for [Company Name] to access pre-vetted engineering resumes, run a custom challenge track, and interface directly with top builder talent.\n\n"
        "Would you be open to a 5-minute chat this week? Happy to share our 1-page executive prospectus.\""
    )
    add_callout(doc, linkedin_script, title="LINKEDIN INMAIL SCRIPT", style="info")

    # ---------------------------------------------------------
    # SECTION 8: OBJECTION HANDLING BATTLECARDS
    # ---------------------------------------------------------
    add_h1(doc, "8. Objection Handling Battlecards")
    add_body(doc, "When prospective sponsors push back, deliver these exact calculated responses:")
    
    obj_headers = ["Corporate Objection", "Underlying Concern", "Immediate Spoken Response"]
    obj_data = [
        ["'We don't have budget for events right now.'", "Wrong budget bucket / timing", "'Totally understand. Many partners fund this from University Recruiting or DevRel adoption rather than standard marketing. Which department leads your tech hiring?'"],
        ["'We sponsored student events before and got zero ROI.'", "Burned by unorganized fests", "'We hear that often. That's why KAIROS is 100% free with a dual-stage qualifier filtering 2,000 teams to 100 elite squads. Plus, we deliver an audited 10-slide ROI Dossier within 10 days post-event.'"],
        ["'Just email us more information.'", "Polite brush-off", "'I will gladly send our executive prospectus right now. So I don't flood your inbox, what is your primary focus right now—talent acquisition, API adoption, or brand visibility?'"],
        ["'₹2 Lakhs is too expensive for our company.'", "Budget mismatch", "'Understood. That is why we designed our Track Partner tier at ₹25,000, which gives you a dedicated challenge track, evaluator seat, and candidate code repos. Shall we explore that tier?'"],
        ["'We are not a tech company; this doesn't fit.'", "Perception of hackathons", "'Every enterprise relies on tech and young consumers. Non-tech partners use our Open Innovation track to solve supply chain and retail bottlenecks, while reaching 500,000+ Gen-Z impressions.'"],
        ["'How do we know a student-led event is reliable?'", "Institutional trust", "'KAIROS is backed by Sathyabama Institute of Science and Technology (NAAC 'A++', NIRF Top 50). All funds flow into the university bank account, and the Dean and Faculty countersign every MoU.'"],
        ["'We need 4 weeks to get internal approvals.'", "Procrastination", "'We understand corporate review cycles. However, our hard Print Freeze is December 20th. After that, no logos can be printed on 110 hoodies, 550 tees, or stage backdrops. Can we lock a provisional MoU by [date]?'"],
        ["'Can we pay in installments across two quarters?'", "Cash flow timing", "'Yes. We offer a 50-50 structured schedule: 50% upon signing the MoU to reserve prime deliverables, and 50% cleared by December 10th prior to print release.'"]
    ]
    add_styled_table(doc, obj_headers, obj_data)

    # ---------------------------------------------------------
    # SECTION 9: FOLLOW-UP SEQUENCE & CADENCE
    # ---------------------------------------------------------
    add_h1(doc, "9. Follow-Up Cadence & Pipeline Execution")
    add_body(doc, "80% of sponsorship deals close on the 3rd to 5th contact. Follow this strict cadence:")
    add_bullet(doc, "Day 1: Initial Outreach", "Send customized email (Template A, B, C, or D) + connect on LinkedIn with personalized note.")
    add_bullet(doc, "Day 3: The Polite Bump", "'Hi [Name], following up to confirm you received our note regarding KAIROS 2027. Would Thursday 3 PM work for a brief 10-minute sync?'")
    add_bullet(doc, "Day 7: The Value-Add Touch", "'Hi [Name], sharing a quick update: JetBrains just came on board as our official tooling partner. We're locking our 5 challenge tracks this week and would love to reserve the [Track Name] slot for [Company].'")
    add_bullet(doc, "Day 14: The Urgency & Print Freeze Notice", "'Hi [Name], we are finalizing our stage backdrop and merchandise printing specifications for our December 20 hard freeze. To guarantee [Company Name]'s crest on 600 builder jerseys, we would need to confirm our tier by this Friday.'")

    # ---------------------------------------------------------
    # SECTION 10: INSTITUTIONAL BANKING & GOVERNANCE
    # ---------------------------------------------------------
    add_h1(doc, "10. Institutional Banking, Escrow & Compliance")
    add_body(doc, "All sponsorships are deposited directly into the official audited institutional bank account of Sathyabama Institute of Science and Technology. GST invoices and official receipts are issued for corporate accounting:")
    
    bank_headers = ["Account Detail Parameter", "Official Institutional Record"]
    bank_data = [
        ["Account Holder / Beneficiary", "SATHYABAMA INSTITUTE OF SCIENCE AND TECHNOLOGY"],
        ["Bank Name", "Indian Bank"],
        ["Branch", "Sathyabama University Branch, Jeppiaar Nagar, Chennai – 600119"],
        ["Account Type", "Institutional Project / Escrow Account"],
        ["IFSC Code", "IDIB000S201"],
        ["MICR Code", "600019156"],
        ["Tax Compliance", "Official GST-Compliant Tax Invoice issued upon fund clearance"],
        ["Prize Escrow Protocol", "₹1,75,000 held in audited escrow, disbursed via NEFT within 72 hours of Grand Finale"]
    ]
    add_styled_table(doc, bank_headers, bank_data)

    # ---------------------------------------------------------
    # SECTION 11: LEADERSHIP ROSTER & CONTACTS
    # ---------------------------------------------------------
    add_h1(doc, "11. Leadership & Team Accountability Roster")
    add_body(doc, "For all corporate negotiations, MoU executions, and escalated questions, contact the leadership team:")
    
    roster_headers = ["Role", "Officer Name", "Register No", "Contact Information", "Key Mandate"]
    roster_data = [
        ["Super Head 1: CPFO & Sponsorship Lead", "Nikki (Nangaiyar M)", "44612059", "+91 8754976892\nnangaiyarmuthkrishnan@gmail.com", "Overall sponsorship lead, corporate pitches, negotiations, contract closing"],
        ["President & SBGL (Apex Chapter)", "Thenappan T", "44110855", "+91 6381801640\nthenappanmasterz1311@gmail.com", "Apex chapter oversight, institutional representation, key enterprise pitches"],
        ["Faculty Coordinator", "Dr. K. Ashok Kumar", "Faculty CSE", "ashokkumar.cse@sathyabama.ac.in", "University endorsement letters, institutional approvals, administrative oversight"],
        ["Faculty Coordinator", "Dr. Balapriya .S", "Faculty CSE", "balapriya.cse@sathyabama.ac.in", "University endorsement letters, MoU vetting, accounting clearance"],
        ["Dean, School of Computing", "Dr. L. Lakshmanan", "Dean CSE", "dean.computing@sathyabama.ac.in", "Official institutional signatory for MoUs and University grant sanction"]
    ]
    add_styled_table(doc, roster_headers, roster_data)
    
    doc.save(output_path)
    print(f"Generated Doc 1: {output_path}")

if __name__ == "__main__":
    build_doc1()
