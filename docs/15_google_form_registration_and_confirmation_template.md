# Google Form Templates & National Participant Data Architecture — Grand Edition

**Document Reference:** `docs/15_google_form_registration_and_confirmation_template.md`  
**Governing Standard:** [00_hackathon_master_brief.md](./00_hackathon_master_brief.md) · [02_agenda_rounds_and_judging_rubric.md](./02_agenda_rounds_and_judging_rubric.md) · [06_tracks_problem_statements_and_tech.md](./06_tracks_problem_statements_and_tech.md) · [08_event_operations_and_volunteer_manual.md](./08_event_operations_and_volunteer_manual.md) · [09_participant_handbook_and_rules.md](./09_participant_handbook_and_rules.md) · [14_official_letters_and_administrative_approvals.md](./14_official_letters_and_administrative_approvals.md) · [18_team_structure_leads_and_workforce_deployment.md](./18_team_structure_leads_and_workforce_deployment.md) · [20_indoor_auditorium_venue_transition_and_budget_plan.md](./20_indoor_auditorium_venue_transition_and_budget_plan.md)  
**Host Entity:** AWS Student Builder Group (AWS SBG) — SIST Chapter  
**Sponsoring Department:** School of Computing, Sathyabama Institute of Science and Technology (Deemed to be University), Chennai – 600119  
**Lead Coordinator:** Thenappan T (Register No: `44110855`), President & SBGL  
**Faculty Coordinators:** Dr. K. Ashok Kumar & Dr. Balapriya .S (Department of CSE, SIST)  
**Official Email:** `sistawscc@gmail.com` | **Phone:** `+91 6381801640`  
**Registration Model:** **100% FREE — ZERO ENTRY FEE** (No fees collected from students at any point)  
**Target Event Dates:** January 22 – 24, 2027 (48 Continuous Hours)  
**Target Venue:** Sathyabama Indoor Stadium (Indoor Auditorium), Sathyabama Campus  
**Scale:** 2,000+ National Applicants $\rightarrow$ 250 Online Semi-Finalists $\rightarrow$ 100 Elite On-Campus Teams (Teams of 4–6 students, ~400–600 Hackers)  
**Cash Prize Pool:** **₹1,75,000 Pure Cash Escrow** + $50,000+ AWS Cloud Credits  
**Status:** `APPROVED PLAN` & `TEMPLATE`  

---

## National Intake Timeline & Architecture Overview

Kairos 2027 operates on a **Dual-Phase Meritocratic Intake Pipeline**:
1. **Form A (Round 0 — Nationwide Free Registration & Idea Abstract):** Open October 15 – December 15, 2026.
2. **Online Qualifier Announcement:** December 24, 2026 (**Top 250 Semi-Finalist Teams Selected**).
3. **Round 1 Submission (Online Technical Qualifier):** January 02 – 04, 2027 (GitHub repo + Loom 3-minute video demo + Live Google Meet defense).
4. **On-Campus Shortlist Reveal:** January 06, 2027 (**Top 100 Elite Teams Qualified**).
5. **Form B (On-Campus Confirmation, Roster Lock & Bus Logistics):** January 07 – 14, 2027 (100% Free; No pre-onboarding — Teams report directly to venue on Event Day).

```text
[Phase 0: Form A Free National Application (Oct 15 - Dec 15)] ──► 2,000+ Applicant Teams
                                                                           │
                                                                           ▼
[Announcement of Top 250 Online Semi-Finalists (Dec 24)] ─────────────────┤
                                                                           │
                                                                           ▼
[Round 1 Online Technical Qualifier Sprint (Jan 02 - 04)] ─────────────────┤
  • Working GitHub Repository Proof-of-Concept
  • 3-Minute Loom Video Architecture Walkthrough
  • Live 7-Minute Google Meet Defense with AWS Architects
                                                                           │
                                                                           ▼
[Announcement of Top 100 Elite On-Campus Finalists (Jan 06)] ──────────────┤
                                                                           │
                                                                           ▼
[Form B: On-Campus Finalist Confirmation (Roster Lock + Swag Sizes)] ──┤
                                                                           │
                                                                           ▼
[Laser-Etched Smart Check-In Pass] ───────────────► [Jan 22: Direct Venue Reporting & On-Ground Check-in]
```

---

# Form A: Round 0 National Registration & Project Abstract

**Form Header Banner:** *KAIROS 2027 | AWS Student Builder Group — SIST (22–24 January 2027)*  
**Form Title:** `KAIROS 2027 — National 48-Hour Hackathon: Round 0 Registration`  
**Description:**
> Welcome to **KAIROS 2027 (Grand Edition)**, the premier national 48-hour hackathon hosted by **AWS Student Builder Group (AWS SBG)** at Sathyabama Institute of Science and Technology, Chennai.  
> 
> 🏆 **Grand Prize Pool & Bounties:** **₹1,75,000 Pure Cash Escrow** (1st: ₹60k, 2nd: ₹35k, 3rd: ₹20k, 5 Tracks: ₹35k, Bounties: ₹25k) + $50,000+ AWS Cloud Credits & VC Incubation  
> 🗓️ **On-Ground Finale Dates:** January 22 – 24, 2027 (Sathyabama Indoor Stadium, Chennai)  
> 👥 **Team Size:** 4 to 6 Members (Cross-college and inter-disciplinary teams permitted)  
> ⚡ **Registration Fee:** **100% FREE — ZERO ENTRY FEE** (Completely sponsored)  
> 🎯 **Selection Funnel:** 2,000+ Applicant Teams $\rightarrow$ Top 250 Online Semi-Finalists (Round 1: Jan 02–04) $\rightarrow$ Top 100 Elite On-Campus Finalists  
> ⏳ **Round 0 Deadline:** December 15, 2026 (11:59 PM IST)  
> 
> *Top 100 finalists receive official university on-duty letters, $50-$100 AWS Cloud Credits, on-campus hostel accommodation, complimentary 8 meals/snacks, builder tees, and smart badges.*

---

### Section 1: Team Profile & Track Selection

| Field # | Field Label | Input Type | Validation / Options | Required |
| :--- | :--- | :--- | :--- | :--- |
| **1.1** | Team Name | Short Answer | Max 40 chars; Unique name across national pool | **Yes** |
| **1.2** | Team Size | Multiple Choice | `4 Members`, `5 Members`, `6 Members` | **Yes** |
| **1.3** | Primary Innovation Track | Multiple Choice | • **Track 1:** Agentic AI & Next-Gen Autonomous Systems (AWS Bedrock)<br/>• **Track 2:** Cloud-Native, Serverless & Distributed Systems<br/>• **Track 3:** Web3, Decentralized Identity & Zero-Trust Security<br/>• **Track 4:** FinTech, High-Frequency Systems & Algorithmic Trust<br/>• **Track 5:** Open Enterprise & Sustainable Engineering Solutions | **Yes** |
| **1.4** | Specific Sponsor Bounty Option | Checkboxes | `[ ] Best All-Women Engineering Team Bounty (₹10,000)`<br/>`[ ] Best Freshmen / First-Time Hackers Bounty (₹7,500)`<br/>`[ ] Most Scalable Cloud Architecture Bounty (₹7,500)`<br/>`[ ] None / Main Track Only` | **Yes** |
| **1.5** | Problem Statement Title | Short Answer | Max 150 characters | **Yes** |
| **1.6** | Team GitHub / GitLab Organization URL | Short Answer | Valid URL (Optional) | No |

---

### Section 2: Team Members & Academic Details

*(Repeated for Member 1 [Lead] through Member 4, 5, or 6)*

| Field # | Field Label | Input Type | Validation / Options | Required |
| :--- | :--- | :--- | :--- | :--- |
| **2.1** | Full Legal Name | Short Answer | As per College ID | **Yes** |
| **2.2** | Institutional Email Address | Short Answer | Valid `.edu` or `.ac.in` / personal email | **Yes** |
| **2.3** | Mobile Number (WhatsApp) | Short Answer | 10-digit Indian mobile number | **Yes** |
| **2.4** | College / University Name | Short Answer | Full official name of institution | **Yes** |
| **2.5** | Degree, Branch & Year | Dropdown | `B.E / B.Tech (1st / 2nd / 3rd / 4th Year)`, `M.E / M.Tech`, `MCA / BCA`, `Other` | **Yes** |
| **2.6** | Gender | Multiple Choice | `Male`, `Female`, `Non-Binary / Prefer not to say` | **Yes** |
| **2.7** | GitHub / Portfolio Profile | Short Answer | Valid URL | **Yes** |
| **2.8** | LinkedIn Profile | Short Answer | Valid URL | **Yes** |

---

# Form B: Finalist Confirmation, Swag Sizes & Bus Logistics (100% Free)

*(Circulated exclusively to the Top 100 Qualified Teams on January 06, 2027)*

### Key Fields:
1. **Attendance Confirmation:** Confirmation of physical arrival at the **Sathyabama Indoor Stadium, Chennai** on Friday, January 22, 2027 by 09:30 AM (Zero fee required).
2. **Builder Merchandise Sizing (100% Complimentary):**
   * Dry-Fit Builder T-Shirt: `[S, M, L, XL, XXL]` per member.
3. **University Bus Fleet Transit Selection (Free):**
   * Select inbound arrival hub (Friday, Jan 22, 06:30 – 09:00 AM): `Chennai Central Station`, `Tambaram Station`, `Chennai Airport`, `CMBT Koyambedu Bus Terminus`, `Direct / Own Transport`.
4. **Corporate Hiring Consent (Opt-In Data Privacy Notice):**
   * Checkbox:  
     `[ ] I affirmatively consent to having my resume, GitHub profile, and contact details included in the verified KAIROS 2027 Corporate Talent Book shared with official enterprise sponsors for internship and employment opportunities.`  
     *(Note: This consent is strictly optional. Choosing to opt out has zero impact on your judging, scoring, or prize eligibility).*
5. **Direct Venue Reporting Directive:**
   * Team confirmation that all 4–6 members will report directly to the Sathyabama Indoor Stadium on Event Day (Friday, Jan 22, 2027 by 09:30 AM). No pre-event on-campus onboarding is required.
