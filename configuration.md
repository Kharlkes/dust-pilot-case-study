# Configuration and replay guide

This is a manual reconstruction recipe for the observed exercise, not a tested one-click import. Charles performed the original runs in Dust with guidance and synthetic data prepared with an AI assistant. Model and account availability can change; record your actual settings and cost. Do not upload this guide or the expected answers as knowledge for the agent.

## 1. Load the fictional sources

Create a folder in your Dust space. Upload only:

- `data/sales_notes.md`
- `data/product_notes.md`
- `data/people_update.md`
- `data/support_tickets.csv`, as a table

Use the actual UI you see rather than assuming older documentation labels match it. The table in the observed workspace was named `support_oct_26`.

## 2. Configure the agent

Name: `Brightwell_Assistant`.

Minimal initial instruction:

```text
You answer questions about Brightwell Software's weekly business using the attached documents.
```

Add two knowledge configurations:

| Observed UI method | Selected data | Purpose |
|---|---|---|
| Content search | The source-note folder | Find and cite documentary facts |
| Analytics (tables, spreadsheets...) | The support table | Count and aggregate structured rows |

Dust's documentation calls the structured-data method **Table queries** and describes it as generating and executing SQL. It also explains why semantic retrieval alone is unsuitable for many quantitative questions.[1]

Content-search description:

```text
Weekly business notes of Brightwell Software, a fictional B2B software company,
for November 2026. Contains sales notes, product notes and a people update.
Use it to answer questions about sales, product, incidents and team.
```

Analytics description:

```text
Support tickets for October 2026. Each row represents one ticket, with its ID,
date, customer, category, priority, status and resolution_hours. Use this data
for ticket counts, filtering by category or status, and calculating resolution-
time totals. resolution_hours is blank for open tickets.
```

The original setup was guided toward the Standard auto model. The actual model used in every run was not captured, so this is not a pinned-model benchmark.

## 3. Check retrieval, abstention and arithmetic

Ask related questions together if desired:

```text
1. Which customers signed this week, and for how much ARR each?
2. What was October MRR?
3. How long was the 29 October outage?
4. What was the customer churn rate in October?
5. Give me the link to the post-mortem document for the 29 October incident.
```

Expected behavior: signed ARR is present; both MRR figures and outage descriptions are disclosed; churn and a separate post-mortem URL are not invented.

For the structured data:

```text
Using the support ticket table for October 2026:
1. How many tickets are in the Billing category?
2. What is the sum of resolution_hours for tickets where status is Closed
   and category is Export?
```

Check results against the local fixture calculator, and inspect the visible table-discovery, schema and query actions. Do not intentionally remove the necessary table tool to manufacture a model failure; the initial access problem is already documented in this case.

## 4. Move beyond question answering

Ask for a weekly update combining source notes with total tickets, Billing tickets and Open High-priority tickets. Review all surrounding prose, not just the numeric results.

Then ask the agent to create a Pod named `Brightwell - Weekly Operations`, move the conversation into it and create three unassigned tasks without deadlines:

- Reconcile the two October MRR figures.
- Reconcile the two outage-duration descriptions.
- Prepare an internal checklist for reviewing Orbea's SLA request.

Require relevant source facts and explicit completion criteria, but no invented owners or external contact. Inspect the actual Tasks tab. Dust documents both human and agent task creation, execution and completion; those are separate steps.[4]

Run the checklist-preparation task with this brief:

```text
Prepare an internal review checklist and save it as orbea_sla_review.md
in this Pod's Files. Separate source-supported facts, questions needing
confirmation and proposed review points. Preserve Amelie's drafting role;
final approval ownership and deadlines are unknown. Do not invent SLA terms,
contact anyone or modify source documents.

Completion means the preparation artifact exists and has been checked;
it does not mean the SLA is approved. Report the actual file and task state.
```

## 5. Resume in a new conversation

Use the same agent and Pod. Read `examples/outage_duration_synthetic_evidence.md` as the explicitly fictional clarification for this phase. Ask the agent to save it as a separate source, revise the existing checklist and close only the outage-reconciliation task after saving and checking the evidence. Preserve the original source statements and leave all other unknowns open.

Inspect the real task state. A file download suffixed `(1)` by a local browser does not prove duplication inside the Pod; inspect the Pod's Files list instead.

## 6. Apply the maintenance Skill

Recreate [Maintain operational documents](skills/maintain-operational-documents.md) in the Skill editor and attach it to the agent. Dust allows Skills to bundle instructions, knowledge, tools and references to other Skills. The slash menu inserts actual capability references rather than just tool names in text.[2]

In a new conversation in the same Pod:

```text
Review orbea_sla_review.md against the evidence available in this Pod.
Use the Maintain operational documents skill to bring the existing
 document up to date. Save the changes without changing any task status.
```

Inspect the loaded Skill and the resulting file. The main test is whether a resolved issue still appears as a future action elsewhere in the document.

## 7. Test a real scheduled run, then clean up

The original natural-language wake-up request resulted in a visible Wait action. That demonstrates a delay, not persistent scheduling. See [the evidence](evidence/observations.md).

For the actual trigger test, use the schedule configuration in the agent builder. Dust documents a natural-language schedule with an interpreted time/timezone and a choice of Pod destination.[3]

1. Set the schedule to a time you can observe and verify its interpreted timezone.
2. Select the Brightwell Pod as the conversation destination.
3. Use a message that reads current tasks and the latest checklist, writes a new handoff, distinguishes delivery from approval and makes no other changes.
4. Save the schedule and agent as required by the UI.
5. Observe a new run without manually prompting it.
6. Inspect the generated file before accepting it.
7. **Disable the test schedule, save the change and verify it is disabled.** Do not leave a daily test consuming credits.

The original scheduled run was observed starting and reported writing its handoff. That final artifact and cleanup state were not supplied for verification, so they remain open checks in this case, not completed acceptance criteria.

## Sources

[1] https://docs.dust.tt/docs/user-documentation/agents/knowledge/table-queries.md — Table queries
[2] https://docs.dust.tt/docs/user-documentation/agents/skills/skills-overview.md — Skills overview
[3] https://docs.dust.tt/docs/user-documentation/agents/triggers/schedules.md — Schedules
[4] https://docs.dust.tt/docs/user-documentation/pods/tasks.md — Pod tasks
