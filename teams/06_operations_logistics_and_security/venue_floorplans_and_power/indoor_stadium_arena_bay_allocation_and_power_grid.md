# KAIROS 2027 — Sathyabama Indoor Stadium Arena Bay Allocation & Electrical Grid Load Sheet

> **Floor Commander:** Nangaiyar M (Community & Events Lead, Reg: `44612059`)  
> **Network & Power Architect:** Viswanathan Ashok (Reg: `44110907`)  
> **Venue Reference:** Sathyabama Indoor Stadium (Indoor Auditorium) — Modeled on Vexora'26 ACM Hackathon  

---

## 1. Arena Floor Seating & Bay Manifest (100 Teams / 450–600 Hackers)

| Zone / Arena Sector | Assigned Track | Team Capacity | Table & Seating Setup | Power Strips | Wi-Fi 6 Access Point |
|---|---|:---:|---|:---:|---|
| **Sector Alpha (Stage Left)** | Track 1: Agentic AI | Teams 01 – 20 (80–120 hackers) | 16 Round Banquet Tables (4–6 per table) | 20 × 6-socket Spike Boards | `KAIROS-STAD-AP1` & `AP2` |
| **Sector Bravo (Stage Center)** | Track 2: Cloud-Native Systems | Teams 21 – 40 (80–120 hackers) | 16 Round Banquet Tables (4–6 per table) | 20 × 6-socket Spike Boards | `KAIROS-STAD-AP3` & `AP4` |
| **Sector Charlie (Stage Right)** | Track 3: Next-Gen Web3 & Security | Teams 41 – 60 (80–120 hackers) | 16 Round Banquet Tables (4–6 per table) | 20 × 6-socket Spike Boards | `KAIROS-STAD-AP5` & `AP6` |
| **Sector Delta (Midcourt Left)** | Track 4: FinTech, Trust & Crypto | Teams 61 – 80 (80–120 hackers) | 16 Round Banquet Tables (4–6 per table) | 20 × 6-socket Spike Boards | `KAIROS-STAD-AP7` & `AP8` |
| **Sector Echo (Midcourt Right)** | Track 5: Open Enterprise & Campus | Teams 81 – 100 (80–120 hackers) | 16 Round Banquet Tables (4–6 per table) | 20 × 6-socket Spike Boards | `KAIROS-STAD-AP9` & `AP10` |
| **Sector Foxtrot (Center Arena)** | Central Apex War Room & NOC | 25 Core Organizers & AWS Architects | 4 Rectangular Modular Workstations | Central Lab Spike Drops | `KAIROS-ADMIN-5G` |
| **Backstage Green Room 1** | Female Rest & Sanctuary | Rotating Lady Participants | Cushioned Lounge Sofas & Rest Beds | Internal Room Outlets | `KAIROS-GUEST-SECURE` |
| **Backstage Green Room 2** | VIP Jury & Dignitary Lounge | 25 VIP Evaluators & VCs | Conference & Boardroom Dining Setup | Executive Floor Outlets | `KAIROS-VIP-JURY` |
| **Upper Bleachers Mezzanine** | Quiet Nap Pods | 40 Rotating Rest Mat Beds | Silent Zone (No Electronics) | Lighting Only | — |
| **Outer Portico & Foyer** | Check-in, 24/7 Fuel Bar & EV Buggy | Organizers & Logistics Desk | 4 Reception Tables + Water Stations | 4 × 4-socket Strips | `KAIROS-FOYER` |

---

## 2. Arena Floor Power Grid Load Calculation (65 kVA Capacity)

```text
ARENA ESTIMATED MAXIMUM ELECTRICAL POWER DEMAND:
────────────────────────────────────────────────────────────────────────
1. Participant Laptops (600 units × 65W avg):           39,000 Watts
2. Mobile Device Fast Chargers (600 units × 18W avg):   10,800 Watts
3. Stage Concert Line-Array PA & Delay Fill Tops:        6,500 Watts
4. Stage P2.5 LED Video Wall (12ft × 8ft canvas):        4,200 Watts
5. Broadcast Video Rig, OBS Live Workstations & Monitors: 3,000 Watts
6. 24/7 Filter Coffee / Tea Brewers & Water Coolers:     4,500 Watts
7. Central Network NOC Switches, Routers & Wi-Fi APs:    1,200 Watts
────────────────────────────────────────────────────────────────────────
TOTAL ESTIMATED ARENA PEAK LOAD:                         ~69.2 kW (~77 kVA)
TYPICAL CONTINUOUS WORKING LOAD (75% concurrency):       ~52.0 kW (~58 kVA)
STADIUM DEDICATED TRANSFORMER FEED:                      125 kVA Main Feeder
CAMPUS BACKUP DIESEL GENERATORS:                         Dual 125 kVA Auto-Synchronized
SWITCH-OVER LATENCY:                                     < 10 Milliseconds (Online Industrial UPS)
SAFETY & PROTECTION PROTOCOL:                            20 Dual-Channel Heavy Rubber Cable Ramps
                                                         + Residue-Free Venue Mat Taping
────────────────────────────────────────────────────────────────────────
```
