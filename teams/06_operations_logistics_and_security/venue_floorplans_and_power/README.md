# Venue Floorplans, Hack Bays & Electrical Power Grid Specification

> **Subfolder:** `teams/06_operations_logistics_and_security/venue_floorplans_and_power/`  
> **Direct Lead:** **Nangaiyar M** (Community & Events Lead, Reg: `44612059`, Phone: `+91 8754976892`)  
> **Electrical Engineer:** **Campus Maintenance Engineer**  
> **IT Systems Lead:** **Viswanathan Ashok** (Hands-On Builder Lead, Reg: `44110907`)  
> **Sign-Off Authority:** **Thenappan T** (President & SBGL, Reg: `44110855`)  

---

## 1. Scope & Mandate

This folder directs the spatial architecture, table bay configurations, high-density electrical distribution, and network infrastructure for KAIROS 2027. Following institutional approval, the primary venue is the **Sathyabama Indoor Stadium (Indoor Auditorium)** (modeled on empirical benchmarks from Vexora'26 ACM Hackathon).

* **Primary Active Spec:** [`indoor_stadium_arena_bay_allocation_and_power_grid.md`](./indoor_stadium_arena_bay_allocation_and_power_grid.md)
* **Master Transition & Budget Plan (Executive Reference):** `DOC-20 (Indoor Auditorium Transition & Budget Plan)`
* **Archival Baseline:** [`central_library_bay_allocation_and_power_grid.md`](./central_library_bay_allocation_and_power_grid.md)

---

## 2. Sathyabama Indoor Stadium Spatial Mapping

```text
INDOOR STADIUM ARENA SPATIAL MAPPING:
────────────────────────────────────────────────────────────────────────
• MAIN ARENA FLOOR:
  - 100 Hacking Bays (75–80 Round Banquet Tables with Fitted Navy Linens)
  - 550+ Institutional Plastic Chairs
  - 3 Main 32A 3-Phase Power Distribution Trunk Lines encased in 20 Heavy Rubber Cable Ramps
  - Central Apex War Room, Network NOC, and Live Broadcast Deck

• ELEVATED STAGE COMPLEX:
  - 50ft × 10ft Mega Stage Backdrop Banner
  - 12ft × 8ft P2.5 High-Resolution LED Video Wall
  - Line-Array Acoustic PA System + UHF Cordless Mics

• BACKSTAGE GREEN ROOMS:
  - Green Room 1: Female Rest Sanctuary (AC, Attached Restroom, Lady Guard Escort)
  - Green Room 2: VIP Industry Jury Lounge & Boardroom Dining

• UPPER BLEACHERS / MEZZANINE:
  - Partitioned Quiet Nap Pods (40 Padded Mats, 100% Silent Zone)

• PORTICO & FOYER:
  - Registration & Smart NFC Badge Scanning Desks
  - 24/7 Filter Coffee / Tea Fuel Bar & Mineral Water Station
  - Campus EV Buggy & University Bus Terminal
────────────────────────────────────────────────────────────────────────
```

---

## 3. Power Grid & Electrical Architecture

- **Total Connected Load:** Designed for **55–65 kVA** continuous demand (~69.2 kW peak) with balanced three-phase 415V distribution.
- **Generator Redundancy:** Dedicated 125 kVA institutional feeder with dual 125 kVA campus diesel generators on auto-synchronization and Automatic Transfer Switch (ATS) providing **< 10 millisecond failover** to prevent laptop or server rebooting.
- **Bay Power Infrastructure:**
  - **100–120 Units of Heavy-Duty 6A/16A Spike-Protected Extension Boards** (commercial grade with individual switches and surge arrestors).
  - Each 4-to-6 person hack bay receives a dedicated 6-socket surge-protected power board.
  - Three-phase trunk lines distributed across Sectors Alpha–Echo encased in 20 dual-channel heavy rubber cable protector ramps to prevent tripping hazards.

---

## 4. Who Fills What (Accountability)

| Task | Lead | Verification Method | Target Date |
|---|---|---|:---:|
| **Physical Room Layout CAD / Blueprint** | Nangaiyar M | Measured tape diagram | Dec 15, 2026 |
| **Circuit Breaker Load Calculation** | Campus Electrician | Clamp meter amp test | Jan 10, 2027 |
| **Power Strip & Spike Guard Deployment** | Logistics Squad | Tagged & labeled per bay | Jan 21, 2027 (14:00) |
| **Wi-Fi Access Point Stress Test (500 devices)** | Viswanathan Ashok | Simulated ping & iperf3 test | Jan 21, 2027 (16:00) |
| **Venue Handover & Cleanliness Audit** | Nangaiyar M | Physical room sign-off | Jan 25, 2027 (12:00) |
