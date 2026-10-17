# KAIROS 2027 — Central Library Bay Allocation & Electrical Power Grid Load Sheet

> [!WARNING]
> **SUPERSEDED ARCHIVAL RECORD — INITIAL PLANNING BASELINE ONLY**  
> This specification documents the initial planning baseline (Central Library Complex). Following institutional capacity review for 100 teams (450–600 hackers), the official approved venue is **Sathyabama Indoor Stadium (Indoor Auditorium)**.  
> **Active Canonical Specification:** [`indoor_stadium_arena_bay_allocation_and_power_grid.md`](./indoor_stadium_arena_bay_allocation_and_power_grid.md)  
> **Master Transition Plan (Executive Reference):** `DOC-20 (Indoor Auditorium Transition & Budget Plan)`

> **Floor Commander:** Nangaiyar M (Community & Events Lead, Reg: `44612059`)  
> **Network Architect:** Viswanathan Ashok (Reg: `44110907`)  

---

## 1. Hack Bay Seating Manifest (100 Teams / 450 Hackers)

| Hall / Zone | Assigned Track | Team Capacity | Desk Layout | Power Strips | Wi-Fi AP Name |
|---|---|:---:|---|:---:|---|
| **LH-1 (2nd Floor)** | Track 1: Agentic AI | Teams 01 – 25 (100 hackers) | 25 Quad Pods (4 per table) | 10 × 6-socket Havells | `KAIROS-5G-LH1` |
| **LH-2 (2nd Floor)** | Track 2: Cloud-Native | Teams 26 – 50 (100 hackers) | 25 Quad Pods (4 per table) | 10 × 6-socket Havells | `KAIROS-5G-LH2` |
| **LH-3 (2nd Floor)** | Track 3: Web3 & Security | Teams 51 – 75 (100 hackers) | 25 Quad Pods (4 per table) | 10 × 6-socket Havells | `KAIROS-5G-LH3` |
| **Computing Lab (1st Fl)** | Tracks 4 & 5 (FinTech/Health) | Teams 76 – 100 (100 hackers) | 25 Workstation Pods | Integrated Lab Power | `KAIROS-5G-LAB1` |
| **Ground Foyer** | Helpdesk & Check-In | Organizers Desk | 4 Reception Tables | 4 × 4-socket Strips | `KAIROS-ADMIN` |
| **Top Floor Lounge** | VIP Jury & Corporate Partners | 35 VIP Delegates | Lounge Sofas & Dining Tables | Executive Floor Outlets | `KAIROS-VIP` |

---

## 2. Electrical Power Grid Load Calculation

```text
ESTIMATED POWER CONSUMPTION BREAKDOWN:
────────────────────────────────────────────────────────────────────────
1. Participant Laptops (450 units × 65W avg):           29,250 Watts
2. Mobile Device Chargers (450 units × 18W avg):          8,100 Watts
3. Stage Concert Line-Array & Lighting Truss:             6,500 Watts
4. Stage P2.5 LED Wall (3840×1920 active canvas):         4,000 Watts
5. Broadcast Video Rig, OBS Workstations & Monitors:      2,500 Watts
6. 24/7 Filter Coffee Machines & Water Dispensers (3 units): 3,600 Watts
────────────────────────────────────────────────────────────────────────
TOTAL ESTIMATED MAXIMUM LOAD:                           ~53.95 kW (~60 kVA)
INSTITUTIONAL TRANSFORMER FEEDER:                       100 kVA Dedicated Line
BACKUP DIESEL GENERATOR:                                125 kVA Auto-Synchronized
SAFETY MARGIN:                                          > 50% Buffer Reserve
────────────────────────────────────────────────────────────────────────
```
