# Synthetic input data

Every organization, person, event, amount and ticket in these files is fictional. They were prepared as a test fixture with AI assistance. No employer, customer or private research material is included.

| File | Content |
|---|---|
| sales_notes.md | New customer wins, pipeline, a reported MRR figure and commercial risks |
| product_notes.md | Releases, incident notes and a different MRR figure |
| people_update.md | Fictional hires and policies; included in the initial corpus, not central to the final workflow |
| support_tickets.csv | One row per support ticket; resolution_hours is blank for open tickets |

The documents deliberately disagree about MRR and incident duration. They do not contain an October churn rate, a post-mortem URL or the pending candidate's salary. Do not resolve these gaps using outside knowledge.

The support CSV has 40 rows. Expected results computed by scripts/check_fixture.py are 14 Billing tickets, 4 Open High-priority tickets and 160 total resolution_hours for Closed Export tickets. These are answer-key values, not evidence of general model reliability.

Keep this README, the answer key and the calculator OUT of Dust when reproducing the exercise. Upload only the three source-note Markdown files and the CSV. The uploaded table appeared as support_oct_26 in the observed workspace; use the actual name in your workspace.
