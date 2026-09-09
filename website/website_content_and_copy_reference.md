# Kairos 2027 (Grand Edition) — Website Content & Copy Reference
**Location:** `Events/Kairos/website/website_content_and_copy_reference.md`  
**Governing Standard:** `E:\AWS SBGL\ANTI-Help\05_COMMUNICATION_TEMPLATES_AND_INSTITUTIONAL_LETTERS.md` & `10_HACKATHON_SPONSORSHIP_LETTERS_AND_OUTREACH_KIT.md`  
**Event Window:** January 22–24, 2027 (On-Campus Grand Finale) · January 02–04, 2027 (Online Technical Qualifier)  
**Host Entity:** AWS Student Builder Group (AWS SBG) — SIST Chapter  
**Registration Model:** **100% FREE — ZERO ENTRY FEE FOR ALL STUDENTS**  
**Scale:** 100 Shortlisted National Teams (400–500 Hackers) · ₹3.5L Working Operational Capital · ₹1,75,000 Pure Cash Prizes  

---

## 1. Global Meta Tags & SEO OpenGraph Copy

```json
{
  "metaTitle": "KAIROS 2027 — National Flagship 48-Hour Hackathon | AWS Student Builder Group SIST",
  "metaDescription": "Join 400+ elite developers at Sathyabama for KAIROS 2027. 48 hours continuous non-stop hacking on AWS Cloud. 100% Free - Zero Entry Fee. ₹1,75,000 pure cash prizes, two-tier technical screening, and tier-1 corporate sponsors. Register for free now!",
  "openGraph": {
    "title": "KAIROS 2027 | The Defining Moment to Build on AWS Cloud",
    "description": "48 Hours Non-Stop • ₹1,75,000 Pure Cash Prize Pool • 100 Elite Teams • Central Library Complex, Sathyabama Chennai.",
    "url": "https://kairos.sathyabama.ac.in",
    "siteName": "Kairos 2027 Hackathon",
    "images": [
      {
        "url": "https://kairos.sathyabama.ac.in/og-image-2027.png",
        "width": 1200,
        "height": 630,
        "alt": "Kairos 2027 Grand Edition Banner"
      }
    ],
    "locale": "en_IN",
    "type": "website"
  },
  "twitter": {
    "card": "summary_large_image",
    "title": "KAIROS 2027 — Build the Future in 48 Hours",
    "description": "100% Free National Hackathon. ₹1,75,000 Pure Cash. Free Meals, Swag, and Travel Support.",
    "creator": "@awssbg_sist"
  }
}
```

---

## 2. Hero Section Copy

* **Top Notification Bar:**  
  `★ NATIONAL APPLICATIONS OPEN NOW • 100% FREE (ZERO ENTRY FEE) • ₹1,75,000 PURE CASH PRIZE POOL • [ REGISTER NOW → ]`
* **Headline:**  
  `Where Architecture Meets Execution.`
* **Sub-Headline:**  
  `48 Hours of Non-Stop Cloud Engineering, Real-Time Architecture Reviews, and High-Stakes Cash Bounties.`
* **Event Details Chip:**  
  `📅 January 22–24, 2027 • 📍 Central Library Complex, Sathyabama Campus, Chennai • 👥 100 Elite National Teams`
* **Primary Call-to-Action:**  
  `[ > Submit Round 0 Project Abstract (Free) ]`
* **Secondary Action:**  
  `[ View Sponsorship Prospectus (PDF) ]`

---

## 3. The 5 Innovation Tracks (JSON Data)

```json
[
  {
    "id": "track-1",
    "title": "Agentic AI & Generative Intelligence",
    "description": "Architect autonomous multi-agent swarms, self-healing developer pipelines, and production generative AI workflows powered by Amazon Bedrock and Claude.",
    "recommendedServices": ["Amazon Bedrock", "AWS Lambda", "Amazon OpenSearch", "LangChain/LlamaIndex"],
    "bounty": "Dedicated Track Winner Bounty: ₹7,000 Cash"
  },
  {
    "id": "track-2",
    "title": "Cloud-Native, High-Throughput & Distributed Systems",
    "description": "Build hyper-scale event-driven architectures, resilient distributed ledgers, and zero-downtime microservices capable of sustaining millions of concurrent events.",
    "recommendedServices": ["Amazon ECS / EKS", "Amazon DynamoDB", "Amazon EventBridge", "AWS Fargate"],
    "bounty": "Dedicated Track Winner Bounty: ₹7,000 Cash"
  },
  {
    "id": "track-3",
    "title": "Autonomous Edge IoT & Sustainable Green Energy",
    "description": "Deploy hardware microcontrollers, intelligent sensor networks, and edge inference systems optimizing renewable energy distribution and smart mobility.",
    "recommendedServices": ["AWS IoT Core", "AWS Greengrass", "Amazon Timestream", "ESP32/Raspberry Pi"],
    "bounty": "Dedicated Track Winner Bounty: ₹7,00,0 Cash"
  },
  {
    "id": "track-4",
    "title": "Next-Gen FinTech, Trust & Cryptographic Security",
    "description": "Engineer low-latency settlement systems, real-time algorithmic fraud prevention, and zero-knowledge identity architectures.",
    "recommendedServices": ["AWS KMS", "Amazon Cognito", "AWS GuardDuty", "Amazon Aurora Serverless"],
    "bounty": "Dedicated Track Winner Bounty: ₹7,000 Cash"
  },
  {
    "id": "track-5",
    "title": "Open Enterprise & Campus Life Innovation",
    "description": "Tackle pressing institutional and societal bottlenecks across healthcare diagnostics, agricultural supply chains, and automated university operations.",
    "recommendedServices": ["Amazon S3", "Amazon Textract", "Amazon SageMaker", "API Gateway"],
    "bounty": "Dedicated Track Winner Bounty: ₹7,000 Cash"
  }
]
```

---

## 4. Cash Prize Pool Cards (₹1,75,000 Pure Cash Pool)

```json
[
  {
    "position": "1st Place — Overall Grand Champion",
    "cashPrize": "₹60,000 Pure Cash",
    "perks": [
      "Grand Kairos Acrylic & Brass Champion Trophy",
      "VC Angel Incubation Fast-Track Pitching",
      "$5,000 in AWS Cloud Promotional Credits",
      "Direct Tier-1 Tech Interview Fast-Track",
      "Streetwear Swag Kit & Gold Certificates"
    ],
    "highlight": true
  },
  {
    "position": "2nd Place — First Runner-Up",
    "cashPrize": "₹35,000 Pure Cash",
    "perks": [
      "1st Runner-Up Acrylic Trophy",
      "$2,500 in AWS Cloud Promotional Credits",
      "Priority Interview Opportunities with Enterprise Sponsors",
      "Streetwear Swag Kit & Silver Certificates"
    ],
    "highlight": false
  },
  {
    "position": "3rd Place — Second Runner-Up",
    "cashPrize": "₹20,000 Pure Cash",
    "perks": [
      "2nd Runner-Up Acrylic Trophy",
      "$1,000 in AWS Cloud Promotional Credits",
      "Streetwear Swag Kit & Bronze Certificates"
    ],
    "highlight": false
  },
  {
    "position": "5 Enterprise Track Category Winners",
    "cashPrize": "₹7,000 Each (Total ₹35,000 Pure Cash)",
    "perks": [
      "Dedicated Enterprise Track Winner Mementos",
      "Direct API Partner Swag Crates & Bounties",
      "Fast-track Evaluation for Sponsor Accelerator Programs"
    ],
    "highlight": false
  },
  {
    "position": "Special Category Bounties",
    "cashPrize": "₹25,000 Pure Cash Total",
    "perks": [
      "Best All-Women Team: ₹10,000 Pure Cash",
      "Best Freshman / Rookie Team: ₹7,500 Pure Cash",
      "Most Scalable AWS Architecture: ₹7,500 Pure Cash"
    ],
    "highlight": false
  }
]
```

---

## 5. Comprehensive FAQ Copy Bank (Zero Entry Fee Focus)

1. **Is there any entry fee or payment required?**  
   *NO. KAIROS 2027 is 100% FREE. There are ZERO registration fees, ZERO qualifier fees, and ZERO attendance fees. All meals, on-campus stay, builder tees, smart badges, bus transit, and AWS credits are completely complimentary.*
2. **What is the Online Technical Qualifier (Round 1)?**  
   *To ensure only teams with peak-quality ideas and verified coding capabilities reach our on-campus stage, the Top 250 semi-finalist teams will participate in a virtual qualifier from January 02–04, 2027. Teams submit a working GitHub repository proof-of-concept, a 3-minute Loom video demo, and defend their architecture live via Google Meet with AWS Solutions Architects. The Top 100 teams advance to the physical finale.*
3. **What are the grand finale dates and venue?**  
   *The on-campus grand finale runs from Friday, January 22 to Sunday, January 24, 2027 at the Central Library Complex, Sathyabama Institute of Science and Technology, Chennai.*
4. **Who owns the intellectual property (IP)?**  
   *You own 100% of your code and intellectual property. Zero equity or claims are made by the organizers, college, or sponsors.*
5. **Will travel support be provided?**  
   *Yes. We operate Sathyabama University buses chartered across major Chennai transit hubs (Central Railway Station, Tambaram, Airport, CMBT Koyambedu) for inbound pickup and outbound drop-off, as well as on-campus EV buggies, all free of cost.*

---

## 6. Higher Management (Batch 2026–2027) Leadership Profile Copy & JSON Schema

```json
{
  "batch": "2026-2027",
  "batchTitle": "Batch of 2026–2027 (The Grand Edition)",
  "apexLeader": {
    "name": "Thenappan T",
    "registerNo": "44110855",
    "role": "President & Student Builder Group Leader (SBGL)",
    "chapter": "AWS Student Builder Group — SIST Chapter",
    "photo": "/assets/members/thenappan_t.webp",
    "mandate": "Directing macro-systems, institutional administration, and external partnerships for India's premier zero-fee hackathon.",
    "quote": "When financial barriers are dropped to zero, authentic engineering brilliance takes the stage.",
    "credentials": [
      "AWS Certified Solutions Architect – Associate",
      "AWS Student Builder Group Leader"
    ],
    "contact": {
      "email": "sistawscc@gmail.com",
      "phone": "+91 6381801640",
      "linkedin": "https://linkedin.com/in/thenappan-t",
      "instagram": "https://instagram.com/awssbg_sist"
    }
  },
  "facultyCoordinators": [
    {
      "name": "Dr. Balapriya .S",
      "role": "Faculty Coordinator",
      "department": "Department of Computer Science & Engineering, SIST"
    },
    {
      "name": "Dr. K. Ashok Kumar",
      "role": "Faculty Coordinator",
      "department": "Department of Computer Science & Engineering, SIST"
    }
  ],
  "institutionalDeans": {
    "deanComputing": "Dr. L. Lakshmanan, Dean — School of Computing",
    "viceChancellor": "Dr. T. Sasipraba, Vice Chancellor"
  }
}
```
