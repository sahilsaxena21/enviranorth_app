---
id: zoneair-vs-commandair-vs-essentialair
name: ZoneAIR vs. CommandAIR vs. EssentialAIR
type: comparison
compares: [essentialair, zoneair, commandair]
source_docs:
  - "Control Options (2023)__Brochure_EN__Rev-01__03.04.2023 (pdfplumber).txt"
  - "Electrical Installation Guide 2022 (pdfplumber).txt"
last_verified: 2026-04-11
---

# ZoneAIR vs. CommandAIR vs. EssentialAIR

## TL;DR
All three are **Lenze AC Tech VFD packages**. They differ in how the operator interacts with the fan(s):
- **EssentialAIR** — wall-mounted Lenze drive, controlled directly at the drive. Single fan. Cheapest.
- **CommandAIR** — fan-mounted Lenze drive + **100 ft CAT-5 remote keypad**. Single fan. Operator gets a remote dial.
- **ZoneAIR** — fan-mounted Lenze drive + **LVC analogue panel**. **Up to 7 fans** over 700 ft. Supports TFD-1 temperature automation.

## Quick decision guide
| Scenario | Choice |
|---|---|
| 1 fan, cheapest | EssentialAIR |
| 1 fan, operator wants a remote dial | CommandAIR |
| 2–7 fans in one zone | ZoneAIR |
| 2–7 fans + temperature automation, no touchscreen | ZoneAIR + TFD-1 |
| 8+ fans | Not these — use TouchAIR or SmartAIR Multi-Fan |
| Need humidity automation | Not these — use SmartAIR (Schneider path) |
| Outdoor mount | Not these — use TouchAIR |

## Side-by-side
| Item | EssentialAIR | CommandAIR | ZoneAIR |
|---|---|---|---|
| Drive | Lenze wall-mounted | Lenze fan-mounted | Lenze fan-mounted |
| Operator interface | At the drive | Remote keypad | LVC panel |
| Connection | Direct | 100 ft CAT-5 | 0–10 V LVC, 7-wire |
| Max fans | 1 | 1 | **7** |
| Max run length | N/A | 100 ft CAT-5 | **700 ft** LVC |
| Temperature automation | No | No | **Yes via TFD-1** |
| Humidity automation | No | No | No |
| Wind sensor | Individual VFD option | Individual VFD option | Via LVC |
| Fire relay | Individual VFD option | Individual VFD option | Via LVC |
| Min speed | 15 Hz / 27 % | 15 Hz / 27 % | 15 Hz / 27 % |

## What they share
- All three drive one fan per Lenze VFD (ZoneAIR just networks up to 7 of them through the LVC)
- All three obey the same motor cable-length table (250 / 160 / 125 ft @ 230 / 460 / 600 V)
- All three respect the 15 Hz minimum speed
- None of them support humidity automation (that's a SmartAIR / Schneider feature)

## Architectural differences

### EssentialAIR
- Simplest install. Drive mounted on a wall near the fan. Operator walks to the drive to start, stop, and change speed.
- No remote anything. No HMI touchscreen.
- Wins when one fan needs to run and nobody wants to pay for extra controls.

### CommandAIR
- Drive lives on the fan. A 100 ft CAT-5 cable runs to a remote keypad where the operator actually stands.
- Still single-fan. The keypad is essentially a remote for the on-board drive panel.
- Wins when the fan is in an overhead location but the operator needs controls at floor level.

### ZoneAIR
- Drive lives on the fan. Each fan's drive runs 0–10 V back to a central LVC panel.
- The LVC panel has a single speed dial that commands all the fans in the zone in unison.
- Add TFD-1 on the LVC to turn the whole zone into an automated temperature-driven system.
- Wins when 2–7 fans in one area should all run at the same speed, with optional temperature automation.

## Common FAQs

**Q: Can I mix an EssentialAIR and a ZoneAIR on the same project?**
A: Yes — they are independent packages, one per fan or per zone. There's no electrical interference between them.

**Q: Does ZoneAIR let me control each fan individually?**
A: No — the LVC is a zone-level analogue dial. All fans in the LVC loop run at the same speed. If you need per-fan control on Lenze drives, use CommandAIR (one fan) or ModAIR (bridge to SmartAIR / TouchAIR).

**Q: Can CommandAIR control 2 fans?**
A: No — CommandAIR is single-fan. For multi-fan Lenze, use ZoneAIR.

**Q: How does TFD-1 fit in?**
A: TFD-1 plugs into the LVC and turns ZoneAIR into an automated temperature controller. See `controls/tfd-1.md`.

**Q: Can any of these do humidity?**
A: No. Humidity automation requires SmartAIR on the Schneider path.

## Source Documents Referenced
- `Control Options (2023)__Brochure_EN__Rev-01__03.04.2023 (pdfplumber).txt`
- `Electrical Installation Guide 2022 (pdfplumber).txt`
