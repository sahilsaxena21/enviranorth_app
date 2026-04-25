---
id: commandair
name: CommandAIR (fan-mounted Lenze VFD + remote keypad)
type: control
category: vfd-package
vfd: Lenze AC Tech
location: fan-mounted
fans_controlled: 1 per unit
interface: 100 ft remote CAT-5 keypad
works_with: [sailfin-geared, sailfin-gearless]
source_docs:
  - "Electrical Installation Guide 2022 (pdfplumber).txt"
  - "Control Options (2023)__Brochure_EN__Rev-01__03.04.2023 (pdfplumber).txt"
last_verified: 2026-04-11
version: "2023"
version_source: "Control Options (2023)__Brochure_EN__Rev-01__03.04.2023 (pdfplumber).txt"
supersedes: null
---

# CommandAIR

## Overview
CommandAIR is a fan-mounted Lenze VFD package with a ground-level remote keypad on a 100 ft CAT-5 cable. You get the short motor-cable run of a fan-mounted VFD and the ground-level access of a wall-mounted one, without needing a separate controller like an LVC. It is single-fan only — CommandAIR is not designed for multi-fan zone control.

## Key Specifications
| Item | Value |
|---|---|
| VFD make | Lenze AC Tech |
| Location | Fan-mounted |
| Interface | Remote keypad |
| Remote keypad cable | 100 ft (30.48 m) CAT-5 |
| Fans per unit | 1 |
| Optional internal fire relay | Available |
| Package includes | Fan-mounted VFD, mounting plate, wiring harness, control wire, 100 ft CAT-5, remote keypad |

## Best Applications
- Single-fan installs where the VFD should be on the fan frame (short motor cable run) but operators want to interact with it from the ground
- Facilities with the electrical panel far from the fan where EssentialAIR's wall-mount location isn't ideal
- Troubleshooting-heavy environments where climbing to the fan repeatedly is impractical

## Key Features & Benefits
- Fan-mounted VFD — short motor cable run
- 100 ft CAT-5 remote keypad — full start/stop/speed/direction control from ground level
- Remote troubleshooting without climbing
- Mounting plate + wiring harness included
- Optional internal fire relay
- Self-contained: no LVC or separate ground controller needed
- **User-friendly, simplified installation and operation** (per installation guide)

## What Makes It Different
- **vs. EssentialAIR:** same operational interface (keypad), but CommandAIR puts the VFD on the fan with a remote keypad at ground level. EssentialAIR mounts the VFD itself on the wall.
- **vs. ZoneAIR:** both are fan-mounted. ZoneAIR is for multi-fan zone control and needs an LVC. CommandAIR is single-fan and self-contained.
- **vs. SmartAIR / TouchAIR:** CommandAIR is a keypad, not a touchscreen; no automation (no temperature-based speed control). It is a manual control.

## Power & Electrical Requirements
- Lenze AC Tech VFD (same drive as EssentialAIR and ZoneAIR)
- Voltage / current / cable-length rules shared with the other Lenze packages — see `guides/electrical-install-lenze.md`
- Single-phase supported on 230 V (L1-L2 + PE); three-phase via L1-L2-L3 + PE
- Separate insulated ground to each VFD
- Motor insulation class F, class F wiring
- Min 1 ft (300 mm) VFD-to-fan separation

## Mounting & Installation Notes
**Fan mount:** mounting plate and wiring harness included. Same conduit rules as all Lenze packages:
- No input and output power in the same conduit
- No control cables with any power cables in the same conduit
- No different fans' output power in the same conduit

**Remote keypad:**
- 100 ft CAT-5 cable from the fan-mounted VFD to the keypad
- Same start/stop/speed/direction operations as the EssentialAIR on-drive keypad
- Nord motor thermal protection wires in the junction box are **not to be used** — the VFD provides overtemperature and overload protection

**Minimum fan speed:** 15 Hz / 27 %. Do not program below this.

## Operating Instructions (CommandAIR Remote Keypad)
- **TO START:** Press the Start button
- **TO STOP:** Press the Stop button
- **TO CHANGE SPEED:** Press the speed buttons
- **TO CHANGE ROTATION:** Press the direction button, then press Start

## Maintenance Requirements
- VFD panel check at 12 months, then every 18 months — see `guides/maintenance-schedule.md`
- Lock out controller during fan/mount work

## Compatible Accessories & Controls
- **Fire relay** — optional internal Lenze VFD component
- **Wind Sensor** — can be wired through if needed (mandatory in agricultural installs) — confirm specific integration with Envira-North
- Upgrading to **SmartAIR / TouchAIR** requires swapping to ModAIR (ModBus module) or Schneider VFD

## Common FAQs

**Q: What is CommandAIR good for?**
A: Single-fan installs where the VFD should be on the fan frame but operators need keypad access at ground level without climbing.

**Q: How long is the remote keypad cable?**
A: 100 ft (30.48 m) CAT-5 cable. Included in the package.

**Q: Is CommandAIR a touchscreen?**
A: No — it's a remote keypad, same interface as the EssentialAIR on-drive keypad. For touchscreen control use SmartAIR or TouchAIR (which require Schneider VFD or ModAIR).

**Q: Can CommandAIR control multiple fans?**
A: No — one VFD per fan, single remote keypad. For multi-fan zone control use ZoneAIR + LVC.

**Q: Does CommandAIR support single-phase power?**
A: Yes on the 230 V model. L1 - L2 + PE.

**Q: What's the minimum fan speed?**
A: 15 Hz / 27 %. Running below this will overheat the motor and void warranty.

**Q: Is fire relay included?**
A: Optional internal component — not standard.

## Source Documents Referenced
- `Electrical Installation Guide 2022 (pdfplumber).txt`
- `Control Options (2023)__Brochure_EN__Rev-01__03.04.2023 (pdfplumber).txt`
