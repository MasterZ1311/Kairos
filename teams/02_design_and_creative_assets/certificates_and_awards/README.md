# Certificates & Awards Engineering Specification

> **Subfolder:** `teams/02_design_and_creative_assets/certificates_and_awards/`  
> **Direct Lead:** **Rikish B** (Design Lead, Reg: `44110664`, Phone: `+91 9597430250`)  
> **Documentation Lead:** **Hemavarshine S** (Reg: `44110263`, Phone: `+91 9345691593`)  
> **Executive Signatory:** **Dr. T. Sasipraba** (Vice Chancellor) & **Thenappan T** (President & SBGL)  

---

## 1. Scope & Mandate

This folder provides graphic templates, manufacturing blueprints, security QR validation mechanisms, and procurement specifications for all physical and digital awards, diplomas, and custom trophies presented at KAIROS 2027.

---

## 2. Physical & Material Specifications

### 1. Physical Parchment Certificates (A4 Landscape)
```text
CERTIFICATE MANUFACTURING SPEC SHEET:
────────────────────────────────────────────────────────────────────────
Dimensions: A4 Landscape | 297 mm (Width) × 210 mm (Height) | 11.69 in × 8.27 in
Resolution: 300 DPI (3508 × 2480 pixels)
Substrate: 350 GSM Premium Natural Textured Ivory Cardstock
Special Embellishments:
  - Outer Geometric Guilloche Border in Dual Metallic Gold Foil Hot-Stamping
  - Raised Embossed Institutional Seal of Sathyabama (Bottom Center)
  - Anti-Counterfeit Dynamic Verification QR Code (Bottom Right, 20 mm × 20 mm)
Signature Fields:
  1. President & SBGL (Thenappan T)
  2. Faculty Coordinators (Dr. Balapriya .S & Dr. K. Ashok Kumar)
  3. Dean, School of Computing (Dr. L. Lakshmanan)
  4. Vice Chancellor, SIST (Dr. T. Sasipraba)
Folder / Enclosure: Matte Black Textured Cardstock Presentation Folder with Gold Debossed Logo
────────────────────────────────────────────────────────────────────────
```

### 2. Physical Winner Trophies (Grand Champions & Track Category Winners)
```text
TROPHY MANUFACTURING SPEC SHEET:
────────────────────────────────────────────────────────────────────────
Quantity: 11 Trophies Total
  - 1 × Grand Champion (1st Place Overall) — 14-inch Master Trophy
  - 1 × 1st Runner-Up (2nd Place Overall) — 12-inch Trophy
  - 1 × 2nd Runner-Up (3rd Place Overall) — 10-inch Trophy
  - 5 × Track Category Winners (AI, Cloud, Web3, FinTech, Health) — 9-inch Trophies
  - 3 × Special Bounties (Women in Tech, Rookie, Scalable AWS) — 9-inch Trophies
Material: High-Grade Optical Acrylic Base & Column with Laser-Cut Brushed Brass Inlay
Base: Heavy Black Granite / Obsidian Crystal Base (Weighted, 100 mm × 100 mm × 40 mm)
Engraving: Precision Fiber Laser Engraving with Gold Infill
Engraved Content:
  - Sathyabama Crest & AWS Student Builder Group Monogram
  - "KAIROS 2027 (GRAND EDITION) — [AWARD TITLE]"
  - "Team: [Winning Team Name] · Sathyabama Campus · Jan 22–24, 2027"
────────────────────────────────────────────────────────────────────────
```

### 3. Digital Verifiable Credentials (Credly / OpenBadges Compatible)
- Automated vector SVG/PDF credentials generated via AWS Lambda microservice.
- Permanent cryptographic hash stored on chapter verification server:
  `https://kairos.sistawscc.org/verify?cert=[CERT_UUID]`
- Direct 1-click LinkedIn Add-to-Profile integration.

---

## 3. Who Fills What (Accountability)

| Component | Responsible Lead | Deadline | Status |
|---|---|:---:|:---:|
| **Certificate Visual Layout** | Rikish B (Design) | Dec 15, 2026 | Drafted |
| **Participant Database Merge & Names** | Hemavarshine S (Documentation) | Jan 23, 2027 (22:00) | Live Queue |
| **Trophy CAD Drafting & Vendor PO** | Rikish B & Nangaiyar M | Dec 20, 2026 | Queued |
| **Institutional Signatures & Seal** | Dr. Balapriya .S & Thenappan T | Jan 24, 2027 (14:00) | Stage Protocol |
| **Digital Certificate Cloud Distribution** | Viswanathan Ashok (Builder Lead) | Jan 26, 2027 | Automated SES |
