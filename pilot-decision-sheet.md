# Pilot decision sheet

A working template by Charles Knaepen, informed by sections 4.1, 4.3, 4.4 and 5.2 of his master's thesis. It is a practical adaptation, not a validated assessment scale. Complete the fields with the users who will do the work; do not turn unknowns into a readiness score.

## Agree on the work before the demo

| Question | Decision to record |
|---|---|
| Who does this work, and who receives it? | Named user group and recipient; who owns the workflow after the pilot |
| What recurring problem are we solving? | A specific trigger, inputs, required output and downstream action |
| What happens today? | Current tools, workarounds, preparation time and review effort |
| Why this use case first? | Expected benefit, frequency, failure consequences and implementation effort |
| Why this platform rather than the current approach? | A testable advantage such as easier handoff or maintenance; no assumed advantage from the product label |

## Define the acceptance boundary

Write one sentence for each state:

- **Generated:** What artifact or proposed action exists?
- **Verified:** Who checks it, against what source, and which errors block acceptance?
- **Accepted:** Who decides that the requested preparation work meets its brief?
- **Authorized:** Which real-world decisions or external actions require separate permission?

For the Brightwell example: a review checklist can be delivered and accepted while contract terms and approval remain unresolved. Completing an outage-reconciliation task does not approve the SLA.

## Check whether the pilot represents normal work

| Condition | Check with the team | If missing |
|---|---|---|
| Data access | Can intended users and agents access the required documents and structured rows? | Fix access/tool configuration before judging the model |
| Source authority | Who owns each source, and how are old versions and conflicts handled? | Keep the disagreement visible and ask for a decision |
| Representative inputs | Does the pilot include messy or missing data and ordinary users, not only curated examples? | Narrow the claim and expand the test before scaling |
| Review capacity | Can someone other than the builder check and accept the result? | Document the method and test a real handoff |
| Allowed actions | Can the agent draft, edit, assign, send or commit? Which actions need confirmation? | Disable consequential actions until the boundary is agreed |
| Maintenance | Who updates shared rules, sources and schedules? | Name an owner and a stop/rollback process |

## Measure usefulness alongside correctness

Choose thresholds with the team before collecting results. The blanks below are intentional.

| Measure | Baseline | Pilot result | Agreed threshold |
|---|---|---|---|
| Time to an accepted output, including review and correction | To measure | To measure | To agree |
| Unsupported statements or missed source conflicts | To measure | To measure | To agree |
| Rework caused downstream | To measure | To measure | To agree |
| Correct persistent actions and completion states | To measure | To measure | To agree |
| Cost per accepted output, including required tools and human effort | To measure | To measure | To agree |
| Use by intended users without the original builder | To measure | To measure | To agree |
| Repeated use after the initial demonstration | To measure | To measure | To agree |

Do not count agent generation time as total time saved. Do not convert a few synthetic runs into a general accuracy percentage or annual ROI. For Brightwell, these baseline, adoption and economic measures have not been collected.

## Make a decision

- **Continue:** the agreed result is useful, reviewable and repeatable; owners and ongoing costs are clear.
- **Adapt:** the use case is promising, but a specific data, tool, acceptance or maintenance issue blocks it. Name one change and retest that issue.
- **Stop:** the current method is better, demand is weak, or the required preparation/review cost outweighs the benefit.

Record the decision, evidence, limitations, owner and next review point. A successful demonstration is evidence of feasibility under its tested conditions, not proof of scalability.
