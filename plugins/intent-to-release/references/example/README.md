# Paper Airship: Fictional Worked Example

Everything here is fictional and illustrative. [The method](../method.md) is normative.

Paper Airship is an invented local-first reading-list application. Readers cannot mark an item finished without deleting it from their list.

## Product Discovery

The ambiguous opportunity is “help readers keep the active list focused without losing reading history.” Fictional interview evidence shows readers want finished items hidden by default and recoverable. Gate 1 approves a narrow outcome: mark an item finished, hide finished items from the default list, and let readers show and restore them. Sharing, recommendations, accounts, and cloud sync are non-goals. The approved product brief owns this intent and the lifecycle links.

## Solution Design

The fictional repository already owns reading-item state in one local model and derives the visible list through one query. The temporary plan adds a nullable completion timestamp, makes the default query exclude completed items, adds a “show finished” view and restore action, preserves ordering, and covers migration, accessibility labels, tests, documentation promotion, rollback, and failure recovery. Hard deletion and a second archive store are rejected. Gate 2 approves the reviewed plan through release.

## Change Delivery

The contributor first adds failing model, query, and interaction tests, then implements completion, filtering, showing, and restoration. The implementation change links the product brief and temporary plan. Reconciliation records conformance, promotes the shipped state/filter/restore contract into durable product and architecture docs, and deletes the temporary plan. An independent maintainer reviews the exact head.

Candidate `paper-airship-v0.8.0+fictional.1` is built once. A teammate other than the implementer verifies the original criteria against those exact fictional bytes: complete an item, confirm it leaves the active list, show finished items, restore it, and confirm ordering and unrelated items remain intact. That candidate is accepted and promoted unchanged as fictional `v0.8.0`; post-release verification repeats the scenarios and records the prior artifact as rollback.

The complete ownership chain is product brief → temporary approved solution plan → implementation evidence and reconciliation → durable shipped documentation → exact-candidate acceptance → release record.
