# Venue Floorplans, Hack Bays & Electrical Power Grid Specification

> **Subfolder:** `teams/06_operations_logistics_and_security/venue_floorplans_and_power/`  
> **Direct Lead:** **Nangaiyar M** (Community & Events Lead, Reg: `44612059`, Phone: `+91 8754976892`)  
> **Electrical Engineer:** **Campus Maintenance Engineer**  
> **IT Systems Lead:** **Viswanathan Ashok** (Hands-On Builder Lead, Reg: `44110907`)  
> **Sign-Off Authority:** **Thenappan T** (President & SBGL, Reg: `44110855`)  

---

## 1. Scope & Mandate

This folder directs the spatial architecture, table bay configurations, high-density electrical distribution, and network infrastructure across all levels of the **Central Library Complex** for KAIROS 2027.

---

## 2. Central Library Complex Multi-Level Floor Allocation

```text
CENTRAL LIBRARY SPATIAL MAPPING:
────────────────────────────────────────────────────────────────────────
• GROUND FLOOR:
  - Grand Auditorium (500-Seat Capacity): Inaugural Ceremony, Keynotes, Stage LED Wall, Valedictory.
  - Portico & Foyer: Registration Desks, Smart NFC Tap Stations, 12x8ft Welcome Banner, Corporate Booths.
  - Hacker Lounge & Resting Pods: Quiet rest zone with floor mattresses for tired builders.

• 1ST FLOOR:
  - Computing Lab (120 Linux Workstations): Track 4 (FinTech) & Track 5 (Healthcare) Hack Bays.
  - Network Server Room: Core fiber patch panel and Wi-Fi controller.

• 2ND FLOOR:
  - Lecture Hall 1 (LH-1): Track 1 Hack Bays (Teams 01–25: Agentic AI & Bedrock).
  - Lecture Hall 2 (LH-2): Track 2 Hack Bays (Teams 26–50: Cloud-Native Systems).
  - Lecture Hall 3 (LH-3): Track 3 Hack Bays (Teams 51–75: Web3 & Decentralized).
  - Central Corridor: Continuous 24/7 Water & Coffee Dispensation Bar.

• TOP FLOOR:
  - VIP Executive Lounge: Corporate Sponsor Suites, CXO Dining, Private Jury Deliberation Room.
────────────────────────────────────────────────────────────────────────
```

---

## 3. Power Grid & Electrical Architecture

- **Total Connected Load:** Capped at **45 kVA** with balanced three-phase 415V distribution.
- **Generator Redundancy:** Dedicated 125 kVA institutional diesel generator on warm standby with an Automatic Transfer Switch (ATS) providing **< 10 millisecond failover** to prevent laptop rebooting.
- **Bay Power Infrastructure:**
  - **40 Units of Heavy-Duty 6A/16A Spike-Protected Extension Strips** (Belkin / Havells commercial grade).
  - Each 4-person team receives a dedicated 4-socket surge-protected power strip.
  - Maximum 3 power strips daisy-chained per main 16A wall circuit breaker to eliminate tripping risk.

---

## 4. Who Fills What (Accountability)

| Task | Lead | Verification Method | Target Date |
|---|---|---|:---:|
| **Physical Room Layout CAD / Blueprint** | Nangaiyar M | Measured tape diagram | Dec 15, 2026 |
| **Circuit Breaker Load Calculation** | Campus Electrician | Clamp meter amp test | Jan 10, 2027 |
| **Power Strip & Spike Guard Deployment** | Logistics Squad | Tagged & labeled per bay | Jan 21, 2027 (14:00) |
| **Wi-Fi Access Point Stress Test (500 devices)** | Viswanathan Ashok | Simulated ping & iperf3 test | Jan 21, 2027 (16:00) |
| **Venue Handover & Cleanliness Audit** | Nangaiyar M | Physical room sign-off | Jan 25, 2027 (12:00) |
