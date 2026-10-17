# KAIROS 2027 — Sponsorship Word (.docx) Document Suite & Audit Register

> **Domain:** Corporate Sponsorship, Outreach, Legal MoUs, Pitch Decks & Fulfillment  
> **Host Organization:** AWS Student Builder Group (SIST Chapter), Sathyabama Institute of Science and Technology  
> **Event Dates:** January 22 – 24, 2027 (48-Hour Continuous National Hackathon)  
> **Canonical Source of Truth:** Markdown files in [`../00_sponsorship_source_of_truth.md`](../00_sponsorship_source_of_truth.md) through [`../07_post_event_roi_and_renewal.md`](../07_post_event_roi_and_renewal.md)  
> **Last Audited:** 17 October 2026

---

## 1. Governance Architecture: Markdown as Canonical Source

All operational policies, pricing matrices, lead statuses, and legal review checklists maintain their **canonical source of truth in Markdown** within the parent `teams/01_sponsorship_and_partnerships/` workspace.

Microsoft Word (`.docx`) documents in this directory represent **audience-specific exports and compiled deliverables**. They are generated via local Python automation scripts (`gen_doc0` to `gen_doc7`) utilizing `python-docx`.

> [!WARNING]
> **AUDIT NOTICE ON EXISTING DOCX EXPORTS:**  
> The existing `.docx` files in this directory were generated prior to the 17 October 2026 audit and reconciliation. As noted in the master source of truth, older exports contain unapproved referral bounty policies, pre-filled sponsor commitments, and published university bank account numbers.  
> 
> All DOCX files must be treated as **`DRAFT WORKING EXPORTS`** and cross-referenced against the canonical Markdown files before external transmission.

---

## 2. DOCX Deliverables Audit & Status Inventory

| File Name | Canonical Markdown Source | Primary Audience | Current Export Status | Audit Notes & Verification Cautions |
|---|---|---|:---:|---|
| [`00_KAIROS_2027_Sponsorship_Meeting_2Hour_Speech_Deck_and_Script.docx`](./00_KAIROS_2027_Sponsorship_Meeting_2Hour_Speech_Deck_and_Script.docx) | [`../03_pitch_deck_and_sponsor_meeting_kit.md`](../03_pitch_deck_and_sponsor_meeting_kit.md) | **Internal Leadership & Team** | `Working Draft` | Internal 2-hour speaking script and training masterclass for Thenappan T & team. Not for external sponsor distribution. |
| [`01_KAIROS_2027_Sponsorship_Strategy_and_Outreach_Playbook.docx`](./01_KAIROS_2027_Sponsorship_Strategy_and_Outreach_Playbook.docx) | [`../01_sponsorship_strategy_and_package_matrix.md`](../01_sponsorship_strategy_and_package_matrix.md) · [`../02_prospecting_outreach_and_negotiation_playbook.md`](../02_prospecting_outreach_and_negotiation_playbook.md) | **CPFO Nikki & Outreach Squad** | `Working Draft — Requires Regen` | Contains legacy referral bounty language; refer to Markdown `01` & `02` for quarantined policy. |
| [`02_KAIROS_2027_Corporate_Pitch_Deck_Slide_Guide.docx`](./02_KAIROS_2027_Corporate_Pitch_Deck_Slide_Guide.docx) | [`../03_pitch_deck_and_sponsor_meeting_kit.md`](../03_pitch_deck_and_sponsor_meeting_kit.md) | **Sponsorship Pitchers** | `Working Draft — Aligned` | 14-slide master corporate pitch guide with presenter notes and CXO talking points. |
| [`03_KAIROS_2027_Official_Corporate_Sponsorship_Proposal_Letter.docx`](./03_KAIROS_2027_Official_Corporate_Sponsorship_Proposal_Letter.docx) | [`../signed_mous_and_contracts/non_tech_corporate_sponsorship_proposal_letter.md`](../signed_mous_and_contracts/non_tech_corporate_sponsorship_proposal_letter.md) | **Corporate VPs, CMOs, CSR Heads** | `Draft — Review Required` | Letterhead proposal template; bank details and GST claims must be confirmed by University Accounts before sending. |
| [`04_KAIROS_2027_Corporate_Sponsorship_MoU_and_Agreement_Template.docx`](./04_KAIROS_2027_Corporate_Sponsorship_MoU_and_Agreement_Template.docx) | [`../signed_mous_and_contracts/corporate_sponsorship_mou_standard_template.md`](../signed_mous_and_contracts/corporate_sponsorship_mou_standard_template.md) | **Legal, Sponsors & Accounting** | `DRAFT — NOT FOR SIGNATURE` | Must undergo formal review by University Legal Cell before execution by Dean/Registrar. |
| [`05_KAIROS_2027_Corporate_Pipeline_CRM_and_Leads_Tracker.docx`](./05_KAIROS_2027_Corporate_Pipeline_CRM_and_Leads_Tracker.docx) | [`../company_leads_tracker/corporate_sponsorship_pipeline_crm.md`](../company_leads_tracker/corporate_sponsorship_pipeline_crm.md) | **Sponsorship Squad & Leads** | `Working Draft — Requires Regen` | Older export contains unverified "Closed-Won" claims; refer to audited Markdown CRM for verified pipeline state. |
| [`06_KAIROS_2027_Sponsor_Benefit_Fulfillment_and_PoP_Checklist.docx`](./06_KAIROS_2027_Sponsor_Benefit_Fulfillment_and_PoP_Checklist.docx) | [`../06_fulfillment_assets_and_proof_of_performance.md`](../06_fulfillment_assets_and_proof_of_performance.md) | **Operations, Media & Treasury** | `Working Draft — Requires Regen` | Older export contains pre-filled tickboxes; refer to Markdown `06` for operational schema. |
| [`KAIROS_2027_Complete_Sponsorship_Master_Operations_Manual.docx`](./KAIROS_2027_Complete_Sponsorship_Master_Operations_Manual.docx) | Compiled Suite (`00` to `07`) | **Executive Leadership Council** | `Working Draft — Master Binder` | All-in-one compiled master compendium. |

---

## 3. Python Document Generators Directory

The automated Python generator scripts are maintained in [`../scripts/`](../scripts/):

- [`../scripts/docx_utils.py`](../scripts/docx_utils.py): Shared design token library, table stylers, callout boxes, and header/footer formatters.
- [`../scripts/gen_doc0_speech_deck.py`](../scripts/gen_doc0_speech_deck.py): Generates Document 0 (Internal Speech Deck & Meeting Script).
- [`../scripts/gen_doc1_playbook.py`](../scripts/gen_doc1_playbook.py): Generates Document 1 (Strategy & Outreach Playbook).
- [`../scripts/gen_doc2_pitch_guide.py`](../scripts/gen_doc2_pitch_guide.py): Generates Document 2 (Pitch Deck Slide Guide).
- [`../scripts/gen_doc3_proposal_letter.py`](../scripts/gen_doc3_proposal_letter.py): Generates Document 3 (Official Proposal Letter).
- [`../scripts/gen_doc4_mou_template.py`](../scripts/gen_doc4_mou_template.py): Generates Document 4 (MoU Agreement Template).
- [`../scripts/gen_doc5_crm_tracker.py`](../scripts/gen_doc5_crm_tracker.py): Generates Document 5 (CRM & Leads Tracker).
- [`../scripts/gen_doc6_fulfillment_checklist.py`](../scripts/gen_doc6_fulfillment_checklist.py): Generates Document 6 (Fulfillment Checklist).
- [`../scripts/gen_doc7_master_binder.py`](../scripts/gen_doc7_master_binder.py): Compiles Documents 0 through 6 into the Master Operations Manual.

### Script Re-Execution Guardrail:
Do not execute generator scripts without verifying that their embedded data structures match [`../00_sponsorship_source_of_truth.md`](../00_sponsorship_source_of_truth.md). Future updates should refactor generators to parse canonical Markdown source files directly.
