# Maintain operational documents

This is the instruction recipe used in the guided test. It is not a native Dust export or an automatically imported configuration.

## Description

Update existing operational documents when new evidence arrives, keeping facts, recommendations and completion checklists consistent.

## When to use this skill

Use this skill when reviewing or updating an existing operational document after new evidence or clarifications, or when checking consistency between its facts, open questions, recommendations and completion checklist.

## Instructions

Use Computer when needed to read the complete document, edit the existing file and verify the saved content. Do not rely on search snippets alone when checking consistency across the document.

When maintaining an existing operational document:

1. Read the current document and the relevant source evidence before editing.
2. Distinguish source facts, user-provided clarifications, assumptions and recommendations. Keep synthetic evidence explicitly labelled.
3. Update every section affected by a change, including facts, open questions, recommendations and completion checklists.
4. Do not leave a recommendation asking to resolve an issue that the same document now records as resolved. Preserve its resolution and any remaining uncertainty.
5. Preserve known ownership. Do not invent approvers, deadlines, contractual terms or missing facts.
6. Update the existing file rather than creating a duplicate. If that is not possible, explain the limitation.
7. Verify the saved content and briefly report what changed and what remains unresolved.
8. Do not change task statuses unless explicitly requested.

## Recreate it in Dust

Enter the fields above in the Skill editor. Replace the plain word Computer in the first instruction with the actual Computer capability chip, using the slash menu. Writing the word alone does not recreate that binding. Add the Skill to the agent and save it. No copy of the target checklist is attached to the Skill; the document is read from the Pod.

The observed run loaded this Skill, Pods and Computer, then used file reads/edits and re-read the saved content. The trace does not establish that a shell command ran or that Computer was necessary. We explicitly named the Skill in the test request; automatic discovery and propagation across multiple agents were not tested.
