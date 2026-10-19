import os
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx_utils import (
    init_document, add_header_banner, add_h1, add_h2, add_h3,
    add_body, add_bullet, add_callout, add_styled_table,
    HEX_AMBER, COLOR_NAVY, COLOR_SLATE_BLUE, COLOR_DARK_TEXT
)

def build_doc2():
    output_path = r"e:\AWS SBGL\Events\Kairos\teams\01_sponsorship_and_partnerships\word_documents\02_KAIROS_2027_Corporate_Pitch_Deck_Slide_Guide.docx"
    doc = init_document("CORPORATE PITCH DECK SLIDE-BY-SLIDE GUIDE")
    
    add_header_banner(
        doc,
        title="KAIROS 2027 (GRAND EDITION)",
        subtitle="Master 14-Slide Corporate Sponsorship Pitch Deck Guide\nComplete Slide Visuals, Content Copy, Presenter Talking Points & CXO Q&A Playbook",
        badges=[
            "PRESENTATION FORMAT: 16:9 4K (3840×2160)",
            "DESIGN LANGUAGE: OBSIDIAN-AMBER DARK MODE",
            "TARGET RUNTIME: 10–12 MINUTES",
            "SELF-CONTAINED OPERATIONAL GUIDE"
        ]
    )
    
    add_callout(
        doc,
        "This guide contains the complete slide-by-slide content, visual specifications, presenter speaking notes, and CXO discussion points for presenting KAIROS 2027 to corporate leadership. Team members presenting to VPs of Engineering, Heads of DevRel, or HR Directors should memorize these talking points.",
        title="PITCH DECK PURPOSE & PRESENTER INSTRUCTIONS",
        style="info"
    )
    
    # ---------------------------------------------------------
    # SECTION 1: PRESENTATION PHILOSOPHY & TECHNICAL SPECS
    # ---------------------------------------------------------
    add_h1(doc, "1. Presentation Philosophy & Technical Specifications")
    add_body(doc, "When pitching to corporate decision makers, our slide deck must project uncompromising aesthetic excellence and engineering discipline. Standard student PowerPoint decks with white backgrounds and bullet walls are strictly prohibited.")
    
    spec_headers = ["Design Element", "Technical Specification", "Presenter Rationale"]
    spec_data = [
        ["Canvas Ratio & Resolution", "16:9 Widescreen (3840 × 2160 px 4K Ultra-HD)", "Crisp rendering on 4K conference room screens and executive monitors"],
        ["Visual Palette", "Obsidian Abyss (#0D1117) & Cyber Gold/Amber (#FF9900)", "High-contrast developer-native aesthetic aligned with AWS branding"],
        ["Primary Typography", "Amazon Ember Display & Amazon Ember Regular", "Authoritative, modern tech typography signaling institutional affiliation"],
        ["Visual Rule", "Maximum 1 core thesis per slide; heavy data infographics", "Prevents cognitive overload; keeps executive attention locked on speaker"],
        ["Target Deck Duration", "10 to 12 minutes spoken + 8 minutes executive Q&A", "Respects CXO calendar constraints; leaves ample time for deal closing"]
    ]
    add_styled_table(doc, spec_headers, spec_data)

    # ---------------------------------------------------------
    # SECTION 2: SLIDE-BY-SLIDE WALKTHROUGH
    # ---------------------------------------------------------
    add_h1(doc, "2. Master 14-Slide Content, Visuals & Speaking Notes")
    
    # Slide 1
    add_h2(doc, "Slide 1: Hero Cover & Title Lockup")
    add_bullet(doc, "Visual Layout", "Deep Obsidian Abyss background with subtle glowing amber circuit vector trace. Top right: Dual emblem lockup of AWS Student Builder Groups and Sathyabama Institute of Science and Technology seal.")
    add_bullet(doc, "Slide Headline", "KAIROS 2027: THE GRAND HORIZON")
    add_bullet(doc, "Sub-Headline", "India's Flagship 48-Hour Student Cloud & Agentic AI Hackathon")
    add_bullet(doc, "Key Badges", "100% FREE ENTRY  •  100 ELITE TEAMS  •  ₹3.5L+ CAPITAL POOL (₹1.75L PURE CASH)  •  JAN 22–24, 2027")
    add_bullet(doc, "Presenter Footer", "Presented by AWS Student Builder Group — SIST Chapter, Sathyabama University, Chennai")
    add_callout(
        doc,
        "\"Good morning / afternoon. Thank you for taking the time to meet with us today. I am [Name], representing the AWS Student Builder Group at Sathyabama Institute of Science and Technology. On January 22nd to 24th, 2027, our university is hosting KAIROS 2027 — India's premier 48-hour continuous student hackathon. Today, I want to show you how [Company Name] can partner with us to capture unparalleled developer mindshare, recruit the top 5% of engineering builders in the country, and showcase your technology on a national stage.\"",
        title="SLIDE 1 PRESENTER SCRIPT",
        style="info"
    )

    # Slide 2
    add_h2(doc, "Slide 2: The Catalyst & Institutional Eminence")
    add_bullet(doc, "Visual Layout", "Two-column layout. Left: High-resolution architectural photography of Sathyabama campus and School of Computing. Right: Institutional metrics cards with subtle gold borders.")
    add_bullet(doc, "Key Content", "Sathyabama Institute of Science and Technology (Category-1 Deemed University, NAAC 'A++' Grade, NIRF Top 50, Chennai). Chartered under Worldwide Amazon Web Services Student Builder Groups Program. National reach across 120+ top engineering institutions in 20+ states.")
    add_callout(
        doc,
        "\"Before we talk about the event itself, it's important to understand who is backing this. Sathyabama is one of India's premier research universities, ranked in the Top 50 by NIRF with the highest NAAC A++ accreditation. Our technical chapter is directly affiliated with the global AWS Student Builder Groups network. This means every aspect of KAIROS—from our cloud infrastructure to our legal agreements and bank escrow—is backed by top-tier institutional governance.\"",
        title="SLIDE 2 PRESENTER SCRIPT",
        style="info"
    )

    # Slide 3
    add_h2(doc, "Slide 3: The 2-Tier Quality Funnel")
    add_bullet(doc, "Visual Layout", "Inverted funnel diagram showing two distinct filtration checkpoints.")
    add_bullet(doc, "Tier 0 (National Funnel)", "2,000+ applicant squads from IITs, NITs, BITS, and premier universities nationwide (Oct 15 – Dec 15).")
    add_bullet(doc, "Tier 1 (Online Qualifier)", "Top 250 semi-finalist teams undergo a 48-hour code sprint + Loom architecture demo + live Google Meet jury grilling (Jan 02–04).")
    add_bullet(doc, "Tier 2 (On-Campus Grand Finale)", "Top 100 elite teams (~400–600 hackers) assemble for 48 hours of uninterrupted physical hacking at Sathyabama University, Chennai (Jan 22–24).")
    add_bullet(doc, "Takeaway", "100% Free Entry guarantees pure meritocracy. Zero noise. Corporate sponsors interface exclusively with the top 5% builder talent in India.")
    add_callout(
        doc,
        "\"Most hackathons in India operate on an open-door policy—anyone who registers shows up. The result is noise. KAIROS operates completely differently. Because we charge ₹0 entry fees, we attract over 2,000 applicant squads nationwide. We put them through an intensive virtual qualifier that filters out 95% of applicants. The 100 teams that arrive on our campus on January 22nd represent the absolute top 5% of builder talent in the nation. That means every single engineer your team meets in Chennai is an exceptional hire.\"",
        title="SLIDE 3 PRESENTER SCRIPT",
        style="info"
    )

    # Slide 4
    add_h2(doc, "Slide 4: Strategic Tracks & Industry Pillars")
    add_bullet(doc, "Visual Layout", "5 horizontal cards with glowing track badges and tech tags.")
    add_bullet(doc, "Track 1: Agentic AI & Foundation Models", "Autonomous multi-agent workflows, AWS Bedrock, Claude 3.5 Sonnet, RAG pipelines, fine-tuned LLMs.")
    add_bullet(doc, "Track 2: Cloud-Native Resilient Systems", "High-throughput serverless microservices, distributed architectures, zero-downtime fault tolerance, Kubernetes.")
    add_bullet(doc, "Track 3: Decentralized Web3 & Cryptographic Security", "Zero-knowledge proofs, smart contract architecture, verifiable identity, tamper-proof state channels.")
    add_bullet(doc, "Track 4: Next-Gen FinTech & Algorithmic Engines", "High-frequency transaction ledgers, fraud detection AI, open banking APIs, automated risk telemetry.")
    add_bullet(doc, "Track 5: Open Enterprise & Societal Innovation", "Enterprise bottlenecks, smart healthcare, green logistics, sustainable supply chain optimization.")
    add_callout(
        doc,
        "\"Our hackathon is structured around five high-impact industry tracks. What makes this exciting for [Company Name] is that you don't just put a logo on a poster—you can own a track. You can bring your own API, your own developer platform, or your proprietary enterprise problem statement. Over 48 hours, 15 to 25 elite squads will build functional, production-ready software directly on your technology stack.\"",
        title="SLIDE 4 PRESENTER SCRIPT",
        style="info"
    )

    # Slide 5
    add_h2(doc, "Slide 5: The Pure Cash Prize Architecture (₹1,75,000 Pure Cash)")
    add_bullet(doc, "Visual Layout", "Prize podium graphic with liquid gold accents and verified bank escrow seal.")
    add_bullet(doc, "Champion (1st Place Overall)", "₹60,000 Pure Liquid Cash + Grand Championship Trophy + VC Incubation Fast-Track.")
    add_bullet(doc, "1st Runner-Up (2nd Place Overall)", "₹35,000 Pure Liquid Cash + Trophy.")
    add_bullet(doc, "2nd Runner-Up (3rd Place Overall)", "₹20,000 Pure Liquid Cash + Trophy.")
    add_bullet(doc, "5 Track Champions", "₹7,000 each = ₹35,000 Pure Liquid Cash.")
    add_bullet(doc, "Special Category Bounties", "₹25,000 Pure Cash (Women in Tech: ₹10k, Freshers: ₹7.5k, Scalable Cloud: ₹7.5k).")
    add_bullet(doc, "Non-Cash Perks", "$50,000+ AWS Cloud Credits, 500 JetBrains developer licenses, fast-track interview pathways.")
    add_callout(
        doc,
        "\"We do not offer coupon codes or voucher promises as main prizes. We offer ₹1,75,000 in pure liquid cash, held in verified university bank escrow. When the Grand Champions walk across the stage on January 24th, their prize money is transferred directly into their bank accounts within 72 hours. This serious financial commitment is why the best hackers from across the country compete at KAIROS.\"",
        title="SLIDE 5 PRESENTER SCRIPT",
        style="info"
    )

    # Slide 6
    add_h2(doc, "Slide 6: Corporate Sponsor ROI & Triple-Lock Value Proposition")
    add_bullet(doc, "Visual Layout", "Three distinct pillars with executive iconography.")
    add_bullet(doc, "Pillar 1: Direct Talent Acquisition & Fast-Track Hiring", "Unrestricted access to the national verified talent database of 2,000+ applicants and Top 100 finalist teams with live GitHub, LeetCode, and architectural telemetry for high-priority hiring and pre-placement interviews.")
    add_bullet(doc, "Pillar 2: Developer Tool & Platform Adoption", "Introduce your APIs, SDKs, or cloud services as flagship challenges with live developer stress-testing, bug discovery, and adoption across 400–600 builders.")
    add_bullet(doc, "Pillar 3: Main Stage Executive Immersion", "20-minute primetime keynote at Inauguration, VIP Grand Jury seats, branded hacker bays, 3840×1920 LED Wall center crest, and continuous 48-hour multicam global live stream commercials.")
    add_callout(
        doc,
        "\"When your executive team looks at this partnership, the ROI is triple-locked. First: Talent Acquisition. A typical campus recruitment drive costs lakhs in logistics. Here, you get 100 pre-screened teams with full GitHub code repositories and live project evaluations. Second: Developer Adoption. You get 500 developers actively coding on your platform for two full days. Third: Brand Eminence. Your company anchors the main stage, the live broadcast, and 500,000 digital impressions.\"",
        title="SLIDE 6 PRESENTER SCRIPT",
        style="info"
    )

    # Slide 7
    add_h2(doc, "Slide 7: Sponsorship Tiers & Investment Matrix")
    add_bullet(doc, "Visual Layout", "Clean 5-column executive matrix highlighting deliverables across Title, Co-Powered By, Associate, and Track tiers.")
    
    tier_summary = [
        ["Deliverable", "Title (₹2,00,000)", "Co-Powered (₹1,00,000)", "Associate (₹50,000)", "Track (₹25,000)"],
        ["Naming Rights", "'Presented By [Brand]'", "'Co-Powered By [Brand]'", "Official Associate", "Track Name"],
        ["LED Wall Logo", "Sole Center (Large)", "Side Crest (Medium)", "Grid Placement", "Rotating Logo"],
        ["Stage Backdrop (20x10ft)", "Hero Crest (35%)", "Sub-Hero (20%)", "Footer Strip", "Track Strip"],
        ["16 Standees", "ALL 16 Standees", "10 Standees", "2 Shared", "1 Dedicated"],
        ["Jerseys / Hoodies", "Prime Chest", "Sleeve / Back", "Back Grid", "Back Grid"],
        ["Keynote Slot", "20-Min Primetime", "10-Min Session", "5-Min Address", "Track Kickoff"],
        ["Grand Jury Seats", "2 VIP Seats", "1 VIP Seat", "1 Evaluator", "1 Track Evaluator"],
        ["Resume Database", "All 2,000+ National", "Top 250 Qualified", "Top 100 Finalists", "Track Finalists"],
        ["Live Stream Ads", "30s Every 2 Hours", "15s Every 4 Hours", "Static Logo", "Lower-Third Stinger"],
        ["Ground Kiosk", "10x10ft VIP Lounge", "6x6ft Kiosk", "Flyer Table", "Track Table"]
    ]
    add_styled_table(doc, tier_summary[0], tier_summary[1:])
    add_callout(
        doc,
        "\"Our engagement tiers are calibrated to fit different corporate objectives. Our Title Partnership at ₹2 Lakhs gives you apex naming rights, main stage keynote, center LED placement, and full national talent database access. For organizations focused on a specific technology or hiring domain, our Track Partnership at ₹25,000 allows you to sponsor a challenge track, evaluate teams, and access track-specific candidate repos.\"",
        title="SLIDE 7 PRESENTER SCRIPT",
        style="info"
    )

    # Slide 8
    add_h2(doc, "Slide 8: Branding & Visual Impact Across Stage & Apparel")
    add_bullet(doc, "Visual Layout", "High-fidelity mockups of the stage backdrop (20x10ft), 3840×1920 LED Wall center crest, custom heavyweight hoodies, streetwear t-shirts, smart NFC badges, and rollup standees.")
    add_bullet(doc, "Key Production Metrics", "110 Custom Heavyweight Hoodies, 550 Streetwear T-Shirts, 650 Jacquard Lanyards, 16 Rollup Standees (6x3ft) across the auditorium, foyer, and dining pavilion.")
    add_bullet(doc, "Print Deadline Alert", "Hard print freeze on December 20, 2026. Logos locked after this date cannot be printed on merchandise.")
    add_callout(
        doc,
        "\"We believe branding should look like high-end streetwear, not cheap promotional merchandise. Every participant, mentor, and judge receives custom heavyweight apparel that they wear long after the event. Your logo is woven directly into lanyards, printed on hoodies, and displayed across 16 venue standees. But I want to be transparent: our merchandise print freeze is December 20th. We must lock partner assets before that date.\"",
        title="SLIDE 8 PRESENTER SCRIPT",
        style="info"
    )

    # Slide 9
    add_h2(doc, "Slide 9: 48-Hour Continuous Global Live Stream & Media Metrics")
    add_bullet(doc, "Visual Layout", "Broadcast control room mockup with multicam YouTube Live/LinkedIn stream overlay.")
    add_bullet(doc, "Digital Metrics", "500,000+ digital impressions across Instagram (@awssbg_sist), LinkedIn, and YouTube.")
    add_bullet(doc, "National Campus Network", "120+ student Campus Ambassadors across 20+ states actively driving registrations and corporate taggings.")
    add_bullet(doc, "Broadcast Features", "Commercial video stingers broadcasted during peak hours, lower-third graphic overlays, and live executive keynote broadcast globally.")
    add_callout(
        doc,
        "\"KAIROS isn't confined to a campus hall in Chennai. We broadcast continuously for 48 hours with a dedicated multicam production crew. We feature 30-second video commercials for our Title and Co-Powered partners throughout the broadcast, reaching thousands of remote developers, alumni, and tech enthusiasts following the hackathon online.\"",
        title="SLIDE 9 PRESENTER SCRIPT",
        style="info"
    )

    # Slide 10
    add_h2(doc, "Slide 10: Physical On-Ground Footprint & Foyer VIP Lounges")
    add_bullet(doc, "Visual Layout", "Floor plan architectural layout of Sathyabama Grand Auditorium and Exhibition Foyer.")
    add_bullet(doc, "Key Facilities", "Main Stage & 400-seat auditorium, 100 team hacker bays with dedicated power grids, Grand Foyer VIP Exhibition Kiosks (10x10ft lounges), Mentor Consultation Rooms, and Midnight Refreshment Pavilions.")
    add_callout(
        doc,
        "\"In our grand foyer, we provide dedicated space for our partners to set up experiential lounges and recruitment kiosks. Your talent team can conduct 1-on-1 interviews with finalists, your DevRel engineers can run live debugging clinics, and your brand team can distribute merchandise directly to 500 top developers.\"",
        title="SLIDE 10 PRESENTER SCRIPT",
        style="info"
    )

    # Slide 11
    add_h2(doc, "Slide 11: Past Track Record, Community Footprint & Partner Testimonials")
    add_bullet(doc, "Visual Layout", "Collage of past hackathon editions, crowd energy, award ceremonies, and logos of existing confirmed partners.")
    add_bullet(doc, "Confirmed Milestone", "JetBrains secured as official tooling partner (500 All-Product Developer Licenses).")
    add_bullet(doc, "Active Pipeline", "AWS, Presidio Cloud, Zoho, Freshworks, and Red Bull currently in advanced stages.")
    add_callout(
        doc,
        "\"Our community has a demonstrated history of delivering flawless technical summits. JetBrains has already joined us as an official partner, providing 500 licenses. Red Bull is partnering for our midnight energy experience. When [Company Name] joins KAIROS 2027, you are entering an elite cohort of industry champions.\"",
        title="SLIDE 11 PRESENTER SCRIPT",
        style="info"
    )

    # Slide 12
    add_h2(doc, "Slide 12: Crowdsourced Rainmaker Referral Engine")
    add_bullet(doc, "Visual Layout", "Decentralized community flywheel diagram illustrating student referrals across 20+ states.")
    add_bullet(doc, "Key Mechanism", "10% – 15% cash commission paid to student referrers upon corporate escrow clearance (₹20,000 – ₹30,000 for Title).")
    add_bullet(doc, "Corporate Value", "Ensures corporate sponsors receive hyper-local advocacy and word-of-mouth endorsement from campus builders nationwide.")
    add_callout(
        doc,
        "\"We also run the Rainmaker program—an innovative referral engine that mobilizes hundreds of student leaders across India to champion our partners. When a company sponsors KAIROS, campus ambassadors across 20 states actively celebrate and endorse your brand on their campus channels.\"",
        title="SLIDE 12 PRESENTER SCRIPT",
        style="info"
    )

    # Slide 13
    add_h2(doc, "Slide 13: Institutional Governance, Bank Escrow & Audited Compliance")
    add_bullet(doc, "Visual Layout", "Official bank badge, university seal, and tax compliance certificates.")
    add_bullet(doc, "Banking Credentials", "Bank: Indian Bank, SIST Branch, Chennai | Beneficiary: Sathyabama Institute of Science and Technology | IFSC: IDIB000S201 | MICR: 600019156.")
    add_bullet(doc, "Compliance Assurance", "100% compliant with university accounting. Formal GST tax invoices issued. ₹1.75L prize pool held in audited escrow with 72-hour automated NEFT payout guarantee.")
    add_callout(
        doc,
        "\"From a corporate compliance and audit standpoint, everything is rock-solid. All payments are made directly to Sathyabama University's official Indian Bank account. We issue standard GST invoices for your procurement records. And all prize funds are strictly escrowed to guarantee timely student disbursement.\"",
        title="SLIDE 13 PRESENTER SCRIPT",
        style="info"
    )

    # Slide 14
    add_h2(doc, "Slide 14: Call to Action, Timeline Deadlines & Executive Contacts")
    add_bullet(doc, "Visual Layout", "Timeline chevron graphic leading up to January 22, 2027, flanked by leadership contact cards.")
    add_bullet(doc, "Immediate Next Steps", "Lock agreed tier by November 15  •  Execute MoU by November 30  •  Asset & Logo Delivery by December 10  •  Hard Print Freeze on December 20.")
    add_bullet(doc, "Executive Contacts", "Nikki (Nangaiyar M) (Sponsorship Lead): +91 8754976892  •  President Thenappan T: +91 6381801640  •  Email: nangaiyarmuthkrishnan@gmail.com / sistawscc@gmail.com.")
    add_callout(
        doc,
        "\"To guarantee prime placement across our stage LED wall, live stream, and merchandise, we would love to align on a tier this week. Our print freeze is December 20th, and we are locking our Title and Co-Powered partners by mid-November. Can we schedule a brief follow-up with your procurement team this Friday to finalize the details? Thank you for your partnership.\"",
        title="SLIDE 14 PRESENTER SCRIPT",
        style="info"
    )

    doc.save(output_path)
    print(f"Generated Doc 2: {output_path}")

if __name__ == "__main__":
    build_doc2()
