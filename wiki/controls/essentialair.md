---
id: essentialair
name: EssentialAIR (wall-mounted Lenze VFD)
type: control
category: vfd-package
vfd: Lenze AC Tech
location: wall-mounted
fans_controlled: 1 per unit
interface: keypad on the VFD
works_with: [sailfin-geared, sailfin-gearless]
source_docs:
  - "Electrical Installation Guide 2022 (pdfplumber).txt"
  - "Control Options (2023)__Brochure_EN__Rev-01__03.04.2023 (pdfplumber).txt"
last_verified: 2026-04-11
version: "2023"
version_source: "Control Options (2023)__Brochure_EN__Rev-01__03.04.2023 (pdfplumber).txt"
supersedes: null
---

# EssentialAIR

## Overview
EssentialAIR is the simplest Lenze-VFD-based control package in the Envira-North lineup. It consists of a single Lenze AC Tech VFD mounted on a wall near the electrical panel, with keypad operation directly on the drive. One VFD per fan. It is the cheapest entry point to Sailfin operation and the only Lenze-based package that puts the drive at ground level instead of on the fan frame.

## Key Specifications
| Item | Value |
|---|---|
| VFD make | Lenze AC Tech |
| Location | Wall-mounted |
| Fans controlled | 1 per VFD |
| Interface | On-drive keypad |
| Optional internal fire relay | Available |
| Shared wiring rules | Same as ZoneAIR and CommandAIR |

## Best Applications
- Single-fan installs where the operator wants the VFD at ground level near the panel (no climbing to adjust or troubleshoot)
- Budget-sensitive installs that don't need HMI touchscreen automation
- Facilities where wall space near the electrical panel is available

## Key Features & Benefits
- Wall-mounted VFD — easy to service without climbing
- On-drive keypad — start/stop/speed/direction at the drive
- Shared wiring rules with ZoneAIR and CommandAIR (same schematics, same conduit rules)
- Single-phase input supported on the 230 V model
- Optional internal fire relay
- Lowest-complexity option in the Lenze lineup

## What Makes It Different
- **vs. ZoneAIR:** EssentialAIR is wall-mounted; ZoneAIR is fan-mounted. EssentialAIR operates the VFD locally from its keypad. ZoneAIR is designed for multi-fan zone control via LVC.
- **vs. CommandAIR:** EssentialAIR is wall-mounted with no remote keypad. CommandAIR is fan-mounted with a 100 ft remote CAT-5 keypad — you get the short motor cable run of a fan-mounted VFD plus ground-level access via the remote keypad.
- **vs. ModAIR:** EssentialAIR has no ModBus module and no SmartAIR/TouchAIR integration. ModAIR is the Lenze path for digital HMI control.
- **vs. Schneider VFD:** EssentialAIR is Lenze; Schneider is a separate drive family. Schneider is required for SmartAIR/TouchAIR.

## Power & Electrical Requirements
- Lenze AC Tech VFD. Full-load current values for all HP and voltage combinations: see `guides/electrical-install-lenze.md` (Power requirements table).
- Single-phase input supported on 230 V: L1 - L2 + PE
- Three-phase: L1 - L2 - L3 + PE
- Separate insulated ground to each VFD from the panel
- Motor insulation class F
- Min 1 ft (300 mm) VFD-to-fan separation
- No splices in the motor cable run

## Mounting & Installation Notes
- Mount on a wall near the electrical panel
- Conduit rules (same for all Lenze packages):
  - Do not run input and output power in the same conduit
  - Do not run control cables with any power cables in the same conduit
  - Do not run different fans' output power in the same conduit
  - Different fans' input-only power cables may share a conduit
- Motor wiring: continuous run, no splices. Nord motor thermal protection wires are **not to be used** — the VFD provides overtemperature and overload protection.
- Cable-length limits and load reactor / dV/dT-filter rules: see `guides/electrical-install-lenze.md`
- Minimum VFD-to-fan separation: 1 ft (300 mm)
- Minimum programmed speed: 15 Hz / 27 %. Do not lower — will overheat the motor and void warranty.

## Operating Instructions (EssentialAIR Keypad)
- **TO START:** Press the Start button
- **TO STOP:** Press the Stop button
- **TO CHANGE SPEED:** Press the speed up/down buttons
- **TO CHANGE ROTATION:** Press the direction button, then press Start

## Maintenance Requirements
- VFD panel check at 12 months initial, then every 18 months (loose/discoloured wires, hot spots, re-tighten connections)
- Lock out controller for any fan/mount work
- See `guides/maintenance-schedule.md` for full product maintenance

## Compatible Accessories & Controls
- **Fire relay** — optional internal component
- **LVC + TFD-1** — the Lenze VFD can also be wired into an LVC network for analogue temperature-based control, but ZoneAIR is the package purpose-built for that

## Common FAQs

**Q: What is EssentialAIR?**
A: The simplest Lenze-VFD-based Sailfin control option. One wall-mounted Lenze VFD per fan, operated from the on-drive keypad.

**Q: Can I control multiple fans with one EssentialAIR?**
A: No. Each fan needs its own VFD. For multi-fan control with Lenze VFDs, use ZoneAIR + LVC, or upgrade to ModAIR + SmartAIR / TouchAIR.

**Q: Does EssentialAIR support single-phase power?**
A: Yes, on the 230 V model. Use L1 - L2 + PE.

**Q: Is the VFD on the fan or on the wall?**
A: On the wall. EssentialAIR is the only Lenze-based package with the VFD at ground level instead of mounted on the fan frame.

**Q: What's the minimum programmed fan speed?**
A: 15 Hz / 27 %. Running below this overheats the motor and voids the warranty.

**Q: Can I add a fire relay?**
A: Yes — optional internal fire relay available.

**Q: What cable length can I run between the EssentialAIR VFD and the motor?**
A: Up to 250 ft at 230 V, 160 ft at 460 V, or 125 ft at 600 V (no extras). Extended runs require a load reactor; very long runs require a dV/dT filter plus upsizing the VFD by +1 HP. See the full 3-tier table in `guides/electrical-install-lenze.md`.

## Source Documents Referenced
- `Electrical Installation Guide 2022 (pdfplumber).txt`
- `Control Options (2023)__Brochure_EN__Rev-01__03.04.2023 (pdfplumber).txt`
