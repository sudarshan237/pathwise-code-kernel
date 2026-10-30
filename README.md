# PathWise — Adaptive Learning for Classes 6–10

**Code Kernel '26 · Prototype and Video Submission**  
**Tagline:** Every learner. Their own pace. One informed teacher.

PathWise is a browser-based prototype responding to the Code Kernel '26 challenge: design learning that adapts to students in Classes 6–10. It demonstrates a student learning journey across **Learn → Solve → Test**, a transparent rule-based adaptation engine, and a teacher dashboard that surfaces suggested interventions while keeping teacher judgement central.

## What works in this prototype

- Three seeded learner profiles with different grade levels, language preferences and mastery levels.
- Sample Mathematics and Science topics spanning Classes 6–10.
- Learner-specific lesson mode: scaffolded explanation for students below 80% mastery; extension explanation at 80% or above.
- Practice and checkpoint question flow with immediate feedback.
- Mastery update after a checkpoint: 65% previous evidence + 35% latest checkpoint score.
- Transparent adaptation bands: below 60% = revisit foundations; 60–79% = consolidate; 80%+ = extend.
- Teacher dashboard with class averages, learners needing support, learners ready to advance and recommended teacher actions.
- Browser-local persistence through `localStorage`; the prototype needs no account or backend.
- Responsive layout for laptop and mobile screens.

## Run locally

Requirements: Node.js 20 or later and npm.

```bash
npm install
npm run dev
```

Open the local URL printed by Vite. To create a production build:

```bash
npm run build
npm run test
npm run preview
```

## Demo path (recommended)

1. Open Student space as **Ananya** (Class 7). Fractions starts at 38% mastery, so PathWise selects a scaffolded explanation and guided practice.
2. Complete Learn → Solve → Test. Select the correct or incorrect answer to show feedback and a mastery update.
3. Switch the demo learner to **Aarav** (Class 8). Fractions starts at 88%, so the lesson changes to extension mode.
4. Open Teacher dashboard. Show that the same topic produces different recommended actions for different learners.
5. Reset demo data before recording another run if needed.

## Adaptation logic

The rules are intentionally explainable for a school setting:

| Mastery signal | Learn | Solve | Test | Pace |
|---|---|---|---|---|
| Below 60% | Scaffolded / prerequisite revisit | Guided | Checkpoint | Revisit |
| 60–79% | Scaffolded / concept consolidation | Guided | Checkpoint | Steady |
| 80–100% | Extension / transfer | Challenge | Transfer checkpoint | Accelerate |

After the Test step, the demo blends existing mastery with the latest checkpoint signal: `newMastery = round(0.65 × previousMastery + 0.35 × checkpointScore)`. This avoids allowing one answer to completely overwrite prior evidence. A classroom deployment should use multiple questions, calibrated item difficulty, teacher review and validated curriculum mappings before making consequential recommendations.

## Architecture

The prototype is a client-side React + TypeScript application. `data.ts` contains sample curriculum content and demo learners; `engine.ts` contains pure adaptation rules; `App.tsx` coordinates the learner journey and teacher dashboard; `localStorage` persists demo progress on the current browser only. See `architecture.png` for the component and data-flow diagram.

## Scope and honest limitations

- This is a prototype, not a validated educational product or a production LMS.
- The included topics and learner data are illustrative demo content, not official NCERT/state-board coverage or real student records.
- Language preferences are represented in demo profiles; the current sample lesson content is English. Full Hindi, Kannada and other Indian-language content is a planned extension and must be reviewed by educators.
- No cloud sync, teacher accounts, parent accounts, analytics backend or multi-device sharing is included.
- The decision rules are transparent heuristics, not a trained AI model. They should be evaluated with educators and real learning-outcome data before classroom use.

## Stack

React · TypeScript · Vite · CSS · localStorage · Vitest

## Team

Team name: **Frontier** 
