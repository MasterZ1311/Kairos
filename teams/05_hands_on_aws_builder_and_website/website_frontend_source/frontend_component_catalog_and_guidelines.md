# KAIROS 2027 — Frontend Component Catalog & Engineering Guidelines

> **Frontend Architect:** Viswanathan Ashok (Hands-On Builder Lead, Reg: `44110907`)  
> **UI Designer:** Rikish B (Design Lead, Reg: `44110664`)  

---

## 1. Core UI Components Catalog

### 1. `HeroScene.tsx`
- **Purpose:** Full-viewport interactive WebGL canvas featuring subtle amber particle telemetry.
- **Physics:** Reduced motion fallback for low-power mobile devices.
- **Dependencies:** Three.js / React Three Fiber.

### 2. `TrackCard.tsx`
- **Purpose:** Displays each of the 5 innovation tracks with hover glow (`#FF9900` border), sponsor logo tag, track bounty amount (₹20,000 Pure Cash), and "View Problem Statement" modal trigger.
- **Animation:** Framer Motion spring physics on hover (`scale: 1.02, y: -4`).

### 3. `LeaderboardTable.tsx`
- **Purpose:** Live real-time scoring matrix updated over WebSocket connection.
- **Features:** Displays Rank, Team Name, Track, Milestone 1, Milestone 2, Milestone 3, Normalized Z-Score, and Final Rank.
- **Security:** Blind review toggle during active judging to hide live scores until official stage reveal.

---

## 2. Accessibility & Performance Benchmarks
- **Lighthouse Performance Score:** Minimum **95+** on Mobile and Desktop.
- **Cumulative Layout Shift (CLS):** strictly `< 0.05`.
- **First Contentful Paint (FCP):** `< 1.2 seconds` over 4G connections.
- **Semantic HTML & WCAG 2.1 AA:** Contrast ratio of at least 4.5:1 for body copy against dark surfaces.
