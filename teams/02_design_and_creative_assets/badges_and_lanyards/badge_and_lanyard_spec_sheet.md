# KAIROS — Participant Identity & Smart Badge Specification

> **Lead:** **Rikish B** (Design Lead, Reg: `44110664`)  
> **Systems Engineer:** **Viswanathan Ashok** (Hands-On Builder Lead, Reg: `44110907`)  
> **Master Slogan:** **`KAIROS: MAKE TIME. MAKE SOMETHING.`**  
> **Badge Tagline:** **`48 HOURS. ONE CHANCE.`**  

---

## 1. Graphic Canvas Dimensional Layout (CR80 Standard)

```text
CR80 BADGE PRINT CANVAS (FRONT & BACK):
────────────────────────────────────────────────────────────────────────
Trim Size: 85.60 mm × 53.98 mm (1011 px × 638 px at 300 DPI)
Bleed Size: 90.60 mm × 58.98 mm (1070 px × 697 px at 300 DPI)
Safe Zone: 80.60 mm × 48.98 mm (952 px × 578 px)
Slot Punch Keepout: Top Center 14.0 mm × 3.0 mm (4 mm from top edge)
Corner Radius: 3.18 mm (0.125 in)
Substrate: Matte Velvet Anodized PVC / Aluminium Composite (0.82 mm thickness)
────────────────────────────────────────────────────────────────────────
```

---

## 2. Participant Card Architecture

### Front Face Architecture (The Builder Identity)
```text
┌────────────────────────────────────────────────────────────────────────┐
│ [SIST Crest]                      KAIROS            [AWS SBG Monogram] │
│                           48 HOURS. ONE CHANCE.                        │
│                                                                        │
│                              ╭───────────╮                             │
│                              │  HOURGLASS│  (Visual Centerpiece)       │
│                              │   ICON    │                             │
│                              ╰───────────╯                             │
│                                                                        │
│                            [PARTICIPANT NAME]                          │
│                                                                        │
│                      Team: [TEAM NAME] · Bay: [BAY_ID]                 │
│                          [COLLEGE / UNIVERSITY]                        │
│                                                                        │
│ [ Dynamic QR Code ]              [ROLE PILL]            [Title Sponsor]│
└────────────────────────────────────────────────────────────────────────┘
```

* **Header:**
  * Top Center: **`K A I R O S`** in bold uppercase (`Space Grotesk Bold`, 16pt, `#FFFFFF`).
  * Sub-Header: **`48 HOURS. ONE CHANCE.`** (`Space Grotesk SemiBold`, 8.5pt, tracked uppercase, Electric Violet `#A855F7`).
* **Visual Centerpiece:**
  * Centered standalone **Celestial Hourglass Emblem** (`kairos_hourglass_emblem.png`) (Height: 22 mm) framed by a subtle glowing violet aura.
* **Participant Metadata:**
  * **Participant Full Name:** `Space Grotesk Bold`, 14pt, Astral White (`#FFFFFF`).
  * **Team Name & Bay:** `Plus Jakarta Sans SemiBold`, 10pt, Cyber Orchid (`#C084FC`).
  * **College / Institution:** `Inter Regular`, 8.5pt, Starlight Lavender (`#E9D5FF`).
* **Bottom Controls:**
  * Left: Dynamic Check-In QR Code (16 mm × 16 mm).
  * Center: Role Status Pill (`HACKER` / `EVALUATOR` / `JURY` / `ORGANIZER` with `#A855F7` border).
  * Right: Title Corporate Sponsor vector crest.

---

### Back Face Architecture (System Telemetry & Connectivity)
```text
┌────────────────────────────────────────────────────────────────────────┐
│                                                                        │
│                         SCAN FOR LIVE PORTAL                           │
│                     ┌───────────────────────────┐                      │
│                     │                           │                      │
│                     │     LARGE DYNAMIC QR      │                      │
│                     │  kairos.sathyabama.ac.in  │                      │
│                     │                           │                      │
│                     └───────────────────────────┘                      │
│                                                                        │
│                         ((( Contactless NFC )))                        │
│                                                                        │
│ Campus Wi-Fi: SATHYABAMA-KAIROS | WPA2: [PRE-CONFIGURED]               │
│ Emergency / Helpdesk: +91 6381801640 · Discord: #helpdesk              │
│ AWS Student Builder Group · Sathyabama Institute of Science & Tech     │
└────────────────────────────────────────────────────────────────────────┘
```

* **Core QR Function:** High-contrast 25 mm × 25 mm Dynamic QR code linking straight to the live event portal / team submission dossier (`https://kairos.sathyabama.ac.in/team/[TEAM_ID]`).
* **Contactless NFC:** NTAG213 chip position marked with universal contactless wave icon. Tapping the badge opens the live participant dashboard, logs meal check-ins, and loads rubric on judge tablets.
* **Support Info:** Emergency contacts, campus Wi-Fi access credentials, and institutional attribution.

---

## 3. Official Lanyard Engineering Specification

```text
CUSTOM JACQUARD SATIN WOVEN LANYARD:
────────────────────────────────────────────────────────────────────────
Base Ribbon Color: Deep Void Black (`#000000`)
Ribbon Width: 20 mm (0.787 in) | Loop Length: 900 mm (450 mm drop)
Weave Pattern: Double-layer high-density jacquard satin weave

REPEATING PATTERN:
KAIROS  •  [ ⏳ ]  •  KAIROS  •  [ ⏳ ]  •  KAIROS  •  [ ⏳ ]  •  KAIROS

Typography Color: Crisp Astral White (`#FFFFFF`) in tracked Space Grotesk Bold
Hourglass Symbol: Tiny woven Electric Violet (`#A855F7`) hourglass icon (6 mm height)
Hardware Clip: Matte gunmetal black swivel lobster claw hook
Safety Feature: Quick-release ergonomic breakaway clasp at the nape of the neck
────────────────────────────────────────────────────────────────────────
```

---

## 4. Procurement & Batch Allocation

* **Total Badges Ordered:** 650 Cards (450 Hackers, 40 Evaluators, 25 Judges, 35 Sponsors, 100 Organizers).
* **Total Lanyards Ordered:** 650 Woven Lanyards.
* **Pre-Encoding Target:** January 15, 2027 (NFC flashing by Hands-On Builder squad).
