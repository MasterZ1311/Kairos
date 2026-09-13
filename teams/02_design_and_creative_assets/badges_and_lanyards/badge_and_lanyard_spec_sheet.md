# KAIROS 2027 — Smart Badge Print Layout & Lanyard PO Specification

> **Lead:** Rikish B (Design Lead, Reg: `44110664`)  
> **Systems Engineer:** Viswanathan Ashok (Reg: `44110907`)  

---

## 1. Graphic Canvas Dimensional Layout (Illustrator / Figma)

```text
CR80 BADGE PRINT CANVAS (FRONT & BACK):
────────────────────────────────────────────────────────────────────────
Trim Size: 85.60 mm × 53.98 mm (1011 px × 638 px at 300 DPI)
Bleed Size: 90.60 mm × 58.98 mm (1070 px × 697 px at 300 DPI)
Safe Zone: 80.60 mm × 48.98 mm (952 px × 578 px)
Slot Punch Keepout: Top Center 20.0 mm × 10.0 mm (Keep blank)
────────────────────────────────────────────────────────────────────────
```

### Front Card Architecture:
- **Top Bar (85.6 mm × 14.0 mm):**
  - Top Left: Sathyabama Logo (Vector Mono White)
  - Top Right: AWS Student Builder Groups Logo
- **Center Body (85.6 mm × 25.0 mm):**
  - Participant First & Last Name (Space Grotesk Bold, 16pt, `#FFFFFF`)
  - Team Name & Assigned Hacker Bay (Plus Jakarta Sans SemiBold, 11pt, `#A855F7` Electric Violet)
  - Track Category & College Name (Inter Regular, 9pt, `#E9D5FF`)
- **Bottom Bar (85.6 mm × 15.0 mm):**
  - Left: Dynamic Verification QR Code (18 mm × 18 mm)
  - Center: Role Badge Pill (`HACKER` / `EVALUATOR` / `VIP JURY` / `ORGANIZER` with `#A855F7` border)
  - Right: Title Sponsor Emblem (Vector)

### Back Card Architecture:
- Laser-engraved **Official Kairos Circular Seal** ([`kairos_official_circular_sticker_seal.jpg`](file:///e:/AWS%20SBGL/Events/Kairos/teams/02_design_and_creative_assets/brand_identity_and_logos/kairos_official_circular_sticker_seal.jpg)).
- Emergency Organizers Hotlines (Thenappan T, Campus Security, General Hospital).
- Wi-Fi Access Credentials & QR code for Helpdesk Discord.
- Important Rules: 10 PM Night Lock-In, Segregated Dining Halls, Free Buffet Hours.
- NFC Tap-Here Icon with contactless wave symbol (NTAG213 chip position).

---

## 2. Procurement Order Details (PO-BDG-01)

- **Total Badges Ordered:** 650 Cards (450 Hackers, 40 Evaluators, 25 Judges, 35 Sponsors, 100 Organizers).
- **Total Lanyards Ordered:** 650 Custom Woven Satin Lanyards.
- **Estimated Unit Cost:** ₹25 / Badge + Lanyard set = ₹16,250 Total.
- **Delivery Target:** January 15, 2027 (to allow pre-encoding of NFC chips by Viswanathan's squad).
