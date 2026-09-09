# Smart ID Badges & Lanyards Engineering Specification

> **Subfolder:** `teams/02_design_and_creative_assets/badges_and_lanyards/`  
> **Direct Lead:** **Rikish B** (Design Lead, Reg: `44110664`, Phone: `+91 9597430250`)  
> **Systems Integration:** **Viswanathan Ashok** (Hands-On Builder Lead, Reg: `44110907`, Phone: `+91 9080809088`)  
> **Operations Lead:** **Nangaiyar M** (Logistics Lead, Reg: `44612059`)  

---

## 1. Scope & Mandate

This folder defines the physical production specifications, graphic templates, NFC chip encoding, and print orders for **650 units of high-grade Smart ID Badges and custom woven satin lanyards** for KAIROS 2027.

---

## 2. Physical & Electronic Specifications

```text
SMART BADGE HARDWARE ARCHITECTURE:
────────────────────────────────────────────────────────────────────────
Form Factor: Standard CR80 Credit Card Size
Exact Dimensions: 85.60 mm (Width) × 53.98 mm (Height) | 3.370 in × 2.125 in
Corner Radius: 3.18 mm (0.125 in) Rounded Corners
Thickness: 0.82 mm (Heavy PVC Cardstock with Matte Velvet Anti-Scratch Lamination)
Slot Hole: Oblong Euro-slot punched centered at top (14 mm × 3 mm, 4 mm from top edge)
Embedded NFC Chip: NTAG213 / NTAG215 High-Frequency (13.56 MHz, ISO/IEC 14443 Type A)
Barcoding: 2D Dynamic QR Code (links to participant verification profile on website)
────────────────────────────────────────────────────────────────────────
CUSTOM WOVEN LANYARD SPEC SHEET:
────────────────────────────────────────────────────────────────────────
Ribbon Length: 900 mm total loop (450 mm drop length)
Ribbon Width: 20 mm (0.787 in)
Material: High-Density Double-Layer Jacquard Satin Weave
Colorway: Obsidian Abyss (`#0D1117`) base with AWS Smile Amber (`#FF9900`) woven lettering
Text Woven: "AWS STUDENT BUILDER GROUP • KAIROS 2027 • BUILD ON AWS"
Hardware Attachment: Heavy-Duty Metal Lobster Claw Swivel Hook in Matte Gunmetal Black
Safety Feature: Quick-Release Breakaway Safety Buckle at nape of neck
────────────────────────────────────────────────────────────────────────
```

---

## 3. Five-Tier Role Colorway Taxonomy

To ensure instant visual identification by campus security and event coordinators, badges are color-coded by role:

| Tier Code | Role Category | Badge Border & Accent Color | Substrate / Accent Details | Qty Ordered |
|:---:|---|:---:|---|:---:|
| **BDG-01** | **Participant / Hacker** | Cyber Slate (`#1A2433`) & Amber | White card face, Dark Obsidian banner, Team Name & ID | 450 |
| **BDG-02** | **Technical Mentor** | Terminal Green (`#3FB950`) | Green accent band, "MENTOR" badge, expertise tags | 40 |
| **BDG-03** | **Grand Finale Jury** | Royal Gold (`#FFD700`) | Metallic gold foil stamp, "VIP JURY", CXO Lounge access | 25 |
| **BDG-04** | **Corporate Sponsor** | Pure Platinum (`#E5E4E2`) | Sponsor company logo, "INDUSTRY PARTNER" | 35 |
| **BDG-05** | **Core Organizer / Lead** | AWS Smile Amber (`#FF9900`) | Obsidian Black face, Amber gradient, "ORGANIZER / ICS" | 100 |

---

## 4. Digital Encoding & Webhook NFC Integration

- **NFC Tag Content:** Each card is pre-flashed with a unique cryptographic URL:
  `https://kairos.sistawscc.org/checkin?uid=[NFC_CARD_UUID]&auth=[HMAC_HASH]`
- **Scan Functionality:**
  1. *Check-In Desk:* Tap to confirm arrival, assign hacker bay, and issue developer kit.
  2. *Mess Hall:* Tap at breakfast/lunch/dinner/midnight food counters to prevent double-serving and manage food count.
  3. *Judging Milestone:* Tap by judges to bring up team evaluation rubric on judge tablets.
- **Builder System Owner:** Viswanathan Ashok (Website & Backend Team).

---

## 5. Pre-Print Quality Checklist
- [ ] Bleed margin of 2.5 mm maintained on all 4 sides of the card canvas.
- [ ] Oblong lanyard punch hole area (14mm × 3mm) is free of critical text or QR codes.
- [ ] QR code minimum size is strictly 18 mm × 18 mm at 300 DPI for reliable camera scanning.
- [ ] Pre-printed test run of 5 cards verified with NFC reader app (NFC Tools) on Android & iOS.
