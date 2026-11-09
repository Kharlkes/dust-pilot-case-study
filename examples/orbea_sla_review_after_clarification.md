> Publication copy of a Dust-generated artifact. Workspace links and citation tags have been replaced or removed; see [publication edits](README.md).

# Orbea SLA Request - Internal Review Checklist

**Status:** Preparation checklist only; this document does not approve an SLA or create any contractual commitment.

**Prepared:** 9 November 2026

## Scope and guardrails

Use this checklist to review the SLA request raised by Orbea after the 29 October outage. Keep documented facts, items requiring confirmation, and recommendations separate. Do not treat any unchecked item or recommendation as an agreed contractual term, commitment, owner, or deadline.

## 1. Facts supported by the source notes

- Orbea Logistics signed on 4 November for **EUR 90,000 ARR** and a **3-year term**. [Sales weekly notes, week 45.](../data/sales_notes.md)
- The sales notes state that **the 2-hour outage on 29 October made Orbea ask for an SLA clause**.
- The sales notes state that **Amélie Roux, Head of Sales, is drafting the SLA clause**. Preserve this documented role; do not substitute another owner.
- The product notes document a 29 October incident with the following facts: **cause:** an expired TLS certificate on the export service; **duration:** 47 minutes, from 14:10 to 14:57; **post-mortem:** by Karim Haddad, Engineering Lead; **action:** certificate-expiry alerts were added. [Product notes, November.](../data/product_notes.md)
- The original source notes contain two different duration descriptions-“2-hour outage” in the sales notes and 47 minutes in the product notes. The original statements are preserved here; the separate synthetic test-evidence file records a clarification of how the two measurement windows relate.
- A separate file, **[Synthetic Test Evidence - Orbea SLA Outage-Duration Clarification](outage_duration_synthetic_evidence.md)**, records a clarification attributed to Karim Haddad: the export service was unavailable for **47 minutes, from 14:10 to 14:57**, while the sales notes’ **two hours** describes the broader period of degraded customer experience, including recovery. For the duration reconciliation, 47 minutes is the technical unavailability window and two hours is the broader customer-experience/recovery window. This does not establish Orbea-specific impact or approve any SLA language.
- The source notes do **not** identify final approval ownership or a deadline for the SLA review or customer response.

## 2. Questions requiring confirmation

### Incident facts

- [x] For the duration reconciliation, the technical export-service unavailability window is **47 minutes (14:10-14:57)**; the sales notes’ **two hours** is the broader degraded-customer-experience period, including recovery, per the synthetic test evidence file. This resolves the measurement-window discrepancy but does not establish Orbea-specific impact or approve customer-facing wording.
- [x] The two durations refer to different measures/windows: technical unavailability versus broader customer experience and recovery. The supplied clarification gives the technical timestamps (14:10-14:57); the broader two-hour period’s exact start/end timestamps and time zone remain unconfirmed.
- [ ] Was Orbea directly affected? If so, confirm the affected service, customer-visible symptoms, impact window, detection and restoration times, and any customer-specific evidence.
- [ ] Confirm whether the expired TLS certificate and the added certificate-expiry alerts are approved facts for inclusion in customer-facing material.
- [ ] Confirm whether any additional incident facts, remediation status, or post-mortem conclusions are needed before reviewing the clause.

### SLA scope and terms

- [ ] What service or services would the requested SLA cover?
- [ ] Is the request for a new clause, an amendment to the signed agreement, or another contractual instrument?
- [ ] What availability or service metric is being requested, and what measurement period and measurement method should apply?
- [ ] What support, response, restoration, maintenance, exclusion, reporting, service-credit, or other remedy provisions-if any-are being considered? Do not assume any of these are agreed.
- [ ] What effective date and relationship to the existing Orbea agreement should be used, if an SLA is approved?
- [ ] Confirm that Amélie’s draft is the current version for review and identify its version/date without changing her documented drafting role.

### Approval and timing

- [ ] Which functions or individuals must review the draft before it can be sent to Orbea?
- [ ] Who has final approval authority? **This is currently unknown and must be confirmed.**
- [ ] What customer-response or internal-review deadline, if any, has been requested or agreed? **No deadline is documented in the source notes.**
- [ ] Who is responsible for recording approvals, open issues, and the final decision once the approval path is confirmed?

## 3. Proposed review points - recommendations

- **Recommendation:** Resolve and document the outage-duration discrepancy before using incident duration in any SLA rationale or customer-facing language.
- **Recommendation:** Prepare a short incident fact sheet that distinguishes technical incident duration from customer-visible impact, if they differ, and have the relevant internal reviewers validate it.
- **Recommendation:** Compare Amélie’s draft against the signed Orbea commercial documents and identify whether the proposed text would add to, amend, or conflict with existing obligations.
- **Recommendation:** Review the draft for clear definitions, measurement and reporting mechanics, exclusions, maintenance treatment, support interactions, remedies, effective date, and change-control treatment-without filling in any term until it is confirmed and approved.
- **Recommendation:** Establish the approval path explicitly before routing the draft; record the final approval owner and any deadline rather than inferring either one.
- **Recommendation:** Keep an issues log showing each unresolved question, the evidence needed, the decision, and the approving authority.
- **Recommendation:** Do not communicate an SLA commitment or incident characterization externally until the required approvals are recorded.

## 4. Completion checklist

- [x] Incident-duration discrepancy reconciled with an agreed explanation: **47 minutes (14:10-14:57)** is the technical export-service unavailability window, while **two hours** is the broader degraded-customer-experience period including recovery, as recorded in the synthetic test evidence file.
- [ ] Customer impact and affected service confirmed.
- [ ] Amélie’s draft identified as the working draft for review.
- [ ] SLA scope and each proposed term confirmed or marked unresolved.
- [ ] Existing Orbea agreement/order documents checked for consistency.
- [ ] Review and approval participants identified.
- [ ] Final approval owner confirmed.
- [ ] Any internal or customer deadline confirmed.
- [ ] Open issues and approval decisions recorded.
- [ ] External communication held until approval is complete.

## References

- Sales weekly notes, week 45, written 7 November: [source file](../data/sales_notes.md)
- Product notes, November: [source file](../data/product_notes.md)
- Synthetic test evidence: [Orbea SLA outage-duration clarification](outage_duration_synthetic_evidence.md) - user-provided fictional evidence, attributed to Karim Haddad.
