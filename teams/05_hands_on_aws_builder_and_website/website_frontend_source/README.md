# Website Frontend Source & Engineering Specification

> **Subfolder:** `teams/05_hands_on_aws_builder_and_website/website_frontend_source/`  
> **Direct Lead:** **Viswanathan Ashok** (Hands-On Builder Lead, Reg: `44110907`, Phone: `+91 9080809088`)  
> **Repository Integration:** Directly maps to [`docs/16_website_design_and_experience_specification.md`](../../../docs/16_website_design_and_experience_specification.md)  

---

## 1. Scope & Mandate

This folder defines the frontend source architecture, page routes, design tokens, UI component specifications, and animation physics for the official KAIROS 2027 web application (`kairos.sistawscc.org`).

---

## 2. Next.js 14 App Router Directory Architecture

```text
src/
├── app/
│   ├── layout.tsx                 # Root layout with Amazon Ember font & meta tags
│   ├── page.tsx                   # Master Hero Landing Page
│   ├── tracks/
│   │   └── page.tsx               # 5 Innovation Tracks & Challenge Statements
│   ├── schedule/
│   │   └── page.tsx               # Interactive 48-Hour Timeline & Milestones
│   ├── sponsors/
│   │   └── page.tsx               # Corporate Sponsor Tiers & Prospectus Download
│   ├── faq/
│   │   └── page.tsx               # Comprehensive Searchable FAQ Accordion
│   ├── register/
│   │   └── page.tsx               # Dual-Phase Team Registration Portal
│   ├── leaderboard/
│   │   └── page.tsx               # Live WebSocket Z-Score Leaderboard (Protected)
│   └── checkin/
│       └── page.tsx               # Smart NFC Badge Check-In Scanner (Admin Only)
├── components/
│   ├── ui/                        # Button, Card, Badge, Modal, Tooltip, Dialog
│   ├── hero/                      # HeroScene, CyberHorizonGlyph, CountdownClock
│   ├── tracks/                    # TrackCard, ProblemModal, TechBadge
│   ├── live/                      # LiveStreamEmbed, WebSocketFeed, ScoreCard
│   └── navigation/                # Navbar, MobileDrawer, Footer
└── lib/
    ├── api.ts                     # REST & WebSocket client
    ├── tokens.ts                  # Obsidian-Amber CSS Color Variables
    └── utils.ts                   # Class merging & formatters
```

---

## 3. Tailwind Design Token Configuration

```typescript
// tailwind.config.ts snippet
export default {
  theme: {
    extend: {
      colors: {
        obsidian: '#0D1117',
        squidInk: '#232F3E',
        cyberSlate: '#1A2433',
        smileAmber: '#FF9900',
        terminalGreen: '#3FB950',
        cloudSilver: '#D5DBDB',
      },
      fontFamily: {
        sans: ['"Amazon Ember"', 'sans-serif'],
        mono: ['"Amazon Ember Mono"', 'monospace'],
        display: ['"Amazon Ember Display"', 'sans-serif'],
      },
    },
  },
};
```

---

## 4. Who Fills What (Accountability)

| Component Area | Lead Developer | Tech Reviewer | Target Completion |
|---|---|---|:---:|
| **Hero Landing & 3D WebGL Canvas** | Viswanathan Ashok | Rikish B | Oct 05, 2026 |
| **Track Cards & Modal System** | Frontend Squad Dev A | Shanmugapriyan S | Oct 12, 2026 |
| **Registration Form & Webhooks** | Frontend Squad Dev B | Viswanathan Ashok | Oct 15, 2026 |
| **Live WebSocket Leaderboard UI** | Viswanathan Ashok | Thenappan T | Jan 10, 2027 |
| **NFC Tap & Check-In Route** | Mobile/Web Squad | Viswanathan Ashok | Jan 15, 2027 |
