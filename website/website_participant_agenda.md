# KAIROS 2027 — Official Participant Agenda (Website & Public View)

> **Location:** Sathyabama Institute of Science and Technology, Chennai  
> **Dates:** Friday, January 22 – Sunday, January 24, 2027  
> **Entry & Participation:** 100% FREE (Fully Sponsored Meals, Swag, Stay & Cloud Credits)  
> **Format:** 48-Hour Continuous High-Velocity Cloud & AI Hackathon  

---

## Interactive 48-Hour Schedule

```text
┌──────────────────────────────────────────────────────────────────────────────┐
│  [DAY 1: KICKOFF & GENESIS]   [DAY 2: CODE VELOCITY]   [DAY 3: GRAND FINALE] │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

### 🚀 Day 1: Friday, January 22, 2027 — Genesis, Architecture & The Starting Bell

| Time | Event / Milestone | Experience Details | Status / Tag |
|---|---|---|:---:|
| **09:30 AM – 10:45 AM** | **Grand Red-Carpet Check-In & Builder Kit Distribution** | • Report to Campus Foyer at Sathyabama Institute of Science and Technology, Chennai.<br/>• Quick Government/College Photo ID verification.<br/>• Receive your 100% Free Developer Kit (T-Shirt, Smart NFC Badge, Stickers).<br/>• Hack bay allocation & high-speed Wi-Fi onboarding. | `CHECK-IN` |
| **10:45 AM – 12:00 PM** | **Grand Inauguration & Keynote Plenary** | • Welcome & institutional address by University Leadership.<br/>• **20-Minute Keynote Address by Title Sponsor Executive (AWS)** (11:15 AM).<br/>• **10-Minute Technical Briefing by Co-Powered Partner** (11:35 AM).<br/>• Official release of the 5 Grand Enterprise Innovation Tracks & Rules. | `CEREMONY` |
| **12:00 PM – 12:15 PM** | **Team Relocation to Hacking Bays** | • Move to designated team bay with spike-protected power drops.<br/>• Connect workstations, peripheral devices, and test cloud environments. | `SETUP` |
| **12:15 PM** | **🚀 CLOCK STARTS: 48-HOUR SPRINT COMMENCES** | • Official GitHub repository initialization with Kairos webhook listener.<br/>• The 48-hour continuous countdown begins! | `HACK LIVE` |
| **01:00 PM – 02:30 PM** | **Complimentary Builder Lunch Buffet** | • Wholesome hot lunch served at campus dining halls.<br/>• 24/7 Filter Coffee & Tea bar opens. | `MEALS` |
| **04:00 PM – 06:30 PM** | **🔍 CHECKPOINT 1: Architecture & Cloud Feasibility Gate** | • Table-side review with Senior AWS Solutions Architects & Industry Evaluators.<br/>• Architecture blueprint, cloud service selection, and IAM security check (25 Pts). | `EVALUATION` |
| **08:30 PM – 10:00 PM** | **Complimentary Builder Dinner Buffet** | • Energizing hot dinner served via segregated dining corridors. | `MEALS` |
| **10:00 PM** | **🔒 Campus Night Lock-In Activated** | • Campus perimeter doors secured for total builder safety.<br/>• 24/7 Campus EV shuttles operating continuous loops across rest facilities. | `SECURITY` |

---

### ⚡ Day 2: Saturday, January 23, 2027 — Deep Sprint, Velocity & Cloud Mastery

| Time | Event / Milestone | Experience Details | Status / Tag |
|---|---|---|:---:|
| **07:30 AM – 09:00 AM** | **Breakfast & Refreshments** | • Energizing hot breakfast and continuous filter coffee to start Day 2. | `MEALS` |
| **09:30 AM – 11:30 AM** | **AWS Cloud Architecture Walkabout** | • AWS Solutions Architects walk through hacking bays offering optional tips on model latency, database caching, and cloud deployment efficiency. | `TECH CLINIC` |
| **01:00 PM – 02:30 PM** | **Executive Lunch Buffet** | • High-protein lunch buffet served to keep builders fueled. | `MEALS` |
| **02:00 PM – 05:30 PM** | **⚡ CHECKPOINT 2: Code Velocity, API Integration & Authenticity Gate** | • Table-side review by Startup CTOs & Staff Engineers.<br/>• Live testing of running frontend/backend endpoints, database schemas, and external APIs.<br/>• Automated commit history verification (35 Pts). | `EVALUATION` |
| **08:30 PM – 10:00 PM** | **Dinner Buffet & Refreshments** | • Nourishing hot dinner buffet. | `MEALS` |
| **10:00 PM** | **🔒 Night Lock-In Enforced** | • Night access protocols in place; rest zones available. | `SECURITY` |
| **01:30 AM** | **Night Fuel Booster** | • Midnight hot coffee/tea and energy snack drops across all hacking halls. | `ENERGY DROP` |
| **02:30 AM – 06:30 AM** | **The Final Sprint ("Kairos Hours")** | • Polish UI/UX, containerize builds, run end-to-end integration tests, and finalize pitch decks. | `SPRINT` |

---

### 🏆 Day 3: Sunday, January 24, 2027 — Demos, Valedictory & Celebrations

| Time | Event / Milestone | Experience Details | Status / Tag |
|---|---|---|:---:|
| **07:30 AM – 08:30 AM** | **Breakfast & Refreshments** | • Quick-service hot breakfast and coffee before the final submission. | `MEALS` |
| **08:30 AM** | **🛑 HARD CODE FREEZE & GITHUB SUBMISSION LOCK** | • Automated GitHub commit freeze via Kairos webhook listener.<br/>• Final submission of working demo video link and pitch deck. Zero extensions. | `DEADLINE` |
| **09:00 AM – 12:30 PM** | **🏆 CHECKPOINT 3: Grand Finale Live Demonstrations** | • Concurrent stage & bay jury evaluations.<br/>• 7-minute live presentation: 4 minutes working demo + 3 minutes grilling by VC Partners, CTOs, and AWS Leaders (40 Pts).<br/>• Real-time algorithmic Z-score normalization. | `EVALUATION` |
| **12:30 PM – 01:30 PM** | **Grand Celebration Luncheon** | • Festive celebration lunch buffet for all builders, organizers, and jury members. | `MEALS` |
| **01:30 PM – 02:15 PM** | **Grand Jury Deliberation & Final Shortlisting** | • Evaluator committee convenes to finalize winners and track bounties. | `DELIBERATION` |
| **02:30 PM – 04:30 PM** | **🎆 Grand Valedictory, Award Ceremony & Finale** | • Addresses by Keynote VIPs and University Leadership.<br/>• Presentation of Track Bounties & Special Innovation Awards.<br/>• **Grand Winner Announcement: 2nd Runner Up, 1st Runner Up, and Grand Champion (National Trophy & Awards Conferral)**. | `CEREMONY` |
| **05:00 PM** | **Formal Campus Dispersal via Sathyabama Bus Fleet** | • Complimentary return transit buses depart campus for Chennai Central, Tambaram, Airport, and CMBT Koyambedu. | `DEPARTURE` |

---

## Frontend Component Specification (`TimelineStepper`)

```typescript
// React Component Props for /schedule Route & Landing Page TimelineStepper
export interface AgendaItem {
  id: string;
  day: 1 | 2 | 3;
  timeRange: string;
  title: string;
  description: string;
  category: 'CHECK-IN' | 'CEREMONY' | 'SETUP' | 'HACK LIVE' | 'MEALS' | 'EVALUATION' | 'SECURITY' | 'TECH CLINIC' | 'ENERGY DROP' | 'SPRINT' | 'DEADLINE' | 'DELIBERATION' | 'DEPARTURE';
  isMandatory: boolean;
  isMilestone: boolean;
}
```
