# Kairos 2027 — Website Technical Architecture, DDL & API Specification (Grand Edition)

**Executive Governance:** Super Head 2 (Chief Technology & Infrastructure Officer)  
**Reporting Directly To:** Thenappan T (President & Apex Organizer)  
**Core Stack:** Next.js 14 (App Router) · TypeScript · Tailwind CSS v3.4 · PostgreSQL (Supabase / RDS Aurora) · Prisma ORM · NextAuth.js  
**Registration Model:** **100% FREE — ZERO ENTRY FEE**  
**Meetup Integration:** Mandatory Meetup RSVP verification for all participants per AWS SBG guidelines  
**Scale Target:** 2,000+ Applications · 250 Online Semi-Finalists · 100 On-Campus Finalist Teams  

---

## 1. Next.js 14 App Router Directory Structure

```text
website/
├── app/
│   ├── layout.tsx                     # Global Root Layout with Amazon Ember fonts & metadata
│   ├── page.tsx                       # / : Public Landing Hub, Countdown & Tracks
│   ├── register/
│   │   └── page.tsx                   # /register : Meetup RSVP Verification & Profile Setup
│   ├── team/
│   │   ├── create/
│   │   │   └── page.tsx               # /team/create : Team Lead Creation & Abstract Upload
│   │   └── join/
│   │       └── page.tsx               # /team/join : Teammate Meetup Verification & Join Link
│   ├── dashboard/
│   │   └── page.tsx                   # /dashboard : Authenticated Hacker Central Command
│   ├── tracks/
│   │   └── page.tsx                   # /tracks : 5 Enterprise Tracks & AWS Blueprints
│   ├── online-qualifier/
│   │   └── page.tsx                   # /online-qualifier : Round 1 Loom & Code Submission Bay
│   ├── on-campus/
│   │   └── page.tsx                   # /on-campus : Central Library Floorplan & Bus Scheduler
│   ├── resources/
│   │   └── page.tsx                   # /resources : AWS Student Content Resource Library
│   ├── leaderboard/
│   │   └── page.tsx                   # /leaderboard : Real-Time Z-Score Normalized Rankings
│   ├── stage/
│   │   └── page.tsx                   # /stage : High-Contrast 20x10ft 4K LED Screen Display Mode
│   ├── judging/
│   │   └── page.tsx                   # /judging : PIN-Protected Digital Jury Scoring Portal
│   ├── sponsors/
│   │   └── page.tsx                   # /sponsors : Enterprise Sponsor Prospectus & MoUs
│   ├── rules/
│   │   └── page.tsx                   # /rules : Code of Conduct & 100% Student IP Charter
│   ├── members/
│   │   ├── page.tsx                   # /members : Public Recognition Wall & Filterable Member Directory
│   │   ├── leadership/
│   │   │   └── page.tsx               # /members/leadership : Higher Management Gallery (2026-27 Batch & Alumni)
│   │   └── [username]/
│   │       └── page.tsx               # /members/[username] : Individual Contributor Dossier & Work Proof
│   ├── csat/
│   │   └── page.tsx                   # /csat : Mandatory Post-Event AWS SBG Feedback Engine
│   └── api/
│       ├── v1/
│       │   ├── register/route.ts      # Handles Round 0 application ingestion
│       │   ├── meetup/verify/route.ts # Validates Meetup Member profile & event RSVP
│       │   ├── team/route.ts          # Team creation, roster locking & code generation
│       │   ├── qualifier/route.ts     # Ingests Loom demo URL & GitHub webhook secret
│       │   ├── judging/score/route.ts # Records rubric points & triggers Z-score service
│       │   ├── telemetry/github/route.ts # Webhook listener for commit velocity tracking
│       │   ├── members/route.ts       # Query members directory with batch/domain/role filters
│       │   ├── members/[id]/route.ts  # Single member profile, badges & work contribution proof
│       │   └── csat/route.ts          # Ingests survey data & exports AWS SBG CSV
└── prisma/
    └── schema.prisma                  # Prisma ORM schema
```

---

## 2. Production PostgreSQL DDL Schema Specifications

```sql
-- KAIROS 2027 PRODUCTION DDL SCHEMA (ZERO-FEE / DUAL-PHASE / MEETUP INTEGRATED)

-- 1. Teams Table
CREATE TABLE teams (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    team_code VARCHAR(12) UNIQUE NOT NULL, -- e.g., 'KAIROS-T042'
    team_name VARCHAR(100) NOT NULL,
    track_id INT NOT NULL CHECK (track_id BETWEEN 1 AND 5),
    institution_name VARCHAR(150) NOT NULL,
    city VARCHAR(80) NOT NULL,
    state VARCHAR(80) NOT NULL,
    github_repo_url VARCHAR(255),
    commit_webhook_secret VARCHAR(64),
    
    -- Selection Stage Enum
    selection_stage VARCHAR(30) DEFAULT 'ROUND_0_APPLICANT',
    -- Stages: 'ROUND_0_APPLICANT', 'ONLINE_SEMI_FINALIST', 'ON_CAMPUS_QUALIFIED', 'DISQUALIFIED'
    
    -- Round 0 Abstract Fields
    problem_title VARCHAR(150) NOT NULL,
    problem_abstract TEXT NOT NULL,
    architecture_pdf_url VARCHAR(255),
    
    -- Round 1: Online Technical Qualifier Fields (Jan 02-04)
    online_qualifier_score DECIMAL(5,2),
    loom_video_url VARCHAR(255),
    online_defense_slot TIMESTAMP WITH TIME ZONE,
    online_meet_room_id VARCHAR(30), -- 'Virtual-Meet-01' through 'Virtual-Meet-10'
    
    -- Round 2: On-Campus Finalist Fields (Jan 22-24)
    on_campus_confirmed BOOLEAN DEFAULT FALSE,
    desk_bay_allocation VARCHAR(20), -- e.g., 'LH2-BAY-14'
    checked_in BOOLEAN DEFAULT FALSE,
    checked_in_at TIMESTAMP WITH TIME ZONE,
    
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 2. Team Members Table (With Mandatory Meetup & AWS Builder Center Integration)
CREATE TABLE team_members (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    team_id UUID REFERENCES teams(id) ON DELETE CASCADE,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    phone_number VARCHAR(15) NOT NULL,
    college_registration_number VARCHAR(50) NOT NULL,
    is_team_leader BOOLEAN DEFAULT FALSE,
    
    -- AWS SBG Guidelines & Community Integration Fields
    meetup_profile_url VARCHAR(255) NOT NULL, -- e.g. https://www.meetup.com/members/12345678/
    meetup_member_id VARCHAR(50),
    meetup_rsvp_verified BOOLEAN DEFAULT FALSE,
    aws_builder_center_url VARCHAR(255), -- Direct community connection
    
    -- On-Campus Free Swag & Logistics Fields
    nfc_badge_uid VARCHAR(32) UNIQUE, -- Laser-Etched Matte Black NFC Chip UID
    hoodie_size VARCHAR(5) NOT NULL CHECK (hoodie_size IN ('S', 'M', 'L', 'XL', 'XXL')),
    tshirt_size VARCHAR(5) NOT NULL CHECK (tshirt_size IN ('S', 'M', 'L', 'XL', 'XXL')),
    bus_hub_route VARCHAR(50) DEFAULT 'NONE', -- 'Central', 'Tambaram', 'Airport', 'CMBT', 'None'
    
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 3. Judges & Technical Evaluators Table
CREATE TABLE judges (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    access_pin VARCHAR(6) UNIQUE NOT NULL, -- 6-Digit PIN
    full_name VARCHAR(100) NOT NULL,
    organization VARCHAR(120) NOT NULL, -- e.g. 'AWS', 'Sequoia', 'Tech Unicorn'
    designation VARCHAR(100) NOT NULL,
    track_specialization INT,
    assigned_hall VARCHAR(20), -- 'Auditorium', 'LH1', 'LH2', 'LH3', 'Virtual-Meet-01..10'
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 4. Checkpoint Evaluations Table (3 Gates + Online Qualifier)
CREATE TABLE evaluations (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    team_id UUID REFERENCES teams(id) ON DELETE CASCADE,
    judge_id UUID REFERENCES judges(id) ON DELETE CASCADE,
    checkpoint_gate INT NOT NULL, -- 0: Online Qualifier, 1: Architecture, 2: Code, 3: Grand Demo
    criterion_1_score DECIMAL(5,2) NOT NULL,
    criterion_2_score DECIMAL(5,2) NOT NULL,
    criterion_3_score DECIMAL(5,2) NOT NULL,
    criterion_4_score DECIMAL(5,2) NOT NULL,
    raw_total_score DECIMAL(5,2) NOT NULL,
    normalized_z_score DECIMAL(7,4), -- Automatically calculated via Z-Score service
    qualitative_feedback TEXT,
    recused_conflict_of_interest BOOLEAN DEFAULT FALSE,
    evaluated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT unique_team_judge_gate UNIQUE (team_id, judge_id, checkpoint_gate)
);

-- 5. Commit Telemetry Table (Live Commit Audits)
CREATE TABLE commit_logs (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    team_id UUID REFERENCES teams(id) ON DELETE CASCADE,
    commit_hash VARCHAR(40) NOT NULL,
    commit_message TEXT,
    author_name VARCHAR(100),
    lines_added INT DEFAULT 0,
    lines_deleted INT DEFAULT 0,
    committed_at TIMESTAMP WITH TIME ZONE NOT NULL,
    logged_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 6. Post-Event CSAT & AWS SBG Metric Reporting Table
CREATE TABLE csat_feedback (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    team_member_id UUID REFERENCES team_members(id) ON DELETE SET NULL,
    overall_satisfaction INT NOT NULL CHECK (overall_satisfaction BETWEEN 1 AND 5),
    nps_score INT NOT NULL CHECK (nps_score BETWEEN 0 AND 10),
    cloud_services_used TEXT[], -- e.g. ARRAY['Bedrock', 'Lambda', 'DynamoDB', 'IoT Core']
    pursuing_aws_certification VARCHAR(20), -- 'YES', 'NO', 'ALREADY_CERTIFIED'
    event_feedback TEXT,
    testimonial_quote TEXT,
    submitted_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 7. Organizational Batches Table (Tenure / Academic Cohort)
CREATE TABLE org_batches (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    batch_slug VARCHAR(20) UNIQUE NOT NULL, -- e.g. '2026-2027', '2025-2026'
    batch_name VARCHAR(100) NOT NULL,       -- e.g. 'Batch of 2026–2027 (The Grand Edition)'
    tenure_start DATE NOT NULL,
    tenure_end DATE NOT NULL,
    is_active_batch BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 8. Organizational Members & Higher Management Table
CREATE TABLE org_members (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    batch_id UUID REFERENCES org_batches(id) ON DELETE CASCADE,
    username VARCHAR(50) UNIQUE NOT NULL,   -- URL slug e.g. 'thenappan-t', 'superhead-cto'
    full_name VARCHAR(100) NOT NULL,
    role_title VARCHAR(120) NOT NULL,       -- e.g. 'President & Apex Organizer', 'Chief Technology Officer (Super Head 2)'
    
    -- Hierarchy & Tier Classification
    tier VARCHAR(30) NOT NULL CHECK (tier IN ('APEX_PRESIDENT', 'SUPER_HEAD', 'SUB_HEAD', 'CORE_LEAD', 'CREW_VOLUNTEER', 'FACULTY_ADVISOR')),
    is_higher_management BOOLEAN DEFAULT FALSE, -- TRUE for President, 6 Super Heads, and Faculty Patrons
    division VARCHAR(60) NOT NULL,          -- e.g. 'Executive', 'Division 1: CPFO', 'Division 2: CTO', etc.
    display_order INT DEFAULT 99,           -- Controls sort priority on the page
    
    -- Profile & Media
    photo_url VARCHAR(255) NOT NULL,        -- High-res portrait
    bio TEXT NOT NULL,
    builder_philosophy_quote TEXT,
    academic_department VARCHAR(100),       -- e.g. 'Computer Science & Engineering, SIST'
    graduation_year INT,
    
    -- Credentials & Ecosystem Integration
    aws_certifications TEXT[],              -- e.g. ARRAY['AWS Solutions Architect - Associate', 'AWS Cloud Practitioner']
    aws_builder_center_url VARCHAR(255),
    linkedin_url VARCHAR(255),
    github_url VARCHAR(255),
    portfolio_url VARCHAR(255),
    
    is_published BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 9. Member Contributions & Recognition Showcase Table
CREATE TABLE member_contributions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    member_id UUID REFERENCES org_members(id) ON DELETE CASCADE,
    event_code VARCHAR(30) DEFAULT 'KAIROS_2027', -- 'KAIROS_2027', 'AWS_COMMUNITY_DAY_2026', etc.
    contribution_category VARCHAR(60) NOT NULL,  -- e.g. 'Infrastructure & Cloud', 'Sponsorship Closure', 'Stage & Media'
    title VARCHAR(150) NOT NULL,                 -- e.g. 'Architected 10Gbps Dual-ISP Redundant Network'
    description TEXT NOT NULL,                   -- Bulleted impact story
    quantifiable_impact VARCHAR(150),            -- e.g. '100% uptime for 500 hackers across 48 hours'
    badge_label VARCHAR(60),                     -- e.g. 'Cloud Infrastructure Legend', 'Elite Sponsorship Closer'
    badge_tier VARCHAR(20) CHECK (badge_tier IN ('DIAMOND', 'PLATINUM', 'GOLD', 'SILVER')),
    proof_media_url VARCHAR(255),                -- Image or artifact link
    verification_hash VARCHAR(64) UNIQUE,        -- For tamper-proof public certificate verification
    awarded_at DATE DEFAULT CURRENT_DATE
);
```

---

## 3. Core REST & Server Actions API Specifications

### 3.1 `POST /api/v1/meetup/verify`
* **Purpose:** Validates that a user profile belongs to the official `AWS Student Builder Group — SIST` chapter on Meetup.com.
* **Request Payload:**
  ```json
  {
    "meetup_profile_url": "https://www.meetup.com/members/12345678/",
    "email": "student@sathyabama.ac.in"
  }
  ```
* **Response (200 OK):**
  ```json
  {
    "verified": true,
    "meetup_member_id": "12345678",
    "member_name": "Arun Kumar",
    "rsvp_status": "CONFIRMED",
    "event_title": "KAIROS 2027 (Grand Edition) — 48H National Hackathon"
  }
  ```

### 3.2 `POST /api/v1/team`
* **Purpose:** Creates a team or adds a verified teammate to an existing team.
* **Validation:** Enforces that every member has `meetup_rsvp_verified: true`.
* **Zero-Fee Guard:** No billing tokens or payment gateway triggers exist in the payload.

### 3.3 `POST /api/v1/qualifier/submit`
* **Purpose:** Ingests Loom 3-minute demo video link, architecture PDF URL, and repository for Round 1 (Jan 02–04).

### 3.4 `POST /api/v1/judging/submit-score`
* **Purpose:** Authenticates judge via PIN, records criteria scores, and triggers the Z-Score normalization algorithm:
  $$Z_{i,j} = \frac{X_{i,j} - \mu_j}{\sigma_j}$$
  Updates the live leaderboard in real time via Supabase Realtime / Server-Sent Events (SSE).

### 3.5 `GET /api/v1/csat/export`
* **Purpose:** Generates a pre-formatted CSV compliant with the official **AWS Student Builder Group Post-Event Reporting Form** within 48 hours of event closeout.

### 3.6 `GET /api/v1/members`
* **Purpose:** Public endpoint powering the Member Recognition Wall. Supports filtering by batch, tier, division, and search query.
* **Query Params:** `?batch=2026-2027&division=all&tier=all&search=arun`
* **Response (200 OK):**
  ```json
  {
    "batch": "2026-2027",
    "total_members": 106,
    "members": [
      {
        "id": "c1f7a4e2-...",
        "username": "thenappan-t",
        "full_name": "Thenappan T",
        "role_title": "President & Apex Organizer",
        "tier": "APEX_PRESIDENT",
        "division": "Executive Directorate",
        "photo_url": "https://assets.sbg-sathyabama.ac.in/members/thenappan_t.webp",
        "aws_certifications": ["AWS Certified Solutions Architect – Associate"],
        "contributions_count": 5,
        "badges": ["Apex Architect 2026-27", "Kairos Grand Director"]
      }
    ]
  }
  ```

### 3.7 `GET /api/v1/members/leadership`
* **Purpose:** Dedicated endpoint powering the Higher Management Showcase (`/members/leadership`).
* **Query Params:** `?batch=2026-2027` (Defaults to active batch)
* **Response (200 OK):** Returns members grouped hierarchically:
  * `apex`: President Thenappan T
  * `faculty`: Faculty Patrons & Department Advisors
  * `super_heads`: The 6 Super Heads (CPFO, CTO, COO, CXO, CCMO, CSO)
  * `sub_heads`: The 18 Squad Sub-Heads across all 6 Divisions

### 3.8 `GET /api/v1/members/[username]`
* **Purpose:** Public endpoint for an individual member's verifiable portfolio & recognition dossier (`/members/[username]`).
* **Response (200 OK):** Returns full bio, social links, photo, itemized list of contributions with quantifiable impact metrics, awarded digital badges, and cryptographic verification hash for their Certificate of Recognition.
