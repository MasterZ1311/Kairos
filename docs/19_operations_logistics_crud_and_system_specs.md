# KAIROS 2027 — Operations, Logistics & Micro-Systems CRUD Specification (Grand Edition)

**Document Reference:** `docs/19_operations_logistics_crud_and_system_specs.md`  
**Host Entity:** AWS Student Builder Group (AWS SBG) — SIST Chapter  
**Sponsoring Institution:** Sathyabama Institute of Science and Technology (Deemed to be University), Chennai – 600119  
**Super Head Mandate:** Super Head 2 (Chief Technology Officer — CTO Rikish P) & Super Head 3 (Chief Operations & Logistics Officer — COO Viswanathan S)  
**Governing Standards:** [00_hackathon_master_brief.md](./00_hackathon_master_brief.md) · [02_hard_office_copy_master_agenda.md](./02_hard_office_copy_master_agenda.md) · [08_event_operations_and_volunteer_manual.md](./08_event_operations_and_volunteer_manual.md) · [11_crisis_management_and_safety_protocol.md](./11_crisis_management_and_safety_protocol.md) · [14_official_letters_and_administrative_approvals.md](./14_official_letters_and_administrative_approvals.md) · [18_team_structure_leads_and_workforce_deployment.md](./18_team_structure_leads_and_workforce_deployment.md) · [20_indoor_auditorium_venue_transition_and_budget_plan.md](./20_indoor_auditorium_venue_transition_and_budget_plan.md)  
**Target Event Venue:** Sathyabama Indoor Stadium (Indoor Auditorium), Sathyabama Campus  
**Status:** `APPROVED PLAN`  

---

## 1. Architectural Overview

This document specifies the complete **Create, Read, Update, Delete (CRUD)** data models, relational database schemas, RESTful API contracts, validation constraints, and operational state machines for all 10 on-ground micro-logistics domains of the KAIROS 2027 event operations engine.

```mermaid
graph TD
    subgraph Operational Cloud & LAN Edge API (/api/v1/ops)
        API[Kairos Edge Ops Engine] --> MOD1[1. Power & Electrical Grid]
        API --> MOD2[2. High-Density Wi-Fi & MAC Whitelist]
        API --> MOD3[3. Restroom & Janitorial Audit]
        API --> MOD4[4. Mezzanine Sleep Pods & Cloakroom]
        API --> MOD5[5. Catering & Midnight Fuel Engine]
        API --> MOD6[6. Stage Pitch Queue & AV Production]
        API --> MOD7[7. Medical Triage & First-Aid]
        API --> MOD8[8. War Room Kanban & Radio Comms]
        API --> MOD9[9. Gate Curfew & EV Buggy Escorts]
        API --> MOD10[10. Golden Envelope & Prize Escrow]
    end
```

---

## 2. Module 1: Arena Power Grid & Table Distribution (65 kVA)

### 2.1 Relational Schema (PostgreSQL)
```sql
CREATE TYPE electrical_phase AS ENUM ('RED', 'YELLOW', 'BLUE');
CREATE TYPE arena_bay_zone AS ENUM ('ARENA_BAY_A', 'ARENA_BAY_B', 'ARENA_BAY_C', 'ARENA_BAY_D', 'STAGE_COMPLEX', 'WAR_ROOM_POD');
CREATE TYPE asset_condition AS ENUM ('PRISTINE', 'FUNCTIONAL', 'DAMAGED', 'DECOMMISSIONED');

CREATE TABLE power_circuits (
    circuit_id VARCHAR(32) PRIMARY KEY,      -- e.g., 'CIRCUIT-BAYA-PHASE-R'
    bay_zone arena_bay_zone NOT NULL,        -- 'ARENA_BAY_A'
    phase electrical_phase NOT NULL,
    max_amperage NUMERIC(5,2) DEFAULT 32.00,
    current_load_kw NUMERIC(5,2) DEFAULT 0.00,
    mcb_switch_number VARCHAR(16) NOT NULL,  -- 'DB-STAD-1A-SW04'
    is_generator_backed BOOLEAN DEFAULT TRUE,
    is_ups_buffered BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE table_power_strips (
    strip_id VARCHAR(32) PRIMARY KEY,         -- 'STRIP-BAYA-T012-A'
    circuit_id VARCHAR(32) REFERENCES power_circuits(circuit_id) ON DELETE RESTRICT,
    table_number INT NOT NULL,               -- Table 1 to 100
    assigned_team_code VARCHAR(16),          -- 'KAIROS-T012'
    total_sockets INT DEFAULT 6,
    active_sockets_used INT DEFAULT 0,
    condition asset_condition DEFAULT 'PRISTINE',
    has_rubber_cable_ramp BOOLEAN DEFAULT TRUE,
    last_inspected_by VARCHAR(64),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);
```

### 2.2 CRUD Operations & REST Contracts
* **Create (`POST /api/v1/ops/power/circuits`):**
  * Registers branch circuits linked to the stadium's 3-Phase Main Distribution Boards.
  * *Request Body:* `{"circuit_id": "CIRCUIT-BAYB-PHASE-Y", "bay_zone": "ARENA_BAY_B", "phase": "YELLOW", "max_amperage": 32.0, "mcb_switch_number": "DB-STAD-2B-SW08", "is_generator_backed": true}`
  * *Response 201 Created:* `{"status": "SUCCESS", "circuit_id": "CIRCUIT-BAYB-PHASE-Y"}`
* **Read (`GET /api/v1/ops/power/telemetry`):**
  * Returns real-time aggregate load across Red, Yellow, and Blue phases to preempt MCB breaker trips.
  * *Response 200 OK:* `{"timestamp": "2027-01-22T14:30:00Z", "total_draw_kw": 42.8, "phases": {"RED": 14.1, "YELLOW": 14.5, "BLUE": 14.2}, "status": "NOMINAL"}`
* **Update (`PATCH /api/v1/ops/power/strips/:strip_id`):**
  * Reports active socket count or flags a unit as damaged for rapid replacement.
  * *Request Body:* `{"active_sockets_used": 5, "condition": "DAMAGED", "notes": "Loose pin on socket #4"}`
* **Delete (`DELETE /api/v1/ops/power/strips/:strip_id`):**
  * Decommissions faulty spike strips from active arena inventory.

---

## 3. Module 2: High-Density Wi-Fi 6 & MAC Whitelisting

### 3.1 Relational Schema (PostgreSQL)
```sql
CREATE TYPE device_category AS ENUM ('BUILDER_LAPTOP', 'TEST_RIG', 'ORGANIZER_MACHINE', 'JURY_TABLET', 'STAGE_BROADCAST');

CREATE TABLE device_whitelist (
    mac_address MACADDR PRIMARY KEY,
    team_code VARCHAR(16),
    device_owner_name VARCHAR(120) NOT NULL,
    category device_category DEFAULT 'BUILDER_LAPTOP',
    ip_assignment INET,
    allocated_bandwidth_mbps INT DEFAULT 30,
    is_blacklisted BOOLEAN DEFAULT FALSE,
    blacklist_reason TEXT,
    registered_at TIMESTAMPTZ DEFAULT NOW(),
    last_seen_ap VARCHAR(64)                -- 'AP-STADIUM-RAFTER-06'
);

CREATE TABLE firewall_whitelisted_endpoints (
    endpoint_id SERIAL PRIMARY KEY,
    hostname VARCHAR(255) UNIQUE NOT NULL,
    port_number INT DEFAULT 443,
    service_name VARCHAR(64) NOT NULL,     -- 'AWS_BEDROCK', 'DOCKER_HUB', 'GITHUB_SSH'
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMPTZ DEFAULT NOW()
);
```

### 3.2 CRUD Operations & REST Contracts
* **Create (`POST /api/v1/ops/network/whitelist`):**
  * Bypasses captive portal for validated developer laptops (maximum 4 per team).
  * *Request Body:* `{"mac_address": "3A:F2:C1:89:44:E2", "team_code": "KAIROS-T012", "device_owner_name": "Aditya Verma", "category": "BUILDER_LAPTOP"}`
* **Read (`GET /api/v1/ops/network/devices?team_code=KAIROS-T012`):**
  * Retrieves all authorized MAC addresses and active IP assignments for a specific team.
* **Update (`PATCH /api/v1/ops/network/whitelist/:mac_address`):**
  * Dynamically throttles bandwidth, increases allocation for live demos, or flags network abuse.
* **Delete (`DELETE /api/v1/ops/network/whitelist/:mac_address`):**
  * Removes network authorization immediately upon disqualification or event closure.

---

## 4. Module 3: Restroom Audits & Janitorial Dispatch

### 4.1 Relational Schema (PostgreSQL)
```sql
CREATE TYPE restroom_gender AS ENUM ('MALE', 'FEMALE', 'NEUTRAL');
CREATE TYPE audit_status AS ENUM ('CLEAN', 'NEEDS_ATTENTION', 'CRITICAL_DISPATCH', 'CLOSED_MAINTENANCE');

CREATE TABLE restroom_facilities (
    facility_id VARCHAR(32) PRIMARY KEY,    -- 'RR-STAD-NORTH-MALE', 'RR-STAD-SOUTH-FEMALE', 'RR-GREEN-ROOM-1'
    location_desc VARCHAR(64) NOT NULL,
    gender restroom_gender NOT NULL,
    stalls_count INT NOT NULL,
    urinals_count INT DEFAULT 0,
    sanitary_pad_dispenser BOOLEAN DEFAULT FALSE,
    current_status audit_status DEFAULT 'CLEAN',
    last_cleaned_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE restroom_inspection_logs (
    log_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    facility_id VARCHAR(32) REFERENCES restroom_facilities(facility_id) ON DELETE CASCADE,
    audited_by_volunteer VARCHAR(64) NOT NULL,
    soap_dispenser_full BOOLEAN NOT NULL,
    water_pressure_normal BOOLEAN NOT NULL,
    dustbin_emptied BOOLEAN NOT NULL,
    floor_dry BOOLEAN NOT NULL,
    sanitary_stock_ok BOOLEAN NOT NULL,
    air_freshener_present BOOLEAN NOT NULL,
    overall_status audit_status NOT NULL,
    corrective_actions_dispatched TEXT,
    created_at TIMESTAMPTZ DEFAULT NOW()
);
```

### 4.2 CRUD Operations & REST Contracts
* **Create (`POST /api/v1/ops/sanitation/inspections`):**
  * Volunteer scans QR code on restroom door every 45 minutes to log sanitation audit.
* **Read (`GET /api/v1/ops/sanitation/telemetry`):**
  * Alerts War Room when any restroom has gone >60 minutes without an inspection or shows `CRITICAL_DISPATCH`.
* **Update (`PATCH /api/v1/ops/sanitation/facilities/:facility_id`):**
  * Janitorial supervisor stamps the restroom as `CLEAN` after mopping and soap replenishment.
* **Delete (`DELETE /api/v1/ops/sanitation/inspections/:log_id`):**
  * Restricted to Super Head 3 (COO) for compliance record pruning.

---

## 5. Module 4: Mezzanine Sleep Pods & Luggage Cloakroom

### 5.1 Relational Schema (PostgreSQL)
```sql
CREATE TYPE cloakroom_status AS ENUM ('DEPOSITED', 'TEMPORARY_RETRIEVAL', 'FINAL_CLAIMED');
CREATE TYPE rest_zone_type AS ENUM ('MEZZANINE_QUIET_PODS', 'GREEN_ROOM_1_FEMALE', 'HOSTEL_WING_BOYS', 'HOSTEL_WING_GIRLS');

CREATE TABLE cloakroom_deposits (
    token_number INT PRIMARY KEY,           -- Physical Brass/PVC Token 1 to 500
    team_code VARCHAR(16),
    owner_name VARCHAR(120) NOT NULL,
    owner_phone VARCHAR(15) NOT NULL,
    bag_count INT DEFAULT 1,
    bag_description TEXT,
    status cloakroom_status DEFAULT 'DEPOSITED',
    deposited_at TIMESTAMPTZ DEFAULT NOW(),
    retrieved_at TIMESTAMPTZ,
    desk_volunteer VARCHAR(64) NOT NULL
);

CREATE TABLE rest_zone_occupancy (
    zone_id VARCHAR(32) PRIMARY KEY,        -- 'ZONE-MEZZANINE-PODS'
    zone_type rest_zone_type NOT NULL,
    max_capacity_mats INT NOT NULL,
    currently_occupied INT DEFAULT 0,
    earplugs_stock INT DEFAULT 100,
    blankets_stock INT DEFAULT 40,
    updated_at TIMESTAMPTZ DEFAULT NOW()
);
```

### 5.2 CRUD Operations & REST Contracts
* **Create (`POST /api/v1/ops/cloakroom/deposit`):**
  * Issues physical brass/PVC token and creates a digital custodial log.
  * *Request Body:* `{"token_number": 84, "team_code": "KAIROS-T014", "owner_name": "Rohan Nair", "owner_phone": "9840123456", "bag_count": 2, "bag_description": "Wildcraft blue trolley + black laptop bag", "desk_volunteer": "Vignesh K"}`
* **Read (`GET /api/v1/ops/cloakroom/lookup/:token_number`):**
  * Displays owner name, phone number, and bag description for verification before handover.
* **Update (`PATCH /api/v1/ops/cloakroom/claim/:token_number`):**
  * Updates state to `FINAL_CLAIMED` and timestamps retrieval.
* **Delete (`DELETE /api/v1/ops/cloakroom/:token_number`):**
  * Re-cycles the token number into the available inventory pool.

---

## 6. Module 5: Catering, Meal Tokens & Midnight Graveyard Fuel

### 6.1 Relational Schema (PostgreSQL)
```sql
CREATE TYPE meal_type AS ENUM (
    'BREAKFAST_D1', 'LUNCH_D1', 'HIGH_TEA_D1', 'DINNER_D1', 'MIDNIGHT_FUEL_D1',
    'BREAKFAST_D2', 'LUNCH_D2', 'HIGH_TEA_D2', 'DINNER_D2', 'MIDNIGHT_FUEL_D2',
    'BREAKFAST_D3'
);
CREATE TYPE dietary_pref AS ENUM ('VEG', 'NON_VEG', 'JAIN');

CREATE TABLE meal_vouchers (
    voucher_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    participant_qr_code VARCHAR(64) NOT NULL,
    team_code VARCHAR(16),
    participant_name VARCHAR(120) NOT NULL,
    dietary dietary_pref DEFAULT 'NON_VEG',
    meal meal_type NOT NULL,
    is_redeemed BOOLEAN DEFAULT FALSE,
    redeemed_at TIMESTAMPTZ,
    counter_volunteer VARCHAR(64),
    CONSTRAINT uq_participant_meal UNIQUE (participant_qr_code, meal)
);

CREATE TABLE midnight_fuel_inventory (
    item_id VARCHAR(32) PRIMARY KEY,
    item_name VARCHAR(64) NOT NULL,
    initial_stock INT NOT NULL,
    dispatched_stock INT DEFAULT 0,
    remaining_stock INT GENERATED ALWAYS AS (initial_stock - dispatched_stock) STORED,
    batch_drop_time TIMESTAMPTZ NOT NULL
);
```

### 6.2 CRUD Operations & REST Contracts
* **Create/Redeem (`POST /api/v1/ops/catering/redeem`):**
  * Scans participant badge QR at the buffet gate. Rejects duplicate scans immediately with a 409 Conflict response.
* **Read (`GET /api/v1/ops/catering/headcount?meal=LUNCH_D1`):**
  * Real-time consumed vs. pending counts to allow the caterer to manage hot food batches.
* **Update (`PATCH /api/v1/ops/catering/midnight-surge/:item_id`):**
  * Increments dispatched count of instant noodles, energy drinks, and hot coffee flasks.
* **Delete (`DELETE /api/v1/ops/catering/vouchers/:voucher_id`):**
  * Super-admin reset in case a student's badge was erroneously scanned.

---

## 7. Module 6: Stage Pitch Queue, AV Production & Timers

### 7.1 Relational Schema (PostgreSQL)
```sql
CREATE TYPE pitch_state AS ENUM ('WAITING_GREEN_ROOM', 'TECH_CHECKED', 'ON_STAGE', 'COMPLETED', 'DISQUALIFIED_NO_SHOW');

CREATE TABLE stage_pitch_queue (
    queue_id SERIAL PRIMARY KEY,
    pitch_order INT UNIQUE NOT NULL,
    team_code VARCHAR(16),
    project_title VARCHAR(150) NOT NULL,
    hdmi_tested BOOLEAN DEFAULT FALSE,
    offline_backup_video_verified BOOLEAN DEFAULT FALSE,
    state pitch_state DEFAULT 'WAITING_GREEN_ROOM',
    scheduled_time TIMESTAMPTZ NOT NULL,
    actual_start_time TIMESTAMPTZ,
    pitch_duration_seconds INT DEFAULT 0,
    qa_duration_seconds INT DEFAULT 0,
    stage_manager VARCHAR(64) NOT NULL
);
```

### 7.2 CRUD Operations & REST Contracts
* **Create (`POST /api/v1/ops/stage/queue`):**
  * Ingests the 10 Grand Finalist teams into the presentation sequence.
* **Read (`GET /api/v1/ops/stage/telemetry`):**
  * Feeds the 12×8ft LED video wall and speaker confidence monitors with countdown timers and speaker metadata.
* **Update (`PATCH /api/v1/ops/stage/queue/:queue_id/advance`):**
  * Advances team status: `WAITING_GREEN_ROOM` $\rightarrow$ `TECH_CHECKED` $\rightarrow$ `ON_STAGE` $\rightarrow$ `COMPLETED`.
* **Delete (`DELETE /api/v1/ops/stage/queue/:queue_id`):**
  * Adjusts sequence order in case of disqualification or technical forfeit.

---

## 8. Module 7: Medical Triage, First-Aid & Emergency Incidents

### 8.1 Relational Schema (PostgreSQL)
```sql
CREATE TYPE severity_tier AS ENUM ('MILD', 'MODERATE', 'CRITICAL_AMBULANCE');

CREATE TABLE medical_incidents (
    incident_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    patient_name VARCHAR(120) NOT NULL,
    team_code VARCHAR(16),
    symptoms TEXT NOT NULL,
    medication_dispensed TEXT,
    severity severity_tier DEFAULT 'MILD',
    duty_first_aider VARCHAR(64) NOT NULL,
    ambulance_dispatched BOOLEAN DEFAULT FALSE,
    hospital_name VARCHAR(120) DEFAULT 'Sathyabama General Hospital',
    parents_notified BOOLEAN DEFAULT FALSE,
    faculty_escort VARCHAR(64),
    admitted_at TIMESTAMPTZ DEFAULT NOW(),
    resolved_at TIMESTAMPTZ
);
```

### 8.2 CRUD Operations & REST Contracts
* **Create (`POST /api/v1/ops/medical/incident`):**
  * Logs medical intake at the Stadium Foyer First-Aid Bay.
* **Read (`GET /api/v1/ops/medical/active`):**
  * Live feed visible to Chief Safety Officer (CSO) and Faculty Coordinators.
* **Update (`PATCH /api/v1/ops/medical/incident/:incident_id`):**
  * Records patient recovery timestamp or hospital transfer details.
* **Delete (`DELETE /api/v1/ops/medical/incident/:incident_id`):**
  * Strictly blocked by API layer. Medical records are permanent legal audit trails.

---

## 9. Module 8: War Room Kanban, Volunteer Shifts & Radio Comms

### 9.1 Relational Schema (PostgreSQL)
```sql
CREATE TYPE ticket_priority AS ENUM ('LOW', 'MEDIUM', 'HIGH', 'CRITICAL_BLOCKED');
CREATE TYPE ticket_status AS ENUM ('OPEN', 'DISPATCHED', 'IN_PROGRESS', 'RESOLVED');

CREATE TABLE war_room_tickets (
    ticket_id SERIAL PRIMARY KEY,
    title VARCHAR(120) NOT NULL,
    category VARCHAR(64) NOT NULL,
    arena_location VARCHAR(64) NOT NULL,     -- 'ARENA_BAY_B_TABLE_42'
    priority ticket_priority DEFAULT 'HIGH',
    status ticket_status DEFAULT 'OPEN',
    created_by_radio_call VARCHAR(64) NOT NULL,
    assigned_runner_name VARCHAR(64),
    assigned_runner_phone VARCHAR(15),
    opened_at TIMESTAMPTZ DEFAULT NOW(),
    resolved_at TIMESTAMPTZ,
    resolution_notes TEXT
);

CREATE TABLE volunteer_shifts (
    shift_id SERIAL PRIMARY KEY,
    volunteer_name VARCHAR(120) NOT NULL,
    register_number VARCHAR(16) NOT NULL,
    phone_number VARCHAR(15) NOT NULL,
    shift_cohort VARCHAR(16) NOT NULL,       -- 'ALPHA', 'BRAVO', 'CHARLIE'
    assigned_domain VARCHAR(32) NOT NULL,
    radio_unit_id VARCHAR(16),
    is_on_duty BOOLEAN DEFAULT FALSE,
    check_in_time TIMESTAMPTZ,
    check_out_time TIMESTAMPTZ
);
```

### 9.2 CRUD Operations & REST Contracts
* **Create (`POST /api/v1/ops/war-room/tickets`):**
  * Radio operator creates ticket following a voice transmission from an arena runner.
* **Read (`GET /api/v1/ops/war-room/kanban`):**
  * Real-time WebSocket feed driving the central War Room projection dashboard.
* **Update (`PATCH /api/v1/ops/war-room/tickets/:ticket_id`):**
  * Assigns runner and advances status from `OPEN` to `RESOLVED`.
* **Delete (`DELETE /api/v1/ops/war-room/tickets/:ticket_id`):**
  * Voids mistaken or duplicate ticket entries.

---

## 10. Module 9: Gate Security, Night Curfew & EV Buggy Escort

### 10.1 Relational Schema (PostgreSQL)
```sql
CREATE TYPE pass_type AS ENUM ('BUILDER_RED', 'VOLUNTEER_BLUE', 'JURY_GOLD', 'FACULTY_GREEN');

CREATE TABLE wristband_registry (
    wristband_rfid VARCHAR(32) PRIMARY KEY,
    participant_qr_code VARCHAR(64) UNIQUE NOT NULL,
    pass_category pass_type NOT NULL,
    team_code VARCHAR(16),
    holder_name VARCHAR(120) NOT NULL,
    holder_phone VARCHAR(15) NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    issued_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE night_lockin_permits (
    permit_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    wristband_rfid VARCHAR(32) REFERENCES wristband_registry(wristband_rfid),
    exit_reason TEXT NOT NULL,
    approved_by_faculty VARCHAR(64) NOT NULL,
    parent_verified_phone VARCHAR(15) NOT NULL,
    departed_at TIMESTAMPTZ DEFAULT NOW(),
    expected_return_at TIMESTAMPTZ NOT NULL,
    actual_return_at TIMESTAMPTZ,
    security_gate_officer VARCHAR(64) NOT NULL
);
```

### 10.2 CRUD Operations & REST Contracts
* **Create (`POST /api/v1/ops/security/wristband/pair`):**
  * Pairs RFID wristband to validated participant badge upon arrival.
* **Read (`GET /api/v1/ops/security/headcount/inside-stadium`):**
  * Real-time census of badges currently inside the Sathyabama Indoor Stadium perimeter.
* **Update (`PATCH /api/v1/ops/security/curfew/:permit_id/return`):**
  * Gate security logs participant return from designated hostel guest rooms.
* **Delete (`DELETE /api/v1/ops/security/wristband/:wristband_rfid`):**
  * Deactivates lost or damaged RFID wristbands.

---

## 11. Module 10: Golden Envelope & Prize Escrow Disbursement

### 11.1 Relational Schema (PostgreSQL)
```sql
CREATE TYPE prize_tier_enum AS ENUM (
    'TITLE_CHAMPION', 'RUNNER_UP_1', 'RUNNER_UP_2',
    'TRACK_AGENTIC_AI', 'TRACK_CLOUD_NATIVE', 'TRACK_WEB3_SECURITY',
    'TRACK_FINTECH_TRUST', 'TRACK_OPEN_ENTERPRISE',
    'BOUNTY_WOMEN_IN_TECH', 'BOUNTY_FRESHMEN', 'BOUNTY_SCALABLE_CLOUD'
);

CREATE TABLE golden_envelope_records (
    envelope_id VARCHAR(32) PRIMARY KEY,    -- e.g., 'ENV-2027-CHAMPION'
    prize_tier prize_tier_enum NOT NULL,
    cash_amount_inr NUMERIC(10,2) NOT NULL, -- Pure cash escrow amount
    assigned_team_code VARCHAR(16),
    winning_team_name VARCHAR(100) NOT NULL,
    bank_account_holder_name VARCHAR(120),
    bank_account_number VARCHAR(32),
    bank_ifsc_code VARCHAR(16),
    pan_card_number VARCHAR(10),
    tds_deducted_inr NUMERIC(10,2) DEFAULT 0.00,
    net_disbursed_inr NUMERIC(10,2),
    neft_utr_number VARCHAR(32),
    faculty_signoff_name VARCHAR(64),
    envelope_sealed_by VARCHAR(64),
    disbursement_completed_at TIMESTAMPTZ
);
```

### 11.2 CRUD Operations & REST Contracts
* **Create (`POST /api/v1/ops/prizes/envelopes`):**
  * Pre-generates the golden envelope allocations prior to the closing ceremony, exactly matching the ₹1,75,000 cash pool.
* **Read (`GET /api/v1/ops/prizes/envelope/:envelope_id`):**
  * Secure credential inspection for CPFO, CTO, and Faculty Coordinators.
* **Update (`PATCH /api/v1/ops/prizes/disburse/:envelope_id`):**
  * Captures winner bank details, computes tax deductions, and records bank NEFT UTR number within 72 hours.
* **Delete (`DELETE /api/v1/ops/prizes/envelopes/:envelope_id`):**
  * Strictly blocked by API layer. Financial audit records cannot be deleted.
